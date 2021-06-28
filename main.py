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
    qDatDir = '.\\pars_test\\questions'
    aDatDir = '.\\pars_test\\answers'
    outFile = '.\\output.txt'
    qFiles = [os.path.join(qDatDir,x) for x in os.listdir(qDatDir)]
    aFiles = [os.path.join(aDatDir,x) for x in os.listdir(aDatDir)]
    total = 0
    for i in range(len(qFiles)):
        conformFlag = True
        qFin = open(qFiles[i], 'r', encoding='utf-8')
        fout = open(outFile, 'w', encoding='utf-8')
        parser = Parser(qFin)
        isEOF = False
        while not isEOF and conformFlag:
            p = parser.analyze()
            p.draw(0,fout)
            if parser.isEOF or parser.isError:
                isEOF = True

        qFin.close()
        fout.close()
        print('done')
         
        aFin = open(aFiles[i], 'r', encoding='utf-8')
        fout = open(outFile, 'r', encoding='utf-8')
        cutter = True
        for line in fout:
            aLine = aFin.readline()
            lineStrip = line.strip()
            aLineStrip = aLine.strip()
            if cutter:
                cutter = False
                aLineStrip = aLineStrip[1:]
            print(len(lineStrip),len(aLineStrip))
            if lineStrip != aLineStrip:
                conformFlag = False

            
        if conformFlag:
            total += 1
            mark = "OK"
        else:
            mark = "FAIL"
            
        print(aFin.name, mark)
        
    print(f"{total} tests from {len(qFiles)} are cleared.")  


def lexAnalysis():
    f = '.\\input.txt'
    f1 = '.\\output.txt'
    fin = open(f, 'r', encoding='utf-8')
    fout = open(f1, 'w', encoding='utf-8')
    lexer = Lexer(fin)
    isEOF = False
    isError = False

    while not isEOF and not isError:
        lex = lexer.analyze()
        if lex.getType() != 'Final':
            fout.write(lex.getString()+'\n')
        if lex.getType() == 'Error':
            isError = True
        elif lex.getType() == 'Final':
            isEOF = True

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
        qFin = open(qFiles[i], 'r', encoding='utf-8')
        aFin = open(aFiles[i], 'r', encoding='utf-8')
        lexer = Lexer(qFin)
        isEOF = False
        isError = False
        allMadeLex = ''
        allReadLex = ''
        while not isEOF and not isError and conformFlag:
            lex = lexer.analyze()
            if lex.getType() == 'Error':
                isError = True
            elif lex.getType() == 'Final':
                isEOF = True

            if lex.getType() != 'Final':
                madeLex = lex.getString()+'\n'
                readLex = aFin.readline()
                if madeLex.strip() != readLex.strip():
                    conformFlag = False
                allMadeLex += madeLex
                allReadLex += readLex
                print(madeLex,readLex)
            
        if conformFlag:
            total += 1
            mark = "OK"
        else:
            mark = "FAIL"
            
        print(aFin.name)
        print(len(allMadeLex), len(allReadLex), mark)
        print()

        aFin.close()
        qFin.close()
        
    print(f"{total} tests from {len(qFiles)} are cleared.")       
            

def main():
    #lexAnalysis()
    #lexTest()
    #parseAnalysis()
    parseTest()


if __name__ == '__main__':
    main()
