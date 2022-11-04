import racun
import stavka

r = racun.Racun("Radnja AirSoft", "Prvomajska 2", "Niš", "2022-11-04", "01:52:00", "Stefan")

racun.dodajStavku(r, stavka.Stavka("Replika M4 VFC", 35000.00))
racun.dodajStavku(r, stavka.Stavka("Baterija 11.1v Li-Po 1500mA", 3850.33))
racun.dodajStavku(r, stavka.Stavka("Klip mid-cap", 4200.50))
racun.dodajStavku(r, stavka.Stavka("Kesa kuglica", 350.45))
racun.dodajStavku(r, stavka.Stavka("Optika RedDot", 4950.00))
racun.dodajStavku(r, stavka.Stavka("Zastitne naocare", 799.99))
racun.dodajStavku(r, stavka.Stavka("Kapa", 299.99))
racun.dodajStavku(r, stavka.Stavka("Rukavice", 350.55))

racun.prikaziRacun(r, 40)
