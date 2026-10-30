def clean_sensor_readings(readings):
    """
    Cleans a list of mixed inputs, converting valid numbers to floats,
    filtering out negatives/None/invalid, and capping at 500.0.
    """
    if not readings:
        return []

    cleaned_list = []
    
    for item in readings:
        try:
            # 1. Type Conversion & Filtering
            # We use float() to convert. If it fails (e.g., string "abc"), it goes to except.
            val = float(item)
            
            # Drop negative values
            if val < 0:
                continue
            
            # 2. Clipping: Cap at 500.0
            if val > 500.0:
                val = 500.0
                
            cleaned_list.append(val)
            
        except (ValueError, TypeError):
            # Drop values that cannot be converted (strings, None, etc.)
            continue
            
    return cleaned_list

# --- Test Cases ---
if __name__ == "__main__":
    print("Test 1 (Mixed Data):")
    test1 = [10, "20.5", None, -5, "abc", 600, 499.9]
    print(f"Input: {test1}")
    print(f"Output: {clean_sensor_readings(test1)}\n") 
    # Expected: [10.0, 20.5, 500.0, 499.9]

    print("Test 2 (Empty List):")
    test2 = []
    print(f"Input: {test2}")
    print(f"Output: {clean_sensor_readings(test2)}\n") 
    # Expected: []

    print("Test 3 (All Invalid):")
    test3 = [None, "error", -10, "NaN"]
    print(f"Input: {test3}")
    print(f"Output: {clean_sensor_readings(test3)}") 
    # Expected: []