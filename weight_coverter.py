converter = 0.45

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.lower() == "k":
    converted_weight = weight / converter
    print(f"You are {converted_weight} kilos")
elif unit.lower() == "l":
    converted_weight = weight * converter
    print(f"You are {converted_weight} pounds")
