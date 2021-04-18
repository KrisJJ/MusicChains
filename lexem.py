class Lexem:
    def __init__(self,pos,l_type,orig):
        self.pos = pos
        self.l_type = l_type
        self.orig = orig
        #self.name = name

    def get(self):
        return self.pos, self.l_type, self.orig, #self.name
