import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import re

def plot_influence_graph(rules, output_path='output/influence_graph.png'):
    """
    Input: Biến 'rules' từ parser
    Nhiệm vụ: Vẽ quan hệ giữa các nút (ai ảnh hưởng tới ai)
    """
    G = nx.DiGraph()
    nodes = list(rules.keys())
    G.add_nodes_from(nodes)
    
    # Duyệt qua rules. Nếu công thức của A có chứa B -> Thêm cạnh B->A
    for target, formula in rules.items():
        for source in nodes:
            # Use regex to match whole word only (e.g. ensure "A" doesn't match "AB")
            if re.search(r'\b' + re.escape(source) + r'\b', formula):
                G.add_edge(source, target)
    
    plt.figure(figsize=(10, 8))
    # Use circular layout for clearer structure of genes
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, arrowsize=20, font_size=12, font_weight='bold')
    plt.title("Influence Graph (Interaction Network)")
    plt.savefig(output_path)
    plt.close() # Close the figure to free memory

def plot_stg(stg_edges, output_path='output/stg.png'):
    """
    Input: stg_edges từ analyzer
    Nhiệm vụ: Vẽ các chấm trạng thái và mũi tên
    """
    G = nx.DiGraph()
    G.add_edges_from(stg_edges)
    
    num_nodes = G.number_of_nodes()
    
    if num_nodes == 0:
        print("STG is empty. Nothing to plot.")
        return

    if num_nodes > 1000:
        print(f"STG has {num_nodes} states. Too large to visualize.")
        print("   Skipping plot generation to avoid crash.")
        return

    # Dynamic styling based on graph size
    if num_nodes < 20:
        figsize = (8, 8)
        node_size = 2000
        font_size = 12
        k_layout = 0.8
        arrow_size = 20
    elif num_nodes < 100:
        figsize = (10, 10)
        node_size = 1000
        font_size = 10
        k_layout = 0.4
        arrow_size = 15
    else:
        figsize = (12, 12)
        node_size = 600
        font_size = 8
        k_layout = 0.15
        arrow_size = 10

    plt.figure(figsize=figsize)
    #spring layout
    pos = nx.spring_layout(G, k=k_layout, iterations=50)
    
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
            node_size=node_size, arrowsize=arrow_size, font_size=font_size, alpha=0.9)
    
    plt.title(f"State Transition Graph (STG) - {num_nodes} States")
    plt.savefig(output_path)
    plt.close()
