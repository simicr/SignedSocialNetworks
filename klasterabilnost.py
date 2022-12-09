from __future__ import annotations
from networkx.utils import nodes_equal
from networkx.utils import edges_equal
import networkx as nx
import sys, threading
sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)

class Klasteri:

    def __init__(self, input:nx.Graph = None):
        
        if(input == None):
            self.graf = nx.Graph()
        else:
            self.graf = nx.Graph(input)

    def __str__(self) -> str:
        cvorovi = self.graf.nodes
        grane = self.graf.edges
        return str(cvorovi)+ " " + str(grane)

    def toNetworkX(self):
        return self.graf

    def __eq__(self, o: object) -> bool:
        
        if o is self:
            return True
        if o == None:
            return False

        if not isinstance(o, (Klasteri, nx.Graph)):
            return False
        
        other = o
        if isinstance(o, Klasteri):
            other = o.toNetworkX()

        jednaki = True
        if not nodes_equal(other.nodes, self.graf.nodes):
            jednaki = False
        if not edges_equal(other.edges, self.graf.edges):
            jednaki = False

        return jednaki
        

    
    def __je_negativna_grana(self,cvor1, cvor2, znak:dict) -> bool:
        if (cvor1, cvor2) in znak:
            return znak[(cvor1, cvor2)] == -1
        return znak[(cvor2, cvor1)] == -1

    def __poztitivan_DFS(self, znak:dict, cvor, visited:set) -> None:

        for komsije in list(nx.neighbors(self.graf, cvor)):
            if(komsije not in visited and not self.__je_negativna_grana(cvor, komsije, znak)):
                visited.add(komsije)
                self.__poztitivan_DFS(znak,komsije,visited)

    def __pozitivne_komponente(self, znak:dict, pripadnostKlasteru:dict):
        
        komp = 0
        for n in self.graf.nodes:
            if not n in pripadnostKlasteru:
                visited = set({n})
                self.__poztitivan_DFS(znak, n, visited)
                for e in visited:
                    pripadnostKlasteru[e] = komp
                komp+=1

        return komp

    def je_klasterabilno(self, znak:dict=None) -> bool:
        if znak == None:
            znak = nx.get_edge_attributes(self.graf, "znak")

        ruse = len(self.grane_koje_ruse_klasterabilnost(znak))
        return  ruse == 0

    def grane_koje_ruse_klasterabilnost(self, znak:dict=None) -> set:

        if znak == None:
            znak = nx.get_edge_attributes(self.graf, "znak")

        graneKojeRuse = set()
        pripadnostKlasteru = dict()
        self.__pozitivne_komponente(znak, pripadnostKlasteru)

        for grana in self.graf.edges():
            if self.__je_negativna_grana(grana[0], grana[1], znak):
                if pripadnostKlasteru[grana[0]] == pripadnostKlasteru[grana[1]]:
                    if grana[0] < grana[1]:
                        graneKojeRuse.add(grana)
                    else:
                        graneKojeRuse.add((grana[1], grana[0]))
                

        return graneKojeRuse


    def dobij_sve_klastere(self, znak:dict=None) -> list:
    
        if znak == None:
            znak = nx.get_edge_attributes(self.graf, "znak")

        klasteri = []
        visitedGlobally = set()
        visitedLocally = set()
        for cvor in self.graf.nodes():
            if cvor not in visitedGlobally:
                visitedGlobally.add(cvor)
                visitedLocally = {cvor}
                self.__poztitivan_DFS(znak, cvor, visitedLocally)

                klaster = nx.Graph(nx.induced_subgraph(self.graf, visitedLocally))
                klasteri.append(klaster)
                visitedGlobally = visitedGlobally | visitedLocally
        return klasteri

    def dobij_podeljene_klastere(self, znak:dict=None) -> dict:

        if znak == None:
            znak = nx.get_edge_attributes(self.graf, "znak")

        koalicije = []
        neKoalicije = []
    
        sviKlasteri = self.dobij_sve_klastere(znak)

        for klaster in sviKlasteri:
            ok = True
            for grana in klaster.edges:
                if self.__je_negativna_grana(grana[0], grana[1], znak):
                    ok = False
                    neKoalicije.append(klaster)
                    break
            
            if ok:
                koalicije.append(klaster)

        return dict({"koalicije":koalicije, "klasteri":neKoalicije})


    def dobij_mrezu_klastera(self, znak:dict=None) -> nx.Graph:
    
        if znak == None:
            znak = nx.get_edge_attributes(self.graf, "znak")
    
        mreza = nx.Graph()
        
        
        pripadnostKlasteru = dict()
        komp = self.__pozitivne_komponente(znak, pripadnostKlasteru)
        mreza.add_nodes_from(range(komp))

        jeKoalicija = dict()        
        for i in range(komp):
            jeKoalicija[i] = 1
                
        for grana in self.graf.edges:
            if self.__je_negativna_grana(grana[0], grana[1], znak):
                klaster1 = pripadnostKlasteru[grana[0]]
                klaster2 = pripadnostKlasteru[grana[1]]
                if klaster1 == klaster2:
                    jeKoalicija[pripadnostKlasteru[klaster1]] = -1
                else:
                    # dodaje se grana izmedju klastera, ukoliko vec postoji nece se dodati
                    mreza.add_edge(klaster1, klaster2)

        nx.set_node_attributes(mreza, jeKoalicija, "koalicija")
        
        return mreza
