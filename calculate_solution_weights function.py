def calculate_solution_weights(molecular_weights, solutions_needed):
    modified_list = []
    
    for solution in solutions_needed:
        try:
            chemical, concentration_str = solution.split('-') #Trying to extract information so splitting the moleular weights into chemical name and concentration. 
            concentration = float(concentration_str.replace('M', ''))  # Convert to float
            
            if chemical in molecular_weights:  # Check if the chemical exists in the molecular weights dictionary
                molecular_weight = molecular_weights[chemical]
                weight = molecular_weight * concentration  # Calculate weight
                modified_list.append(f"{chemical}-{concentration_str}-{weight:.2f}g")
            else:
                modified_list.append("unknown")
        except Exception:
            modified_list.append("unknown")
    
    return modified_list

result = calculate_solution_weights(molecular_weights, solutions_needed) # Calculate solution weights

print(result)
