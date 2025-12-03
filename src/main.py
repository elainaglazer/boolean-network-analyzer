import sys
import os
import time
import json
import logging
from bnet_parser import load_bnet
from visualizer import plot_influence_graph, plot_stg
from pyboolnet_analyzer import analyze_with_pyboolnet, PYBOOLNET_AVAILABLE

# --- Configuration ---
OUTPUT_DIR = 'output'

# Silence library logs
logging.getLogger().setLevel(logging.CRITICAL)


def print_section(title):
    print(f"\n>>> {title}")
    print("-" * 40)

def save_results(base_name, attractors_info):
    json_output = os.path.join(OUTPUT_DIR, f'{base_name}_results.json')
    
    with open(json_output, 'w') as f:
        json.dump(attractors_info, f, indent=2, default=str)

    attractors = attractors_info.get('attractors', [])
    print(f"\nTotal Attractors Found: {len(attractors)}")
    
    for i, attr in enumerate(attractors, 1):
        is_steady = attr.get('is_steady', False)
        type_str = "Fixed Point" if is_steady else "Limit Cycle"
        
        state_repr = "N/A"
        if 'state' in attr and 'str' in attr['state']:
            state_repr = attr['state']['str']
        elif 'min_trap_space' in attr and 'str' in attr['min_trap_space']:
                state_repr = f"Trap Space: {attr['min_trap_space']['str']}"
        
        print(f"  {i}. {type_str}")
        print(f"     State: {state_repr}")

def run_analysis(input_file, base_name):
    print(f"File: {input_file}")
    
    # 2. Load Network
    start_time = time.time()
    rules = load_bnet(input_file) 
    if not rules:
        print("Failed to load rules.")
        return

    # 3. Visualize
    influence_output = os.path.join(OUTPUT_DIR, f'{base_name}_influence.png')
    plot_influence_graph(rules, output_path=influence_output)

    # 4. Analyze (PyBoolNet)
    _, attractors_info, stg_edges = analyze_with_pyboolnet(input_file, compute_stg=True)
    
    if attractors_info:
        print_section("Result:")
        save_results(base_name, attractors_info)

        if stg_edges:
            stg_output = os.path.join(OUTPUT_DIR, f'{base_name}_stg.png')
            plot_stg(stg_edges, output_path=stg_output)
            print(f"STG Graph: {stg_output}")
            print(f"Influence Graph: {influence_output}")
        
        elapsed = time.time() - start_time
        print(f"Time: {elapsed:.4f} seconds.")


def resolve_input_path(arg):
    """Resolves the input argument to a valid file path."""
    if arg.endswith('.bnet'):
        return arg, os.path.splitext(os.path.basename(arg))[0]
    
    # Check common locations
    paths = [
        f'input_data/test_cases/{arg}.bnet',
        f'input_data/{arg}.bnet',
        arg
    ]
    
    for p in paths:
        if os.path.exists(p):
            return p, arg
            
    return None, None

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if len(sys.argv) < 2:
        print("Usage: python src/main.py <test_case_name>")
        return

    for arg in sys.argv[1:]:
        input_file, base_name = resolve_input_path(arg)
        if input_file:
            run_analysis(input_file, base_name)
        else:
            print(f"Error: Could not find input file for '{arg}'")

if __name__ == "__main__":
    main()
