value = input("Enter a value: ")
if "." in value:
    int_part, deci_part = value.split(".")
    deci_part = "." + deci_part
else:
    int_part = value
    deci_part = ""

n = len(int_part)
if n <= 3:
    formated = int_part + deci_part
else:
    last3 = int_part[-3:]
    first = int_part[:-3]
    
    final_value = ""
    while len(first) > 2:
        final_value = "," + first[-2:] + final_value
        first = first[:-2]

    if first != "":
        final_value = first + final_value

    formated = final_value + "," + last3 + deci_part


print("Indian Currency Formate:", formated)

