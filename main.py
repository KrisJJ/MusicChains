from lex_anz import Lex_analyzer
from lexem import Lexem

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
