from lex_anz import Lex_analyzer

f = '../input.txt'
f1 = '../output.txt'
fin = open(f,'r')
fout = open(f1,'w')
an = Lex_analyzer()
while not an.is_finalised():
    an.analyze(fin,fout)
fin.close()
fout.close()
