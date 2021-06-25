from lex_anz import Lex_analyzer
from lexem import Lexem

f = '../input.txt'
f1 = '../output.txt'
fin = open(f,'r')
fout = open(f1,'w')
an = Lex_analyzer(fin)

while not an.isEOF() and not an.isError():
    lex = an.analyze()
    fout.write(str(lex.get())+'\n')

fin.close()
fout.close()
