from lex_anz import Lex_analyzer
from lexem import Lexem

<<<<<<< HEAD
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
=======
names = ['prog','ops','dot','float','str','ex']
#names = ['ex']
for n in names:
    f = '../test_'+n+'.txt'
    f1 = '../res_'+n+'.txt'
    fin = open(f,'r')
    fout = open(f1,'w')
    an = Lex_analyzer()
    while not an.is_finalised():
        lex = an.analyze(fin)
        lex.write_lex(fout)
    fin.close()
    fout.close()
>>>>>>> 57581682d4cd848517ef9a5580807a674eacff0f
