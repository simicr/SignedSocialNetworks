from operator import le
from networkx.algorithms import community as cm
import klasterabilnost as kl
import networkx as nx

class Analiza():

    def __init__(self, input:nx.Graph) -> None:
        self.__graf = kl.Klasteri(input)
        self.__znak = nx.get_edge_attributes(input, "znak")

    
    def analiziranje(self):
        jeKlasterabilno = self.__graf.je_klasterabilno(self.__znak) 
        brojGranaKojeRuse = len(self.__graf.grane_koje_ruse_klasterabilnost(self.__znak))
        klasteri = self.__graf.dobij_podeljene_klastere(self.__znak)

        report = dict()

        report["Klasterabilno"] = jeKlasterabilno
        report["Broj grana"] = brojGranaKojeRuse
        report["Koalicije"] = len(klasteri["koalicije"])
        report["Ostali"] = len(klasteri["klasteri"])

        return report
    
    def struktura_koalicija(self):
        koalicije = self.__graf.dobij_podeljene_klastere(self.__znak)["koalicije"]
        trivijalne = 0 
        neTrivajlneKlike = 0
        ostatak = 0

        for e in koalicije:
            if len(e.nodes) == 1:
                trivijalne +=1
            else:

                if nx.density(e) == 1.0:
                    neTrivajlneKlike += 1
                else:
                    ostatak +=1

        report = dict()
        report["Trivijalne"] = trivijalne
        report["Netrivijalne klike"] = neTrivajlneKlike
        report["Ostale"] = ostatak

        return report

    def struktura_najveceg_klastera_u_odnosu_na_mrezu(self):
        klasteri = self.__graf.dobij_podeljene_klastere(self.__znak)["klasteri"]

        maks = -1
        najveci = None
        for e in klasteri:
            if len(e.nodes) > maks:
                maks = len(e.nodes)
                najveci = e

        graf = self.__graf.toNetworkX()

        report = dict()
        report["Broj cvorova"] = (len(graf.nodes), len(najveci.nodes))
        report["Broj grana"] = (len(graf.edges), len(najveci.edges))
        report["Gustine"] = (nx.density(graf), nx.density(najveci))
        report["Prosecan koef klaster"] = (nx.average_clustering(graf), nx.average_clustering(najveci))

        return report


    def statistika_grana_MK(self):
        mreza = self.__graf.dobij_mrezu_klastera(self.__znak)

        infoOCvorovima = nx.get_node_attributes(mreza, "koalicija")

        ukupno = 0
        isti = 0 
        razliciti = 0
        for e in mreza.edges:
            ukupno +=1
            if infoOCvorovima[e[0]] == infoOCvorovima[e[1]]:
                isti += 1
            else:
                razliciti +=1

        report = dict()
        report["Ukupno grana"] = ukupno
        report["Grana izmedju istih"] = isti
        report["Grana izmedju razlicitih"] = razliciti

        return report

    def mreza_klastera_to_GML(self, naziv):
        m = self.__graf.dobij_mrezu_klastera(self.__znak)
        nx.write_gml(m, naziv + ".gml")

    def negativne_iz_trivijalnih(self):
        koalicije = self.__graf.dobij_podeljene_klastere(self.__znak)["koalicije"]

        
        report = dict()
        for e in koalicije:
            if len(e.nodes) == 1:
                cvor = list(e.nodes)
                brojNeg = nx.degree(self.__graf.toNetworkX(), cvor)[cvor[0]]
                if brojNeg in report:
                    report[brojNeg] += 1
                else:
                    report[brojNeg] = 1

        
        
        return report

    def zajednicki_neprijatelji_klike(self):

        neprijatelji = set()

        k = self.__graf.dobij_podeljene_klastere(self.__znak)
        koalicije = k["koalicije"]

        negativne = set()
        for e in self.__znak.keys():
            if self.__znak[e] == -1:
                negativne.add(e)


        report = list()
        for e in koalicije:
            if len(e.nodes) > 1 and nx.density(e) == 1:
                broj = 0
                for g in negativne:
                    if (g[0] in e.nodes):
                        neprijatelji.add(g[1])
                        broj += 1
                    
                    if self.__znak[g] == -1 and (g[1] in e.nodes):
                        neprijatelji.add(g[0])
                        broj += 1
                
                report.append((broj, len(neprijatelji)))
                neprijatelji.clear()

        return report

 

        
