from random import shuffle
from collections import OrderedDict
from pydilemma.game_play import *


OUTLAST_THRESHOLD = 70
SURVIVE_THRESHOLD = 50
INITIAL_POPULATION = 50


def predicate(comparable):
    def compare(player):
        return player.score >= comparable
    return compare

outlast = predicate(OUTLAST_THRESHOLD)
survive = predicate(SURVIVE_THRESHOLD)
 

class Generational:
    """ Performs a generational game with the following rules:
    1 - There is a initial queue filled randomly with strategies in STRATEGIES.
    2 - It pulls the first 2 players of the queue and performs a game with MAX_ROUNDS rounds per game.
    3 - If one player reaches OUTLAST_THRESHOLD points, 2 players with the same strategy will be added to the queue.
        At that time, if the other one has more than SURVIVE_THRESHOLD points, 1 player with the same strategy will
        be added to the queue. Both scores reset.
    4 - Repeat until queue is empty or GENERATIONS limit has reached.""" 
    
    def __init__(self, matrix, strategies, generations, rounds=50):
        self._matrix = matrix
        self._generations = generations
        self._rounds = rounds
        self._queue = []
        for idx in range(INITIAL_POPULATION):
            self._queue.append(strategies[idx % len(strategies)])
        shuffle(self._queue)
    
    
    def start(self):
        generation_idx = 0
        while len(self._queue) > 1 and generation_idx < self._generations:
            generation_idx += self._next_generation()
        self._report_results(generation_idx)
       
                
    def _next_generation(self):
        competitors = self._take_players()
        game = Game(competitors, self._matrix, None)
        for _ in range(self._rounds):
            game.play()
            self._update_population(*competitors)
        return 1    

                   
    def _update_population(self, player, opponent, toReverse=True):
        if outlast(player) :
            self._replicate(player, 2)
            if outlast(opponent):
                self._replicate(opponent, 2)
            elif survive(opponent):
                self._replicate(opponent)
            Generational.reset(player, opponent)
        elif toReverse:
            self._update_population(opponent, player, False)
    
            
    @staticmethod
    def reset(*players):
        [player.reset() for player in players]
    
    
    def _replicate(self, player, times=1):
        [self._queue.insert(0, player.strategy) for _ in range(times)]
            
    
    def _take_players(self):
        return [self._take_player('Alice'), self._take_player('Bob')]


    def _take_player(self, name):
        strategy = self._queue.pop()
        if 'DomainBased' in strategy:
            return Player(name, globals()[strategy](BOARDS[self._matrix]))
        else:
            return Player(name, globals()[strategy]())

    
    def _report_results(self, generations):
        print('Population size after {0} generations is {1}'.format(generations, len(self._queue)))
        groups = {}
        [groups.update({individual: self._queue.count(individual)}) for individual in self._queue]
        totals = sum(groups.values())
        for individual, freq in OrderedDict(sorted(groups.items(), key=lambda t: t[1], reverse=True)).items():
            if freq * 100 / totals > 1:
                print('{0}% of the population are {1}'.format(round((freq * 100 / totals), 1), individual))
        
        
        

