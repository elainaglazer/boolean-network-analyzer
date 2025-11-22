import matplotlib.pyplot as plt
import networkx as nx

def plot_influence_graph(rules): # <--- NHẬN BIẾN RULES Ở ĐÂY
    """
    Input: Biến 'rules' từ parser
    Nhiệm vụ: Vẽ quan hệ giữa các nút (ai ảnh hưởng tới ai)
    """
    G = nx.DiGraph()
    
    # TODO: Logic vẽ
    # Duyệt qua rules. Nếu công thức của A có chứa B -> Thêm cạnh B->A
    
    print("Plotting Influence Graph...")
    # nx.draw(G, ...)
    # plt.show()

def plot_stg(stg_edges):
    """
    Input: stg_edges từ analyzer
    Nhiệm vụ: Vẽ các chấm trạng thái và mũi tên
    """
    G = nx.DiGraph()
    G.add_edges_from(stg_edges)
    
    print("Plotting STG...")
    # nx.draw(G, ...)
    # plt.show()
