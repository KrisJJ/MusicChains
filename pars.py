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


class StringNode(Node):
    lexem = None
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')


class CharNode(Node):
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
    operPart = None
    rightPart = None
    
    def __init__(self,aLeft,aOper,aRight):
        self.leftPart = aLeft
        self.operPart = aOper
        self.rightPart = aRight
        

    def draw(self,deep,fout):
        self.leftPart.draw(deep,fout)
        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.operPart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.operPart.getValue())+'\n')
        
        self.rightPart.draw(deep+1,fout)



class BlockNode(Node):
    beginPart = None
    mainPart = None
    endPart = None

    def __init__(self,blBegin,blMain,blEnd):
        self.beginPart = blBegin
        self.mainPart = blMain
        self.endPart = blEnd

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.beginPart.getValue())+'\n')
        else:
            fout.write(str(self.beginPart.getValue())+'\n')

        self.mainPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.endPart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.endPart.getValue())+'\n')


class WhileNode(Node):
    whilePart = None
    conditionPart = None
    doPart = None
    mainPart = None

    def __init__(self,wlWhile,wlCond,wlDo,wlMain):
        self.whilePart = wlWhile
        self.conditionPart = wlCond
        self.doPart = wlDo
        self.mainPart = wlMain

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.whilePart.getValue())+'\n')
        else:
            fout.write(str(self.whilePart.getValue())+'\n')

        self.conditionPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.doPart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.doPart.getValue())+'\n')

        self.mainPart.draw(deep+2,fout)


class UntilNode(Node):
    doPart = None
    mainPart = None
    untilPart = None
    conditionPart = None

    def __init__(self,ulDo,ulMain,ulUntil,ulCond):
        self.doPart = ulDo
        self.mainPart = ulMain
        self.untilPart = ulUntil
        self.conditionPart = ulCond

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.doPart.getValue())+'\n')
        else:
            fout.write(str(self.doPart.getValue())+'\n')

        self.mainPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.untilPart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.untilPart.getValue())+'\n')

        self.conditionPart.draw(deep+2,fout)


class ForNode(Node):
    forPart = None
    identifPart = None
    startPart = None
    coursePart = None
    endPart = None
    mainPart = None

    def __init__(self,frFor,frId,frStart,frCourse,frEnd,frMain):
        self.forPart = frFor
        self.identifPart = frId
        self.startPart = frStart
        self.coursePart = frCourse
        self.endPart = frEnd
        self.mainPart = frMain

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.forPart.getValue())+'\n')
        else:
            fout.write(str(self.forPart.getValue())+'\n')

        self.identifPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.coursePart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.coursePart.getValue())+'\n')

        self.startPart.draw(deep+2,fout)

        self.endPart.draw(deep+2,fout)

        self.mainPart.draw(deep+1,fout)


class IfNode(Node):
    ifPart = None
    condPart = None
    thenPart = None
    mainPart = None
    elsePart = None
    restPart = None

    def __init__(self,ifIf,ifCond,ifThen,ifMain,ifElse,ifRest):
        self.ifPart = ifIf
        self.condPart = ifCond
        self.thenPart = ifThen
        self.mainPart = ifMain
        self.elsePart = ifElse
        self.restPart = ifRest

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.ifPart.getValue())+'\n')
        else:
            fout.write(str(self.ifPart.getValue())+'\n')

        self.condPart.draw(deep+1,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.thenPart.getValue())+'\n')
        else:
            fout.write('└-' + str(self.thenPart.getValue())+'\n')

        self.mainPart.draw(deep+2,fout)

        if not self.elsePart is None:
            if deep>0:
                fout.write('  '*(deep)+ '└-' + str(self.elsePart.getValue())+'\n')
            else:
                fout.write('└-' + str(self.elsePart.getValue())+'\n')

            self.restPart.draw(deep+2,fout)


class MainNode(Node):
    leftPart = None
    rightPart = None

    def __init__(self,left,right):
        self.leftPart = left
        self.rightPart = right

    def draw(self,deep,fout):
        self.leftPart.draw(deep,fout)
        self.rightPart.draw(deep,fout)


