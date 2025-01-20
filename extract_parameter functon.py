def extract_parameter(unit_operations_data, unit_name, parameter_name, index):
  
    if unit_name not in unit_operations_data: #Check if the unit_name exists in the dictionary and if not then return invalid input 
        return "Invalid input"
        
    unit_data = unit_operations_data[unit_name] # Check if the parameter_name exists within the unit and if not then return invalid input 
    if parameter_name not in unit_data:
        return "Invalid input"
    
    parameter_values = unit_data[parameter_name] # Check if the index is within range and if not then it will return invalid input
    if not (0 <= index < len(parameter_values)): 
        return "Invalid input"
    
    value = parameter_values[index] # Extract the value and format the output
    return f"{unit_name}_{parameter_name}_{value}"