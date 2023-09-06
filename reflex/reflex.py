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
        raise NotImplementedError()

    def setEnvironment(self):
        raise NotImplementedError()
    

class ReflexAgent():
    def __init__():
        return

    def __str__():
        raise NotImplementedError()

    def selectAction(percept):
        """ obtains percepts from the environment using available sensors """
        raise NotImplementedError()

    def execAction(self, action, environment):
        """ excecutes selectd action, updatintg its state and the environment as appropriate """
        raise NotImplementedError()
        
    def preceptAndAct(self,environment):
        """ Basic Reflex cycle """
        
        # uses sensor to ask the environment
        percept = environment.getEnvironment()   

        # selects proper action based on internal logic, state,  and percept
        action  = self.selectAction(percept)     
        
        # applies selected action
        self.execAction(action, environment)     

        return 

    
