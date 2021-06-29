from abc import ABC, abstractmethod
from lexer import Lexer
 
"""class Drawer:
    itemsList = None

    def __init__(self,items):
        self.itemsList = items

    def draw(self,deep,fout):"""
        

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
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')


class FloatNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')


class StringNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')


class CharNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')


class IdentifNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')


class BinOperNode(Node):
    leftPart = None
    operPart = None
    rightPart = None
    
    def __init__(self,binLeft,binOper,binRight):
        self.leftPart = binLeft
        self.operPart = binOper
        self.rightPart = binRight
        

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.operPart.getValue())+'\n')
        else:
            fout.write(str(self.operPart.getValue())+'\n')
        self.leftPart.draw(deep+1,fout)
        self.rightPart.draw(deep+1,fout)


class AssignNode(Node):
    leftPart = None
    rightPart = None
    
    def __init__(self,aLeft,aRight):
        self.leftPart = aLeft
        self.rightPart = aRight
        

    def draw(self,deep,fout):
        self.leftPart.draw(deep,fout)
        if deep>0:
            fout.write('  '*(deep)+ '└-:=\n')
        else:
            fout.write('└-:=\n')
        
        self.rightPart.draw(deep+2,fout)


class StatementNode(Node):
    inner = None

    def __init__(self,node):
        self.inner = node

    def draw(self,deep,fout):
        print(self.inner)
        self.inner.draw(deep,fout)


class BlockNode(StatementNode):
    inner = None

    def __init__(self,blList):
        self.inner = blList

    def draw(self,deep,fout):
        for elem in self.inner:
            elem.draw(deep,fout)


class WhileNode(StatementNode):
    conditionPart = None
    mainPart = None

    def __init__(self,wlCond,wlMain):
        self.conditionPart = wlCond
        self.mainPart = wlMain

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-while\n')
        else:
            fout.write('while\n')

        self.conditionPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-do\n')
        else:
            fout.write('└-do\n')

        self.mainPart.draw(deep+2,fout)


class UntilNode(StatementNode):
    mainPart = None
    conditionPart = None

    def __init__(self,ulMain,ulCond):
        self.mainPart = ulMain
        self.conditionPart = ulCond

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-repeat\n')
        else:
            fout.write('repeat\n')

        for elem in self.mainPart:
            elem.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-until\n')
        else:
            fout.write('└-until\n')

        self.conditionPart.draw(deep+2,fout)


