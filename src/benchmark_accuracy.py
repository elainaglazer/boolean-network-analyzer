import time
import sys
import os
import logging
from analyzer import generate_stg, find_attractors
from pyboolnet_analyzer import analyze_with_pyboolnet
from benchmark_utils import (
    suppress_stdout, 
    generate_random_rules, 
    save_rules
)

# Silence logs
logging.getLogger().setLevel(logging.CRITICAL)

def run_benchmark(n_nodes=10):
    TRIALS = 3
    TEMP = "temp_bench.bnet"
    
    print(f"--- PyBoolNet vs. Exhaustive Search ({n_nodes} nodes, {TRIALS} trials) ---")
    
    matches = 0
    start = time.time()
    
    for i in range(TRIALS):
        print(f"\nTrial {i+1}/{TRIALS}:")
        rules = generate_random_rules(n_nodes)
        save_rules(rules, TEMP)
        
        # Ground Truth (Exhaustive)
        py_rules = {k: v.replace('&',' and ').replace('|',' or ').replace('!',' not ') for k,v in rules.items()}
        
        with suppress_stdout():
            stg, states = generate_stg(py_rules)
            true_attrs = find_attractors(stg, states)
        
        # PyBoolNet
        with suppress_stdout():
            _, info, _ = analyze_with_pyboolnet(TEMP, silent=True, compute_stg=True)
        
        # --- Comparison Logic ---
        bf_lines = []
        bf_sets = set()
        for attr in true_attrs:
            bf_sets.add(frozenset(attr))
            if len(attr) == 1:
                bf_lines.append(f"Fixed Point: {attr[0]}")
            else:
                # Sort for display consistency
                cycle_str = " -> ".join(sorted(attr))
                bf_lines.append(f"Cycle: {cycle_str}")
        bf_lines.sort()

        pb_lines = []
        pb_sets = set()
        if info and 'attractors' in info:
            for attr in info['attractors']:
                state_str = attr['state']['str']
                # Parse back to set for accuracy check
                states_in_attr = state_str.split(" -> ")
                pb_sets.add(frozenset(states_in_attr))
                
                if attr['is_steady']:
                    pb_lines.append(f"Fixed Point: {state_str}")
                else:
                    sorted_disp = " -> ".join(sorted(states_in_attr))
                    pb_lines.append(f"Cycle: {sorted_disp}")
        pb_lines.sort()

        # Check Accuracy
        is_match = (bf_sets == pb_sets)
        if is_match: matches += 1

        # Print Side by Side
        print(f"{'BRUTE FORCE':<40} | {'PYBOOLNET':<40}")
        print("-" * 83)
        
        max_len = max(len(bf_lines), len(pb_lines))
        for j in range(max_len):
            left = bf_lines[j] if j < len(bf_lines) else ""
            right = pb_lines[j] if j < len(pb_lines) else ""
            
            # Truncate for display
            d_left = (left[:37] + "...") if len(left) > 40 else left
            d_right = (right[:37] + "...") if len(right) > 40 else right
            print(f"{d_left:<40} | {d_right:<40}")

        if is_match:
            print(f"{'>>>>>>>>>>    MATCH   <<<<<<<<<<':}")
        else:
            print(f"{'>>>>>>>>>>  MISMATCH  <<<<<<<<<<':}")

    if os.path.exists(TEMP): os.remove(TEMP)
    
    acc = (matches / TRIALS) * 100
    print(f"\n" + "="*83)
    print(f"Total Time: {time.time()-start:.2f}s | Overall Accuracy: {acc:.2f}%")
    print("="*83)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            run_benchmark(n)
        except ValueError:
            print("Node is integer")
    else:
        run_benchmark()
