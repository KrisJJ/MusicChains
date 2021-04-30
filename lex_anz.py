from lexem import Lexem
from buffer import Buffer
from state import State
from admission import Admission

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

            else:
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

        
