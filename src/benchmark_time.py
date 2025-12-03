import time
import os
import logging
import matplotlib.pyplot as plt
from benchmark_utils import generate_random_rules, save_rules, suppress_stdout
from pyboolnet_analyzer import analyze_with_pyboolnet

# Silence library logs
logging.getLogger().setLevel(logging.CRITICAL)

def benchmark_execution_time(max_nodes=30):
    TRIALS = 5
    print(f"Benchmarking execution time for 1 to {max_nodes} nodes (Average of {TRIALS} trials)...")
    
    times = []
    node_counts = list(range(1, max_nodes + 1))
    temp_file = "temp_time_bench.bnet"
    
    # Ensure output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    for n in node_counts:
        print(f"Testing {n} nodes...", end=" ", flush=True)
        
        total_duration = 0
        for _ in range(TRIALS):
            # 1. Generate random network
            rules = generate_random_rules(n)
            save_rules(rules, temp_file)
            
            # 2. Measure Analysis Time
            start_time = time.time()
            with suppress_stdout():
                # disable STG generation
                analyze_with_pyboolnet(temp_file, silent=True, compute_stg=False)
            end_time = time.time()
            
            total_duration += (end_time - start_time)
        
        avg_duration = total_duration / TRIALS
        times.append(avg_duration)
        print(f"{avg_duration:.4f}s (avg)")

    # 3. Cleanup
    if os.path.exists(temp_file):
        os.remove(temp_file)

    # 4. Plot Results
    plt.figure(figsize=(10, 6))
    plt.plot(node_counts, times, marker='o', linestyle='-', color='b', label=f'Average of {TRIALS} trials')
    
    plt.title(f"Average Execution Time vs. Network Size (1-{max_nodes} Nodes)")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Time (seconds)")
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    
    output_path = os.path.join('output', 'benchmark_execution_time.png')
    plt.savefig(output_path)
    print(f"\n✅ Benchmark complete. Graph saved to: {output_path}")

if __name__ == "__main__":
    benchmark_execution_time(30)
