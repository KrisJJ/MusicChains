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

    def getMessage(self):
        return self.message   

    def gelValue(self):
        return self.lexem

class IntegerNode(Node):
    lexem = None
    idType = 'integer'
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')

    def getType(self):
        return self.idType


class FloatNode(Node):
    lexem = None
    idType = 'float'
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')

    def getType(self):
        return self.idType


class StringNode(Node):
    lexem = None
    idType = 'string'
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')

    def getType(self):
        return self.idType


class CharNode(Node):
    lexem = None
    idType = 'char'
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')

    def getType(self):
        return self.idType


class BooleanNode(Node):
    lexem = None
    idType = 'boolean'
    
    def __init__(self,inputLexem):
        self.lexem = inputLexem

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.lexem.getValue())+'\n')
        else:
            fout.write(str(self.lexem.getValue())+'\n')

    def getType(self):
        return self.idType


class IdentifNode(Node):
    lexem = None
    idType = None
    
    def __init__(self,inputLexem,inputType):
        self.lexem = inputLexem
        self.idType = inputType

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ f'└-' + str(self.lexem.getValue()) + ': ' + self.idType + '\n')
        else:
            fout.write(str(self.lexem.getValue()) + ': ' + self.idType + '\n')

    def getType(self):
        return self.idType


class BinOperNode(Node):
    leftPart = None
    operPart = None
    rightPart = None
    idType = None
    
    def __init__(self,binLeft,binOper,binRight,idType):
        self.leftPart = binLeft
        self.operPart = binOper
        self.rightPart = binRight
        self.idType = idType
        

    def draw(self,deep,fout):
        if deep>0:
            fout.write('  '*(deep-1)+ '└-' + str(self.operPart.getValue()) + ': ' + self.idType + '\n')
        else:
            fout.write(str(self.operPart.getValue()) + ': ' + self.idType + '\n')
        self.leftPart.draw(deep+1,fout)
        self.rightPart.draw(deep+1,fout)

    def getType(self):
        return self.idType


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


class SymbolStack:
    def __init__(self):
        self.stack = []

    def add(self,table):
        self.stack.append(table)

    def find(self,var):
        i = len(self.stack) - 1
        if i == -1:
            return '-1'
        while not var in self.stack[i].keys() and i>=0:
            i -= 1

        if i == -1:
            return '-1'
        else:
            return self.stack[i][var]

    def remove(self):
        self.stack = self.stack[:-1]


        
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~main body~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

