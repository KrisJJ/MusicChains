from lexem import Lexem
from buffer import Buffer
from state import State

class Lex_analyzer:
    keys = ['and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto', 'else', 'end',
            'false', 'file', 'for', 'foreach', 'function', 'goto', 'if', 'in', 'label', 'mod',
            'nil', 'not', 'of', 'or', 'packed', 'procedure', 'program', 'record', 'repeat',
            'set', 'then', 'to', 'true', 'type', 'until', 'var', 'while', 'with']

    delims = ['.', ',', ';', ':', '(', ')', '=', '+', '-', '*', '/', '<', '>', '[', ']', '{', '}', '$', '"', "'"]

    delim_ds = ['+=', '-=', '*=', '/=', ':=', '<>', '<=', '>=', '..']

    separs = [' ', '\n', '\t', '\0', '\r', '']

    transit = {1: {1: 7, 2: 7, 3: 7, 4: 3, 5: 1, 6: 5, 7: 10, 8: [3, 10],
                   9: 10, 10: 10, 11: 10, 12: 10, 13: 10, 14: 10, 15: 10, 16: 10,
                   17: 10, 18: 9, 19: 9, 20: 6, 21: 10, 22: 10, 23: 7},
                        
                2: {a: 8 for a in range(1,24)},
                        
                3: {1: 8, 2: 8, 3: 8, 4: 3, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: [1, 4], 12: 8, 13: 1, 14: 8, 15: 1, 16: 8,
                    17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8},
                        
                4: {1: 8, 2: 8, 3: 4, 4: 4, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: 8, 12: 8, 13: 1, 14: 8, 15: 1, 16: 8,
                    17: 8, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8},
                        
                5: {1: 8, 2: 5, 3: 8, 4: 5, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: 8, 12: 8, 13: 1, 14: 8, 15: 1, 16: 8,
                    17: 8, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8},
                        
                6: {a: 6 if a!=20 else 1 for a in range(1,24)},
                        
                7: {1: 7, 2: 7, 3: 7, 4: 7, 5: 1, 6: 8, 7: 1, 8: 1,
                    9: 1, 10: 1, 11: [2, 8, 10], 12: 1, 13: 1, 14: 1, 15: 1, 16: 1,
                    17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 7},
                        
                8: {a: 2 for a in range(1,24)},
                        
                9: {a: 9 if a!=19 else 10 for a in range(1,24)},
                        
                10: {a: 10 for a in range(1,24)}}

    delim_transit = {6: {a: 8 if a!=2 and a!=4 else 5 for a in range(1,24)},
                              
                     7: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                         9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                         17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 10, 23: 1},
                              
                     8: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                         9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                         17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 10, 23: 1},
                              
                     9: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                         9: 9, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                         17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 10, 23: 1},
                              
                     10: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: [3, 10],
                          9: 7, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1},
                              
                     11: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 8, 7: 8, 8: 8,
                          9: 8, 10: 8, 11: 10, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 8, 23: 1},
                              
                     12: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 8, 7: 8, 8: 8,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 10, 23: 1},
                              
                     13: {1: 1, 2: 1, 3: 1, 4: 8, 5: 1, 6: 8, 7: 8, 8: 8,
                          9: 1, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 8, 22: 8, 23: 1},
                              
                     14: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 1,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 1, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1},

                     15: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 1,
                          9: 1, 10: 1, 11: 1, 12: 8, 13: 1, 14: 1, 15: 1, 16: 8,
                          17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8},
                              
                     16: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 8, 7: 8, 8: 1,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 1,
                          17: 1, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1},

                     17: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 1,
                          9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 8, 15: 1, 16: 1,
                          17: 1, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8},
                              
                     18: {a: 9 if a!=19 else 1 for a in range(1,24)},

                     19: {a: 1 for a in range(1,24)},
                              
                     20: {1: 8, 2: 8, 3: 8, 4: 8, 5: 1, 6: 8, 7: 1, 8: 8,
                          9: 8, 10: 1, 11: 8, 12: 8, 13: 1, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 8, 21: 1, 22: 1, 23: 8},
                              
                     21: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 8,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 10, 23: 1},
                              
                     22: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 8, 8: 1,
                          9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 1, 15: 8, 16: 8,
                          17: 8, 18: 1, 19: 8, 20: 1, 21: 8, 22: 8, 23: 1}}

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
              'dash': 20,
              '<>': 21,
              '=': 22,
              '_': 23}

    def __init__(self,file):
        self.f = open(file, 'r')

        self.lex_array = []

        self.analyze()

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
        elif current=='"' or current=="'":
            return 'dash'
        elif current=='<' or current=='>':
            return '<>'
        elif current=='_':
            return '_'
        elif current=='$':
            return '$'

    def analyze(self):
        buf = Buffer()
        state = State()
        current = self.f.read(1)
        inc = ''
        prev_inc = ''
        mas_flag = False
        k = 1
        '''Нужно переместить, чтобы учесть создание нового анализатора при открытии скобок'''
        
        while state.get_name()!='final':

            if state.get_name()=='error':
                prev_state = state.get_id()
                state.set(2)

            else:
                if not mas_flag:
                    inc = self.cur_to_inc(current)
                
                if state.get_name()=='delimit':
                    next_state = self.delim_transit[self.income[prev_inc]][self.income[inc]]
                else:
                    next_state = self.transit[state.get_id()][self.income[inc]]

                if isinstance(next_state , list):
                    #print('Massive', state.get_name())
                    mas_flag = True
                    #print(buf.get())
                    if state.get_name()=='num_int':
                        buf.add(current)
                        current = self.f.read(1)
                        prev_prev_inc = prev_inc
                        prev_inc = inc
                        inc = self.cur_to_inc(current)
                        #print(prev_prev_inc, prev_inc, inc)
                        
                        if current.isdigit():
                            next_state = next_state[1]
                            prev_state = state.get_id()
                            state.set(next_state)
                            print(current, buf.get(), state.get_name())
                        else:
                            prev_state = state.get_id()
                            next_state = next_state[0]
                            state.set(next_state)
                            print(current, buf.get(), state.get_name())
                            
                    elif state.get_name()=='name':
                        if buf.get() in self.keys:
                            if buf.get()=='end':
                                buf.add(current)
                                prev_state = state.get_id()
                                next_state = next_state[0]
                                state.set(next_state)
                            else:
                                buf.add(current)
                                prev_state = state.get_id()
                                next_state = next_state[1]
                                state.set(next_state)
                        else:
                            self.lex_array.append(Lexem(k, state.get_name(), buf.get()))
                            k+=1
                            buf.clear()
                            
                            buf.add(current)
                            current = self.f.read(1)
                            prev_prev_inc = prev_inc
                            prev_inc = inc
                            inc = self.cur_to_inc(current)
                            #print(prev_prev_inc, prev_inc, inc)
                            
                            prev_state = state.get_id()
                            state.set(next_state[2])
                            self.lex_array.append(Lexem(k, state.get_name(), buf.get()))
                            k+=1
                            buf.clear()
                            
                            #buf.add(current)
                            prev_state = state.get_id()
                            next_state = self.delim_transit[self.income[prev_inc]][self.income[inc]]
                            state.set(next_state)
                            
                    elif prev_inc==',':
                        self.lex_array.append(Lexem(k, state.get_name(), buf.get()))
                        k+=1
                        buf.clear()
                        
                        buf.add(current)
                        current = self.f.read(1)
                        prev_prev_inc = prev_inc
                        prev_inc = inc
                        inc = self.cur_to_inc(current)
                        if current.isdigit():
                            next_state = next_state[0]
                            prev_state = state.get_id()
                            state.set(next_state)
                        else:
                            prev_state = state.get_id()
                            state.set(next_state[1])
                            self.lex_array.append(Lexem(k, state.get_name(), buf.get()))
                            k+=1
                            buf.clear()
                            
                            prev_state = state.get_id()
                            next_state = self.delim_transit[self.income[prev_inc]][self.income[inc]]
                            state.set(next_state)

                    elif state.get_name()=='start':
                        buf.add(current)
                        current = self.f.read(1)
                        prev_prev_inc = prev_inc
                        prev_inc = inc
                        inc = self.cur_to_inc(current)

                        if current.isdigit() and (prev_state==10 or prev_state==1):
                            next_state = next_state[0]
                            prev_state = state.get_id()
                            state.set(next_state)
                        else:
                            prev_state = state.get_id()
                            next_state = next_state[1]
                            state.set(next_state)
                            self.lex_array.append(Lexem(k, state.get_name(), buf.get()))
                            k+=1
                            buf.clear()
                            next_state = self.delim_transit[self.income[prev_inc]][self.income[inc]]
                            state.set(next_state)

                    else:
                        print('Error: found massive does not exist')
                                                

                else:
                    if prev_inc!='}':
                        prev_state = state.get_id()
                    state.set(next_state)
                    mas_flag = False   

                if not mas_flag:
                    prev_inc = inc

                    if state.get_name()!='start':
                        buf.add(current)
                        prev_cur = current
                        current = self.f.read(1)
                    else:
                        if State.options[prev_state]=='start':
                            self.lex_array.append(Lexem(k, inc, current))
                            prev_cur = current
                            current = self.f.read(1)
                        else:
                            self.lex_array.append(Lexem(k, State.options[prev_state], buf.get()))

                        k+=1
                        buf.clear()

                    if current=='' and prev_cur=='':
                        state.set(2)

                #if k>100:
                #    state.set(2)

            #print(state.get_name(),inc, buf.get())

        print('bugs: .. "" 2.3e')
        
        self.lex_array.append(Lexem(k, State.options[prev_state], buf.get()))
        k+=1
        self.lex_array.append(Lexem(k, state.get_name(), ''))
        for i in self.lex_array:
            print(i.get())

        while current!='':
            current = self.f.read(1)
            if self.cur_to_inc(current)!='separ':
                print('Error: found symbols after final tag')
                break
                
            
