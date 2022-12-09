from analiza_mreza import Analiza
from distutils.log import info
from operator import le
from traceback import print_tb
import networkx as nx
import klasterabilnost as kl
import os

path = os.getcwd() + "/res/realne_mreze/wiki-RfA.txt"
f = open(path, "r")


korisnik = dict()
idKorisnika = 0
infoOGranama = dict()
input = nx.Graph()
input.add_nodes_from(range(11381))
while(linija := f.readline()):

    if linija.startswith("SRC"):
        token = linija.split(":")
        k = token[1].replace("\n", "")
        if not k in korisnik:
            korisnik[k] = idKorisnika
            src = idKorisnika
            idKorisnika+=1
        else:
            src = korisnik[k]

    elif linija.startswith("TGT"):
        token = linija.split(":")
        k = token[1].replace("\n", "")
        if not k in korisnik:
            korisnik[k] = idKorisnika
            tgt = idKorisnika
            idKorisnika+=1
        else:
            tgt = korisnik[k]


    elif linija.startswith("VOT"):
        token = linija.split(":")
        odnos = int(token[1])

        if odnos == 0:
            continue

        if tgt != src:
            if src < tgt:
                grana = (src, tgt)
            else:
                grana = (tgt, src)
            #input.add_edge(src, tgt)
            if (not grana in infoOGranama): 
                infoOGranama[grana] = odnos
            elif odnos == -1:
                infoOGranama[grana] = -1

f.close()

input.add_edges_from(list(infoOGranama.keys()))
nx.set_edge_attributes(input, infoOGranama, "znak")
graf = kl.Klasteri(input)


a = Analiza(input)

#print(a.analiziranje())
#print(a.struktura_koalicija())
#print(a.struktura_najveceg_klastera_u_odnosu_na_mrezu())
#print(a.statistika_grana_MK())
#print(a.negativne_iz_trivijalnih())
#print(a.zajednicki_neprijatelji_klike())


