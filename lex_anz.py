from enum import Enum

class CurrentValue(Enum):
    ValUnknown = 0
    ValAF = 1
    ValE = 2
    ValLetter = 3
    Val01 = 4
    Val27 = 5
    Val89 = 6
    ValSpace = 7
    ValMinus = 8
    ValOper = 9
    ValCompar = 10
    ValEqual = 11
    ValDot = 12
    ValSepar = 13
    ValOpenCom = 14
    ValCloseCom = 15
    ValQuote = 16
    ValDollar = 17
    ValPercent = 18
    ValAmper = 19
    ValOctot = 20


class State(Enum):
    StStart = 1
    StFinal = 2
    StError = 3
    StSpace = 4
    StOpenCom = 5
    StCloseCom = 6
    StOpenDir = 7
    StCloseDir = 8
    StIdent = 9
    StDecimal = 10
    StBinary = 11
    StOctal = 12
    StHeximal = 13
    StRealWDot = 14
    StRealWDec = 15
    StRealWE = 16
    StRealWEMin = 17
    StRealFull = 18
    StOpenChar = 19
    StCloseChar = 20
    StOpenString = 21
    StCloseString = 22
    StOper = 23
    StSepar = 24
    StAmper = 25
    StASCII = 26


class Buffer:
    def __init__(self):
        self.inner = ''

    def clear(self):
        self.inner = ''

    def add(self,c):
        self.inner += c

    def get(self):
        return self.inner

    def isEmpty(self):
        return self.inner==''


class Lexem:
    def __init__(self,line,pos,state,bufferedString):
        self.line = line
        self.pos = pos
        self.original = bufferedString

        if state is State.StError:
            self.lexemType = 'Error'
        elif state is State.StCloseDir:
            self.lexemType = 'Directory'
            self.lexemValue = bufferedString
        elif state is State.StIdent:
            if bufferedString in Lex_analyzer.keywords:
                self.lexemType = 'Keyword'
            else:
                self.lexemType = 'Identif'
            self.lexemValue = bufferedString
        elif state is State.StDecimal:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString)
        elif state is State.StBinary:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString[1:],2)
        elif state is State.StOctal:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString[1:],8)
        elif state is State.StHeximal:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString[1:],16)
        elif state is State.StRealWDec or state is State.StRealFull:
            self.lexemType = 'Float'
            self.lexemValue = float(bufferedString)
        elif state is State.StCloseChar:
            self.lexemType = 'Char'
            self.lexemValue = bufferedString
        elif state is State.StCloseString:
            self.lexemType = 'String'
            self.lexemValue = bufferedString
        elif state is State.StOper:
            self.lexemType = 'Operator'
            self.lexemValue = bufferedString
        elif state is State.StSepar:
            self.lexemType = 'Separator'
            self.lexemValue = bufferedString
        elif state is State.StASCII:
            self.lexemType = 'Char'
            self.lexemValue = chr(int(bufferedString[1:]))
        

    def get(self):
        if self.lexemType == 'Error':
            return f"{self.line}\t{self.pos}\tError: wrong sequence of symbols: {self.original}"
        else:
            return f"{self.line}\t{self.pos}\t{self.lexemType}\t{self.lexemValue}\t{self.original}"
    

