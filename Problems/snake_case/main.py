input_str = input()
if input_str.islower():
    print(input_str)
elif not input_str[0].islower() and input_str[1:].islower():
    print(input_str.lower())
else:
    output = input_str[0].lower()
    for alpha in input_str[1:]:
        if alpha.islower():
            output = output + alpha
        else:
            output = output + "_" + alpha.lower()
    print(output)
