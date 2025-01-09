name = input("what is your name? ")
"""if name == "Pepu" or name =="Yvonne":
    print("SA")
elif name == "Masi":
    print("Zim")
else:
    print("who? ")
    """
match name:
    case "Pepu"|"Yvonne":
        print("SA")
    case "Masi":
        print("ZIM")