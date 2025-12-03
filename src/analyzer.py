import itertools
from collections import defaultdict

def generate_stg(rules, update_scheme='synchronous'):
    """
    Input: Biến 'rules' từ parser.py
    Output: List các cạnh chuyển đổi trạng thái (stg_edges)
    """
    stg_edges = []
    nodes = sorted(rules.keys())
    n = len(nodes)
    all_states = []

    # Change True, False -> 1, 0
    for values in itertools.product([True, False], repeat=n):
        state_str = ''.join('1' if v else '0' for v in values)
        all_states.append(state_str)
    # print(f"Generated {len(all_states)} states for {n} nodes...")

    #===============SYNCHRONOUS UPDATE===============
    if update_scheme == 'synchronous':
        for state in all_states:
            # Change state string to dictionary
            # EX: '010' + ['A','B','C'] → {'A': False, 'B': True, 'C': False}
            curr_state = {nodes[i]: (state[i] == '1') for i in range(n)}

            # Evaluating next state by using rules
            next_state_val = []
            for node in nodes:
                formula = rules[node]
                try:
                    result = eval(formula, {"__builtins__": {}}, curr_state) # disable Python built-in
                    next_state_val.append('1' if result else '0')
                except Exception as e:
                    print(f"Error evaluating {node}: {formula} ⚠️")
                    print(f"Current state: {curr_state}")
                    print(f"Error: {e}")
                    return [], []
                
            # Add state to std_edges
            next_state_str = ''.join(next_state_val)
            stg_edges.append((state, next_state_str))

    #===============ASYNCHRONOUS UPDATE===============
    elif update_scheme == 'asynchronous':
        for state in all_states:
            # Change state string to dictionary
            # EX: '010' + ['A','B','C'] → {'A': False, 'B': True, 'C': False}
            curr_state = {nodes[i]: (state[i] == '1') for i in range(n)}

            # Evaluating next state by using rules(for only 1 node)
            for node_idx, node in enumerate(nodes):
                formula = rules[node]
                try:
                    result = eval(formula, {"__builtins__": {}}, curr_state) # disable Python built-in
                    next_state_val = list(state)
                    next_state_val[node_idx] = '1' if result else '0' # Update only 1 node here
                    next_state_str = ''.join(next_state_val)

                    # Add state to std_edges
                    stg_edges.append((state, next_state_str))

                except Exception as e:
                    print(f"Error evaluating {node}: {formula} ⚠️")
                    print(f"Current state: {curr_state}")
                    print(f"Error: {e}")
                    return [], []
                
    else:
        print(f"Error: Unknown update scheme ⚠️")
        return [], []
    # print(f'Already generated {len(stg_edges)} edges...')
    return stg_edges, all_states

def find_attractors(stg_edges, all_states):
    """
    Input: stg_edges từ hàm trên
    Output: List các attractor
    """
    # Build adjacent list from stg_edges
    graph = defaultdict(list)
    for source, target in stg_edges:
        graph[source].append(target)

    # Find Strongly Connected Components
    sccs = find_ssc(graph, all_states)
    
    attractors = []
    for scc in sccs:
        is_attractor = True
        scc_set = set(scc)

        for state in scc:
            for next_state in graph[state]:
                if next_state not in scc_set:
                    is_attractor = False
                    break
            if not is_attractor:
                break
        if is_attractor:
            attractors.append(sorted(scc))
    return attractors

def find_ssc(graph, all_states):
    """
    Tìm Strongly Connected Components bằng thuật toán Tarjan
    
    Input:
        - graph: adjacency list
        - all_states: list tất cả các node
    Output:
        - List các SCC (mỗi SCC là list các state)
    """
    idx_counter = [0]
    stack = []
    onStack = defaultdict(bool)
    num = {} # visit order
    low = {} # smallest index that can reach
    sccs = []
    def strong_connect(node):
        num[node] = idx_counter[0]
        low[node] = idx_counter[0]
        idx_counter[0] += 1
        stack.append(node)
        onStack[node] = True
        
        # Traversing to succesor and update low
        succesors = graph[node]
        for succesor in succesors:
            # Successor is not visited
            if succesor not in num:
                strong_connect(succesor)
                low[node] = min(low[succesor], low[node])
            # Successor in stack -> part of current SCC
            elif onStack[succesor]:
                low[node] = min(low[node], num[succesor])
        # Check if node is SCC root
        if low[node] == num[node]:
            scc = []
            while True:
                succesor = stack.pop()
                onStack[succesor] = False # To confirm that current SCC has finished
                scc.append(succesor)
                if succesor == node:
                    break
            sccs.append(scc)
    
    # Traversing all transition graph
    for node in all_states:
        if node not in num:
            strong_connect(node)
    return sccs

def classify_attractors(attractors):
    """
    Phân loại attractors thành:
    - Fixed points (điểm cố định): attractor chỉ có 1 trạng thái
    - Limit cycles (chu trình): attractor có nhiều hơn 1 trạng thái
    
    Input: attractors (list of lists)
    Output: dictionary với classification
    """
    fixed_points = []
    limited_cycles = []
    for attractor in attractors:
        if len(attractor) == 1:
            fixed_points.append(attractor)
        else:
            limited_cycles.append(attractor)
    return {
        'fixed_points': fixed_points,
        'limit_cycles': limited_cycles,
        'total': len(attractors)
    }
