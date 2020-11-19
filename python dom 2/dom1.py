sent = input("Upisite recenicu:")
reci = sent.split()
j = 0

for i in reci:
    slovo = reci[j][0]
    print(slovo.upper(), end='')
    j += 1
