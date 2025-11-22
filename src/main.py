from parser import load_bnet
from analyzer import generate_stg, find_attractors
from visualizer import plot_influence_graph, plot_stg

def main():
    # Đường dẫn file mẫu (tự tạo file .bnet để test)
    input_file = "input_data/example.bnet" 
    
    try:
        # 1. Đọc dữ liệu
        print("--- Loading Network ---")
        rules = load_bnet(input_file)
        print(f"Loaded {len(rules)} nodes.")

        # 2. Vẽ Influence Graph
        print("--- Plotting Influence Graph ---")
        plot_influence_graph(rules)

        # 3. Tính toán STG
        print("--- Generating State Transition Graph ---")
        stg = generate_stg(rules, mode='synchronous')
        
        # 4. Vẽ STG
        print("--- Plotting STG ---")
        plot_stg(stg)

        # 5. Tìm Attractors
        print("--- Finding Attractors ---")
        attractors = find_attractors(stg)
        print(f"Found attractors: {attractors}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
