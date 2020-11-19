file = open("korisnici.txt", "a", encoding = 'utf-8')

ime = input("Korisnicko ime:")
lozinka = input("Lozinka:")

file.write(ime + "|" + lozinka + "\n")

file.close()