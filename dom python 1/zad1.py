mesec = input("Broj meseca:")

if mesec == '1' or mesec == '3' or mesec == '5' or mesec == '7' or mesec == '8' or mesec == '10' or mesec == '12':
    print("31")
elif mesec == '4' or mesec == '6' or mesec == '9' or mesec == '11':
    print("30")
else:
    print("28,29")