class ForNode(StatementNode):
    identifPart = None
    startPart = None
    coursePart = None
    endPart = None
    mainPart = None

    def __init__(self,frId,frStart,frCourse,frEnd,frMain):
        self.identifPart = frId
        self.startPart = frStart
        self.coursePart = frCourse
        self.endPart = frEnd
        self.mainPart = frMain

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-for\n')
        else:
            fout.write('for\n')

        self.identifPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.coursePart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.coursePart.getValue())+'\n')

        self.startPart.draw(deep+2,fout)

        self.endPart.draw(deep+2,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-do\n')
        else:
            fout.write('└-do\n')

        self.mainPart.draw(deep+2,fout)


class IfNode(StatementNode):
    condPart = None
    mainPart = None
    elsePart = None

    def __init__(self,ifCond,ifMain,ifElse):
        self.condPart = ifCond
        self.mainPart = ifMain
        self.elsePart = ifElse

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-if\n')
        else:
            fout.write('if\n')

        self.condPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-then\n')
        else:
            fout.write('└-then\n')

        self.mainPart.draw(deep+2,fout)

        if not self.elsePart is None:
            if deep>0:
                fout.write('  '*(deep)+ '└-else\n')
            else:
                fout.write('└-else\n')

            self.elsePart.draw(deep+2,fout)


class VariableComponentNode(Node):
    var = None
    comp = None

    def __init__(self,var,comp):
        self.var = var
        self.comp = comp

    def draw(self,deep,fout):
        self.var.draw(deep,fout)
        self.comp.draw(deep+1,fout)


class FuncParsNode(Node):
    parsList = None

    def __init__(self,parsList):
        self.parsList = parsList

    def draw(self,deep,fout):
        for elem in self.parsList:
            elem.draw(deep,fout)


class FunctionNode(Node):
    var = None
    parsList = None

    def __init__(self,var,parsList):
        self.var = var
        self.parsList = parsList

    def draw(self,deep,fout):
        self.var.draw(deep,fout)
        for elem in self.parsList:
            elem.draw(deep+1,fout)


class ExprListNode(Node):
    parsList = None

    def __init__(self,parsList):
        self.parsList = parsList

    def draw(self,deep,fout):
        for elem in self.parsList:
            elem.draw(deep,fout)


class ArrayElemNode(Node):
    var = None
    idList = None

    def __init__(self,var,idList):
        self.var = var
        self.idList = idList

    def draw(self,deep,fout):
        self.var.draw(deep,fout)

        if deep>0:
            fout.write('  '*(deep-1)+ '└-[\n')
        else:
            fout.write('└-[\n')

        for elem in self.idList:
            elem.draw(deep+2,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-]\n')
        else:
            fout.write('  └-]\n')


class EmptyNode(Node):
    def draw(self,deep,fout):
        pass

        
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~main body~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

class Parser:
    
    def __init__(self,fin):
        self.lexer = Lexer(fin)
        self.isEOF = False
        self.isError = False
        self.isMoved = False
        self.currentLexem = None
        self.parentes = 0
        

    def getNextLexem(self):
        print('NL')
        lexem = self.lexer.analyze()
        print('Got lexem')
        print(lexem.getValue())
        while (lexem.getType() == 'Directory'):
            lexem = self.lexer.analyze()
            print(lexem.getValue())

        print('Finished NL')
        return lexem


    def parseExpr(self):
        print('PE')
        left = self.parseTerm()
        if not type(left) is ErrorNode and not type(left) is EmptyNode:
            oper = self.currentLexem
            self.isMoved = False
            while oper.getValue() == '+' or oper.getValue() == '-' or oper.getValue() == 'or':
                right = self.parseTerm()
                if type(right) is FinalNode:
                    return ErrorNode(self.currentLexem,'expected second operand')
                else:
                    left = BinOperNode(left, oper, right)
                    oper = self.currentLexem
                    self.isMoved = False

        print('Finished PE')
        return left


    def parseTerm(self):
        print('PT')
        left = self.parseFactor()
        if not type(left) is ErrorNode and not type(left) is EmptyNode:
            oper = self.currentLexem
            self.isMoved = False
            while (oper.getValue() == '*' or oper.getValue() == '/' or
                   oper.getValue() == 'div' or oper.getValue() == 'mod' or oper.getValue() == 'and'):
                right = self.parseFactor()
                if type(right) is FinalNode:
                    return ErrorNode(self.currentLexem,'expected second operand')
                else:
                    left = BinOperNode(left, oper, right)
                    oper = self.currentLexem
                    self.isMoved = False

        print('Finished PT')
        return left


    def parseFactor(self):
        print('PF')
        temperNode = None
        if not self.isMoved:
            self.currentLexem = self.getNextLexem()
        else:
            self.isMoved = False
            
        if self.currentLexem.getType() == 'Identif':
            temperNode = self.parseIdentif()
            
        elif self.currentLexem.getType() == 'Integer':
            temperNode = IntegerNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            
        elif self.currentLexem.getType() == 'Float':
            temperNode = FloatNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True

        elif self.currentLexem.getType() == 'String':
            temperNode = StringNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True

        elif self.currentLexem.getType() == 'Char':
            temperNode = CharNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            
        elif self.currentLexem.getValue() == '(':
            print('found (')
            self.parentes += 1
            exp = self.parseExpr()
            if self.currentLexem.getValue() == ')':
                self.parentes -= 1
                self.currentLexem = self.getNextLexem()
                self.isMoved = True
                temperNode = exp

            else:
                self.isError = True
                print('Error )1')
                return ErrorNode(self.currentLexem,'Expected ")"')
                
        elif self.currentLexem.getType() == 'Final':
            if self.parentes > 0:
                self.isError = True
                print('Error end1')
                return ErrorNode(self.currentLexem,'Expected ")"')
            else:
                self.isEOF = True
                temperNode = FinalNode(self.currentLexem)

        elif self.currentLexem.getType() == 'Error':
            self.isError = True
            print('Error error1')
            return ErrorNode(self.currentLexem,self.currentLexem.getValue())

        elif self.currentLexem.getValue() == ';' or self.currentLexem.getValue() == '.':
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            return EmptyNode()
            
        else:
            self.isError = True
            print('Error unexpected1')
            self.isMoved = True
            return ErrorNode(self.currentLexem,'Unexpected lexem')

        print('Finished PF')
        return temperNode


    def parseStatement(self):
        print('PS')
        if not self.isMoved:
            self.currentLexem = self.getNextLexem()
        else:
            self.isMoved = False

        if self.currentLexem.getType() == 'Final':
            self.isEOF = True
            return StatementNode(FinalNode(self.currentLexem))

        elif self.currentLexem.getType() == 'Error':
            self.isError = True
            print('Error unexpected')
            return StatementNode(ErrorNode(self.currentLexem,'Unexpected lexem'))
            
        elif self.currentLexem.getType() == 'Keyword':
            if self.currentLexem.getValue() == 'begin':
                return StatementNode(self.parseBlock())
                    
            elif self.currentLexem.getValue() == 'while':
                return StatementNode(self.parseWhile())

            elif self.currentLexem.getValue() == 'repeat':
                return StatementNode(self.parseUntil())

            elif self.currentLexem.getValue() == 'for':
                return StatementNode(self.parseFor())

            elif self.currentLexem.getValue() == 'if':
                return StatementNode(self.parseIf())

            elif (self.currentLexem.getValue() == 'end' or self.currentLexem.getValue() == 'until' or
                  self.currentLexem.getValue() == 'else'):
                return EmptyNode()

            else:
                self.isError = True
                print('Error bad kw')
                return StatementNode(ErrorNode(self.currentLexem,'Bad keyword'))

        elif self.currentLexem.getType() == 'Identif':
            return StatementNode(self.parseIdentif())

        else:
            self.isMoved = True
            return StatementNode(self.parseExpr())


    def parseStatementSeq(self):
        print('Pss')
        print('Cycle')
        blockList = []
        blockList.append(self.parseStatement())
        self.isMoved = False
        while self.currentLexem.getValue() == ';':
            blockList.append(self.parseStatement())
            self.isMoved = False
            
        return blockList


    def parseBlock(self):
        print('PB')
        self.currentLexem = self.getNextLexem()
        self.isMoved = True
        blockList = self.parseStatementSeq()
        if (self.currentLexem.getValue() == 'end'):
            self.currentLexem = self.getNextLexem()
        else:
            print('needed end')
            self.isError = True
            return ErrorNode(self.currentLexem,'expected "end"')
        print('Finished PB')
        return BlockNode(blockList)


    def parseCondition(self):
        print('PC')
        left = self.parseExpr()
        oper = self.currentLexem
        if (oper.getValue() == '<' or oper.getValue() == '>' or
            oper.getValue() == '=' or oper.getValue() == '>=' or
            oper.getValue() == '<=' or oper.getValue() == '<>'):

            right = self.parseExpr()
            left = BinOperNode(left,oper,right)

        print('Finished PC')
        return left


    def parseWhile(self):
        print('PW')
        condPart = self.parseCondition()
        if self.currentLexem.getValue() != 'do':
            self.isError = True
            print('Error do')
            return ErrorNode(self.currentLexem,'Expected "do"')
        mainPart = self.parseStatement()
        #self.currentLexem = self.getNextLexem()

        print('Finished PW')
        return WhileNode(condPart,mainPart)


    def parseUntil(self):
        print('PU')
        mainPart = self.parseStatementSeq()
        if self.currentLexem.getValue() != 'until':
            self.isError = True
            print('Error until')
            return ErrorNode(self.currentLexem,'Expected "until"')
        conditionPart = self.parseCondition()

        #self.currentLexem = self.getNextLexem()

        print('Finished PU')
        return UntilNode(mainPart,conditionPart)


    def parseIf(self):
        print('PI')
        condPart = self.parseCondition()
        if self.currentLexem.getValue() != 'then':
            self.isError = True
            print('Error then')
            return ErrorNode(self.currentLexem,'Expected "then"')
        mainPart = self.parseStatement()
        print('kinda else',self.currentLexem.getValue())
        if self.currentLexem.getValue() == 'else':
            elsePart = self.parseStatement()
            self.currentLexem = self.getNextLexem()
        else:
            elsePart = None


        print('Finished PI')
        return IfNode(condPart,mainPart,elsePart)


    def parseFor(self):
        print('Pfor')
        self.currentLexem = self.getNextLexem()
        if self.currentLexem.getType() == 'Identif':
            identifPart = IdentifNode(self.currentLexem)
        else:
            return ErrorNode(self.currentLexem,'Expected Identificator')
        self.currentLexem = self.getNextLexem()
        if self.currentLexem.getValue() != ':=':
            self.isError = True
            print('Error :')
            return ErrorNode(self.currentLexem,'Expected ":="') 
        startPart = self.parseExpr()
        coursePart = self.currentLexem
        if coursePart.getValue() != 'to' and coursePart.getValue() != 'downto':
            self.isError = True
            print('Error to')
            return ErrorNode(coursePart,'Expected "to"')
        endPart = self.parseExpr()
        if self.currentLexem.getValue() != 'do':
            self.isError = True
            print('Error do')
            return ErrorNode(self.currentLexem,'Expected "do"')
        mainPart = self.parseStatement()

        #self.currentLexem = self.getNextLexem()

        print('Finished Pfor')
        return ForNode(identifPart,startPart,coursePart,endPart,mainPart)


    def parseIdentif(self):
        print('Pid')
        if self.currentLexem.getType() == 'Identif':
            var = IdentifNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = False
        else:
            self.isError = True
            print('Error id')
            return ErrorNode(self.currentLexem,'Expected Identificator')

        while (self.currentLexem.getValue() == '.' or self.currentLexem.getValue() == ':=' or
               self.currentLexem.getValue() == '[' or self.currentLexem.getValue() == '('):
        
            if self.currentLexem.getValue() == '.':
                self.currentLexem = self.getNextLexem()
                comp = self.parseIdentif()
                var = VariableComponentNode(var,comp)

            elif self.currentLexem.getValue() == ':=':
                print('is assignment')
                self.isMoved = False
                exp = self.parseExpr()
                return AssignNode(var,exp)

            elif self.currentLexem.getValue() == '[':
                parsList = []
                parsList.append(self.parseExpr())
                self.isMoved = False
                while self.currentLexem.getValue() ==',':
                    parsList.append(self.parseExpr())
                    self.isMoved = False
                    
                if self.currentLexem.getValue() == ']':
                    self.currentLexem = self.getNextLexem()
                    self.isMoved = True
                    var = ArrayElemNode(var,parsList)
                else:
                    print('Current',self.currentLexem.getValue())
                    self.isError = True
                    print('Error ]')
                    return ErrorNode(self.currentLexem,'Expected "]"')

            elif self.currentLexem.getValue() == '(':
                parsList = [self.parseExpr()]
                self.isMoved = False
                while self.currentLexem.getValue() ==',':
                    parsList.append(self.parseExpr())
                    self.isMoved = False
                    
                if self.currentLexem.getValue() == ')':
                    self.currentLexem = self.getNextLexem()
                    self.isMoved = True
                    var = FunctionNode(var,parsList)
                else:
                    print('Current',self.currentLexem.getValue())
                    self.isError = True
                    print('Error )')
                    return ErrorNode(self.currentLexem,'Expected ")"')

        self.isMoved = True

        print('Finished Pid')
        return var
        

    def analyze(self):
        return self.parseStatement()
            
