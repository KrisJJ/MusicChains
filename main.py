from lex_anz import Lex_analyzer
import os

def lexAnalysis():
    f = '.\\lex_test\\input.txt'
    f1 = '.\\lex_test\\output.txt'
    fin = open(f,'r')
    fout = open(f1,'w')
    an = Lex_analyzer(fin)

    while not an.isEOF() and not an.isError():
        lex = an.analyze()
        fout.write(str(lex.get())+'\n')

    fin.close()
    fout.close()


def lexTest():
    qDatDir = '.\\lex_test\\questions'
    aDatDir = '.\\lex_test\\answers'
    qFiles = [os.path.join(qDatDir,x) for x in os.listdir(qDatDir)]
    aFiles = [os.path.join(aDatDir,x) for x in os.listdir(aDatDir)]
    total = 0
    for i in range(len(qFiles)):
        conformFlag = True
        qFin = open(qFiles[i],'r')
        aFin = open(aFiles[i],'r')
        an = Lex_analyzer(qFin)
        while not an.isEOF() and not an.isError() and conformFlag:
            lex = str(an.analyze().get())
            readLex = aFin.readline()
            if lex != readLex:
                conformFlag = False
        if conformFlag:
            total += 1
        print(len(lex), len(readLex))
    print(f"{total} tests from {len(qFiles)} are cleared.")
            
            

def main():
    lexAnalysis()
    #lexTest()


if __name__ == '__main__':
    main()