class FunctionNode(Node):
    leftPart = None
    rightPart = None

    def __init__(self,left,right):
        self.leftPart = left
        self.rightPart = right

    def draw(self,deep,fout):
        self.leftPart.draw(deep,fout)
        self.rightPart.draw(deep+1,fout)


class ArrayNode(Node):
    leftPart = None
    rightPart = None

    def __init__(self,left,right):
        self.leftPart = left
        self.rightPart = right

    def draw(self,deep,fout):
        self.leftPart.draw(deep,fout)
        self.rightPart.draw(deep,fout)


class ArrayElemNode(Node):
    leftPart = None
    rightPart = None
    leftBracket = None
    rightBracket = None

    def __init__(self,left,brLeft,right,brRight):
        self.leftPart = left
        self.rightPart = right
        self.leftBracket = brLeft
        self.rightBracket = brRight

    def draw(self,deep,fout):
        self.leftPart.draw(deep,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.leftBracket.getValue())+'\n')
        else:
            fout.write('└-' + str(self.leftBracket.getValue())+'\n')
                
        self.rightPart.draw(deep+2,fout)

        if deep>0:
            fout.write('  '*(deep)+ '└-' + str(self.rightBracket.getValue())+'\n')
        else:
            fout.write('└-' + str(self.rightBracket.getValue())+'\n')


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
        while (lexem.getType() != 'Integer' and lexem.getType() != 'Float' and
               lexem.getType() != 'Identif' and lexem.getType() != 'Operator' and
               lexem.getType() != 'Separator' and lexem.getType() != 'Final' and
               lexem.getType() != 'Error' and lexem.getType() != 'Keyword' and
               lexem.getType() != 'String' and lexem.getType() != 'Char'):
            lexem = self.lexer.analyze()
            print(lexem.getValue())

        print('Finished NL')
        return lexem


    def parseExpr(self):
        print('PE')
        left = self.parseTerm()
        oper = self.currentLexem
        self.isMoved = False
        while oper.getValue() == '+' or oper.getValue() == '-':
            right = self.parseTerm()
            left = BinOperNode(left, oper, right)
            oper = self.currentLexem
            self.isMoved = False

        print('Finished PE')
        return left


    def parseTerm(self):
        print('PT')
        left = self.parseFactor()
        oper = self.currentLexem
        self.isMoved = False
        while (oper.getValue() == '*' or oper.getValue() == '/' or
               oper.getValue() == 'div' or oper.getValue() == 'mod'):
            right = self.parseFactor()
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
            print('Moved',self.currentLexem.getValue())
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


    def parseMain(self):
        print('PM')
        self.currentLexem = self.getNextLexem()
        left = EmptyNode()
        right = EmptyNode()
        while not (self.isEOF or self.isError or
                   self.currentLexem.getValue() == 'end' or self.currentLexem.getValue() == 'until' or
                   self.currentLexem.getValue() == 'else'):
            print('Cycle')
            if self.currentLexem.getType() == 'Final':
                self.isEOF = True
                right = FinalNode(self.currentLexem)
                left = MainNode(left,right)

            elif self.currentLexem.getType() == 'Error':
                self.isError = True
                print('Error unexpected')
                return ErrorNode(self.currentLexem,'Unexpected lexem')
            
            elif self.currentLexem.getType() == 'Keyword':
                if self.currentLexem.getValue() == 'begin':
                    right = self.parseBlock()
                    left = MainNode(left,right)
                    break
                    
                elif self.currentLexem.getValue() == 'while':
                    right = self.parseWhile()
                    left = MainNode(left,right)

                elif self.currentLexem.getValue() == 'do':
                    right = self.parseUntil()
                    left = MainNode(left,right)

                elif self.currentLexem.getValue() == 'for':
                    right = self.parseFor()
                    left = MainNode(left,right)

                elif self.currentLexem.getValue() == 'if':
                    right = self.parseIf()
                    left = MainNode(left,right)

                else:
                    self.isError = True
                    print('Error bad kw')
                    return ErrorNode(self.currentLexem,'Bad keyword')

            elif self.currentLexem.getType() == 'Identif':
                right = self.parseIdentif()
                left = MainNode(left,right)

            else:
                self.isMoved = True
                right = self.parseExpr()
                left = MainNode(left,right)

            if not (self.isEOF or self.isError or
                    self.currentLexem.getValue() == 'end' or self.currentLexem.getValue() == 'until' or
                    self.currentLexem.getValue() == 'else'):
                print('Not stoper, wait ;')
                if self.currentLexem.getValue() == ';':
                    print('founded ;')
                    self.currentLexem = self.getNextLexem()
                    if self.currentLexem.getType() == 'Final':
                        self.isError = True
                        print('Error ;')
                        return ErrorNode(self.currentLexem,'Expected "."')
                    else:
                        right = EmptyNode()
                        left = MainNode(left,right)

                elif self.currentLexem.getValue() == '.':
                    self.currentLexem = self.getNextLexem()
                    if self.currentLexem.getType() == 'Final':
                        right = EmptyNode()
                        left = MainNode(left,right)
                    else:
                        self.isError = True
                        print('Error .')
                        return ErrorNode(self.currentLexem,'Expected ";"')
                    
                elif self.currentLexem.getType() == 'Final':
                    right = FinalNode(self.currentLexem)
                    left = MainNode(left,right)
                    
                else:
                    self.isError = True
                    print('Error ;')
                    return ErrorNode(self.currentLexem,'Expected ";"')

        print(right)
        print(left)
        print('Finished PM')
        return left


    def parseBlock(self):
        print('PB')
        beginPart = self.currentLexem
        mainPart = self.parseMain()
        endPart = self.currentLexem
        print('Finished PB')
        if endPart.getValue() == 'end':
            self.currentLexem = self.getNextLexem()
            #self.isMoved = True
            return BlockNode(beginPart,mainPart,endPart)
        elif endPart.getType() == 'Error':
            self.isErrore = True
            print('Error error')
            return ErrorNode(endPart,endPart.getValue())
        else:
            self.isErrore = True
            print('Error end')
            return ErrorNode(endPart,'Expected "end"')



    def parseCondition(self):
        print('PC')
        left = self.parseConditionInner1()
        oper = self.currentLexem
        while oper.getValue() == 'or':
            right = self.parseConditionInner1()
            left = BinOperNode(left,oper,right)
            oper = self.currentLexem

        print('Finished PC')
        return left


    def parseConditionInner1(self):
        print('PC1')
        left = self.parseConditionInner2()
        oper = self.currentLexem
        while oper.getValue() == 'and':
            right = self.parseConditionInner2()
            left = BinOperNode(left,oper,right)
            oper = self.currentLexem

        print('Finished PC1')
        return left

    def parseConditionInner2(self):
        print('PC2')
        left = None
        if not self.isMoved:
            self.currentLexem = self.getNextLexem()
        else:
            self.isMoved = False

        if (self.currentLexem.getType() == 'Identif' or self.currentLexem.getType() == 'Integer' or
            self.currentLexem.getType() == 'Float'):
            self.isMoved = True
            left = self.parseExpr()
            
        elif self.currentLexem.getValue() == '(':
            self.parentes += 1
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            cond = self.parseCondition()
            if self.currentLexem.getValue() == ')':
                print('found ) yay')
                self.parentes -= 1
                self.currentLexem = self.getNextLexem()
                left = cond

        else:
            self.isError = True
            return ErrorNode(self.currentLexem,'Unexpected lexem')

        oper = self.currentLexem
            
        if (oper.getValue() == '<' or oper.getValue() == '>' or
            oper.getValue() == '=' or oper.getValue() == '>=' or
            oper.getValue() == '<=' or oper.getValue() == '<>'):
            
            right = self.parseExpr()
            left = BinOperNode(left,oper,right)

        print('Finished PC2',self.parentes)
        return left


    def parseWhile(self):
        print('PW')
        whilePart = self.currentLexem
        condPart = self.parseCondition()
        doPart = self.currentLexem
        if doPart.getValue() != 'do':
            self.isError = True
            print('Error do')
            return ErrorNode(doPart,'Expected "do"')
        mainPart = self.parseMain()

        print('Finished PW')
        return WhileNode(whilePart,condPart,doPart,mainPart)


    def parseUntil(self):
        print('PU')
        doPart = self.currentLexem
        mainPart = self.parseMain()
        untilPart = self.currentLexem
        if untilPart.getValue() != 'until':
            self.isError = True
            print('Error until')
            return ErrorNode(untilPart,'Expected "until"')
        conditionPart = self.parseCondition()

        print('Finished PU')
        return UntilNode(doPart,mainPart,untilPart,conditionPart)


    def parseIf(self):
        print('PI')
        ifPart = self.currentLexem
        condPart = self.parseCondition()
        thenPart = self.currentLexem
        if thenPart.getValue() != 'then':
            self.isError = True
            print('Error then')
            return ErrorNode(thenPart,'Expected "then"')
        mainPart = self.parseMain()
        elsePart = self.currentLexem
        print('kinda else',elsePart.getValue())
        if elsePart.getValue() == 'else':
            restPart = self.parseMain()
        else:
            elsePart = None
            restPart = None

        print('Finished PI')
        return IfNode(ifPart,condPart,thenPart,mainPart,elsePart,restPart)


    def parseFor(self):
        print('Pfor')
        forPart = self.currentLexem
        self.currentLexem = self.getNextLexem()
        if self.currentLexem.getType() == 'Identif':
            identifPart = IdentifNode(self.currentLexem)
        else:
            return ErrorNode(self.currentLexem,'Expected Identificator')
        self.currentLexem = self.getNextLexem()
        comsPart = self.currentLexem
        if comsPart.getValue() != ':=':
            self.isError = True
            print('Error :')
            return ErrorNode(comsPart,'Expected ":"') 
        startPart = self.parseExpr()
        coursePart = self.currentLexem
        if coursePart.getValue() != 'to' and coursePart.getValue() != 'downto':
            self.isError = True
            print('Error to')
            return ErrorNode(coursePart,'Expected "to"')
        endPart = self.parseExpr()
        mainPart = self.parseMain()

        print('Finished Pfor')
        return ForNode(forPart,identifPart,startPart,coursePart,endPart,mainPart)


    def parseIdentif(self):
        print('Pid')
        print('ismoved',self.isMoved)
        if not self.isMoved:
            left = IdentifNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
        else:
            left = EmptyNode()
            self.isMoved = False

        if self.currentLexem.getValue() == '.':
            self.currentLexem = self.getNextLexem()
            right = self.parseIdentif()
            left = FunctionNode(left,right)

        elif self.currentLexem.getValue() == ':=':
            oper = self.currentLexem
            right = self.parseExpr()
            left = AssignNode(left,oper,right)

        elif self.currentLexem.getValue() == '[':
            brLeft = self.currentLexem
            right = self.parseExpr()
            if self.currentLexem.getValue() == ']':
                brRight = self.currentLexem
                left = ArrayElemNode(left,brLeft,right,brRight)
                self.currentLexem = self.getNextLexem()
                self.isMoved = True
                right = self.parseIdentif()
                left = FunctionNode(left,right)
            else:
                print('Current',self.currentLexem.getValue())
                self.isError = True
                print('Error ]')
                left = ErrorNode(self.currentLexem,'Expected "]"')

        elif self.currentLexem.getValue() == '(':
            right = self.parseArray()
            left = FunctionNode(left,right)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            right = self.parseIdentif()
            left = FunctionNode(left,right)

        print('Finished Pid')

        return left


    def parseArray(self):
        print('PA')
        '''left = self.parseExpr()
        oper = self.currentLexem
        self.isMoved = False'''
        left = EmptyNode()
        self.currentLexem = self.getNextLexem()
        self.isMoved = True
        if self.currentLexem.getValue() ==')':
            oper = self.currentLexem
        else:
            left = self.parseExpr()
            oper = self.currentLexem
            self.isMoved = False
            
        while oper.getValue() == ',':
            right = self.parseExpr()
            left = ArrayNode(left,right)
            '''self.currentLexem = self.getNextLexem()'''
            oper = self.currentLexem
            self.isMoved = False

        print('Finished PA')

        if oper.getValue() == ')':
            return left
        
        else:
            self.isError = True
            print('Error unexpected2')
            return ErrorNode(oper,'Unexpected symbol')
        

    def analyze(self):
        if not self.currentLexem is None:
            self.isMoved = True
        return self.parseMain()
            
