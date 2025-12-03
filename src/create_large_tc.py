from benchmark_utils import generate_random_rules, save_rules
import os

def create_large_test_case(n_nodes):
    print(f"Generating {n_nodes} node network...")
    rules = generate_random_rules(n_nodes)
    
    output_dir = "input_data/test_cases"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = os.path.join(output_dir, f"tc_{n_nodes}_nodes.bnet")
    save_rules(rules, filename)
    print(f"Saved to {filename}")

if __name__ == "__main__":
    create_large_test_case(30)
