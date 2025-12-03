import os
import sys
from contextlib import contextmanager

# Try to import pyboolnet
try:
    from pyboolnet.file_exchange import bnet2primes
    from pyboolnet.attractors import compute_attractors
    from pyboolnet.state_transition_graphs import primes2stg
    PYBOOLNET_AVAILABLE = True
except ImportError:
    PYBOOLNET_AVAILABLE = False

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def analyze_with_pyboolnet(bnet_file, silent=False, compute_stg=False):
    """
    Uses the PyBoolNet library to analyze the network.
    This uses advanced BDD (Binary Decision Diagram) based algorithms
    which are much faster and more accurate than brute force or random sampling.
    """
    if not PYBOOLNET_AVAILABLE:
        if not silent:
            print("❌ Error: PyBoolNet is not installed.")
        return None, None, None

    if not silent:
        print(f"   PyBoolNet (BDDs)")
    
    # 1. Parse BNET file to 'Primes' (PyBoolNet's internal format)
    try:
        with suppress_stdout():
            primes = bnet2primes(bnet_file)
        if not silent:
            print(f"Parsed {len(primes)} nodes successfully.")
    except Exception as e:
        if not silent:
            print(f"PyBoolNet Parsing Error: {e}")
        return None, None, None

    # 2. Compute Attractors
    if not silent:
        print("   Computing attractors")
    try:
        with suppress_stdout():
            attractors_info = compute_attractors(primes, update="synchronous")
        
        stg_edges = None
        if compute_stg:
            n_nodes = len(primes)
            if n_nodes > 12:
                if not silent:
                    print(f"Skipping STG generation: Network has {n_nodes} nodes (2^{n_nodes} states).")
            else:
                if not silent:
                    print("   Generating STG")
                with suppress_stdout():
                    stg_graph = primes2stg(primes, update="synchronous")
                stg_edges = list(stg_graph.edges())

        return primes, attractors_info, stg_edges

    except Exception as e:
        if not silent:
            print(f"PyBoolNet Analysis Error: {e}")
        return None, None, None
