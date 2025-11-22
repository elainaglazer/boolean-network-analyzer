from parser import load_bnet
from analyzer import generate_stg, find_attractors
from visualizer import plot_influence_graph, plot_stg

def main():
    # 1. TẠO RULES (Gọi Parser)
    print("--- Step 1: Loading Rules ---")
    rules = load_bnet('input_data/example.bnet') # <--- Biến rules được sinh ra ở đây
    print("Rules loaded:", rules)

    # 2. VẼ INFLUENCE GRAPH (Dùng Rules)
    plot_influence_graph(rules) # <--- Truyền rules vào Visualizer

    # 3. TÍNH TOÁN STG (Dùng Rules)
    print("--- Step 2: Generating STG ---")
    stg_edges = generate_stg(rules) # <--- Truyền rules vào Analyzer

    # 4. VẼ STG & TÌM ATTRACTOR (Dùng kết quả của Analyzer)
    plot_stg(stg_edges)
    attractors = find_attractors(stg_edges)
    print("Attractors found:", attractors)

if __name__ == "__main__":
    main()
