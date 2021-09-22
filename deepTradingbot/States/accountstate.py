

class State():
    def __init__(self):
        self.positions=[]


class account():
    def __init__(self):
        self.reward_sum=0





class Trade():
    def __init__(self, start_price, close_price, long_short):
        self.start_price=start_price
        self.close_price=close_price
        self.long_short=long_short
        self.reward=0
        self.isOpen=True



