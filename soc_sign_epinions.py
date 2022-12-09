from analiza_mreza import Analiza
from operator import le
import networkx as nx
from numpy import inf, rint
import klasterabilnost as kl
import os

def znakBroja(broj):
    if broj > 0:
        return 1
    return -1


path = os.getcwd() + "/res/realne_mreze/soc-sign-epinions.txt"
f = open(path, "r")
f.readline()
f.readline()
f.readline()
f.readline()

nxGraf = nx.Graph()
nxGraf.add_nodes_from(range(131828))
infoOGranama = dict()
for linija in f:
    grana = linija.split("\t")
    source = int(grana[0])
    target = int(grana[1])

    if target == source:
        continue

    if infoOGranama.get((target, source)) == None:
        infoOGranama[(source,target)] = znakBroja(int(grana[2]))
    elif infoOGranama[(target, source)] == 1:
        infoOGranama[(target, source)] = znakBroja(int(grana[2]))
f.close()

nxGraf.add_edges_from(list(infoOGranama.keys()))
nx.set_edge_attributes(nxGraf, infoOGranama, "znak")

a = Analiza(nxGraf)

#print(a.analiziranje())
#print(a.struktura_koalicija())
#print(a.struktura_najveceg_klastera_u_odnosu_na_mrezu())
#print(a.statistika_grana_MK())
#print(a.negativne_iz_trivijalnih())
print(a.zajednicki_neprijatelji_klike())