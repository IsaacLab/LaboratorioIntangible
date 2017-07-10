import unittest
from pydilemma.generational import Generational



class Test(unittest.TestCase):


    def testEmptyGenerational(self):
        generational = Generational('PrisonerMatrix', ['TitForTat', 'Naive'], 0)
        generational.start()
        self.assertEqual(generational._queue.count('TitForTat'), 25)
        self.assertEqual(generational._queue.count('Naive'), 25)


    def test3Generations(self):
        competitors = ['TitForTat', 'Naive']
        generational = Generational('PrisonerMatrix', competitors, 2)
        #override initial population
        generational._queue = competitors
        
        generational.start()
        self.assertEqual(generational._queue.count('TitForTat'), 2)
        self.assertEqual(generational._queue.count('Naive'), 4)

        generational._next_generation()
        self.assertEqual(generational._queue.count('TitForTat'), 4)
        self.assertEqual(generational._queue.count('Naive'), 4)


    def test100Generations(self):
        generational = Generational('ChickenMatrix', ['Selfish', 'Spiteful'], 100)
        generational.start()
        self.assertEqual(len(generational._queue), 0)


if __name__ == "__main__":
    unittest.main()