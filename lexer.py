from enum import Enum

class CharType(Enum):
    CTUnknown = 0
    CTAF = 1
    CTE = 2
    CTLetter = 3
    CT01 = 4
    CT27 = 5
    CT89 = 6
    CTSpace = 7
    CTMinus = 8
    CTOper = 9
    CTCompar = 10
    CTEqual = 11
    CTDot = 12
    CTSepar = 13
    CTOpenCom = 14
    CTCloseCom = 15
    CTQuote = 16
    CTDollar = 17
    CTPercent = 18
    CTAmper = 19
    CTOctot = 20


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
    StHexadecimal = 13
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
            self.lexemValue = 'wrong sequence of symbols'

        elif state is State.StCloseDir:
            self.lexemType = 'Directory'
            self.lexemValue = bufferedString

        elif state is State.StIdent:
            if bufferedString in Lexer.keywords:
                self.lexemType = 'Keyword'
            else:
                self.lexemType = 'Identif'
            self.lexemValue = bufferedString

        elif state is State.StDecimal:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString)
            if self.lexemValue > 2147483647 or self.lexemValue < -2147483648:
                self.lexemType = 'Error'
                self.lexemValue = 'unable to present as integer'

        elif state is State.StBinary:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString[1:],2)
            if self.lexemValue > 2147483647 or self.lexemValue < -2147483648:
                self.lexemType = 'Error'
                self.lexemValue = 'unable to present as integer'

        elif state is State.StOctal:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString[1:],8)
            if self.lexemValue > 2147483647 or self.lexemValue < -2147483648:
                self.lexemType = 'Error'
                self.lexemValue = 'unable to present as integer'

        elif state is State.StHexadecimal:
            self.lexemType = 'Integer'
            self.lexemValue = int(bufferedString[1:],16)
            if self.lexemValue > 2147483647 or self.lexemValue < -2147483648:
                self.lexemType = 'Error'
                self.lexemValue = 'unable to present as integer'
                

        elif state is State.StRealWDec or state is State.StRealFull:
            self.lexemType = 'Float'
            self.lexemValue = float(bufferedString)
            if self.lexemValue > 1.8e307+9 or self.lexemValue < -1.8e307-9:
                self.lexemType = 'Error'
                self.lexemValue = 'unable to present as float'

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
            tempervalue = int(bufferedString[1:])
            if False: #tempervalue>127 or tempervalue<0:
                self.lexemType = 'Error'
                self.lexemValue = 'unable to get ASCII symbol from utf-8 code'
            else:
                self.lexemType = 'Char'
                self.lexemValue = chr(tempervalue)

        elif state is State.StFinal:
            self.lexemType = 'Final'
            self.lexemValue = bufferedString

    def getString(self):
        if self.lexemType == 'Error':
            return f"{self.line}\t{self.pos}\tError: {self.lexemValue}: {self.original}"
        else:
            return f"{self.line}\t{self.pos}\t{self.lexemType}\t{self.lexemValue}\t{self.original}"


    def getType(self):
        return self.lexemType


    def getValue(self):
        return self.lexemValue


    def getPosition(self):
        return f"line {self.line} position {self.pos}"


    def get(self):
        return self
    
    

