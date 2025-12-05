import os
import sys
import networkx as nx
from contextlib import contextmanager

# Try to import pyboolnet
try:
    from pyboolnet.file_exchange import bnet2primes
    from pyboolnet.attractors import compute_attractors
    from pyboolnet.state_transition_graphs import primes2stg
    PYBOOLNET_AVAILABLE = True
except ImportError:
    PYBOOLNET_AVAILABLE = False

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def find_attractors_exact(stg_graph):
    """
    Finds attractors exactly using Tarjan's algorithm on the STG.
    Returns a structure compatible with PyBoolNet's output.
    """
    attractors = []
    sccs = list(nx.strongly_connected_components(stg_graph))
    
    for scc in sccs:
        # Check if it's a terminal SCC (no edges leaving the set)
        is_terminal = True
        for node in scc:
            for neighbor in stg_graph.neighbors(node):
                if neighbor not in scc:
                    is_terminal = False
                    break
            if not is_terminal:
                break
        
        if is_terminal:
            # Sort states to be deterministic
            states = sorted(list(scc))
            if len(states) > 1:
                cycle_path = []
                curr = states[0]
                visited = set()
                while curr not in visited:
                    visited.add(curr)
                    cycle_path.append(curr)
                    # Find next state in SCC
                    for neighbor in stg_graph.neighbors(curr):
                        if neighbor in scc:
                            curr = neighbor
                            break
                state_repr = " -> ".join(cycle_path)
            else:
                state_repr = states[0]

            is_steady = (len(states) == 1)
            
            attractors.append({
                'is_steady': is_steady,
                'state': {'str': state_repr},
                'min_trap_space': {'str': 'Exact-STG'}
            })
    
    # Sort attractors by state string to be deterministic
    attractors.sort(key=lambda x: x['state']['str'])
    return {'attractors': attractors}

def analyze_with_pyboolnet(bnet_file, silent=False, compute_stg=False, update_scheme='synchronous'):
    if not PYBOOLNET_AVAILABLE:
        if not silent:
            print("❌ Error: PyBoolNet is not installed.")
        return None, None, None

    if not silent:
        print(f"   PyBoolNet (BDDs) - {update_scheme.capitalize()} Update")
    
    # 1. Parse BNET file to 'Primes' (PyBoolNet's internal format)
    try:
        with suppress_stdout():
            primes = bnet2primes(bnet_file)
        if not silent:
            print(f"Parsed {len(primes)} nodes successfully.")
    except Exception as e:
        if not silent:
            print(f"PyBoolNet Parsing Error: {e}")
        return None, None, None

    # 2. Compute Attractors
    if not silent:
        print("   Computing attractors")
    try:
        with suppress_stdout():
            attractors_info = compute_attractors(primes, update=update_scheme)
        
        stg_edges = None
        if compute_stg:
            n_nodes = len(primes)
            if n_nodes > 12:
                if not silent:
                    print(f"Skipping STG generation: Network has {n_nodes} nodes (2^{n_nodes} states).")
            else:
                if not silent:
                    print("   Generating STG")
                with suppress_stdout():
                    stg_graph = primes2stg(primes, update=update_scheme)
                stg_edges = list(stg_graph.edges())
                
                # Use exact STG analysis for small networks
                attractors_info = find_attractors_exact(stg_graph)

        return primes, attractors_info, stg_edges

    except Exception as e:
        if not silent:
            print(f"PyBoolNet Analysis Error: {e}")
        return None, None, None
