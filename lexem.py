class Lexem:
    def __init__(self,line,pos,l_type,orig):
        self.pos = pos
        self.line = line
        self.l_type = l_type
        self.orig = orig

    def get(self):
        return self.pos, self.line, self.l_type, self.orig

    def write_lex(self,fout):
        if self.orig!='':
            fout.write(str(self.line)+'\t'+str(self.pos)+'\t'+self.l_type+'\t'
                       +str(self.orig)+'\n')
