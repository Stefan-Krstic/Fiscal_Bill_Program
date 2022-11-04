def Stavka(naziv, cena):
    return {
        'naziv' : naziv,
        'cena'  : cena
    }
def stampajStavku(stavka, sirinaPapira):
    mestaZaNaziv = sirinaPapira - 13

    nazivZaStampu = stavka['naziv']
    if len(nazivZaStampu) > mestaZaNaziv:
        nazivZaStampu = nazivZaStampu[0:mestaZaNaziv-3]+"..."
    print( ("{0:" + str(mestaZaNaziv) + "s} {1:12.2f}").format(nazivZaStampu, stavka['cena']))
