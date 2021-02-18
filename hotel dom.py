class  smestaj:
    def __init__(self, naziv, adresa, grad):
        self.naziv = naziv
        self.adresa = adresa
        self.grad = grad

    def __str__(self):
        return (self.naziv,self.adresa,self.grad)

class hotel(smestaj):
    def __init__(self, naziv, adresa, grad, brojzv):
        smestaj.__init__(self, naziv, adresa, grad)
        self.brojzv = brojzv

    def __str__(self):
        return(self.naziv, self.adresa, self.grad, self.brojzv)

if __name__ == "__main__":
    Smestaj1 = smestaj('Smestaj', 'adresa 22', 'Novi Sad')

    print(Smestaj1.__str__())

    Hotel1 = hotel('Hotel', 'adresa 21', 'Novi Sad', '5')

    print(Hotel1.__str__())