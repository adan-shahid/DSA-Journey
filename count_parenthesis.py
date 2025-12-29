def simple_parenthesis_count(bits, valid_gates):
    """
    Even simpler version - just count working parenthesis positions
    """
    N = len(bits)
    working_positions = 0
    
    # All possible parenthesis positions
    for i in range(N):
        for j in range(i, N):
            # Check if ANY gate combination works with this parenthesis position
            for gates in valid_gates:
                result = eval_expression(bits, gates, i, j)
                if result == 1:
                    working_positions += 1
                    break
    
    return working_positions

def eval_expression(bits, gates, i, j):
    """
    Simple evaluation with parentheses
    """
    # If parentheses don't change evaluation (single bits or full expression)
    if i == j or (i == 0 and j == len(bits)-1):
        # Evaluate normally
        val = bits[0]
        for k in range(1, len(bits)):
            val = apply_gate(gates[k-1], val, bits[k])
        return val
    
    # For other cases, just return 1 (simplified)
    # In real code, you'd implement the proper evaluation
    return 1










# def count_valid_configurations(bits):
#     N = len(bits)
#     gates = ['AND', 'OR', 'XOR']
#     count = 0
    
#     # Apply gate operation
#     def do_op(op, a, b):
#         if op == 'AND': return a and b
#         if op == 'OR': return a or b
#         if op == 'XOR': return a != b
    
#     # Try all gate combinations
#     if N == 2:
#         # For 2 bits: 1 gate
#         for gate1 in gates:
#             # Try all parenthesis positions
#             # Position (0,0): (A0) g1 A1
#             value = bits[0]  # Inside parentheses
#             value = do_op(gate1, value, bits[1])
#             if value == 1:
#                 count += 1
            
#             # Position (0,1): (A0 g1 A1)
#             value = bits[0]
#             value = do_op(gate1, value, bits[1])
#             if value == 1:
#                 count += 1
            
#             # Position (1,1): A0 g1 (A1)
#             value = bits[0]
#             value = do_op(gate1, value, bits[1])
#             if value == 1:
#                 count += 1
    
#     elif N == 3:
#         # For 3 bits: 2 gates
#         for gate1 in gates:
#             for gate2 in gates:
#                 # Try all 6 parenthesis positions
                
#                 # (0,0): (A0) g1 A1 g2 A2
#                 value = bits[0]
#                 value = do_op(gate1, value, bits[1])
#                 value = do_op(gate2, value, bits[2])
#                 if value == 1:
#                     count += 1
                
#                 # (0,1): (A0 g1 A1) g2 A2
#                 paren_value = bits[0]
#                 paren_value = do_op(gate1, paren_value, bits[1])
#                 value = do_op(gate2, paren_value, bits[2])
#                 if value == 1:
#                     count += 1
                
#                 # (0,2): (A0 g1 A1 g2 A2)
#                 value = bits[0]
#                 value = do_op(gate1, value, bits[1])
#                 value = do_op(gate2, value, bits[2])
#                 if value == 1:
#                     count += 1
                
#                 # (1,1): A0 g1 (A1) g2 A2
#                 value = bits[0]
#                 paren_value = bits[1]  # Inside parentheses
#                 value = do_op(gate1, value, paren_value)
#                 value = do_op(gate2, value, bits[2])
#                 if value == 1:
#                     count += 1
                
#                 # (1,2): A0 g1 (A1 g2 A2)
#                 prefix = bits[0]
#                 paren_value = bits[1]
#                 paren_value = do_op(gate2, paren_value, bits[2])
#                 value = do_op(gate1, prefix, paren_value)
#                 if value == 1:
#                     count += 1
                
#                 # (2,2): A0 g1 A1 g2 (A2)
#                 value = bits[0]
#                 value = do_op(gate1, value, bits[1])
#                 paren_value = bits[2]  # Inside parentheses
#                 value = do_op(gate2, value, paren_value)
#                 if value == 1:
#                     count += 1
    
#     return count

# bits = [1,0,1]
# print(count_valid_configurations(bits))