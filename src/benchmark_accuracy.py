import time
import sys
import os
import logging
from analyzer import generate_stg, find_attractors
from pyboolnet_analyzer import analyze_with_pyboolnet
from benchmark_utils import (
    suppress_stdout, 
    generate_random_rules, 
    save_rules, 
    normalize, 
    extract_pyboolnet
)

# Silence logs
logging.getLogger().setLevel(logging.CRITICAL)

def run_benchmark(n_nodes=5):
    TRIALS = 20
    TEMP = "temp_bench.bnet"
    
    print(f"--- PyBoolNet vs. Exhaustive Search ({n_nodes} nodes, {TRIALS} trials) ---")
    print("Running...", end=" ", flush=True)
    
    matches = 0
    start = time.time()
    
    for i in range(TRIALS):
        rules = generate_random_rules(n_nodes)
        save_rules(rules, TEMP)
        
        # Ground Truth (Exhaustive)
        # Convert & -> and, | -> or, ! -> not for Python eval
        py_rules = {k: v.replace('&',' and ').replace('|',' or ').replace('!',' not ') for k,v in rules.items()}
        
        with suppress_stdout():
            stg, states = generate_stg(py_rules)
            true_attrs = [a for a in find_attractors(stg, states) if len(a) == 1]
        
        # PyBoolNet
        with suppress_stdout():
            _, info, _ = analyze_with_pyboolnet(TEMP, silent=True)
        
        if normalize(true_attrs) == extract_pyboolnet(info):
            matches += 1
            
        if (i+1) % 5 == 0: print(f"{i+1}..", end=" ", flush=True)

    if os.path.exists(TEMP): os.remove(TEMP)
    
    acc = (matches / TRIALS) * 100
    print(f"\n\nTime: {time.time()-start:.2f}s | Accuracy: {acc:.2f}%")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            run_benchmark(n)
        except ValueError:
            print("Node is integer")
    else:
        run_benchmark()
