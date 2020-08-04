# Max of 2 numbers

a = input("\nEnter 1st number : ")
b = input("\nEnter 2nd number : ")

if a.isnumeric() and b.isnumeric():
    if int(a) > int(b):
        print("\n{} is the greater number.".format(a))
    elif int(b) > int(a):
        print("\n{} is the greater number.".format(b))
    else:
        print("\nBoth the number are equal.")
else:
    print("\nInput values are not numeric.")