class Lexer:
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

    transit = {State.StStart: {CharType.CTAF: State.StIdent,
                               CharType.CTE: State.StIdent,
                               CharType.CTLetter: State.StIdent,
                               CharType.CT01: State.StDecimal,
                               CharType.CT27: State.StDecimal,
                               CharType.CT89: State.StDecimal,
                               CharType.CTSpace: State.StSpace,
                               CharType.CTMinus: State.StOper,
                               CharType.CTOper: State.StOper,
                               CharType.CTCompar: State.StOper,
                               CharType.CTEqual: State.StOper,
                               CharType.CTDot: State.StOper,
                               CharType.CTSepar: State.StSepar,
                               CharType.CTOpenCom: State.StOpenCom,
                               CharType.CTCloseCom: State.StError,
                               CharType.CTQuote: State.StOpenChar,
                               CharType.CTDollar: State.StHexadecimal,
                               CharType.CTPercent: State.StBinary,
                               CharType.CTAmper: State.StAmper,
                               CharType.CTOctot: State.StASCII,
                               CharType.CTUnknown: State.StError},
                  
                  State.StFinal: {i: State.StError for i in CharType},

                  State.StError: {i: State.StStart for i in CharType},

                  State.StSpace: {i: State.StStart if i != CharType.CTUnknown
                                  else State.StError
                                  for i in CharType},

                  State.StOpenCom: {i: State.StOpenCom if not i in [CharType.CTCloseCom, CharType.CTDollar, CharType.CTUnknown]
                                    else State.StCloseCom if not i in [CharType.CTDollar, CharType.CTUnknown]
                                    else State.StOpenDir if i!=CharType.CTUnknown
                                    else State.StError
                                    for i in CharType},

                  State.StCloseCom: {i: State.StStart if i!=CharType.CTUnknown
                                     else State.StError
                                     for i in CharType},

                  State.StOpenDir: {i: State.StOpenCom if not i in [CharType.CTCloseCom, CharType.CTUnknown]
                                    else State.StCloseDir if i!=CharType.CTUnknown
                                    else State.StError
                                    for i in CharType},

                  State.StCloseDir: {i: State.StStart if i!=CharType.CTUnknown
                                     else State.StError
                                     for i in CharType},

                  State.StIdent: {i: State.StStart if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                CharType.CTAF, CharType.CTE, CharType.CTLetter,
                                                                CharType.CTCloseCom, CharType.CTQuote, CharType.CTDollar,
                                                                CharType.CTPercent, CharType.CTAmper, CharType.CTOctot,
                                                                CharType.CTUnknown]
                                  else State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                  CharType.CTAF, CharType.CTE, CharType.CTLetter]
                                  else State.StIdent
                                  for i in CharType},

                  State.StDecimal: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                  CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                  CharType.CTCompar, CharType.CTEqual,
                                                                  CharType.CTSepar, CharType.CTOpenCom,
                                                                  CharType.CTDot]
                                    else State.StStart if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                    CharType.CTDot]
                                    else State.StDecimal if i != CharType.CTDot
                                    else State.StRealWDot
                                    for i in CharType},

                  State.StBinary: {i: State.StError if not i in [CharType.CT01,
                                                                 CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                 CharType.CTCompar, CharType.CTEqual,
                                                                 CharType.CTSepar, CharType.CTOpenCom]
                                   else State.StStart if i != CharType.CT01
                                   else State.StBinary
                                   for i in CharType},

                  State.StOctal: {i: State.StError if not i in [CharType.CT01, CharType.CT27,
                                                                CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                CharType.CTCompar, CharType.CTEqual,
                                                                CharType.CTSepar, CharType.CTOpenCom]
                                  else State.StStart if not i in [CharType.CT01, CharType.CT27]
                                  else State.StOctal
                                  for i in CharType},

                  State.StHexadecimal: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                      CharType.CTAF, CharType.CTE,
                                                                      CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                      CharType.CTCompar, CharType.CTEqual,
                                                                      CharType.CTSepar, CharType.CTOpenCom]
                                        else State.StStart if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                      CharType.CTAF, CharType.CTE]
                                        else State.StHexadecimal
                                        for i in CharType},

                  State.StRealWDot: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89]
                                     else State.StRealWDec
                                     for i in CharType},

                  State.StRealWDec: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                   CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                   CharType.CTCompar, CharType.CTEqual,
                                                                   CharType.CTSepar, CharType.CTOpenCom,
                                                                   CharType.CTE]
                                     else State.StStart if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                     CharType.CTE, CharType.CTOpenCom]
                                     else State.StRealWDec if not i in [CharType.CTE, CharType.CTOpenCom]
                                     else State.StRealWE if i != CharType.CTOpenCom
                                     else State.StOpenCom
                                     for i in CharType},

                  State.StRealWE: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                 CharType.CTMinus]
                                   else State.StRealFull if i != CharType.CTMinus
                                   else State.StRealWEMin
                                   for i in CharType},

                  State.StRealWEMin: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89]
                                      else State.StRealFull
                                      for i in CharType},

                  State.StRealFull: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                   CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                   CharType.CTCompar, CharType.CTEqual,
                                                                   CharType.CTSepar, CharType.CTOpenCom]
                                     else State.StStart if not i in [CharType.CT01, CharType.CT27, CharType.CT89]
                                     else State.StRealFull
                                     for i in CharType},

                  State.StOpenChar: {i: State.StOpenString if i!=CharType.CTQuote
                                     else State.StCloseChar
                                     for i in CharType},

                  State.StCloseChar: {i: State.StStart if i!=CharType.CTUnknown
                                      else State.StError
                                      for i in CharType},

                  State.StOpenString: {i: State.StOpenString if i!=CharType.CTQuote
                                       else State.StCloseString
                                       for i in CharType},

                  State.StCloseString: {i: State.StStart if i!=CharType.CTUnknown
                                        else State.StError
                                        for i in CharType},

                  State.StOper: {i: State.StStart if not i in [CharType.CTMinus, CharType.CTOper, CharType.CTCompar,
                                                               CharType.CTEqual, CharType.CTDot, CharType.CTUnknown]
                                 else State.StOper if i!=CharType.CTUnknown
                                 else State.StError
                                 for i in CharType},

                  State.StSepar: {i: State.StStart if i!=CharType.CTUnknown
                                  else State.StError
                                  for i in CharType},

                  State.StAmper: {i: State.StError if not i in [CharType.CTAF, CharType.CTE, CharType.CTLetter,
                                                                CharType.CT01, CharType.CT27, CharType.CT89]
                                  else State.StIdent if not i in [CharType.CT01, CharType.CT27, CharType.CT89]
                                  else State.StOctal
                                  for i in CharType},

                  State.StASCII: {i: State.StError if not i in [CharType.CT01, CharType.CT27, CharType.CT89,
                                                                CharType.CTSpace, CharType.CTMinus, CharType.CTOper,
                                                                CharType.CTCompar, CharType.CTEqual, CharType.CTDot,
                                                                CharType.CTSepar, CharType.CTOpenCom]
                                  else State.StStart if not i in [CharType.CT01, CharType.CT27, CharType.CT89]
                                  else State.StASCII
                                  for i in CharType}
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

        self.charTypeTurner = {i: CharType.CTAF for i in ['A', 'B', 'C', 'D', 'F', 'a', 'b', 'c', 'd', 'f']}
        self.charTypeTurner.update([(i, CharType.CTE) for i in ['E','e']])
        self.charTypeTurner.update([(i, CharType.CTLetter) for i in ['G','H','I','J','K','L','M','N','O','P','Q','R','S',
                                                                     'T','U','V','W','X','Y','Z','g','h','i','j','k','l',
                                                                     'm','n','o','p','q','r','s','t','u','v','w','x','y',
                                                                     'z','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К',
                                                                     'Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч',
                                                                     'Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д',
                                                                     'е','ё','ж','з','и','й','к','л','м','н','о','п','р',
                                                                     'с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э',
                                                                     'ю','я']])
        self.charTypeTurner.update([(i, CharType.CT01) for i in ['0','1']])
        self.charTypeTurner.update([(i, CharType.CT27) for i in ['2','3','4','5','6','7']])
        self.charTypeTurner.update([(i, CharType.CT89) for i in ['8','9']])
        self.charTypeTurner.update([(i, CharType.CTSpace) for i in [' ', '\n', '\t', '\0', '\r', '']])
        self.charTypeTurner.update([('-', CharType.CTMinus)])
        self.charTypeTurner.update([(i, CharType.CTOper) for i in ['+', '*', '/', ':']])
        self.charTypeTurner.update([(i, CharType.CTCompar) for i in ['<', '>']])
        self.charTypeTurner.update([('=', CharType.CTEqual)])
        self.charTypeTurner.update([('.', CharType.CTDot)])
        self.charTypeTurner.update([(i, CharType.CTSepar) for i in ['(', ')', ';', '[', ']', ',']])
        self.charTypeTurner.update([('{', CharType.CTOpenCom)])
        self.charTypeTurner.update([('}', CharType.CTCloseCom)])
        self.charTypeTurner.update([('\'', CharType.CTQuote)])
        self.charTypeTurner.update([('$', CharType.CTDollar)])
        self.charTypeTurner.update([('%', CharType.CTPercent)])
        self.charTypeTurner.update([('&', CharType.CTAmper)])
        self.charTypeTurner.update([('#', CharType.CTOctot)])


    def getNextSymbol(self):
        symbol = self.fin.read(1)
        if symbol == '\n':
            self.currentLine += 1
            self.currentPosition = 0
        else:
            self.currentPosition += 1
        return symbol
    

    def getNextValue(self):
        if self.currentSymbol in self.charTypeTurner.keys():
            return self.charTypeTurner[self.currentSymbol]
        else:
            return CharType.CTUnknown


    def isError(self):
        return self.isErrorCaught


    def analyze(self):
        if self.isEndOfFile and not self.isErrorCaught:
            self.lexem = self.lexem = Lexem(self.lexemLine, self.lexemPosition, State.StFinal, '')
        else:
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
                
        
