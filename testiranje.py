from cgi import test
from os import listxattr
import os
import unittest
import networkx as nx
from numpy import union1d
import klasterabilnost as kl

class Testiranje(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.__path = os.getcwd() + "/res/"

        # Pripremanje test grafova 
        self.__test1 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test1.gml"))
        self.__test2 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test2.gml"))
        self.__test3 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test3.gml"))
        self.__test4 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test4.gml"))
        self.__test5 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test5.gml"))
        self.__test6 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test6.gml"))
        self.__test7 = kl.Klasteri(nx.read_gml(self.__path +"testovi/test7.gml"))

        # Odgovori za test 1 i test 3
        # za dobij_sve_klastere i dobij_podeljene_klastere
        self.__klasteri_1_i_3 = []
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom0.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom1.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom2.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom3.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom4.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom5.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom6.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom7.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom8.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom9.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom10.gml")))
        self.__klasteri_1_i_3.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom11.gml")))
        self.__podeljeno_1_i_3 = dict()
        self.__podeljeno_1_i_3["koalicije"] = self.__klasteri_1_i_3
        self.__podeljeno_1_i_3["klasteri"] = []
        
        # Odgovori za test 2
        # za dobij_sve_klastere i dobij_podeljene_klastere   
        self.__klasteri_2 = []
        self.__klasteri_2.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_svim.gml")))
        self.__podeljeno_2 = dict()
        self.__podeljeno_2["koalicije"] = self.__klasteri_2 
        self.__podeljeno_2["klasteri"] = []

        # Odgovori za test 4
        # za dobij_sve_klastere i dobij_podeljene_klastere
        self.__klasteri_4 = []
        self.__klasteri_4.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom7.gml")))
        self.__klasteri_4.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_1_test4.gml")))
        self.__klasteri_4.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_2_test4.gml")))

        self.__podeljeno_4 = dict()
        self.__podeljeno_4["koalicije"] = [self.__klasteri_4[0]] 
        self.__podeljeno_4["klasteri"] = [self.__klasteri_4[2], self.__klasteri_4[1]]

        # Odgovori za test 5
        # za dobij_sve_klastere i dobij_podeljene_klastere
        self.__klasteri_5 = []
        self.__klasteri_5.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_1_test5.gml")))
        self.__klasteri_5.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_2_test5.gml")))
        self.__klasteri_5.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_3_test5.gml")))
        self.__podeljeno_5 = dict()
        self.__podeljeno_5["koalicije"] = [self.__klasteri_5[0],  self.__klasteri_5[1]] 
        self.__podeljeno_5["klasteri"] = [self.__klasteri_5[2]]

        # Odgovori za test 6
        # za dobij_sve_klastere i dobij_podeljene_klastere
        self.__klasteri_6 = []
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_1_test6.gml")))
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_2_test6.gml")))
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_3_test6.gml")))
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom0.gml")))
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom1.gml")))
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom6.gml")))
        self.__klasteri_6.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom7.gml")))
        self.__podeljeno_6 = dict()
        self.__podeljeno_6["koalicije"] = self.__klasteri_6 
        self.__podeljeno_6["klasteri"] = []

        # Odgovori za test 7
        # za dobij_sve_klastere i dobij_podeljene_klastere
        self.__klasteri_7 = []
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom0.gml")))
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom2.gml")))
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom3.gml")))
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom11.gml")))
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_sa_cvorom5.gml")))
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_1_test7.gml")))
        self.__klasteri_7.append(kl.Klasteri(nx.read_gml(self.__path +"klasteri_mreze/klaster_2_test7.gml")))
        self.__podeljeno_7 = dict()
        self.__podeljeno_7["koalicije"] = self.__klasteri_7 
        self.__podeljeno_7["klasteri"] = []

        # Odgovori za sve testove
        # za dobij_mrezu_klastera
        self.__mreza1 = nx.read_gml(self.__path + "mreze/mreza_klastera_1.gml")
        self.__mreza2 = nx.read_gml(self.__path + "mreze/mreza_klastera_2.gml")
        self.__mreza3 = nx.read_gml(self.__path + "mreze/mreza_klastera_3.gml")
        self.__mreza4 = nx.read_gml(self.__path + "mreze/mreza_klastera_4.gml")
        self.__mreza5 = nx.read_gml(self.__path + "mreze/mreza_klastera_5.gml")
        self.__mreza6 = nx.read_gml(self.__path + "mreze/mreza_klastera_6.gml")
        self.__mreza7 = nx.read_gml(self.__path + "mreze/mreza_klastera_7.gml")

    def test_je_klasterabilno(self):
        self.assertTrue(self.__test1.je_klasterabilno())
        self.assertTrue(self.__test2.je_klasterabilno())
        self.assertTrue(self.__test3.je_klasterabilno())
        self.assertTrue(self.__test6.je_klasterabilno())
        self.assertTrue(self.__test7.je_klasterabilno())
        self.assertFalse(self.__test4.je_klasterabilno())
        self.assertFalse(self.__test5.je_klasterabilno())
    
    def test_grane_koje_ruse_klasterabilnost(self):
        self.assertSetEqual(self.__test1.grane_koje_ruse_klasterabilnost(), set({}))
        self.assertSetEqual(self.__test2.grane_koje_ruse_klasterabilnost(), set({}))
        self.assertSetEqual(self.__test3.grane_koje_ruse_klasterabilnost(), set({}))
        self.assertSetEqual(self.__test6.grane_koje_ruse_klasterabilnost(), set({}))
        self.assertSetEqual(self.__test7.grane_koje_ruse_klasterabilnost(), set({}))
        self.assertSetEqual(self.__test4.grane_koje_ruse_klasterabilnost(), set({(1, 11), (6, 8)}))
        self.assertSetEqual(self.__test5.grane_koje_ruse_klasterabilnost(), set({(6, 9), (7, 8), (6, 10)}))

    def test_dobij_sve_klastere(self):
        self.assertCountEqual(self.__test1.dobij_sve_klastere(), self.__klasteri_1_i_3)
        self.assertCountEqual(self.__test2.dobij_sve_klastere(), self.__klasteri_2)
        self.assertCountEqual(self.__test3.dobij_sve_klastere(), self.__klasteri_1_i_3)
        self.assertCountEqual(self.__test4.dobij_sve_klastere(), self.__klasteri_4)
        self.assertCountEqual(self.__test5.dobij_sve_klastere(), self.__klasteri_5)
        self.assertCountEqual(self.__test6.dobij_sve_klastere(), self.__klasteri_6)
        self.assertCountEqual(self.__test7.dobij_sve_klastere(), self.__klasteri_7)

    def test_dobij_podeljene_klastere(self):
        trenutno = self.__test1.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_1_i_3["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_1_i_3["klasteri"])
        trenutno = self.__test3.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_1_i_3["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_1_i_3["klasteri"])
        trenutno = self.__test2.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_2["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_2["klasteri"])
        trenutno = self.__test4.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_4["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_4["klasteri"])
        trenutno = self.__test5.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_5["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_5["klasteri"])
        trenutno = self.__test6.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_6["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_6["klasteri"])
        trenutno = self.__test7.dobij_podeljene_klastere()
        self.assertCountEqual(trenutno["koalicije"], self.__podeljeno_7["koalicije"])
        self.assertCountEqual(trenutno["klasteri"], self.__podeljeno_7["klasteri"])

    def test_dobij_mrezu_klastera(self):
        self.assertTrue(nx.is_isomorphic(self.__test1.dobij_mrezu_klastera(), self.__mreza1))
        self.assertTrue(nx.is_isomorphic(self.__test2.dobij_mrezu_klastera(), self.__mreza2))
        self.assertTrue(nx.is_isomorphic(self.__test3.dobij_mrezu_klastera(), self.__mreza3))
        self.assertTrue(nx.is_isomorphic(self.__test4.dobij_mrezu_klastera(), self.__mreza4))
        self.assertTrue(nx.is_isomorphic(self.__test5.dobij_mrezu_klastera(), self.__mreza5))
        self.assertTrue(nx.is_isomorphic(self.__test6.dobij_mrezu_klastera(), self.__mreza6))
        self.assertTrue(nx.is_isomorphic(self.__test7.dobij_mrezu_klastera(), self.__mreza7))
        

unittest.main()