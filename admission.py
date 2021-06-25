from enum import Enum

class Admission(Enum):
    l1 = (1,'letter')
    l2 = (2,'letters_AF')
    l3 = (3,'letter_e')
    l4 = (4,'digit')
    l5 = (5,'separ')
    l6 = (6,'$')
    l7 = (7,'+*')
    l8 = (8,'-')
    l9 = (9,'/')
    l10 = (10,',')
    l11 = (11,'.')
    l12 = (12,':')
    l13 = (13,';')
    l14 = (14,'(')
    l15 = (15,')')
    l16 = (16,'[')
    l17 = (17,']')
    l18 = (18,'{')
    l19 = (19,'}')
    l20 = (20,'dash2')
    l21 = (21,'<>')
    l22 = (22,'=')
    l23 = (23,'_')
    l24 = (24,'dash1')
    l25 = (25,'none')

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def get_from_title(title):
        for a in Admission:
            if a.title==title:
                return a.id
                break
