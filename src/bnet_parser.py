import os
def load_bnet(file_path):
    rules = {}
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return rules
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines[1:], start = 2):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                # Check invalid format
                if ',' not in line:
                    print(f"Warning: Line {line_num} has invalid format(missing comma): {line}")
                parts = line.split(',', 1)
                if len(parts) != 2:
                    print(f"Warning: Line {line_num} has invalid format: {line}")
                    continue
                # Define target, factor
                target = parts[0].strip()
                factors = parts[1].strip()

                if not target:
                    print(f"Warning: Line {line_num} has empty target: {line}")
                    continue
                if not factors:
                    factors = False
                
                # Convert to Boolean sign
                factors = factors.replace('&', ' and ')
                factors = factors.replace('|', ' or ')
                factors = factors.replace('!', 'not ')

                factors = ' '.join(factors.split())
                # Add to rules
                rules[target] = factors
            if not rules:
                print(f"No valid rules found in {file_path}")

            return rules
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
# Optional, for debugging only
def validate_rules(rules):
    if not rules:
        print(f"Error: Rules is empty!")
        return False
    print(f"Successfully loaded {len(rules)} rules:")
    for target, factors in rules.items():
        print(f"  {target} <- {factors}")
    return True
    

