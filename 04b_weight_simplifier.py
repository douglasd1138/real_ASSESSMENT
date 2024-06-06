def convert_weight(weight_input):
    # Assuming weight_input is in grams
    weight_kg = weight_input / 1000  # converting grams to kilograms
    return weight_kg


# Loop for quick testing...
for _ in range(0, 6):  # Use _ as a throwaway variable if you don't need the loop index
    weight_input_inner = float(input("Enter weight in grams: "))
    converted_weight = convert_weight(weight_input_inner)
    print("Weight: {:.2f} kg".format(converted_weight))
    print()
                