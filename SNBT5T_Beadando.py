from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, tipus, ar):
        self.tipus = tipus
        self.ar = ar

    @abstractmethod
    def get_szoba_tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self):
        super().__init__("egyágyas", 20000)

    def get_szoba_tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def __init__(self):
        super().__init__("kétágyas", 30000)

    def get_szoba_tipus(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}
        self.foglalasok = {}

    def uj_szoba(self, szoba):
        self.szobak[szoba.tipus] = szoba

    def foglalas_hozzaadasa(self, szobatipus, erkezes_napja, napok_szama):
        if szobatipus in self.szobak:
            osszes_ar = self.szobak[szobatipus].ar * napok_szama
            szobaszam = len(self.foglalasok) + 1
            self.foglalasok[szobaszam] = {"Szobatipus": szobatipus, "Erkezes_napja": erkezes_napja, "Napok_szama": napok_szama, "Osszes_ar": osszes_ar}
            print(f"Sikeres foglalás. A szobád ára: {osszes_ar} Ft. Szobaszám: {szobaszam}")
        else:
            print("Nincs ilyen szobatípus.")

    def foglalas_modositasa(self, szobaszam, regi_erkezes_napja, uj_erkezes_napja):
        if szobaszam in self.foglalasok:
            self.foglalasok[szobaszam]["Erkezes_napja"] = uj_erkezes_napja
            print("Foglalás módosítva.")
        else:
            print("Nincs ilyen szobaszámú foglalás.")

    def foglalas_lemondasa(self, szobaszam, erkezes_napja):
        if szobaszam in self.foglalasok:
            if self.foglalasok[szobaszam]["Erkezes_napja"] == erkezes_napja:
                del self.foglalasok[szobaszam]
                print("Foglalás törölve.")
            else:
                print("Nem megfelelő érkezési dátum.")
        else:
            print("Nincs ilyen szobaszámú foglalás.")

    def foglalasok_listazasa(self):
        print("Foglalások:")
        for szobaszam, adatok in self.foglalasok.items():
            print(f"Szobaszám: {szobaszam}, Szobatípus: {adatok['Szobatipus']}, Érkezés napja: {adatok['Erkezes_napja']}, Tartózkodási napok száma: {adatok['Napok_szama']}, Összes ár: {adatok['Osszes_ar']} Ft")


def main():
    szalloda = Szalloda("NoLo Hotel")
    szalloda.uj_szoba(EgyagyasSzoba())
    szalloda.uj_szoba(KetagyasSzoba())

    print("\n*** NoLo Hotel szobatípusok ***")
    for tipus, szoba in szalloda.szobak.items():
        print(f"{tipus.capitalize()}: {szoba.ar} Ft/éj")

    while True:
        print("\n*** NoLo Hotel foglalási felület ***")
        print("1. Foglalás")
        print("2. Módosítás")
        print("3. Lemondás")
        print("4. Foglalások listázása")
        print("5. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            szobatipus = input("Adja meg a szobatípust (egyágyas/kétágyas): ")
            erkezes_napja = input("Adja meg az érkezés napját (YYYY-MM-DD): ")
            napok_szama = int(input("Adja meg a tartózkodási napok számát: "))
            szalloda.foglalas_hozzaadasa(szobatipus, erkezes_napja, napok_szama)
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a foglalás szobaszámát: "))
            regi_erkezes_napja = input("Adja meg a régi érkezés napját (YYYY-MM-DD): ")
            uj_erkezes_napja = input("Adja meg az új érkezés napját (YYYY-MM-DD): ")
            szalloda.foglalas_modositasa(szobaszam, regi_erkezes_napja, uj_erkezes_napja)
        elif valasztas == "3":
            szobaszam = int(input("Adja meg a foglalás szobaszámát: "))
            erkezes_napja = input("Adja meg az érkezés napját (YYYY-MM-DD): ")
            szalloda.foglalas_lemondasa(szobaszam, erkezes_napja)
        elif valasztas == "4":
            szalloda.foglalasok_listazasa()
        elif valasztas == "5":
            print("Kilépés...")
            break
        else:
            print("Nem megfelelő választás.")

if __name__ == "__main__":
    main()
