import matplotlib.pyplot as plt
import networkx as nx

def plot_influence_graph(rules):
    """
    Vẽ và hiển thị đồ thị ảnh hưởng (Influence Graph).
    """
    G = nx.DiGraph()
    # TODO: Parse rules để tìm mối quan hệ cha-con và thêm vào đồ thị
    # G.add_edge(src, dest, sign=...)
    
    plt.figure(figsize=(8, 6))
    # Code vẽ đồ thị tại đây
    plt.title("Influence Graph")
    plt.show()

def plot_stg(stg_edges):
    """
    Vẽ và hiển thị đồ thị chuyển đổi trạng thái.
    """
    G = nx.DiGraph()
    G.add_edges_from(stg_edges)
    
    plt.figure(figsize=(10, 8))
    # Code vẽ đồ thị tại đây
    plt.title("State Transition Graph")
    plt.show()