class Parser:
    
    def __init__(self,fin):
        self.lexer = Lexer(fin)
        self.isEOF = False
        self.isError = False
        self.isMoved = False
        self.currentLexem = None
        self.parentes = 0
        self.isSymbolTableCreated = False
        

    def getVars(self):
        self.currentLexem = self.getNextLexem()
        symbolTable = {}
        if self.currentLexem.getValue() == 'var':
            self.currentLexem = self.getNextLexem()
            while self.currentLexem.getValue() != 'begin' and self.currentLexem.getType() != 'Final':
                vars = [self.currentLexem.getValue()]
                self.currentLexem = self.getNextLexem()

                while self.currentLexem.getValue() == ',':
                    self.currentLexem = self.getNextLexem()
                    if self.currentLexem.getType() != 'Identif':
                        self.isError = True
                        print('Error id')
                        return ErrorNode(self.currentLexem,'Expected Identifier')
                    else:
                        vars.append(self.currentLexem.getValue())
                    self.currentLexem = self.getNextLexem()

                if self.currentLexem.getValue() != ':':
                    self.isError = True
                    print('Error :')
                    return ErrorNode(self.currentLexem,'Expected ":"')
                else:
                    self.currentLexem = self.getNextLexem()
                    if not self.currentLexem.getValue() in ['integer','float','char','string','array','boolean']:
                        self.isError = True
                        print('Unknown type')
                        return ErrorNode(self.currentLexem,'Unknown type')
                    else:
                        symbolTable.update([(elem,self.currentLexem.getValue()) for elem in vars])
                        vars.clear()
                        self.currentLexem = self.getNextLexem()
                        if self.currentLexem.getValue() != ';':
                            self.isError = True
                            print('Error ;')
                            return ErrorNode(self.currentLexem,'Expected ";"')
                        else:
                            self.currentLexem = self.getNextLexem()

            self.symbolStack.add(symbolTable)

        self.isMoved = True

        return EmptyNode()


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
                    if oper.getValue() == '+':
                        if left.getType() in ['integer','float'] or right.getType() in ['integer','float']:
                            if left.getType() in ['string','char'] or right.getType() in ['string','char']:
                                typeB = 'string'
                            elif left.getType() == right.getType():
                                typeB = left.getType()
                            elif left.getType() in ['integer','float'] and right.getType() in ['integer','float']:
                                typeB = 'float'
                            else:
                                self.isError = True
                                print('Error types in expr')
                                return ErrorNode(self.currentLexem,f'Unable to transform {right.getType()} to {left.getType()}')
                        elif left.getType() in ['string','char'] and right.getType() in ['string','char']:
                            typeB = 'string'
                        elif left.getType() == right.getType():
                            typeB = left.getType()
                        else:
                            self.isError = True
                            print('Error types in expr')
                            return ErrorNode(self.currentLexem,f'Unable to transform {right.getType()} to {left.getType()}')

                    elif oper.getValue() == '-':
                        if left.getType() in ['integer','float'] or right.getType() in ['integer','float']:
                            if left.getType() == right.getType():
                                typeB = left.getType()
                            elif left.getType() in ['integer','float'] and right.getType() in ['integer','float']:
                                typeB = 'float'
                            else:
                                self.isError = True
                                print('Error types in expr')
                                return ErrorNode(self.currentLexem,f'Unable to transform {right.getType()} to {left.getType()}')
                        else:
                            self.isError = True
                            print('Error types in expr')
                            return ErrorNode(self.currentLexem,f'Unable to transform {right.getType()} to {left.getType()}')

                    elif (oper.getValue() == 'or' and ((left.getType() == 'integer' and right.getType() == 'integer') or
                                                       (left.getType() == 'boolean' and right.getType() == 'boolean'))):
                        typeB = left.getType()

                    else:
                        self.isError = True
                        print('Error types in expr')
                        return ErrorNode(self.currentLexem,f'Unable to transform {right.getType()} to {left.getType()}')
                    left = BinOperNode(left, oper, right,typeB)
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
                elif type(right) is ErrorNode:
                    return ErrorNode(right.gelValue(),right.getMessage())
                else:
                    if oper.getValue() == '*':
                        if left.getType() == 'float' and right.getType() == 'float':
                            typeB = 'float'
                        elif left.getType() == 'integer' or right.getType() == 'integer':
                            if left.getType() == 'integer':
                                typeB = right.getType()
                            else:
                                typeB = left.getType()
                        else:
                            self.isError = True
                            print('Error types in term')
                            return ErrorNode(self.currentLexem,f'Unable to multiplicate {right.getType()} and {left.getType()}')
                    elif (oper.getValue() == '/' and left.getType() in ['integer','float'] and
                         right.getType() in ['integer','float']):
                        typeB = 'float'
                    elif ((oper.getValue() == 'div' or oper.getValue() == 'mod') and left.getType() == 'integer' and
                         right.getType() == 'integer'):
                        typeB = 'integer'
                    elif (oper.getValue() == 'and' and ((left.getType() == 'integer' and right.getType() == 'integer') or
                                                       (left.getType() == 'boolean' and right.getType() == 'boolean'))):
                        typeB = left.getType()
                    else:
                        self.isError = True
                        print('Error types in expr')
                        return ErrorNode(self.currentLexem,f'Unable to transform {right.getType()} to {left.getType()}')
                    left = BinOperNode(left, oper, right, typeB)
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

        elif self.currentLexem.getType() == 'Boolean':
            temperNode = BooleanNode(self.currentLexem)
            self.currentLexem = self.getNextLexem()
            self.isMoved = True
            
        elif self.currentLexem.getValue() == '(':
            print('found (')
            self.parentes += 1
            exp = self.parseCondition()
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

        st = EmptyNode()

        if self.currentLexem.getType() == 'Final':
            self.isEOF = True
            return FinalNode(self.currentLexem)

        elif self.currentLexem.getType() == 'Error':
            self.isError = True
            print('Error unexpected')
            return ErrorNode(self.currentLexem,'Unexpected lexem')
            
        elif self.currentLexem.getType() == 'Keyword':
            if self.currentLexem.getValue() == 'begin':
                st = self.parseBlock()
                    
            elif self.currentLexem.getValue() == 'while':
                st = self.parseWhile()

            elif self.currentLexem.getValue() == 'repeat':
                st = self.parseUntil()

            elif self.currentLexem.getValue() == 'for':
                st = self.parseFor()

            elif self.currentLexem.getValue() == 'if':
                st = self.parseIf()

            elif (self.currentLexem.getValue() == 'end' or self.currentLexem.getValue() == 'until' or
                  self.currentLexem.getValue() == 'else'):
                return EmptyNode()

            else:
                self.isError = True
                print('Error bad kw')
                ErrorNode(self.currentLexem,'Bad keyword')

        elif self.currentLexem.getType() == 'Identif':
            st = self.parseIdentif()

        else:
            self.isMoved = True
            st = self.parseExpr()

        if type(st) is ErrorNode:
            return ErrorNode(st.gelValue(),st.getMessage())
        else:
            return StatementNode(st)


    def parseStatementSeq(self):
        print('Pss')
        print('Cycle')
        blockList = []
        stat = self.parseStatement()
        if type(stat) is ErrorNode:
            return ErrorNode(stat.gelValue(),stat.getMessage())
        blockList.append(stat)
        self.isMoved = False
        while self.currentLexem.getValue() == ';':
            blockList.append(self.parseStatement())
            self.isMoved = False
            
        return blockList


    def parseBlock(self):
        print('PB')
        self.currentLexem = self.getNextLexem()
        symbolTable = {}
        isVarSet = False
        while self.currentLexem.getValue() == 'var':
            isVarSet = True
            self.currentLexem = self.getNextLexem()
            if self.currentLexem.getType() != 'Identif':
                self.isError = True
                print('Error id')
                return ErrorNode(self.currentLexem,'Expected Identifier')
            else:
                vars = [self.currentLexem.getValue()]
                self.currentLexem = self.getNextLexem()
                while self.currentLexem.getValue() == ',':
                    self.currentLexem = self.getNextLexem()
                    if self.currentLexem.getType() != 'Identif':
                        self.isError = True
                        print('Error id')
                        return ErrorNode(self.currentLexem,'Expected Identifier')
                    else:
                        vars.append(self.currentLexem.getValue())
                    self.currentLexem = self.getNextLexem()

                if self.currentLexem.getValue() != ':':
                    self.isError = True
                    print('Error :')
                    return ErrorNode(self.currentLexem,'Expected ":"')
                else:
                    self.currentLexem = self.getNextLexem()
                    if not self.currentLexem.getValue() in ['integer','float','char','string','array','boolean']:
                        self.isError = True
                        print('Unknown type')
                        return ErrorNode(self.currentLexem,'Unknown type')
                    else:
                        symbolTable.update([(elem,self.currentLexem.getValue()) for elem in vars])
                        vars.clear()
                        self.currentLexem = self.getNextLexem()
                        if self.currentLexem.getValue() != ';':
                            self.isError = True
                            print('Error ;')
                            return ErrorNode(self.currentLexem,'Expected ";"')
                        else:
                            self.currentLexem = self.getNextLexem()
        
        if isVarSet:
            self.symbolStack.add(symbolTable)

        self.isMoved = True
        blockList = self.parseStatementSeq()
        if type(blockList) is ErrorNode:
            return ErrorNode(blockList.gelValue(),blockList.getMessage())
        if (self.currentLexem.getValue() == 'end'):
            self.currentLexem = self.getNextLexem()
        else:
            print('needed end')
            self.isError = True
            return ErrorNode(self.currentLexem,'expected "end"')

        if isVarSet:
            self.symbolStack.remove()

        print('Finished PB')
        return BlockNode(blockList)


    def parseCondition(self):
        print('PC')
        left = self.parseExpr()
        if type(left) is ErrorNode:
            return ErrorNode(left.gelValue(),left.getMessage())
        oper = self.currentLexem
        if (oper.getValue() == '<' or oper.getValue() == '>' or
            oper.getValue() == '=' or oper.getValue() == '>=' or
            oper.getValue() == '<=' or oper.getValue() == '<>'):

            right = self.parseExpr()
            if type(right) is ErrorNode:
                return ErrorNode(right.gelValue(),right.getMessage())
            elif ((left.getType() in ['integer','float'] and right.getType() in ['integer','float']) or
                (left.getType() in ['string','char'] and right.getType() in ['string','char'])):

                return BinOperNode(left,oper,right,'boolean')

            else:
                self.isError = True
                print('Error type on condition')
                return ErrorNode(self.currentLexem,f'Unable to compare {right.getType()} and {left.getType()}')

        print('Finished PC')
        return left


    def parseWhile(self):
        print('PW')
        condPart = self.parseCondition()
        if type(condPart) is ErrorNode:
            return ErrorNode(condPart.gelValue(),condPart.getMessage())
        elif condPart.getType() != 'boolean':
            self.isError = True
            print('Error condition type')
            return ErrorNode(self.currentLexem,'Expected boolean')

        if self.currentLexem.getValue() != 'do':
            self.isError = True
            print('Error do')
            return ErrorNode(self.currentLexem,'Expected "do"')

        mainPart = self.parseStatement()
        if type(mainPart) is ErrorNode:
            return ErrorNode(mainPart.gelValue(),mainPart.getMessage())

        print('Finished PW')
        return WhileNode(condPart,mainPart)


    def parseUntil(self):
        print('PU')
        mainPart = self.parseStatementSeq()
        if type(mainPart) is ErrorNode:
            return ErrorNode(mainPart.gelValue(),mainPart.getMessage())

        if self.currentLexem.getValue() != 'until':
            self.isError = True
            print('Error until')
            return ErrorNode(self.currentLexem,'Expected "until"')

        condPart = self.parseCondition()
        if type(condPart) is ErrorNode:
            return ErrorNode(condPart.gelValue(),condPart.getMessage())
        elif condPart.getType() != 'boolean':
            self.isError = True
            print('Error condition type')
            return ErrorNode(self.currentLexem,'Expected boolean')

        print('Finished PU')
        return UntilNode(mainPart,condPart)


    def parseIf(self):
        print('PI')
        condPart = self.parseCondition()
        if type(condPart) is ErrorNode:
            return ErrorNode(condPart.gelValue(),condPart.getMessage())

        elif condPart.getType() != 'boolean':
            self.isError = True
            print('Error condition type')
            return ErrorNode(self.currentLexem,'Expected boolean')

        if self.currentLexem.getValue() != 'then':
            self.isError = True
            print('Error then')
            return ErrorNode(self.currentLexem,'Expected "then"')

        mainPart = self.parseStatement()
        if type(mainPart) is ErrorNode:
            return ErrorNode(mainPart.gelValue(),mainPart.getMessage())

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
        isTableAddaed = False
        self.currentLexem = self.getNextLexem()
        if self.currentLexem.getValue() == 'var':
            self.currentLexem = self.getNextLexem()
            isVarSet = True
        else:
            isVarSet = False

        if self.currentLexem.getType() == 'Identif':
            identifPart = self.currentLexem
            if not isVarSet:
                self.currentLexem = self.getNextLexem()
                typeF = self.symbolStack.find(identifPart.getValue())
                if self.currentLexem.getValue() != ':' and typeF == '-1':
                    self.isError = True
                    print('Error for unknown variable')
                    return ErrorNode(self.currentLexem,f'variable {self.currentLexem.getValue()} wasnt\'t declared')
                elif typeF != '-1':
                    identifPart = IdentifNode(identifPart,typeF)
                    self.isMoved = True
                else:
                    self.currentLexem = self.getNextLexem()
                    if self.currentLexem.getValue() == 'integer':
                        self.symbolStack.add({identifPart.getValue(): 'integer'})
                        identifPart = IdentifNode(identifPart,'integer')
                        isTableAdded = True
                    else:
                        self.isError = True
                        print('Error for uncountable')
                        return ErrorNode(self.currentLexem,'uncountable variable')
            else:
                pass
        else:
            return ErrorNode(self.currentLexem,'Expected Identificator')

        if not self.isMoved:
            self.currentLexem = self.getNextLexem()
        else:
            self.isMoved = False
        if self.currentLexem.getValue() != ':=':
            self.isError = True
            print('Error :')
            return ErrorNode(self.currentLexem,'Expected ":="') 

        startPart = self.parseExpr()
        if type(startPart) is ErrorNode:
            return ErrorNode(startPart.gelValue(),startPart.getMessage())
        elif startPart.getType() != 'integer':
            self.isError = True
            print('Error for start type')
            return ErrorNode(self.currentLexem,'uncountable variable')

        if isVarSet:
            self.symbolStack.add({identifPart.getValue(): 'integer'})
            identifPart = IdentifNode(identifPart,'integer')
            isTableAdded = True

        coursePart = self.currentLexem
        if coursePart.getValue() != 'to' and coursePart.getValue() != 'downto':
            self.isError = True
            print('Error to')
            return ErrorNode(coursePart,'Expected "to"')

        endPart = self.parseExpr()
        if type(endPart) is ErrorNode:
            return ErrorNode(endPart.gelValue(),endPart.getMessage())
        elif endPart.getType() != 'integer':
            self.isError = True
            print('Error for end type')
            return ErrorNode(self.currentLexem,'uncountable variable')

        if self.currentLexem.getValue() != 'do':
            self.isError = True
            print('Error do')
            return ErrorNode(self.currentLexem,'Expected "do"')

        mainPart = self.parseStatement()
        if type(mainPart) is ErrorNode:
            return ErrorNode(mainPart.gelValue(),mainPart.getMessage())

        print('Finished Pfor')
        self.symbolStack.remove()
        return ForNode(identifPart,startPart,coursePart,endPart,mainPart)


    def parseIdentif(self):
        print('Pid')
        if self.currentLexem.getType() == 'Identif':
            typeV = self.symbolStack.find(self.currentLexem.getValue())
            if typeV != '-1':
                var = IdentifNode(self.currentLexem,typeV)
            else:
                self.isError = True
                print('Error unknown variable')
                return ErrorNode(self.currentLexem,f'variable {self.currentLexem.getValue()} wasnt\'t declared')
            self.currentLexem = self.getNextLexem()
            self.isMoved = False
        else:
            self.isError = True
            print('Error id')
            return ErrorNode(self.currentLexem,'Expected Identificator')

        while ((self.currentLexem.getValue() == '.' or self.currentLexem.getValue() == ':=' or
               self.currentLexem.getValue() == '[' or self.currentLexem.getValue() == '(') and
               not self.isError):
        
            if self.currentLexem.getValue() == '.':
                self.currentLexem = self.getNextLexem()
                comp = self.parseIdentif()
                var = VariableComponentNode(var,comp)

            elif self.currentLexem.getValue() == ':=':
                print('is assignment')
                self.isMoved = False
                exp = self.parseExpr()
                if type(exp) is ErrorNode:
                    return ErrorNode(self.currentLexem,exp.getMessage())
                elif exp.getType() == var.getType():
                    return AssignNode(var,exp)
                else:
                    self.isError = True
                    print('Error assign type')
                    return ErrorNode(self.currentLexem,f'Unable to transform {exp.getType()} to {var.getType()}')

            elif self.currentLexem.getValue() == '[':
                parsList = []
                exp = self.parseExpr()
                if type(exp) is ErrorNode:
                    return ErrorNode(self.currentLexem,exp.getMessage())
                elif exp.getType() != 'integer':
                    self.isError = True
                    print('Error type arrElem')
                    return ErrorNode(self.currentLexem,'uncountable variable')
                else:
                    parsList.append(exp)
                self.isMoved = False
                while self.currentLexem.getValue() ==',':
                    exp = self.parseExpr()
                    if type(exp) is ErrorNode:
                        return ErrorNode(self.currentLexem,exp.getMessage())
                    elif exp.getType() != 'integer':
                        self.isError = True
                        print('Error type arrElem')
                        return ErrorNode(self.currentLexem,'uncountable variable')
                    else:
                        parsList.append(exp)
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
        if not self.isSymbolTableCreated:
            self.symbolStack = SymbolStack()
            self.isSymbolTableCreated = True
            return self.getVars()

        return self.parseStatement()
            
