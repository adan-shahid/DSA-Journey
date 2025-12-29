def find_valid_gate_combinations(bits):    
    N = len(bits)
    num_gates = N - 1
    
    if N == 1:
        if bits[0] == 1:
            return []
        else:
            None
    
    gate_types = ['&', '|', '^']
    # valid_combinations = []
    count = 0
    
    # Try all possible gate combinations
    total = 3 ** num_gates
    
    for combination_num in range(total):
        gates = []
        temp = combination_num
        
        # Generate this combination of gates
        for i in range(num_gates):
            gate_index = temp % 3
            gates.append(gate_types[gate_index])
            temp = temp // 3
        
        # Now EVALUATE: Does this combination give us 1?
        result = bits[0]  # Start with first bit
        
        for i in range(num_gates):
            gate = gates[i]
            next_bit = bits[i + 1]
            
            # Apply the gate (left to right)
            if gate == '&':
                result = result & next_bit
            elif gate == '|':
                result = result | next_bit
            else:  # gate == '^'
                result = result ^ next_bit
        
        # Check if result is 1
        if result == 1:
            count += 1
    
    return count


bits = [1,1]
print(find_valid_gate_combinations(bits))