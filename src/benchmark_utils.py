import random
import sys
import os
from contextlib import contextmanager

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old = sys.stdout
        sys.stdout = devnull
        try: yield
        finally: sys.stdout = old

def generate_random_rules(n_nodes):
    # Use names > 1 char for PyBoolNet compatibility
    nodes = [f"Gene{i+1:02d}" for i in range(n_nodes)]
    rules = {}
    ops = ['&', '|']
    for node in nodes:
        # Ensure we don't sample more nodes than exist
        max_k = min(len(nodes), 3)
        k = random.randint(1, max_k)
        inputs = random.sample(nodes, k)
        parts = []
        for i, inp in enumerate(inputs):
            if random.random() > 0.5: inp = f"!{inp}"
            parts.append(inp)
            if i < len(inputs) - 1: parts.append(random.choice(ops))
        rules[node] = " ".join(parts)
    return rules

def save_rules(rules, filename):
    with open(filename, 'w') as f:
        f.write("targets, factors\n")
        for t, form in rules.items(): f.write(f"{t}, {form}\n")

def normalize(attractors):
    return set(frozenset(a) for a in attractors)

def extract_pyboolnet(info):
    normalized = set()
    if not info or 'attractors' not in info: return normalized
    for attr in info['attractors']:
        if attr.get('is_steady'):
            normalized.add(frozenset([attr['state']['str']]))
    return normalized
