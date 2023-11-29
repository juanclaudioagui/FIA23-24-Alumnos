import copy
import math

class Mdp():
    def __init__(self) -> None:
        pass
    
    def allStates(self):
        """ returns a list of possible states"""
        raise NotImplementedError
    
    def allActions(self):
        """ returns the list of possible actions"""
        raise NotImplementedError
    
    def actionsForState(self, state):
        """ return a list of actions permissible for the given state"""
        raise NotImplementedError
    
    def isTerminalState(self,state):
        raise NotImplementedError
    
    def isNotTerminalState(self,state):
        return not self.isTerminalState(state)
    
    def reward(self, initState,action, endState):
        """ returns the reward of the combination """
        raise NotImplementedError

    def transitionProbs(self, initState, action):
        """ returns a colection of (endState,Prob) resulting from applying the given action to the initState """
        raise NotImplementedError
    
    def value_iteration(self, lambdafactor, epsilon,DEBUG=True,trace=False):
        """ returns a state-value function
        inpus:
            self: an MDP with states S, actions A(s), rewards R(s, a, s 0 ) and transition probs P(s 0 |s, a)
            lambda: a discount factor
            epsilon: the maximum error allowed in the value of any state
        local variables:
            Vold , Vnew : two vectors of utilities for states in S, initialized to all-zeros
            delta: the maximum relative change in the utility of any state between iterations
        """
        traceSet = []
        V_new = {state:0 for state in self.allStates()}

        iters = 0 
        
        while True:
            iters += 1
            delta = 0
            V_old = copy.copy(V_new)
            
            # trace 
            if trace: traceSet.append([(key,value) for key,value in V_old.items() ])
            
            for  s in self.allStates():
                
                max_a = -math.inf
                for action in self.actionsForState(s):
                    
                    sum_sp_a = 0 
                    for sp,prob in self.transitionProbs(s,action):
                        # if the sp is outside, the space set, it is assumed to produce a zero value
                        sum_sp_a += prob*(self.reward(s,action,sp)+lambdafactor*V_old.get(sp,0.0)) 
                    
                    if sum_sp_a > max_a: max_a = sum_sp_a
                    
                V_new[s] = max_a if max_a != -math.inf else V_old[s]
                delta = max(delta, abs(V_new[s]-V_old[s]))
            
            if DEBUG: print (V_new, delta)
            if delta < epsilon: break
        if trace:
            return V_old,iters,traceSet
        else:
            return V_old,iters
    
    def policyFromValue(self, V,lambdaFactor,DEBUG=False):
        """ 
            returns the optimal policy under a given value vector
            for each s, returns argMax_a de Sum_sp[ P(sp|(s,a)*(R(s,a,sp)+lambdaFactor*V(sp)))]
        """
        policy = {}    
        for s in filter(self.isNotTerminalState, self.allStates()):
            max_val,max_action = -math.inf,None
            for action in self.actionsForState(s):
                
                sum_sp_a = 0 
                for sp,prob in self.transitionProbs(s,action):
                    sum_sp_a += prob*(self.reward(s,action,sp)+lambdaFactor*V.get(sp,0)) 
                
                if sum_sp_a > max_val:
                    max_val,max_action = sum_sp_a,action
            
            policy[s] = max_action
        return policy
            