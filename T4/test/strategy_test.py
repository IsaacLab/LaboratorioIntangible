from pydilemma import strategy, game_play
import unittest


class Test(unittest.TestCase):

    def testTitForTat(self):
        titfortat = strategy.TitForTat()
        self.assertEqual(titfortat.decide(None), 1)
        self.assertEqual(titfortat.decide(1), 1)
        self.assertEqual(titfortat.decide(0), 0)
        
        
    def testNaive(self):
        naive = strategy.Naive()
        self.assertEqual(naive.decide(None), 1)
        self.assertEqual(naive._last_play, 1)
        self.assertEqual(naive._last_rs, 1)

        naive._last_play = 0
        self.assertEqual(naive.decide(naive._last_rs), 0)
        self.assertEqual(naive._last_play, 0)
        self.assertEqual(naive._last_rs, 1)
        
        naive._last_rs = 0
        self.assertEqual(naive.decide(naive._last_rs), 1)
        self.assertEqual(naive._last_play, 1)
        self.assertEqual(naive._last_rs, 0)


    def testTitForTwoTats(self):
        titfortat = strategy.TitForTwoTats()
        self.assertEqual(titfortat.decide(None), 0)
        titfortat.decide(1)
        self.assertEqual(titfortat.decide(1), 1)
        self.assertEqual(titfortat.decide(0), 0)
        self.assertEqual(titfortat.decide(0), 0)
        self.assertEqual(titfortat.decide(1), 0)
        self.assertEqual(titfortat.decide(1), 1)


    def testAlternate(self):
        alternate = strategy.Alternate()
        self.assertEqual(alternate.decide(None), 1)
        self.assertEqual(alternate.decide(1), 0)
        self.assertEqual(alternate.decide(1), 1)
        self.assertEqual(alternate.decide(0), 0)


    def testAlternateCCD(self):
        alternate = strategy.AlternateCCD()
        self.assertEqual(alternate.decide(None), 1)
        self.assertEqual(alternate.decide(1), 1)
        self.assertEqual(alternate.decide(0), 0)
        self.assertEqual(alternate.decide(1), 1)
        

    def testSpiteful(self):
        spiteful = strategy.Spiteful()
        self.assertEqual(spiteful.decide(None), 1)
        self.assertEqual(spiteful.decide(1), 1)
        self.assertEqual(spiteful.decide(0), 0)
        self.assertEqual(spiteful.decide(0), 0)
        self.assertEqual(spiteful.decide(1), 0)
        
        
    def testMajority(self):
        majority = strategy.Majority()
        self.assertEqual(majority.decide(None), 1)
        self.assertEqual(majority.decide(1), 1)
        self.assertEqual(majority.decide(0), 1)
        self.assertEqual(majority.decide(0), 1)
        self.assertEqual(majority.decide(0), 0)
        self.assertEqual(majority.decide(1), 1)
        
        
    def testAdaptive(self):
        adaptive = strategy.Adaptive()
        self.assertEqual(adaptive.decide(None), 1)
        self.assertEqual(adaptive.decide(1), 1)
        self.assertEqual(adaptive.decide(0), 1)
        self.assertEqual(adaptive.decide(0), 1)
        self.assertEqual(adaptive.decide(0), 0)
        self.assertEqual(adaptive.decide(1), 0)

    
    def testDomainBasedAdaptive(self):
        dba = strategy.DomainBasedAdaptive(game_play.BOARDS['PrisonerMatrix'])
        self.assertEqual(dba.decide(1), 1)
        self.assertEqual(dba.decide(0), 0)
        self.assertEqual(dba.decide(1), 0)
        self.assertEqual(dba.decide(1), 0)
        self.assertEqual(dba.decide(0), 0)

        
    def testSpitefulProbabilisticAdaptiveState(self):
        spa = strategy.SpitefulProbabilisticAdaptive()
        spa.decide(None)
        spa.decide(1)
        spa.decide(0)        
        self.assertEqual(spa._counter, 3)
        self.assertEqual(spa._weights[0], 3)
        self.assertEqual(spa._weights[1], 3)


if __name__ == "__main__":
    unittest.main()