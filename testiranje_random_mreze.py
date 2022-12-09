from operator import ne
from random import random
from random import choice
import unittest
import networkx as nx
from scipy import rand
import klasterabilnost as kl


class TestiranjeRandom(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.__test1 = self.__oznaceni_Erdos_Renji(100, 150, 0.9, True)
        self.__test2 = self.__oznaceni_Erdos_Renji(100, 150, 0.9, False)
        self.__test3 = self.__oznaceni_Erdos_Renji(250, 250, 0.9, False)
        self.__test4 = self.__oznaceni_Erdos_Renji(250, 250, 0.9, True)
        self.__test5 = self.__oznaceni_Erdos_Renji(500, 1000, 0.9, True)
        self.__test6 = self.__oznaceni_Erdos_Renji(500, 1000, 0.9, False)
        self.__test7 = self.__oznaceni_Erdos_Renji(1000, 2500, 0.9, False)
        self.__test8 = self.__oznaceni_Erdos_Renji(1000, 2500, 0.9, True)


    def test_n01(self):
        odgovor = kl.Klasteri(self.__test1["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test1["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test1["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test1["sve komp"])
        self.assertCountEqual(koalicije, self.__test1["koalicije"])
        self.assertCountEqual(ostali, self.__test1["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test1["mreza klastera"]))

    def test_n02(self):
        odgovor = kl.Klasteri(self.__test2["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test2["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test2["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test2["sve komp"])
        self.assertCountEqual(koalicije, self.__test2["koalicije"])
        self.assertCountEqual(ostali, self.__test2["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test2["mreza klastera"]))

    def test_n03(self):
        odgovor = kl.Klasteri(self.__test3["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test3["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test3["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test3["sve komp"])
        self.assertCountEqual(koalicije, self.__test3["koalicije"])
        self.assertCountEqual(ostali, self.__test3["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test3["mreza klastera"]))
    
    def test_n04(self):
        odgovor = kl.Klasteri(self.__test4["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test4["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test4["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test4["sve komp"])
        self.assertCountEqual(koalicije, self.__test4["koalicije"])
        self.assertCountEqual(ostali, self.__test4["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test4["mreza klastera"]))       

    def test_n05(self):
        odgovor = kl.Klasteri(self.__test5["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test5["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test5["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test5["sve komp"])
        self.assertCountEqual(koalicije, self.__test5["koalicije"])
        self.assertCountEqual(ostali, self.__test5["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test5["mreza klastera"])) 
    
    def test_n06(self):
        odgovor = kl.Klasteri(self.__test6["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test6["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test6["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test6["sve komp"])
        self.assertCountEqual(koalicije, self.__test6["koalicije"])
        self.assertCountEqual(ostali, self.__test6["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test6["mreza klastera"])) 

    def test_n07(self):
        odgovor = kl.Klasteri(self.__test7["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test7["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test7["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test7["sve komp"])
        self.assertCountEqual(koalicije, self.__test7["koalicije"])
        self.assertCountEqual(ostali, self.__test7["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test7["mreza klastera"])) 
    
    def test_n08(self):
        odgovor = kl.Klasteri(self.__test8["mreza"])
        self.assertEqual(odgovor.je_klasterabilno(), self.__test8["klasterabilna"])
        self.assertSetEqual(odgovor.grane_koje_ruse_klasterabilnost(), self.__test8["grane koje ruse"])

        svi = []
        koalicije = []
        ostali = []
        k = odgovor.dobij_podeljene_klastere()
        for e in k["koalicije"]:
            koalicije.append(kl.Klasteri(e))
        for e in k["klasteri"]:
            ostali.append(kl.Klasteri(e))
        svi = koalicije + ostali

        self.assertCountEqual(svi, self.__test8["sve komp"])
        self.assertCountEqual(koalicije, self.__test8["koalicije"])
        self.assertCountEqual(ostali, self.__test8["klasteri"])
        self.assertTrue(nx.is_isomorphic(odgovor.dobij_mrezu_klastera(), self.__test8["mreza klastera"])) 


    def __komponenta(self,pripadnost, e):

        for komp in pripadnost:
            if e in komp:
                return pripadnost.index(komp)


    def __oznaceni_Erdos_Renji(self,n, m, pozitivna, klasterabilna):

        mreza = nx.Graph()
        mreza.add_nodes_from(range(n))
        znak = dict()
        graneKojeRuse = set()

        preostaleGrane = []
        for i in range(n):
            for j in range(i+1,n):
                preostaleGrane.append((i,j))
        brojPozG = int(pozitivna*m)
        brojNegG = m - brojPozG

        
        pripadnost = []
        for e in range(n):
            pripadnost.append(set({e}))

        while brojPozG > 0:

            grana = choice(preostaleGrane)
            preostaleGrane.remove(grana)

            znak[grana] = 1
            mreza.add_edge(grana[0], grana[1])
            brojPozG -= 1

            k1 = self.__komponenta(pripadnost, grana[0])
            k2 = self.__komponenta(pripadnost, grana[1])
            if k1 != k2:
                komp = pripadnost[k2]
                pripadnost[k1] = pripadnost[k1] | komp
                pripadnost.remove(komp)

        mrezaKlastera = nx.Graph()
        mrezaKlastera.add_nodes_from(range(len(pripadnost)))
        jeKoalicija = dict()
        for e in range(len(pripadnost)):
            jeKoalicija[e] = 1

        if not klasterabilna:
            brojKNG = choice(range(brojNegG))
            if brojKNG == 0:
                brojKNG = 1

            brojNegG -= brojKNG

            while brojKNG > 0:
                grana = choice(preostaleGrane)
                k1 = self.__komponenta(pripadnost, grana[0])
                k2 = self.__komponenta(pripadnost, grana[1])
                if k1 != k2:
                    continue            
                
                brojKNG -= 1
                preostaleGrane.remove(grana)
                znak[grana] = -1
                mreza.add_edge(grana[0], grana[1])
                graneKojeRuse.add(grana)
                jeKoalicija[k1] = -1
    
        
        while brojNegG > 0:

            grana = choice(preostaleGrane)
            k1 = self.__komponenta(pripadnost, grana[0])
            k2 = self.__komponenta(pripadnost, grana[1])
            
            if k1 == k2:
                continue
            
            brojNegG -= 1
            preostaleGrane.remove(grana)
            znak[grana] = -1
            mreza.add_edge(grana[0], grana[1])
            mrezaKlastera.add_edge(k1, k2)

        nx.set_node_attributes(mrezaKlastera, jeKoalicija, "koalicija")
        nx.set_edge_attributes(mreza, znak, "znak")



        svi = []
        koalicije = []
        ostali = []
        
        for e in pripadnost:
            novi = nx.Graph(nx.induced_subgraph(mreza,list(e)))

            svi.append(novi)
            ok = True
            for grane in novi.edges:
                
                if grane[0] > grane[1]:
                    grane = (grane[1], grane[0])
                if znak[grane] == -1:
                    ostali.append(novi)
                    ok = False
                    break
            
            if ok:
                koalicije.append(novi)


        report = dict()
        report["mreza"] = mreza
        report["info o granama"] = znak
        report["klasterabilna"] = klasterabilna
        report["grane koje ruse"] = graneKojeRuse
        report["sve komp"] = svi
        report["koalicije"] = koalicije
        report["klasteri"] = ostali
        report["mreza klastera"] = mrezaKlastera
        report["info o klasterima"] = jeKoalicija
        return report

unittest.main()
    

