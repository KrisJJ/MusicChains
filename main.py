from lexer import Lexer
from pars import Parser
import os

def parseAnalysis():
    f = '.\\input.txt'
    f1 = '.\\output.txt'
    fin = open(f, 'r', encoding='utf-8')
    fout = open(f1, 'w', encoding='utf-8')
    parser = Parser(fin)
    isEOF = False

    while not isEOF:
        p = parser.analyze()
        p.draw(0,fout)
        if parser.isEOF or parser.isError:
            isEOF = True

    fin.close()
    fout.close()


def parseTest():
    qDatDir = '.\\questions'
    aDatDir = '.\\answers'
    qFiles = [os.path.join(qDatDir,x) for x in os.listdir(qDatDir)]
    aFiles = [os.path.join(aDatDir,x) for x in os.listdir(aDatDir)]
    total = 0
    for i in range(len(qFiles)):
        conformFlag = True
        qFin = open(qFiles[i], 'r', encoding='utf-8')
        aFin = open(aFiles[i], 'r', encoding='utf-8')
        parser = Parser(fin)
        isEOF = False
        allMadeLex = ''
        allReadLex = ''
        while not isEOF and conformFlag:
            lex = lexer.analyze()
            if lex.getType() == 'Final':
                isEOF = True
            madeLex = lex.getString()+'\n'
            readLex = aFin.readline()
            if madeLex != readLex:
                conformFlag = False
            allMadeLex += madeLex
            allReadLex += readLex
            #print(madeLex)
            #print(readLex)
            
        if conformFlag:
            total += 1
            
        print(len(allMadeLex), len(allReadLex))
        
    print(f"{total} tests from {len(qFiles)} are cleared.")  


def lexAnalysis():
    f = '.\\input.txt'
    f1 = '.\\output.txt'
    fin = open(f, 'r', encoding='utf-8')
    fout = open(f1, 'w', encoding='utf-8')
    lexer = Lexer(fin)
    isEOF = False

    while not isEOF and not lexer.isError():
        lex = lexer.analyze()
        fout.write(lex.getString()+'\n')
        if lex.getType() == 'Final':
            isEOF = True

    fin.close()
    fout.close()


def lexTest():
    qDatDir = '.\\questions'
    aDatDir = '.\\answers'
    qFiles = [os.path.join(qDatDir,x) for x in os.listdir(qDatDir)]
    aFiles = [os.path.join(aDatDir,x) for x in os.listdir(aDatDir)]
    total = 0
    for i in range(len(qFiles)):
        conformFlag = True
        qFin = open(qFiles[i], 'r', encoding='utf-8')
        aFin = open(aFiles[i], 'r', encoding='utf-8')
        lexer = Lexer(qFin)
        isEOF = False
        allMadeLex = ''
        allReadLex = ''
        while not isEOF and not lexer.isError() and conformFlag:
            lex = lexer.analyze()
            if lex.getType() == 'Final':
                isEOF = True
            madeLex = lex.getString()+'\n'
            readLex = aFin.readline()
            if madeLex != readLex:
                conformFlag = False
            allMadeLex += madeLex
            allReadLex += readLex
            #print(madeLex)
            #print(readLex)
            
        if conformFlag:
            total += 1
            
        print(len(allMadeLex), len(allReadLex))
        
    print(f"{total} tests from {len(qFiles)} are cleared.")       
            

def main():
    #lexAnalysis()
    #lexTest()
    parseAnalysis()
    #parseTest()


if __name__ == '__main__':
    main()
