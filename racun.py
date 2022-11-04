import random
import stavka

def Racun(radnja, adresa, mesto, datum, vreme, kasir):
    r = random.Random()
    return {
        'radnja': radnja,
        'adresa': adresa,
        'mesto' : mesto,
        'datum' : datum,
        'vreme' : vreme,
        'kasir' : kasir,
        'transakcija' : int(r.random()*100000),
        'stavke': [ ]
    }
def dodajStavku(racun, stavka):
    racun['stavke'].append(stavka)

def separator(sirinaPapira):
    print("= " * (sirinaPapira//2) )

def prikaziRacun(racun, sirinaPapira):
    separator(sirinaPapira)
    print( ("{0:^" + str(sirinaPapira)+ "s}").format(racun['radnja']) )
    print( ("{0:^" + str(sirinaPapira)+ "s}").format(racun['adresa'] + ", "  + racun['mesto']) )
    separator(sirinaPapira)
    print( "Datum: " + racun['datum'] )
    print( "Vreme: " + racun['vreme'] )
    separator(sirinaPapira)
    suma = 0
    for s in racun['stavke']:
        stavka.stampajStavku(s, sirinaPapira)
        suma += s['cena']
    separator(sirinaPapira)
    porez = suma * 0.2
    cena = suma - porez
    mestaZaOznaku = sirinaPapira - 13
    print(("{0:" + str(mestaZaOznaku) + "s} {1:12.2f}").format("Ukupna cena:", cena))
    print(("{0:" + str(mestaZaOznaku) + "s} {1:12.2f}").format("Porez:", porez))
    print(("{0:" + str(mestaZaOznaku) + "s} {1:12.2f}").format("Iznos za uplatu:", suma))
    separator(sirinaPapira)
    print(("Kasir: " + racun['kasir']))
    print(("Broj tansakcije: " + str(racun['transakcija'])))
    separator(sirinaPapira)
