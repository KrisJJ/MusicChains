from abc import ABC, abstractmethod
from lexer import Lexer
 
class Node(ABC):
    @abstractmethod
    def draw(self):
        pass


class FinalNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        print()


class ErrorNode(Node):
    lexem = None
    
    def __init__(self,inputLexem,message):
        self.lexem = inputLexem
        self.message = message

    def draw(self,deep,fout):
        fout.write(f'Error: {self.message} on {self.lexem.getPosition()}')
    

class IntegerNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')


class FloatNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')


class IdentifNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')


class BinOperNode(Node):
    binLeft = None
    binOper = None
    binRight = None
    
    def __init__(self,lexemLeft,lexemOper,lexemRight):
        self.binLeft = lexemLeft
        self.binOper = lexemOper
        self.binRight = lexemRight
        

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.binOper.getValue())+'\n')
        else:
            fout.write(str(self.binOper.getValue())+'\n')
        self.binLeft.draw(deep+1,fout)
        self.binRight.draw(deep+1,fout)


class Parser:
    
    def __init__(self,fin):
        self.lexer = Lexer(fin)
        self.isEOF = False
        self.isError = False
        self.isMoved = False
        self.currentLexem = None
        self.parentes = 0
        

    def getNextLexem(self):
        #print('NL')
        lexem = self.lexer.analyze()
        while (lexem.getType() != 'Integer' and lexem.getType() != 'Float' and
               lexem.getType() != 'Identif' and lexem.getType() != 'Operator' and
               lexem.getType() != 'Separator' and lexem.getType() != 'Final' and
               lexem.getType() != 'Error'):
            lexem = self.lexer.analyze()
            if lexem.getType() == 'Final' or lexem.getType() == 'Error':
                self.isEOF = True
                
        #print(lexem.getString())
        return lexem


    def parseExpr(self):
        #print('PE')
        left = self.parseTerm()
        oper = self.currentLexem
        self.isMoved = False
        while oper.getType() == 'Operator' and (oper.getValue() == '+' or
                                                oper.getValue() == '-'):
            right = self.parseTerm()
            #print(right)
            left = BinOperNode(left, oper, right)
            oper = self.currentLexem
            self.isMoved = False
        #print(left)
        return left


    def parseTerm(self):
        #print('PT')
        left = self.parseFactor()
        oper = self.currentLexem
        self.isMoved = False
        while oper.getType() == 'Operator' and (oper.getValue() == '*' or
                                                oper.getValue() == '/'):
            right = self.parseFactor()
            left = BinOperNode(left, oper, right)
            oper = self.currentLexem
            self.isMoved = False
        #print(left)
        return left


    def parseFactor(self):
        #print('PF')
        #print(self.isMoved)
        temperNode = None
        if not self.isMoved:
            self.currentLexem = self.getNextLexem()
        else:
            self.isMoved = False
            
        if self.currentLexem.getType() == 'Identif':
            temperNode = IdentifNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            #print("fUCK")
            
        elif self.currentLexem.getType() == 'Integer':
            temperNode = IntegerNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            
        elif self.currentLexem.getType() == 'Float':
            temperNode = FloatNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            
        elif (self.currentLexem.getType() == 'Separator' and
              self.currentLexem.getValue() == '('):
            self.parentes += 1
            exp = self.parseExpr()
            if (self.currentLexem.getType() == 'Separator' and
                self.currentLexem.getValue() == ')'):

                self.parentes -= 1
                self.currentLexem = self.getNextLexem()
                self.isMoved = True
                temperNode = exp

            else:
                self.isError = True
                temperNode = ErrorNode(self.currentLexem,'Expected ")"')
                
        elif self.currentLexem.getType() == 'Final':
            if self.parentes > 0:
                self.isError = True
                temperNode = ErrorNode(self.currentLexem,'Expected ")"')
            else:
                self.isEOF = True
                temperNode = FinalNode(self.currentLexem)
            
        else:
            self.isError = True
            temperNode = ErrorNode(self.currentLexem,'Unexpected lexem')

        return temperNode


    def analyze(self):
        if not self.currentLexem is None:
            self.isMoved = True
        return self.parseExpr()
            
