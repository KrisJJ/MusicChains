from lexem import Lexem
from buffer import Buffer
from state import State
import pickle

class Lex_analyzer:
    keys = ['and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto', 'else', 'end',
            'false', 'file', 'for', 'foreach', 'function', 'goto', 'if', 'in', 'label', 'mod',
            'nil', 'not', 'of', 'or', 'packed', 'procedure', 'program', 'record', 'repeat',
            'set', 'then', 'to', 'true', 'type', 'until', 'var', 'while', 'with']

    delims = ['.', ',', ';', ':', '(', ')', '=', '+', '-', '*', '/', '<', '>', '[', ']', '{', '}', '$', '"', "'"]

    delim_ds = ['+=', '-=', '*=', '/=', ':=', '<>', '<=', '>=', '..']

    separs = [' ', '\n', '\t', '\0', '\r']

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

    income = {'letter': 1,
              'letters_AF': 2,
              'letter_e': 3,
              'digit': 4,
              'separ': 5,
              '$': 6,
              '+*': 7,
              '-': 8,
              '/': 9,
              ',': 10,
              '.': 11,
              ':': 12,
              ';': 13,
              '(': 14,
              ')': 15,
              '[': 16,
              ']': 17,
              '{': 18,
              '}': 19,
              'dash2': 20,
              '<>': 21,
              '=': 22,
              '_': 23,
              'dash1': 24,
              'none': 25}

    def __init__(self):
        self.buf = Buffer()
        self.state = State()
        self.prev_state = 0
        self.next_state = 0
        self.current = ''
        self.inc = ''
        self.prev_inc = ''
        self.k = 0
        self.file_end = False

    def is_finalised(self):
        return self.file_end

    def cur_to_inc(self,current):
        if current=='e':
            return 'letter_e'
        elif current in ['A','B','C','D','E','F']:
            return 'letter_AF'
        elif current.isalpha():
            return 'letter'
        elif current.isdigit():
            return 'digit'
        elif current in self.separs:
            return 'separ'
        elif current=='+' or current=='*':
            return '+*'
        elif current=='-':
            return '-'
        elif current=='/':
            return '/'
        elif current=='=':
            return '='
        elif current==',':
            return ','
        elif current=='.':
            return '.'
        elif current==':':
            return ':'
        elif current==';':
            return ';'
        elif current=='(':
            return '('
        elif current==')':
            return ')'
        elif current=='[':
            return '['
        elif current==']':
            return ']'
        elif current=='{':
            return '{'
        elif current=='}':
            return '}'
        elif current=='"':
            return 'dash2'
        elif current=="'":
            return 'dash1'
        elif current=='<' or current=='>':
            return '<>'
        elif current=='_':
            return '_'
        elif current=='$':
            return '$'
        elif current=='':
            return 'none'

    def analyze(self,fin,fout):
        lex = []
        lex_found = False
        mas_flag = False
        err_mess = False

        if self.k==0:
            self.current = fin.read(1)

        while not lex_found:            
            if self.state.get_name()=='error':
                if not err_mess and not self.buf.isempty():
                    print('Error: unexpected symbol sequence',self.buf.get())
                    lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                    self.k+=1
                    err_mess = True
                    self.buf.clear()
                    lex_found = True
                self.prev_state = self.state.get_id()
                self.state.set(1)

            elif self.state.get_name()=='final':
                lex.append(Lexem(self.k, self.state.get_name(), self.current))
                self.k+=1
                self.buf.clear()
                lex_found = True
                self.prev_state = self.state.get_id()
                self.state.set(1)
                self.current = fin.read(1)
                self.inc = self.cur_to_inc(self.current)

            else:
                if not mas_flag:
                    self.inc = self.cur_to_inc(self.current)

                if self.state.get_name()=='delimit':
                    self.next_state = self.delim_transit[self.income[self.prev_inc]][self.income[self.inc]]
                    if not isinstance(self.next_state , list) and State.options[self.next_state]=='delimit':
                        if self.buf.get()+self.current not in self.delim_ds:
                            self.next_state = 8
                else:
                    self.next_state = self.transit[self.state.get_id()][self.income[self.inc]]

                if isinstance(self.next_state , list):
                    mas_flag = True

                    if self.state.get_name()=='num_int':
                        self.prev_cur = self.current
                        self.current = fin.read(1)
                        self.prev_prev_inc = self.prev_inc
                        self.prev_inc = self.inc
                        self.inc = self.cur_to_inc(self.current)
                        if self.current.isdigit():
                            self.buf.add(self.prev_cur)
                            self.next_state = self.next_state[1]
                            self.prev_state = self.state.get_id()
                            self.state.set(self.next_state)
                        else:
                            lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                            self.k+=1
                            self.buf.clear()
                            lex_found = True
                            self.buf.add(self.prev_cur)
                            self.prev_state = self.state.get_id()
                            self.next_state = self.next_state[0]
                            self.state.set(self.next_state)

                    elif self.state.get_name()=='num_float':
                        if self.income[self.inc]==3:
                            if self.buf.get().rfind('e')==-1:
                                self.prev_state = self.state.get_id()
                                self.next_state = self.next_state[0]
                                self.state.set(self.next_state)
                                self.buf.add(self.current)
                            else:
                                self.prev_state = self.state.get_id()
                                self.next_state = self.next_state[1]
                                self.state.set(self.next_state)
                                self.buf.add(self.current)
                                lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                                self.k+=1
                                print('Error: unexpected symbol sequence',self.buf.get())
                                err_mess = True
                                self.buf.clear()
                                lex_found = True
                                
                        elif self.income[self.inc]==8:
                            if self.buf.get().rfind('e')==-1:
                                self.prev_state = self.state.get_id()
                                self.next_state = self.next_state[0]
                                self.state.set(self.next_state)
                                lex.append(Lexem(self.k, State.options[self.prev_state], self.buf.get()))
                                self.k+=1
                                self.buf.clear()
                                lex_found = True
                                self.buf.add(self.current)
                            elif  self.buf.get().find('e')>self.buf.get().find('-'):
                                self.next_state = self.next_state[1]
                                self.prev_state = self.state.get_id()
                                self.state.set(self.next_state)
                                self.buf.add(self.current)
                            else:
                                self.prev_state = self.state.get_id()
                                self.next_state = self.next_state[2]
                                self.state.set(self.next_state)
                                self.buf.add(self.current)
                                lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                                self.k+=1
                                print('Error: unexpected symbol sequence',self.buf.get())
                                err_mess = True
                                self.buf.clear()
                                lex_found = True
                        self.prev_cur = self.current
                        self.current = fin.read(1)
                        self.prev_prev_inc = self.prev_inc
                        self.prev_inc = self.inc
                        self.inc = self.cur_to_inc(self.current)

                    elif self.state.get_name()=='name':
                        if self.buf.get() in self.keys:
                            if self.buf.get()=='end':
                                lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                                self.k+=1
                                self.buf.clear()
                                lex_found = True
                                self.prev_state = self.state.get_id()
                                self.next_state = self.next_state[0]
                                self.state.set(self.next_state)
                            else:
                                self.buf.add(self.current)
                                self.prev_state = self.state.get_id()
                                self.next_state = self.next_state[1]
                                self.state.set(self.next_state)
                                print('Error: unexpected symbol sequence',self.buf.get())
                                err_mess = True
                                lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                                self.k+=1
                                self.buf.clear()
                                lex_found = True
                                self.prev_cur = self.current
                                self.current = fin.read(1)
                                self.prev_prev_inc = self.prev_inc
                                self.prev_inc = self.inc
                                self.inc = self.cur_to_inc(self.current)
                        else:
                            lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                            self.k+=1
                            self.buf.clear()
                            lex_found = True
                            self.prev_state = self.state.get_id()
                            self.state.set(self.next_state[2])
                            

                    elif self.prev_inc==',':
                        lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                        self.k+=1
                        self.buf.clear()
                        lex_found = True
                        self.current = fin.read(1)
                        self.prev_prev_inc = self.prev_inc
                        self.prev_inc = self.inc
                        self.inc = self.cur_to_inc(self.current)
                        if self.current.isdigit():
                            self.buf.add(self.prev_inc)
                            self.next_state = self.next_state[0]
                            self.prev_state = self.state.get_id()
                            self.state.set(self.next_state)
                        else:
                            self.buf.add(self.prev_inc)
                            self.next_state = self.next_state[1]
                            self.prev_state = self.state.get_id()
                            self.state.set(self.next_state)

                    elif self.state.get_name()=='start':
                        self.buf.add(self.current)
                        self.current = fin.read(1)
                        self.prev_prev_inc = self.prev_inc
                        self.prev_inc = self.inc
                        self.inc = self.cur_to_inc(self.current)
                        if self.current.isdigit() and (self.prev_state==10 or self.prev_state==1 or self.k==0):
                            self.next_state = self.next_state[0]
                            self.prev_state = self.state.get_id()
                            self.state.set(self.next_state)
                        else:
                            self.prev_state = self.state.get_id()
                            self.next_state = self.next_state[1]
                            self.state.set(self.next_state)
                            lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                            lex_found = True
                            self.k+=1
                            self.buf.clear()
                            self.next_state = self.delim_transit[self.income[self.prev_inc]][self.income[self.inc]]
                            self.state.set(self.next_state)

                    else:
                        self.prev_state = self.state.get_id()
                        self.state.set(8)
                        print('Error: unable to choose the next state', self.prev_state)
                        lex_found = True

                else:
                    if self.prev_inc!='}':
                        self.prev_state = self.state.get_id()
                    self.state.set(self.next_state)
                    mas_flag = False

                if not mas_flag:
                    self.prev_inc = self.inc
                    if self.state.get_name()!='start':
                        self.buf.add(self.current)
                        self.prev_cur = self.current
                        self.current = fin.read(1)
                    else:
                        if State.options[self.prev_state]=='start':
                            lex.append(Lexem(self.k, self.inc, self.current))
                            self.prev_cur = self.current
                            self.current = fin.read(1)
                        elif not self.buf.isempty():
                            if self.buf.get()[-1]=='"' or self.buf.get()[-1]=="'":
                                lex.append(Lexem(self.k, State.options[60], self.buf.get()))
                            else:
                                lex.append(Lexem(self.k, State.options[self.prev_state], self.buf.get()))

                        self.k+=1
                        self.buf.clear()
                        lex_found = True

                if self.current=='':
                    if self.state.get_name()=='string':
                        self.prev_state = self.state.get_id()
                        self.state.set(8)
                        print('String seems to have no end')
                        err_mess = True
                    elif not self.buf.isempty():
                        lex.append(Lexem(self.k, self.state.get_name(), self.buf.get()))
                        self.k+=1
                        lex_found = True
                        self.prev_state = self.state.get_id()
                        self.state.set(1)
                    else:
                        self.prev_state = self.state.get_id()
                        self.state.set(1)
                        self.file_end = True


        for a in lex:
            fout.write(str(a.get())+'\n')

        