if __name__ == "__main__":
    """A demo to see how different populations evolve."""
    
    # Initial population has 50 individuals and each match has 50 rounds.
    
    # Lets see what happens after 200 generations...


    # Mostly good guys...
    Generational('PrisonerMatrix', ['TitForTat', 'Alternate', 'Majority', 'Naive', 'Nice'], 200).start()
    # Population size after 200 generations is 329
    # 37.0% of the population are TitForTat
    # 34.0% of the population are Naive
    # 21.0% of the population are Majority
    # 3.0% of the population are Nice
    # 2.0% of the population are Alternate


    # Quite a lot genetic variability, eh? All the strategies managed to survive!

    
    # What about having mostly bad guys?
    Generational('PrisonerMatrix', ['TitForTwoTats', 'Alternate', 'Majority', 'Selfish', 'Spiteful'], 200).start()
    # Population size after 200 generations is 350
    # 54.0% of the population are Spiteful
    # 45.0% of the population are Majority
    
    
    # (Don't worry about 54 + 45 not beeing 100. The minorities are excluded from the output.)
    
    
    # And some good, some bad guys mixed togheter...    
    Generational('PrisonerMatrix', ['Nice', 'AlternateCCD', 'TitForTat', 'Selfish', 'Spiteful'], 200).start()
    # Population size after 200 generations is 324
    # 63.0% of the population are Spiteful
    # 34.0% of the population are TitForTat


    # Not a chance for Nice or AlternateCCD. Lets swap one of them with an adaptive strategy!
    # This DamainBasedAdaptive gathers information of the payout matrix to make his choices...
    Generational('PrisonerMatrix', ['Nice', 'DomainBasedAdaptive', 'TitForTat', 'Selfish', 'Spiteful'], 200).start()
    # Population size after 200 generations is 388
    # 35.0% of the population are TitForTat
    # 34.0% of the population are Spiteful
    # 27.0% of the population are DomainBasedAdaptive

        
    # DomainBasedAdaptive manages to survive, but SpitefulProbabilisticAdaptive does better...
    Generational('PrisonerMatrix', ['Nice', 'SpitefulProbabilisticAdaptive', 'TitForTat', 'Selfish', 'Spiteful'], 200).start()
    # Population size after 200 generations is 372
    # 45.0% of the population are SpitefulProbabilisticAdaptive
    # 27.0% of the population are Spiteful
    # 25.0% of the population are TitForTat
    

    # So far, so good. Now, lets move into a more challenging payout matrix...
    
    # The fearsome ChickenMatrix!
    Generational('ChickenMatrix', ['Nice', 'AlternateCCD', 'TitForTat', 'Selfish', 'Spiteful'], 200).start()
    # Population size after 25 generations is 0
    
    
    # Oops...


    # That one was too hard, no one survived! 
    # Lets try 100 rounds per match, to give the players more chances to replicate themselves...
    Generational('ChickenMatrix', ['Nice', 'AlternateCCD', 'TitForTat', 'Selfish', 'Spiteful'], 200, 100).start()
    # Population size after 200 generations is 360
    # 64.0% of the population are TitForTat
    # 35.0% of the population are Spiteful
    
    
    # Looks better, but not a huge difference comparing with the PrisonerMatrix.
    # Lets put into play our kick-ass adaptive strategy...
    Generational('ChickenMatrix', ['Nice', 'SpitefulProbabilisticAdaptive', 'TitForTat', 'Selfish', 'Spiteful'], 200, 100).start()
    # Population size after 200 generations is 384
    # 50.0% of the population are Spiteful
    # 25.0% of the population are SpitefulProbabilisticAdaptive
    # 25.0% of the population are TitForTat


    # Hummm... not too bad. The ChickenMatrix resolves the defeat-defeat situations with a high penalty.
    # The domain-based adaptive strategy should use this information to avoid mutual destruction and positionate itself something higher...
    Generational('ChickenMatrix', ['Nice', 'DomainBasedAdaptive', 'TitForTat', 'Selfish', 'Spiteful'], 200, 100).start()
    # And here we go!
    #     
    # Population size after 200 generations is 386
    # 41.0% of the population are DomainBasedAdaptive
    # 33.0% of the population are Spiteful
    # 24.0% of the population are TitForTat
    

    # That's cool, but really, nothing can beat a bunch of well-intentioned guys!
    Generational('ChickenMatrix', ['Naive', 'TitForTat', 'ProbabilisticAdaptive'], 200, 100).start()
    # Population size after 200 generations is 450
    # 34.0% of the population are ProbabilisticAdaptive
    # 33.0% of the population are TitForTat
    # 32.0% of the population are Naive
    
    # Did you see that? Birth rate is 20%-30% higher!! 