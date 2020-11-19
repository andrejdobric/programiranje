file = open("korisnici.txt")

korisnici = []

for line in file:
    items = line.split('\n')
    for i in items:
        if i != '':
            korisnici.append(i)

for korisnik in korisnici:
    podaci = korisnik.split('|')
    print("Ime korisnika:" + podaci[0])
    print("Lozinka:" + podaci[1])


file.close()