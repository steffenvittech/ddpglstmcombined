import numpy as np



class mem():
    def __init__(self, length, state):
        self.data=[]
        self.state_mem=[]
        for i in range(0,length):
            self.state_mem.append(state)
        self.isfull=False
        self.count=length



    def validateState(self):
        if self.count==0:
            self.isfull=True
        else:
            self.count -= 1
    def add_data(self, state):
        self.validateState()
        if len(self.data)==10000:
            self.data.pop(0)
        self.data.append(state)
        self.state_mem.pop(0)
        self.state_mem.append(state)







class state():
    def __init__(self, forcast_state, account_state, data_state):
        return np.array([ np.array(forcast_state).flatten(),
        np.array(account_state).flatten(),
        np.array(data_state).flatten()
        ]).flatten()
