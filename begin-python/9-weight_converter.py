weight = input("weight: ")
lb_kg = input("(L)bs or (K)g: ")

if lb_kg.upper() == "L":
    output = int(weight) * 0.45
    print (f"you are {output} kilograms")
else:
    output = int(weight) / 0.45
    print (f"you are {output} pounds")
    
