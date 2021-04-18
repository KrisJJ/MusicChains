class State:
    options = {1: 'start',
               2: 'final',
               3: 'num_int',
               4: 'num_float',
               5: 'num_16',
               60: 'string',
               61: 'string',
               7: 'name',
               8: 'error',
               9: 'comment',
               10: 'delimit'}

    def __init__(self):
        self.state = 1

    def set(self,opt):
        if opt in self.options.keys():
            self.state = opt
        else:
            print('Given option doesn`t relate to state')

    def get_id(self):
        return self.state

    def get_name(self):
        return self.options[self.state]
