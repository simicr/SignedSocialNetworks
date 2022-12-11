# Signed Social networks analysis

Signed Social networks can be seen as a special case of Social networks, that maps each link with a sign. A link can be positive (+, 1, +1 etc) and that
represent that two nodes are friends, on the other hand a negative link (-, -1 etc) represents that the two connected nodes are foes. 

All of the code is written in Serbian so it can be tricky for non-speakers, the plan is to translate and make it more readable in the future.

## About the functionality
In this project, written for an intro in Social networks course at the Faculty of Sciences, Novi Sad, Serbia, the main function that can be seen in 
<b>klasterabilnost.py</b>. There we check if a given network can be partitioned into clussters where inter links are negative and intro are positive, this is achieved with the method <b>Klasteri.je_klasterabilno</b>. The <b>Klasteri.grane_koje_ruse_klasterabilnost</b> method returns a set of all intro links that are negative. The <b>Klasteri.dobij_sve_klastere</b> and <b>Klasteri.dobij_podeljene_klastere</b> methods return all clusters, where in the second method they are divided in those who have and those who do not have negative intro links.<Klasteri.dobij_mrezu_klastera> method returns a small network where nodes/entities are the clusters and are connected only if there is a inter negative link between them.


## Testing

Testing was done in two parts. First part hand written test were tested in <b>testiranje.py</b>. The test cases can be seen in the file <b>res/testovi</b>.
Second part of the testing was done over large random generated tests in <b>testiranje_random_mreze.py</b>. With the method <b>__oznaceni_Erdos_Renji</b>, I modified the classic <a href="https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model">ER Model</a> for signed networks. All tests were passed.


## Analysis of real world networks

Analysis of real world networks was done over: soc-sign-Slashdot090221, wiki-RfA, soc-sign-epinions, soc-sign-bitcoin-alpha, soc-sign-bitcoin-otc. All of the networks can be found <a href="https://snap.stanford.edu/data/">here</a>. The results are not public yet, they first have to be translated from Serbian.

