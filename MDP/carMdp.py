from mdp import Mdp
import math
import copy

class Car(Mdp):
    def __init__(self) -> None:
        super().__init__()
            
    def allStates(self):
        return  ['Cool','Warm','Over']
    
    def allActions(self):
        return  ['Fast','Slow'] 
    
    def actionsForState(self,state):
        """ return all actions permissible for a given state"""
        if self.isNotTerminalState(state):
            return self.allActions()
        else:
            return []
        
    def isTerminalState(self, state):
        if state == 'Over': return True
        return False
    
    def reward(self, initState,action, endState):
        """ returns the reward of the combination """
        if self.isTerminalState(initState):
            return 0.0
        if action == 'Slow':
            return 1
        elif action == 'Fast':
            if   initState == 'Cool':
                return 2
            elif initState == 'Warm':
                return -10

    def transitionProbs(self,initState, action):
        """ returns a colection of (endState,Prob) resulting from applying the action to the initState """
        match initState:
            case 'Cool':
                if action == 'Slow': return [('Cool',1.0)]
                if action == 'Fast': return [('Cool',0.5),('Warm',0.5)]
            case 'Warm':
                if action == 'Slow': return [('Cool',0.5),('Warm',0.5)]
                if action == 'Fast': return [('Over',1.0)]
            case _:
                raise Exception("invalid transition requested")            
    
        
# play time
car = Car()
# check
    
lambdaFactor = 0.9 # no discount in time
epsilon = 0.001
V,iters = car.value_iteration(lambdaFactor,epsilon,DEBUG=False)
print (f"U = {V} converged after {iters} iterations")
policy = car.policyFromValue(V,lambdaFactor)
print (f"Policy={policy}")
