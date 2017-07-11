from pydilemma.strategy import *

BOARDS = {
          'FoFMatrix'       : {(1 , 1) : (1 , 1),
                               (0 , 1) : (2 , 0),
                               (1 , 0) : (0 , 2),
                               (0 , 0) : (0 , 0)},
          
          'ChickenMatrix'   : {(1 , 1) : (1 , 1),
                               (0 , 1) : (3 ,-3),
                               (1 , 0) : (-3, 3),
                               (0 , 0) : (-6,-6)},
          
          'PrisonerMatrix'  : {(1 , 1) : (2 , 2),
                               (0 , 1) : (3 , 0),
                               (1 , 0) : (0 , 3),
                               (0 , 0) : (-2,-2)}

          }


class Game():
    """It takes a list of players, a payout matrix and a number of rounds. 
    It exposes a play() function which triggers a single match and a start() function which 'plays' 
    as many rounds as specified in constructor."""
    def __init__(self, players, matrix, rounds):
        self._players = players
        self._rounds = rounds
        self._board = BOARDS[matrix]


    def start(self):
        [self.play() for _ in range(self._rounds)]
        for player in self._players:
            print(player)
        print('*** END ***\n')


    def play(self):
        plays = [player.play() for player in self._players]
        results = Game.resolve(self._board, tuple(plays))
        [self._players[idx].update(*results[idx]) for idx in range(len(self._players))]


    @staticmethod
    def resolve(matrix, plays):
        """Given a payout matrix, and a list of plays, it returns a list of tuples
           containing the calculated payout and the opponent's play."""
        return list(zip(matrix[plays], tuple(reversed(plays))))


class Player:
    """A player has a name, a strategy, a score and a context.
       The context is the opponent's last play.
       The result of the next play will depend on the context (mutable) and the strategy (immutable).""" 
    def __init__(self, name, strategy):
        self._name = name
        self._strategy = strategy
        self._score = 0
        self._context = None
    
    @property
    def score(self):
        return self._score
    
    @property
    def name(self):
        return self._name
    
    @property
    def strategy(self):
        return self._strategy.__class__.__name__

    def play(self):
        return self._strategy.decide(self._context)

    def update(self, score, rs):
        self._score += score
        self._context = rs
        
    def reset(self):
        self._score = 0
                
    def __str__(self):
        return self.name + ' scored ' + str(self.score) + ' with strategy ' + self.strategy
    



def play_with(strategy1, strategy2, rounds):
    rounds_per_game = rounds
    alice = Player('Alice', globals()[strategy1]()) 
    bob = Player('Bob', globals()[strategy2]()) 
    Game([alice, bob], 'PrisonerMatrix', rounds_per_game).start()




if __name__ == "__main__":
    """A simple demo."""
    
    # Lets kick some matches with a Prissoner's Dilemma matrix and 100 rounds per match...    
    
    play_with('Nice', 'TitForTat')
    # These 2 guys get along very well... 
    #
    # Alice scored 151 points with strategy Nice
    # Bob scored 151 points with strategy TitForTat


    play_with('Nice', 'Naive')
    # Naive tries to get advantage of what works...
    #
    # Alice scored 82 with strategy Nice
    # Bob scored 139 with strategy Naive
    
    
    play_with('Nice', 'NaiveProber')
    # And Naive Prober tries aggressively...
    #
    # Alice scored 41 with strategy Nice
    # Bob scored 167 with strategy NaiveProber


    play_with('NaiveProber', 'Majority')
    # But the NaiveProber can't compete against a Majority!
    #
    # Alice scored -102 with strategy NaiveProber
    # Bob scored 24 with strategy Majority
    
    
    play_with('SmoothTitForTat', 'TitForTwoTats')
    # On the other hand, Tit For Tat cousins destroy each other...
    #
    # Alice scored -182 points with strategy SmoothTitForTat
    # Bob scored -155 points with strategy TitForTwoTats
    
    
    play_with('Selfish', 'Crazy')
    # A Selfish guy gets a good chance against someone who doesn't know
    # too much about the game...
    #
    # Alice scored 66 points with strategy Selfish
    # Bob scored -12 points with strategy Crazy
    
 
    play_with('Alternate', 'Majority')
    # Some really simple strategies can get good results sometimes...
    #
    # Alice scored 250 with strategy Alternate
    # Bob scored 100 with strategy Majority
    
    
    play_with('SpitefulProbabilisticAdaptive', 'Alternate')
    # But there are smart strategies out there...
    #
    # Alice scored 53 with strategy SpitefulProbabilisticAdaptive
    # Bob scored -79 with strategy Alternate

    play_with('SpitefulProbabilisticAdaptive', 'Selfish')
    # ...who doesn't let the bad guys win...
    #
    # Alice scored -193 with strategy SpitefulProbabilisticAdaptive
    # Bob scored -193 with strategy Selfish

    play_with('SpitefulProbabilisticAdaptive', 'TitForTat')
    # ...look for a sustainable world...
    #
    # Alice scored 200 with strategy SpitefulProbabilisticAdaptive
    # Bob scored 200 with strategy TitForTat    
    
    play_with('SpitefulProbabilisticAdaptive', 'Nice')
    # ...and still can't avoid taking advantage of the weaker!
    #
    # Alice scored 161 with strategy SpitefulProbabilisticAdaptive
    # Bob scored -49 with strategy Nice

