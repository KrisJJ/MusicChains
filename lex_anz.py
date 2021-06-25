<<<<<<< HEAD
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
=======
from lexem import Lexem
from buffer import Buffer
from state import State
from admission import Admission
>>>>>>> 57581682d4cd848517ef9a5580807a674eacff0f

    def clear(self):
        self.inner = ''

    def add(self,c):
        self.inner += c

    def get(self):
        return self.inner

    def isEmpty(self):
        return self.inner==''

<<<<<<< HEAD

class Lexem:
    def __init__(self,line,pos,state,bufferedString):
        self.line = line
        self.pos = pos
        self.original = bufferedString
=======
    transit = {1: {1: 7, 2: 7, 3: 7, 4: 3, 5: 1, 6: 5, 7: 10, 8: [3, 10],
                   9: 10, 10: 10, 11: 10, 12: 10, 13: 10, 14: 10, 15: 10, 16: 10,
                   17: 10, 18: 9, 19: 9, 20: 60, 21: 10, 22: 10, 23: 7, 24: 61, 25: 1},
                        
                2: {a: 8 for a in range(1,26)},
                        
                3: {1: 8, 2: 8, 3: 4, 4: 3, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: [10, 4], 12: 8, 13: 1, 14: 8, 15: 1, 16: 8,
                    17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8, 24: 8, 25: 1},
                        
                4: {1: 8, 2: 8, 3: [4, 8], 4: 4, 5: 1, 6: 8, 7: 1, 8: [1, 4, 8],
                    9: 1, 10: 1, 11: 8, 12: 8, 13: 1, 14: 8, 15: 1, 16: 8,
                    17: 8, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8, 24: 8, 25: 1},
                        
                5: {1: 8, 2: 5, 3: 8, 4: 5, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: 8, 12: 8, 13: 1, 14: 8, 15: 1, 16: 8,
                    17: 8, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8, 24: 8, 25: 1},
                        
                60: {a: 60 if a!=20 else 10 for a in range(1,26)},

                61: {a: 61 if a!=24 else 10 for a in range(1,26)},
                        
                7: {1: 7, 2: 7, 3: 7, 4: 7, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: [2, 8, 1], 12: 1, 13: 1, 14: 1, 15: 1, 16: 1,
                    17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 7, 24: 8, 25: 1},
                        
                8: {a: 2 for a in range(1,26)},
                        
                9: {a: 9 if a!=19 else 10 for a in range(1,26)},
                        
                10: {a: 10 for a in range(1,26)}}

    delim_transit = {6: {a: 8 if a!=2 and a!=4 else 5 for a in range(1,26)},
                              
                     7: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                         9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                         17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 10, 23: 1, 24: 1, 25: 1},
                              
                     8: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                         9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                         17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 10, 23: 1, 24: 8, 25: 1},
                              
                     9: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                         9: 9, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                         17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 10, 23: 1, 24: 8, 25: 1},
                              
                     10: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: [3, 10],
                          9: 7, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1, 24: 1, 25: 1},
                              
                     11: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 8, 7: 8, 8: 8,
                          9: 8, 10: 8, 11: 10, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 8, 23: 1, 24: 8, 25: 1},
                              
                     12: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 8, 7: 8, 8: 8,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 10, 23: 1, 24: 8, 25: 1},
                              
                     13: {1: 1, 2: 1, 3: 1, 4: 8, 5: 1, 6: 8, 7: 8, 8: 8,
                          9: 1, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 8, 23: 1, 24: 8, 25: 1},
                              
                     14: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 1,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 1, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1, 24: 1, 25: 1},

                     15: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 1,
                          9: 1, 10: 1, 11: 1, 12: 8, 13: 1, 14: 1, 15: 1, 16: 8,
                          17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8, 24: 8, 25: 1},
                              
                     16: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 8, 7: 8, 8: 1,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 1,
                          17: 1, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1, 24: 1, 25: 1},

                     17: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 1,
                          9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 8, 15: 1, 16: 1,
                          17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8, 24: 8, 25: 1},
                              
                     18: {a: 9 if a!=19 else 1 for a in range(1,26)},

                     19: {a: 1 for a in range(1,26)},
                              
                     20: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 8,
                          9: 8, 10: 1, 11: 8, 12: 8, 13: 1, 14: 1, 15: 1, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 1, 22: 1, 23: 8, 24: 1, 25: 1},
                              
                     21: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 10, 22: 10, 23: 1, 24: 1, 25: 1},
                              
                     22: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 1,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1, 24: 1, 25: 1},

                     24: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 8,
                          9: 8, 10: 1, 11: 8, 12: 8, 13: 1, 14: 1, 15: 1, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 1, 22: 1, 23: 8, 24: 1, 25: 1}}


    def __init__(self):
        self.buf = Buffer()
        self.state = State()
        self.prev_state = 0
        self.next_state = 0
        self.current = ''
        self.admis = ''
        self.prev_admis = ''
        self.k = 1
        self.k_cur = 1
        self.s = 1
        self.file_end = False
        
        self.new_line = False

    def is_finalised(self):
        return self.file_end

    def cur_to_admis(self,current):
        cur_d = {let1:'letter' for let1 in 'GHIJKLMNOPQRSTUVWXYZabcdfghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}
        cur_d.update([(let0,'letter_AF') for let0 in ['A','B','C','D','E','F']])
        cur_d.update([(str(dig),'digit') for dig in range(10)])
        cur_d.update([(sep,'separ') for sep in self.separs])
        cur_d.update([(sig0,'+*') for sig0 in ['+','*']])
        cur_d.update([(sig1,sig1) for sig1 in ['-','/','=',',','.',':',';','(',')','[',']','{','}','_','$']])
        cur_d.update([(sig2,'<>') for sig2 in ['<','>']])
        cur_d.update([("'",'dash1'),('"','dash2'),('','none'),('e','letter_e')])
        return cur_d[current]

    def make_lex(self,s,k,state,buf):
        if state!='separ' and state!='comment':
            self.lex = Lexem(s,k,state,buf)
            self.lex_found = True
        self.buf.clear()
        self.k = self.k_cur
        if self.new_line:
            self.s+=1
            self.k_cur = 1
            self.new_line = False

    def next_cur(self,fin):
        self.prev_cur = self.current
        self.current = fin.read(1)
        self.k_cur+=1
        if self.current=='\n':
            self.new_line = True
        self.prev_prev_admis = self.prev_admis
        self.prev_admis = self.admis
        self.admis = self.cur_to_admis(self.current)

    def new_state(self,next_state):
        self.prev_state = self.state.get_id()
        self.next_state = next_state
        self.state.set(self.next_state)

    def analyze(self,fin):
        mas_flag = False
        err_mess = False
        self.lex_found = False

        if self.s==1 and self.k==1:
            self.next_cur(fin)
            if self.current=='\n':
                self.new_line = True

        while not self.lex_found:            
            if self.state.get_name()=='error':
                if not err_mess and not self.buf.isempty():
                    print('Error: unexpected symbol sequence',self.buf.get(),'on line',self.s,'in file',fin)
                    self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                    err_mess = True
                self.new_state(1)

            elif self.state.get_name()=='final':
                self.make_lex(self.s, self.k, self.state.get_name(), self.current)
                self.new_state(1)
                self.next_cur(fin)
                if self.current=='\n':
                    self.new_line = True
                self.admis = self.cur_to_admis(self.current)
>>>>>>> 57581682d4cd848517ef9a5580807a674eacff0f

        if state is State.StError:
            self.lexemType = 'Error'
        elif state is State.StCloseDir:
            self.lexemType = 'Directory'
            self.lexemValue = bufferedString
        elif state is State.StIdent:
            if bufferedString in Lex_analyzer.keywords:
                self.lexemType = 'Keyword'
            else:
<<<<<<< HEAD
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
        
=======
                if not mas_flag:
                    self.admis = self.cur_to_admis(self.current)

                if self.state.get_name()=='delimit':
                    self.next_state = self.delim_transit[Admission.get_from_title(self.prev_admis)][Admission.get_from_title(self.admis)]
                    if not isinstance(self.next_state , list) and State.options[self.next_state]=='delimit':
                        if self.buf.get()+self.current not in self.delim_ds:
                            self.next_state = 8
                else:
                    self.next_state = self.transit[self.state.get_id()][Admission.get_from_title(self.admis)]

                if isinstance(self.next_state , list):
                    mas_flag = True

                    if self.state.get_name()=='num_int':
                        self.next_cur(fin)
                        if self.current.isdigit():
                            self.buf.add(self.prev_cur)
                            self.new_state(self.next_state[1])
                        else:
                            self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                            self.buf.add(self.prev_cur)
                            self.new_state(self.next_state[0])

                    elif self.state.get_name()=='num_float':
                        if Admission.get_from_title(self.admis)==3:
                            if self.buf.get().rfind('e')==-1:
                                self.new_state(self.next_state[0])
                                self.buf.add(self.current)
                            else:
                                self.new_state(self.next_state[1])
                                self.buf.add(self.current)
                                print('Error: unexpected symbol sequence',self.buf.get(),'on line',self.s,'in file',fin)
                                self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                                err_mess = True
                                
                        elif Admission.get_from_title(self.admis)==8:
                            if self.buf.get().rfind('e')==-1:
                                self.new_state(self.next_state[0])
                                self.make_lex(self.s, self.k, State.options[self.prev_state], self.buf.get())
                                self.buf.add(self.current)
                            elif  self.buf.get().find('e')>self.buf.get().find('-'):
                                self.new_state(self.next_state[1])
                                self.buf.add(self.current)
                            else:
                                self.new_state(self.next_state[2])
                                self.buf.add(self.current)
                                print('Error: unexpected symbol sequence',self.buf.get(),'on line',self.s,'in file',fin)
                                self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                                err_mess = True
                        self.next_cur(fin)

                    elif self.state.get_name()=='name':
                        if self.buf.get() in self.keys:
                            if self.buf.get()=='end':
                                self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                                self.new_state(self.next_state[0])
                            else:
                                self.buf.add(self.current)
                                self.new_state(self.next_state[1])
                                print('Error: unexpected symbol sequence',self.buf.get(),'on line',self.s,'in file',fin)
                                err_mess = True
                                self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                                self.next_cur(fin)
                        else:
                            self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                            self.new_state(self.next_state[2])
                            

                    elif self.prev_admis==',':
                        self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                        self.next_cur(fin)
                        if self.current.isdigit():
                            self.buf.add(self.prev_inc)
                            self.new_state(self.next_state[0])
                        else:
                            self.buf.add(self.prev_inc)
                            self.new_state(self.next_state[1])

                    elif self.state.get_name()=='start':
                        self.buf.add(self.current)
                        self.next_cur(fin)
                        if self.current.isdigit() and (self.prev_state==10 or self.prev_state==1 or self.k==0):
                            self.new_state(self.next_state[0])
                        else:
                            self.new_state(self.next_state[1])
                            self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                            self.new_state(self.delim_transit[Admission.get_from_title(self.prev_admis)][Admission.get_from_title(self.admis)])
                            
                    else:
                        self.new_state(8)
                        print('Error: unable to choose the next state', self.prev_state)
                        lex_found = True

                else:
                    if self.prev_admis!='}':
                        self.prev_state = self.state.get_id()
                    self.state.set(self.next_state)
                    mas_flag = False

                if not mas_flag:
                    self.prev_admis = self.admis
                    if self.state.get_name()!='start':
                        self.buf.add(self.current)
                        self.next_cur(fin)
                        if self.current=='\n':
                            self.new_line = True
                    else:
                        if State.options[self.prev_state]=='start':
                            self.make_lex(self.s, self.k, self.admis, self.current)
                            self.next_cur(fin)
                            if self.current=='\n':
                                self.new_line = True
                        elif not self.buf.isempty():
                            if self.buf.get()[-1]=='"' or self.buf.get()[-1]=="'":
                                self.make_lex(self.s, self.k, State.options[60], self.buf.get())
                            else:
                                self.make_lex(self.s, self.k, State.options[self.prev_state], self.buf.get())
                                

                if self.current=='':
                    if self.state.get_name()=='string':
                        self.new_state(8)
                        print('String seems to have no end')
                        err_mess = True
                    elif not self.buf.isempty():
                        self.make_lex(self.s, self.k, self.state.get_name(), self.buf.get())
                        self.new_state(1)
                    else:
                        self.new_state(1)
                        self.file_end = True

                #print(self.s, self.k, self.current, self.state.get_name(), self.buf.get())


        return self.lex
>>>>>>> 57581682d4cd848517ef9a5580807a674eacff0f

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
                
        
