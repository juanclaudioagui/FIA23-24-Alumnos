###################################################################################
# this is a template for a Reflex Agent
# please remember that the methods which raise NotImplementedError() exceptions are 
# meant to be rewritten, or overloaded in a subclass
###################################################################################

class Environment():
    def __init__():
        return

    def __str__():
        raise NotImplementedError()
    
    def getEnvironment(self):
        # get percept from environment
        raise NotImplementedError()

    def setEnvironment(self):
        # change some aspect of the environment
        raise NotImplementedError()
    

class ReflexAgent():
    def __init__():
        return

    def __str__():
        raise NotImplementedError()

    def selectAction(percept):
        # selects action based on percept and condition-action rules
        raise NotImplementedError()

    def execAction(self, action, environment):
        # excecutes selected action, updating its state and the environment state
        raise NotImplementedError()
        
    def preceptAndAct(self,environment):
        # one step of interaction with the environment
        
        # uses sensor to perceive the environment
        percept = environment.getEnvironment()   

        # selects action
        action  = self.selectAction(percept)     
        
        # applies selected action
        self.execAction(action, environment)     

        return 

    
