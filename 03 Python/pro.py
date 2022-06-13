def calculte():
    mult = input("introduce un numero ")
    result = ""
    if "x" in mult:
        result = 1
        for i in mult.split("x"):
            print(type(int(i)) == int)
            if type(int(i)) == int:
                result = result *  int(i)
            else:
                result ="no valid"
    else:
        result ="no valid"
    return print(result)


def fond_in_num(params):
    list = []
    for i in range(params):
        if "6" in str(i):
            list.append(i)
    return print(list)