class Lex_analyzer:
    keywords = [ 'and', 'asm', 'array', 'begin', 'case', 'const', 'constructor',
                 'destructor', 'div', 'do', 'downto', 'else', 'end', 'exports',
                 'file', 'for', 'function', 'goto', 'if', 'implementation', 'in',
                 'inherited', 'inline', 'interface', 'label', 'library', 'mod',
                 'nil', 'not', 'object', 'of', 'or', 'packed', 'procedure',
                 'program', 'record', 'repeat', 'set', 'shl', 'shr', 'string',
                 'then', 'to', 'type', 'unit', 'until', 'uses', 'var', 'while',
                 'with', 'xor', 'as', 'class', 'dispose', 'except', 'exit',
                 'exports', 'finalization', 'finally', 'inherited', 'initialization',
                 'is', 'library', 'new', 'on', 'out', 'property', 'raise', 'self',
                 'threadvar', 'try' ]
    
    directives = [ 'absolute', 'abstract', 'alias', 'assembler', 'cdecl', 'cppdecl',
                   'default', 'export', 'external', 'forward', 'index', 'local',
                   'name', 'nostackframe', 'oldfpccall', 'override', 'pascal',
                   'private', 'protected', 'public', 'published', 'read', 'register',
                   'reintroduce', 'safecall', 'softfloat', 'stdcall', 'virtual',
                   'write' ]

    pairOpers = [ ':=', '<>', '<=', '>=', '><', '..']

    separs = [' ', '\n', '\t', '\0', '\r']

    transit = {State.StStart: {CurrentValue.ValAF: State.StIdent,
                               CurrentValue.ValE: State.StIdent,
                               CurrentValue.ValLetter: State.StIdent,
                               CurrentValue.Val01: State.StDecimal,
                               CurrentValue.Val27: State.StDecimal,
                               CurrentValue.Val89: State.StDecimal,
                               CurrentValue.ValSpace: State.StSpace,
                               CurrentValue.ValMinus: State.StOper,
                               CurrentValue.ValOper: State.StOper,
                               CurrentValue.ValCompar: State.StOper,
                               CurrentValue.ValEqual: State.StOper,
                               CurrentValue.ValDot: State.StOper,
                               CurrentValue.ValSepar: State.StSepar,
                               CurrentValue.ValOpenCom: State.StOpenCom,
                               CurrentValue.ValCloseCom: State.StError,
                               CurrentValue.ValQuote: State.StOpenChar,
                               CurrentValue.ValDollar: State.StHeximal,
                               CurrentValue.ValPercent: State.StBinary,
                               CurrentValue.ValAmper: State.StAmper,
                               CurrentValue.ValOctot: State.StASCII,
                               CurrentValue.ValUnknown: State.StError},
                  
                  State.StFinal: {i: State.StError for i in CurrentValue},

                  State.StError: {i: State.StStart for i in CurrentValue},

                  State.StSpace: {i: State.StStart if i!=CurrentValue.ValUnknown
                                  else State.StError for i in CurrentValue},

                  State.StOpenCom: {i: State.StOpenCom if i!=CurrentValue.ValCloseCom
                                    and i!=CurrentValue.ValDollar and i!=CurrentValue.ValUnknown
                                    else State.StCloseCom if i!=CurrentValue.ValDollar
                                    and i!=CurrentValue.ValUnknown else State.StOpenDir
                                    if i!=CurrentValue.ValUnknown else State.StError
                                    for i in CurrentValue},

                  State.StCloseCom: {i: State.StStart if i!=CurrentValue.ValUnknown
                                     else State.StError for i in CurrentValue},

                  State.StOpenDir: {i: State.StOpenCom if i!=CurrentValue.ValCloseCom
                                    and i!=CurrentValue.ValUnknown else State.StCloseDir
                                    if i!=CurrentValue.ValUnknown else State.StError
                                    for i in CurrentValue},

                  State.StCloseDir: {i: State.StStart if i!=CurrentValue.ValUnknown
                                     else State.StError for i in CurrentValue},

                  State.StIdent: {CurrentValue.ValAF: State.StIdent,
                                  CurrentValue.ValE: State.StIdent,
                                  CurrentValue.ValLetter: State.StIdent,
                                  CurrentValue.Val01: State.StIdent,
                                  CurrentValue.Val27: State.StIdent,
                                  CurrentValue.Val89: State.StIdent,
                                  CurrentValue.ValSpace: State.StStart,
                                  CurrentValue.ValMinus: State.StStart,
                                  CurrentValue.ValOper: State.StStart,
                                  CurrentValue.ValCompar: State.StStart,
                                  CurrentValue.ValEqual: State.StStart,
                                  CurrentValue.ValDot: State.StStart,
                                  CurrentValue.ValSepar: State.StStart,
                                  CurrentValue.ValOpenCom: State.StStart,
                                  CurrentValue.ValCloseCom: State.StError,
                                  CurrentValue.ValQuote: State.StError,
                                  CurrentValue.ValDollar: State.StError,
                                  CurrentValue.ValPercent: State.StError,
                                  CurrentValue.ValAmper: State.StError,
                                  CurrentValue.ValOctot: State.StError,
                                  CurrentValue.ValUnknown: State.StError},
                  
                  State.StDecimal: {CurrentValue.ValAF: State.StError,
                                    CurrentValue.ValE: State.StRealWE,
                                    CurrentValue.ValLetter: State.StError,
                                    CurrentValue.Val01: State.StDecimal,
                                    CurrentValue.Val27: State.StDecimal,
                                    CurrentValue.Val89: State.StDecimal,
                                    CurrentValue.ValSpace: State.StStart,
                                    CurrentValue.ValMinus: State.StStart,
                                    CurrentValue.ValOper: State.StStart,
                                    CurrentValue.ValCompar: State.StStart,
                                    CurrentValue.ValEqual: State.StStart,
                                    CurrentValue.ValDot: State.StRealWDot,
                                    CurrentValue.ValSepar: State.StStart,
                                    CurrentValue.ValOpenCom: State.StStart,
                                    CurrentValue.ValCloseCom: State.StError,
                                    CurrentValue.ValQuote: State.StError,
                                    CurrentValue.ValDollar: State.StError,
                                    CurrentValue.ValPercent: State.StError,
                                    CurrentValue.ValAmper: State.StError,
                                    CurrentValue.ValOctot: State.StError,
                                    CurrentValue.ValUnknown: State.StError},

                  State.StBinary: {CurrentValue.ValAF: State.StError,
                                   CurrentValue.ValE: State.StError,
                                   CurrentValue.ValLetter: State.StError,
                                   CurrentValue.Val01: State.StBinary,
                                   CurrentValue.Val27: State.StError,
                                   CurrentValue.Val89: State.StError,
                                   CurrentValue.ValSpace: State.StStart,
                                   CurrentValue.ValMinus: State.StStart,
                                   CurrentValue.ValOper: State.StStart,
                                   CurrentValue.ValCompar: State.StStart,
                                   CurrentValue.ValEqual: State.StStart,
                                   CurrentValue.ValDot: State.StError,
                                   CurrentValue.ValSepar: State.StStart,
                                   CurrentValue.ValOpenCom: State.StStart,
                                   CurrentValue.ValCloseCom: State.StError,
                                   CurrentValue.ValQuote: State.StError,
                                   CurrentValue.ValDollar: State.StError,
                                   CurrentValue.ValPercent: State.StError,
                                   CurrentValue.ValAmper: State.StError,
                                   CurrentValue.ValOctot: State.StError,
                                   CurrentValue.ValUnknown: State.StError},

                  State.StOctal: {CurrentValue.ValAF: State.StError,
                                  CurrentValue.ValE: State.StError,
                                  CurrentValue.ValLetter: State.StError,
                                  CurrentValue.Val01: State.StOctal,
                                  CurrentValue.Val27: State.StOctal,
                                  CurrentValue.Val89: State.StError,
                                  CurrentValue.ValSpace: State.StStart,
                                  CurrentValue.ValMinus: State.StStart,
                                  CurrentValue.ValOper: State.StStart,
                                  CurrentValue.ValCompar: State.StStart,
                                  CurrentValue.ValEqual: State.StStart,
                                  CurrentValue.ValDot: State.StError,
                                  CurrentValue.ValSepar: State.StStart,
                                  CurrentValue.ValOpenCom: State.StStart,
                                  CurrentValue.ValCloseCom: State.StError,
                                  CurrentValue.ValQuote: State.StError,
                                  CurrentValue.ValDollar: State.StError,
                                  CurrentValue.ValPercent: State.StError,
                                  CurrentValue.ValAmper: State.StError,
                                  CurrentValue.ValOctot: State.StError,
                                  CurrentValue.ValUnknown: State.StError},

                  State.StHeximal: {CurrentValue.ValAF: State.StHeximal,
                                    CurrentValue.ValE: State.StHeximal,
                                    CurrentValue.ValLetter: State.StError,
                                    CurrentValue.Val01: State.StHeximal,
                                    CurrentValue.Val27: State.StHeximal,
                                    CurrentValue.Val89: State.StHeximal,
                                    CurrentValue.ValSpace: State.StStart,
                                    CurrentValue.ValMinus: State.StStart,
                                    CurrentValue.ValOper: State.StStart,
                                    CurrentValue.ValCompar: State.StStart,
                                    CurrentValue.ValEqual: State.StStart,
                                    CurrentValue.ValDot: State.StError,
                                    CurrentValue.ValSepar: State.StStart,
                                    CurrentValue.ValOpenCom: State.StStart,
                                    CurrentValue.ValCloseCom: State.StError,
                                    CurrentValue.ValQuote: State.StError,
                                    CurrentValue.ValDollar: State.StError,
                                    CurrentValue.ValPercent: State.StError,
                                    CurrentValue.ValAmper: State.StError,
                                    CurrentValue.ValOctot: State.StError,
                                    CurrentValue.ValUnknown: State.StError},

                  State.StRealWDot: {i: State.StError if i!=CurrentValue.Val01
                                     and i!=CurrentValue.Val27 and i!=CurrentValue.Val89
                                     else State.StRealWDec for i in CurrentValue},

                  State.StRealWDec: {CurrentValue.ValAF: State.StError,
                                     CurrentValue.ValE: State.StRealWE,
                                     CurrentValue.ValLetter: State.StError,
                                     CurrentValue.Val01: State.StRealWDec,
                                     CurrentValue.Val27: State.StRealWDec,
                                     CurrentValue.Val89: State.StRealWDec,
                                     CurrentValue.ValSpace: State.StStart,
                                     CurrentValue.ValMinus: State.StStart,
                                     CurrentValue.ValOper: State.StStart,
                                     CurrentValue.ValCompar: State.StStart,
                                     CurrentValue.ValEqual: State.StStart,
                                     CurrentValue.ValDot: State.StError,
                                     CurrentValue.ValSepar: State.StStart,
                                     CurrentValue.ValOpenCom: State.StOpenCom,
                                     CurrentValue.ValCloseCom: State.StError,
                                     CurrentValue.ValQuote: State.StError,
                                     CurrentValue.ValDollar: State.StError,
                                     CurrentValue.ValPercent: State.StError,
                                     CurrentValue.ValAmper: State.StError,
                                     CurrentValue.ValOctot: State.StError,
                                     CurrentValue.ValUnknown: State.StError},

                  State.StRealWE: {CurrentValue.ValAF: State.StError,
                                   CurrentValue.ValE: State.StError,
                                   CurrentValue.ValLetter: State.StError,
                                   CurrentValue.Val01: State.StRealFull,
                                   CurrentValue.Val27: State.StRealFull,
                                   CurrentValue.Val89: State.StRealFull,
                                   CurrentValue.ValSpace: State.StError,
                                   CurrentValue.ValMinus: State.StRealWEMin,
                                   CurrentValue.ValOper: State.StError,
                                   CurrentValue.ValCompar: State.StError,
                                   CurrentValue.ValEqual: State.StError,
                                   CurrentValue.ValDot: State.StError,
                                   CurrentValue.ValSepar: State.StError,
                                   CurrentValue.ValOpenCom: State.StError,
                                   CurrentValue.ValCloseCom: State.StError,
                                   CurrentValue.ValQuote: State.StError,
                                   CurrentValue.ValDollar: State.StError,
                                   CurrentValue.ValPercent: State.StError,
                                   CurrentValue.ValAmper: State.StError,
                                   CurrentValue.ValOctot: State.StError,
                                   CurrentValue.ValUnknown: State.StError},

                  State.StRealWEMin: {i: State.StError if i!=CurrentValue.Val01
                                      and i!=CurrentValue.Val27 and i!=CurrentValue.Val89
                                      else State.StRealFull for i in CurrentValue},

                  State.StRealFull: {CurrentValue.ValAF: State.StError,
                                     CurrentValue.ValE: State.StError,
                                     CurrentValue.ValLetter: State.StError,
                                     CurrentValue.Val01: State.StRealFull,
                                     CurrentValue.Val27: State.StRealFull,
                                     CurrentValue.Val89: State.StRealFull,
                                     CurrentValue.ValSpace: State.StStart,
                                     CurrentValue.ValMinus: State.StStart,
                                     CurrentValue.ValOper: State.StStart,
                                     CurrentValue.ValCompar: State.StStart,
                                     CurrentValue.ValEqual: State.StStart,
                                     CurrentValue.ValDot: State.StError,
                                     CurrentValue.ValSepar: State.StStart,
                                     CurrentValue.ValOpenCom: State.StStart,
                                     CurrentValue.ValCloseCom: State.StError,
                                     CurrentValue.ValQuote: State.StError,
                                     CurrentValue.ValDollar: State.StError,
                                     CurrentValue.ValPercent: State.StError,
                                     CurrentValue.ValAmper: State.StError,
                                     CurrentValue.ValOctot: State.StError,
                                     CurrentValue.ValUnknown: State.StError},

                  State.StOpenChar: {i: State.StOpenString if i!=CurrentValue.ValQuote
                                     else State.StCloseChar for i in CurrentValue},

                  State.StCloseChar: {i: State.StStart if i!=CurrentValue.ValUnknown
                                      else State.StError for i in CurrentValue},

                  State.StOpenString: {i: State.StOpenString if i!=CurrentValue.ValQuote
                                       else State.StCloseString for i in CurrentValue},

                  State.StCloseString: {i: State.StStart if i!=CurrentValue.ValUnknown
                                        else State.StError for i in CurrentValue},

                  State.StOper: {i: State.StStart if i!=CurrentValue.ValMinus
                                 and i!=CurrentValue.ValOper and i!=CurrentValue.ValCompar
                                 and i!=CurrentValue.ValEqual and i!=CurrentValue.ValDot
                                 and i!=CurrentValue.ValUnknown else State.StOper
                                 if i!=CurrentValue.ValUnknown else State.StError
                                 for i in CurrentValue},

                  State.StSepar: {i: State.StStart if i!=CurrentValue.ValUnknown
                                  else State.StError for i in CurrentValue},

                  State.StAmper: {CurrentValue.ValAF: State.StIdent,
                                  CurrentValue.ValE: State.StIdent,
                                  CurrentValue.ValLetter: State.StIdent,
                                  CurrentValue.Val01: State.StOctal,
                                  CurrentValue.Val27: State.StOctal,
                                  CurrentValue.Val89: State.StOctal,
                                  CurrentValue.ValSpace: State.StError,
                                  CurrentValue.ValMinus: State.StError,
                                  CurrentValue.ValOper: State.StError,
                                  CurrentValue.ValCompar: State.StError,
                                  CurrentValue.ValEqual: State.StError,
                                  CurrentValue.ValDot: State.StError,
                                  CurrentValue.ValSepar: State.StError,
                                  CurrentValue.ValOpenCom: State.StError,
                                  CurrentValue.ValCloseCom: State.StError,
                                  CurrentValue.ValQuote: State.StError,
                                  CurrentValue.ValDollar: State.StError,
                                  CurrentValue.ValPercent: State.StError,
                                  CurrentValue.ValAmper: State.StError,
                                  CurrentValue.ValOctot: State.StError,
                                  CurrentValue.ValUnknown: State.StError},

                  State.StASCII: {CurrentValue.ValAF: State.StError,
                                  CurrentValue.ValE: State.StError,
                                  CurrentValue.ValLetter: State.StError,
                                  CurrentValue.Val01: State.StASCII,
                                  CurrentValue.Val27: State.StASCII,
                                  CurrentValue.Val89: State.StASCII,
                                  CurrentValue.ValSpace: State.StStart,
                                  CurrentValue.ValMinus: State.StStart,
                                  CurrentValue.ValOper: State.StStart,
                                  CurrentValue.ValCompar: State.StStart,
                                  CurrentValue.ValEqual: State.StStart,
                                  CurrentValue.ValDot: State.StStart,
                                  CurrentValue.ValSepar: State.StStart,
                                  CurrentValue.ValOpenCom: State.StStart,
                                  CurrentValue.ValCloseCom: State.StError,
                                  CurrentValue.ValQuote: State.StError,
                                  CurrentValue.ValDollar: State.StError,
                                  CurrentValue.ValPercent: State.StError,
                                  CurrentValue.ValAmper: State.StError,
                                  CurrentValue.ValOctot: State.StError,
                                  CurrentValue.ValUnknown: State.StError}
                  }


    def __init__(self,fin):
        self.buf = Buffer()
        self.state = State.StStart
        self.fin = fin
        self.isEndOfFile = False
        self.isErrorCaught = False
        self.currentSymbol = ''
        self.currentLine = 1
        self.currentPosition = 0;
        self.lexemLine = 1;
        self.lexemPosition = 1;


    def getNextSymbol(self):
        symbol = self.fin.read(1)
        if symbol == '\n':
            self.currentLine += 1
            self.currentPosition = 0
        else:
            self.currentPosition += 1
        return symbol
    

    def getNextValue(self):
        if self.currentSymbol in ['A', 'B', 'C', 'D', 'F', 'a', 'b', 'c', 'd', 'f']:
            return CurrentValue.ValAF
        elif self.currentSymbol in ['E','e']:
            return CurrentValue.ValE
        elif self.currentSymbol.isalpha():
            return CurrentValue.ValLetter
        elif self.currentSymbol in ['0','1']:
            return CurrentValue.Val01
        elif self.currentSymbol in ['2','3','4','5','6','7']:
            return CurrentValue.Val27
        elif self.currentSymbol in ['8','9']:
            return CurrentValue.Val89
        elif self.currentSymbol in [' ', '\n', '\t', '\0', '\r', '']:
            return CurrentValue.ValSpace
        elif self.currentSymbol == '-':
            return CurrentValue.ValMinus
        elif self.currentSymbol in ['+', '*', '/', ':']:
            return CurrentValue.ValOper
        elif self.currentSymbol in ['<', '>']:
            return CurrentValue.ValCompar
        elif self.currentSymbol == '=':
            return CurrentValue.ValEqual
        elif self.currentSymbol == '.':
            return CurrentValue.ValDot
        elif self.currentSymbol in ['(', ')', ';', '[', ']', ',']:
            return CurrentValue.ValSepar
        elif self.currentSymbol == '{':
            return CurrentValue.ValOpenCom
        elif self.currentSymbol == '}':
            return CurrentValue.ValCloseCom
        elif self.currentSymbol == '\'':
            return CurrentValue.ValQuote
        elif self.currentSymbol == '$':
            return CurrentValue.ValDollar
        elif self.currentSymbol == '%':
            return CurrentValue.ValPercent
        elif self.currentSymbol == '&':
            return CurrentValue.ValAmper
        elif self.currentSymbol == '#':
            return CurrentValue.ValOctot
        else:
            return CurrentValue.ValUnknown


    def isEOF(self):
        return self.isEndOfFile


    def isError(self):
        return self.isErrorCaught


    def analyze(self):
        self.lexemIsFound = False
        while not self.lexemIsFound:
            if not self.state is State.StStart or self.currentSymbol == '':
                self.currentSymbol = self.getNextSymbol()

            self.currentValue = self.getNextValue()

            self.prevState = self.state
            self.state = self.transit[self.state][self.currentValue]

            if self.state == State.StError:
                self.isErrorCaught = True

            if self.state is State.StOper and not self.buf.isEmpty():
                probOper = self.buf.get() + self.currentSymbol
                if not probOper in self.pairOpers:
                    self.lexem = Lexem(self.lexemLine, self.lexemPosition, self.prevState, self.buf.get())
                    self.lexemPosition = self.currentPosition
                    self.lexemLine = self.currentLine
                    self.lexemIsFound = True
                    self.buf.clear()

            elif self.state is State.StStart:
                if self.prevState!=State.StSpace and self.prevState!=State.StCloseCom:
                    self.lexem = Lexem(self.lexemLine, self.lexemPosition, self.prevState, self.buf.get())
                    self.lexemIsFound = True
                self.lexemPosition = self.currentPosition
                self.lexemLine = self.currentLine
                self.buf.clear()
                

            if self.currentSymbol == '':
                self.isEndOfFile = True
            elif not self.state is State.StStart:
                self.buf.add(self.currentSymbol)

        return self.lexem
                
        
