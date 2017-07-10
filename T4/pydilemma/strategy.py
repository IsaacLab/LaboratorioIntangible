from functools import wraps
from random import randint
import abc

COOP = 'cooperate'
DEF = 'defeat'

def coop():
    return 1

def defeat():
    return 0

def swap(val):
    return 1 - val

def rnd(threshold):
    return coop() if randint(0,9) >= threshold else defeat()



class Strategy:
    """Abstract Base Class which stores state (last and second last plays)."""
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._last_play = self._last_rs = self._last_second_play = 1


    @abc.abstractmethod
    def decide(self, rs):
        """Returns the next play (cooperate or defeat) based on the own state 
        and the opponent's play in the last iteration."""
        return


    @staticmethod
    def default(play):
        """Overrides arg of the decorated function if it is None."""
        def decorate(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if args[1] is None:
                    largs = list(args)
                    largs[1] = coop() if play is COOP else defeat()
                    return fn(*tuple(largs), **kwargs)
                else:
                    return fn(*args, **kwargs)
            return wrapper
        return decorate
    
    
    @staticmethod
    def record(fn):
        """Keeps track of the last decission."""
        @wraps(fn)
        def wrapper(*args, **kwargs):
            _aux = args[0]._last_play
            args[0]._last_play = fn(*args, **kwargs)
            args[0]._last_second_play = _aux
            if args[1] is not None:
                args[0]._last_rs = args[1]
            return args[0]._last_play
        return wrapper





class Nice(Strategy):
    """Cooperates (almost) always."""
    def decide(self, _):
        return coop() if rnd(3) else defeat()



class Naive(Strategy):
    """Repeats the last play if the opponent cooperated."""
    @Strategy.default(COOP)
    @Strategy.record
    def decide(self, rs):
        return self._last_play if rs else swap(self._last_play)



class NaiveProber(Strategy):
    """Defeats with 20% chance, else repeats the last play if the opponent cooperated."""
    @Strategy.default(DEF)
    @Strategy.record
    def decide(self, rs):
        if rnd(8):
            return defeat()
        else:
            return self._last_play if rs else swap(self._last_play)



class Crazy(Strategy):
    """Cooperates with 50% chance."""
    def decide(self, _):
        return rnd(5)



class TitForTat(Strategy):
    """Plays what the opponent played last time."""
    @Strategy.default(COOP)
    def decide(self, rs):
        return rs



class TitForTwoTats(Strategy):
    """Cooperates if the opponent cooperated the last 2 times."""
    @Strategy.default(DEF)
    @Strategy.record
    def decide(self, rs):
        return rs and self._last_rs



class SmoothTitForTat(Strategy):
    """Cooperates with 10% chance, othewise like tit for tat."""
    @Strategy.default(COOP)
    def decide(self, rs):
        return coop() if rnd(9) else rs



class Selfish(Strategy):
    """Cooperates with 50% chance only if the opponent cooperated the last time."""
    @Strategy.default(DEF)
    def decide(self, rs):
        return rs and rnd(5)



class Alternate(Strategy):
    """Alternates cooperate / defeat."""
    def __init__(self):
        self._last_play = 0

    @Strategy.record
    def decide(self, _):
        return swap(self._last_play)
 
 
 
class Majority(Strategy):
    """Defects when the opponent defected more that 50% of the times."""
    def __init__(self):
        self._defcount = self._coopcount = 0

    @Strategy.default(COOP)
    def decide(self, rs):
        self._defcount += swap(rs)
        self._coopcount += rs
        return coop() if self._coopcount >= self._defcount else defeat()



class AlternateCCD(Strategy):
    """Cooperates 2 of every 3 times."""
    def __init__(self):
        self._last_play = 0

    @Strategy.record
    def decide(self, _):
        return swap(self._last_play and self._last_second_play)



class Spiteful(Strategy):
    """Cooperates until opponent defeats. Then defeats always."""
    def __init__(self):
        self._mood = coop()
  
    @Strategy.default(COOP)
    def decide(self, rs):
        self._mood = self._mood and rs
        return self._mood
            



class CustomAdapt(Strategy):
    """Abstract Base Class with common functionality for the adaptive family."""
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, init=0):
        self._weights = {0:init,1:init}
        super(CustomAdapt, self).__init__()
        
    def update(self, pairs):
        for k, v in pairs.items():
            self._weights[k] += v
        self._calibrate()
        return self

    def smax(self):
        return coop() if self._draw() else max(self._weights, key=self._weights.get)
    
    def pmax(self):
        return rnd(self._weights[0] * 10 / (1 + float(sum(self._weights.values()))))
    
    def _draw(self):
        return self._weights[0] is self._weights[1]
    
    def _calibrate(self):
        self._weights[0] = max(self._weights[0], 0)
        self._weights[1] = max(self._weights[1], 0)



    
class Adaptive(CustomAdapt):
    """Adapts to the opponent in a way that if both defeat, it favours cooperation."""
    def __init__(self):
        super(Adaptive, self).__init__()

    @Strategy.default(COOP)
    @Strategy.record
    def decide(self, rs):
        return super(Adaptive, self).update({self._last_play : rs, 
                                             swap(self._last_play) : swap(rs)}).smax()



class ProbabilisticAdaptive(CustomAdapt):
    """Like adaptive, but all the choices are random."""
    def __init__(self):
        super(ProbabilisticAdaptive, self).__init__()

    @Strategy.default(COOP)
    @Strategy.record
    def decide(self, rs):
        return super(ProbabilisticAdaptive, self).update({self._last_play : rs, 
                                                          swap(self._last_play) : swap(rs)}).pmax()
    
    
    
class SpitefulProbabilisticAdaptive(CustomAdapt):
    """Like probabilistic adaptive, but does not try to recover from a series of defeats.
       Weights increases linearly with time.
    """
    def __init__(self):
        self._counter = 0
        super(SpitefulProbabilisticAdaptive, self).__init__()

    @Strategy.default(COOP)
    @Strategy.record
    def decide(self, rs):
        self._counter += 1
        return super(SpitefulProbabilisticAdaptive, self).update({self._last_play and rs : self._counter}).pmax()



class DomainBasedAdaptive(CustomAdapt):
    """Like adaptive, but updates are weighted by matrix payouts."""
    def __init__(self, matrix):
        self._matrix = matrix
        super(DomainBasedAdaptive, self).__init__(5)

    @Strategy.default(COOP)
    @Strategy.record
    def decide(self, rs):
        w = self._matrix[(self._last_play, rs)]
        return super(DomainBasedAdaptive, self).update({self._last_play : w[0], 
                                                        swap(self._last_play) : w[1]}).smax()


