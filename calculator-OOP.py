from tkinter import *
import math
class GUI(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.main()
        self.num = ['','']
        self.status = {'sum' : False ,'difference' : False , 'product' : False ,'quotient' : False , 'exponent' : False  , 'radical' : False}
        self.Situation = {'st' : False ,'eq' : False , 'Oparenthesis': False,'Cparenthesis' : False ,'parenthesis' : '', 'result' : '' , 'negative' : False ,'float' :False}
    def one1(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '1'
        elif self.Situation['st'] == True :
            self.res['text'] = '1'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '1'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def two2(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '2'
        elif self.Situation['st'] == True :
            self.res['text'] = '2'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '2'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def three3(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '3'
        elif self.Situation['st'] == True :
            self.res['text'] = '3'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '3'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def four4(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '4'
        elif self.Situation['st'] == True :
            self.res['text'] = '4'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '4'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def five5(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '5'
        elif self.Situation['st'] == True :
            self.res['text'] = '5'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '5'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def six6(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '6'
        elif self.Situation['st'] == True :
            self.res['text'] = '6'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '6'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def seven7(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '7'
        elif self.Situation['st'] == True :
            self.res['text'] = '7'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '7'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def eight8(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '8'
        elif self.Situation['st'] == True :
            self.res['text'] = '8'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '8'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def nine9(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '9'
        elif self.Situation['st'] == True :
            self.res['text'] = '9'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '9'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def zero0(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '0'
        elif self.Situation['st'] == True :
            self.res['text'] = '0'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '0'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def dot1(self) :
        if self.Situation['st'] == False :
            self.res['text'] = self.res['text'] + '.'
        elif self.Situation['st'] == True :
            self.res['text'] = '.'
            self.Situation['st'] = False
        if self.Situation['eq'] == True :
            self.res['text'] = '.'
            self.his['text'] = ''
            self.num[0] = ''
            self.num[1] = ''
            self.Situation['st'] = False
            self.Situation['eq'] = False
    def sum1(self) :
        if self.Situation['eq'] == True :
            self.his['text'] = str(self.his['text']) + str(self.res['text'])
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == False: 
            self.his['text'] = str(self.his['text']) + str(self.res['text']) + '+'
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == True: 
            self.his['text'] = str(self.his['text']) + '+'
            self.Situation['Cparenthesis'] = False
        if self.num[0] == '' :
            self.num[0] = self.res['text']
            self.res['text'] = ''
        elif self.num[0] != '' and self.num[1] == '' :
            self.num[1] = self.res['text']
            self.res['text'] = ''
        if self.num[0] != '' and self.num[1] != '' :
            self.equality()
            self.num[0] = self.res['text']
            self.num[1] = ''
            self.Situation['st'] = True
        if self.num[0] == '' :
            self.status['sum'] = True
        if self.num[1] == '' :
            self.status['sum'] = True
    def difference(self) :
        if self.Situation['eq'] == True :
            self.his['text'] = str(self.his['text']) + str(self.res['text'])
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == False: 
            self.his['text'] = str(self.his['text']) + str(self.res['text']) + '-'
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == True: 
            self.his['text'] = str(self.his['text']) + '-'
            self.Situation['Cparenthesis'] = False
        if self.num[0] == '' :
            self.num[0] = self.res['text']
            self.res['text'] = ''
            self.status['difference'] = True
        elif self.num[0] != '' and self.num[1] == '' :
            self.num[1] = self.res['text']
            self.res['text'] = ''
        if self.num[0] != '' and self.num[1] != '' :
            self.equality()
            self.num[0] = self.res['text']
            self.num[1] = ''
            self.Situation['st'] = True
        if self.num[0] == '' :
            self.status['difference'] = True
        if self.num[1] == '' :
            self.status['difference'] = True
    def product(self) :
        if self.Situation['eq'] == True :
            self.his['text'] = str(self.his['text']) + str(self.res['text'])
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == False: 
            self.his['text'] = str(self.his['text']) + str(self.res['text']) + '×'
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == True: 
            self.his['text'] = str(self.his['text']) + '×'
            self.Situation['Cparenthesis'] = False
        if self.num[0] == '' :
            self.num[0] = self.res['text']
            self.res['text'] = ''
            self.status['product'] = True
        elif self.num[0] != '' and self.num[1] == '' :
            self.num[1] = self.res['text']
            self.res['text'] = ''
        if self.num[0] != '' and self.num[1] != '' :
            self.equality()
            self.num[0] = self.res['text']
            self.num[1] = ''
            self.Situation['st'] = True
        if self.num[0] == '' :
            self.status['product'] = True
        if self.num[1] == '' :
            self.status['product'] = True 
    def quotient(self) :
        if self.Situation['eq'] == True :
            self.his['text'] = str(self.his['text']) + str(self.res['text'])
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == False: 
            self.his['text'] = str(self.his['text']) + str(self.res['text']) + '÷'
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == True: 
            self.his['text'] = str(self.his['text']) + '÷'
            self.Situation['Cparenthesis'] = False
        if self.num[0] == '' :
            self.num[0] = self.res['text']
            self.res['text'] = ''
            self.status['quotient'] = True
        elif self.num[0] != '' and self.num[1] == '' :
            self.num[1] = self.res['text']
            self.res['text'] = ''
        if self.num[0] != '' and self.num[1] != '' :
            self.equality()
            self.num[0] = self.res['text']
            self.num[1] = ''
            self.Situation['st'] = True
        if self.num[0] == '' :
            self.status['quotient'] = True
        if self.num[1] == '' :
            self.status['quotient'] = True
    def Negative(self) :
        value = int(self.res['text'])
        if abs(value) == value :
            self.res['text'] = '-' + str(self.res['text'])
        else :
            value = abs(value)
            self.res['text'] = value
    def Ce(self) :
        self.res['text'] = self.res['text'].rstrip(self.res['text'][-1])
    def C(self) :
        self.his['text'] = ''
        self.res['text'] = ''
        self.num[0] = ''
        self.num[1] = ''
        self.status['sum'] = False
        self.status['difference'] = False
        self.status['product'] = False
        self.status['quotient'] = False
        self.status['exponent'] = False
        self.Situation['st'] = False
        self.Situation['eq'] = False
        self.Situation['result'] = False
        self.Situation['Cparenthesis'] = False
    def Persent(self) :
        first_value = int(self.res['text'])
        value =  int(self.res['text']) / 100
        self.his['text'] = self.his['text'] + str(first_value) + '%'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = value
    def equality(self) :
        if self.status['sum'] == True :
            self.res['text'] = float(self.num[0]) + float(self.num[1])
            self.status['sum'] = False
        elif self.status['difference'] == True :
            self.res['text'] = float(self.num[0]) - float(self.num[1])
            self.status['difference'] = False
        elif self.status['product'] == True :
            self.res['text'] = float(self.num[0]) * float(self.num[1])
            self.status['product'] = False
        elif self.status['quotient'] == True :
            self.res['text'] = float(self.num[0]) / float(self.num[1])
            self.status['quotient'] = False
        elif self.status['exponent'] == True :
            self.res['text'] = float(self.num[0]) ** float(self.num[1])
            self.status['exponent'] = False
    def equals(self) :
        if self.status['sum'] == True and self.Situation['eq'] == False :
            self.Situation['eq'] = True
            self.sum1()
        elif self.status['difference'] == True :
            self.Situation['eq'] = True
            self.difference()
        elif self.status['product'] == True :
            self.Situation['eq'] = True
            self.product()
        elif self.status['quotient'] == True :
            self.Situation['eq'] = True
            self.quotient()
        elif self.status['exponent'] == True :
            self.Situation['eq'] = True
            self.Exponent ()
    def Oparenthesis(self) :
        self.his['text'] = self.his['text'] + '('
        self.Situation['Oparenthesis'] = True
        if self.num[0] != '' :
            self.Situation['result']  = self.num[0]
            self.num[0] = ''
        if self.status['sum'] == True :
            self.Situation['parenthesis'] = 'sum'
        if self.status['difference'] == True :
            self.Situation['parenthesis'] = 'difference'
        if self.status['product'] == True :
            self.Situation['parenthesis'] = 'product'
        if self.status['quotient'] == True :
            self.Situation['parenthesis'] = 'quotient'
        self.status['sum'] = False
        self.status['difference'] = False
        self.status['product'] = False
        self.status['quotient'] = False
    def Cparenthesis(self) :
        if self.Situation['Oparenthesis'] == True :
            self.Situation['Cparenthesis'] = True
            if self.Situation['result'] != '' :
                if self.num[0] == '' :
                    self.his['text'] = self.his['text'] + self.res['text']
                    self.num[0] = self.Situation['result'] 
                    self.num[1] = self.res['text']
                    self.equality()      
                if self.num[0] != '' and self.num[1] == '' :
                    self.his['text'] = self.his['text'] + self.res['text']
                    self.num[1] = self.res['text']
                    self.equality()
                    self.num[1] = self.res['text']
                    self.num[0] = self.Situation['result']
                    if self.Situation['parenthesis']  == 'sum' :
                        self.status['sum'] = True
                    if self.Situation['parenthesis']  == 'difference' :
                        self.status['difference'] = True  
                    if self.Situation['parenthesis']  == 'product' :
                        self.status['product'] = True
                    if self.Situation['parenthesis']  == 'quotient' :
                        self.status['quotient'] = True  
                    self.equality()
            if self.Situation['result'] == '' :
                if self.num[0] == '' :
                    self.his['text'] = self.his['text'] + self.res['text']
                    self.num[0] = self.res['text']
                if self.num[0] != '' and self.num[1] == '' :
                    self.his['text'] = self.his['text'] + self.res['text']
                    self.num[1] = self.res['text']
                    self.equality()
            self.his['text'] = self.his['text'] + ')'
    def P(self) :
        self.res['text'] = 3.1415926535897932384626433832795  
    def Sin(self) :
        first_value = int(self.res['text'])
        value = math.sin(int(self.res['text']))
        self.his['text'] = self.his['text'] + 'sin(' + str(first_value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = value
    def Cos(self) :
        first_value = int(self.res['text'])
        value = math.cos(int(self.res['text']))
        self.his['text'] = self.his['text'] + 'cos(' + str(first_value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = value
    def Tan(self) :
        first_value = int(self.res['text'])
        value = math.tan(int(self.res['text']))
        self.his['text'] =self. his['text'] + 'tan(' + str(first_value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = value
    def Exponent(self) :
        if self.Situation['eq'] == True :
            self.his['text'] = str(self.his['text']) + str(self.res['text'])
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == False: 
            self.his['text'] = str(self.his['text']) + str(self.res['text']) + '^'
        elif self.res['text'] != '' and self.Situation['Cparenthesis'] == True: 
            self.his['text'] = str(self.his['text']) + '^'
            self.Situation['Cparenthesis'] = False
        if self.num[0] == '' :
            self.num[0] = self.res['text']
            self.res['text'] = ''
            self.status['exponent'] = True
        elif self.num[0] != '' and self.num[1] == '' :
            self.num[1] = self.res['text']
            self.res['text'] = ''
        if self.num[0] != '' and self.num[1] != '' :
            self.equality()
            self.num[0] = self.res['text']
            self.num[1] = ''
            self.Situation['st'] = True
        if self.num[0] == '' :
            self.status['exponent'] = True
        if self.num[1] == '' :
            self.status['exponent'] = True
    def Radical(self) :
        first_value = int(self.res['text'])
        rad = int(self.res['text']) ** 0.5
        self.his['text'] = self.his['text'] + '√(' + str(first_value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = rad
    def Factorial(self) :
        i = int(self.res['text'])
        j = i
        while i > 1 :
            j = j * (i-1)
            i = i-1
        self.res['text'] = str(j)
    def Exponent2(self) :
        first_value = int(self.res['text'])
        value = int(self.res['text']) ** 2
        self.his['text'] = self.his['text'] + 'sqr(' + str(first_value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = value
    def Radical3(self) :
        first_value = int(self.res['text'])
        rad = int(self.res['text']) ** (1/3)
        self.his['text'] = self.his['text'] + '∛(' + str(first_value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = rad
    def Logaritm(self) :
        value = math.log(int(self.res['text']))
        self.his['text'] = self.his['text'] + 'log(' + str(value) + ')'
        self.Situation['Cparenthesis'] = True
        self.res['text'] = value
    def x(self) :
        self.his['text'] = self.his['text'] + '1/' + self.res['text']
        self.res['text'] = 1 / int(self.res['text'])
    def Absolute(self) :
        value = int(self.res['text'])
        value = abs(value)
        self.res['text'] = value
    def e(self) :
        self.res['text'] = 2.7182818284590452353602874713527 
    def main (self):
        
        self.geometry('760x600+500+250')
        self.attributes('-alpha',0.99)        
        self.configure(bg = '#DEE2E6')

        self.result = LabelFrame(self , bg = '#DEE2E6',relief = 'flat')

        self.his = Label(self.result,bg = '#42A5F5',text = '',width = 100,height = 2,anchor ='w',font = ('tahoma',10))

        self.res = Label(self.result,bg = '#2196F3',text = '',width = 50,height = 3,anchor ='e',font = ('tahoma',19))

        self.keyss = LabelFrame(self,bg = '#DEE2E6',relief = 'flat')

        self.key1 = LabelFrame(self.keyss,bg = '#DEE2E6',relief = 'flat')

        self.key2 = LabelFrame(self.keyss,bg = '#DEE2E6',relief = 'flat')

        self.darsad = PhotoImage(file = 't.png')
        self.si = PhotoImage(file = 'C.png')
        self.sie = PhotoImage(file = 'CE.png')
        self.taqsim = PhotoImage(file = '÷.png')
        self.percent = Button(self,image = self.darsad ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Persent)
        self.c = Button(self,image =self.si,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.C)
        self.ce = Button(self,image = self.sie,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Ce)
        self.Division = Button(self,image = self.taqsim,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.quotient)


        self.haft = PhotoImage(file = '7.png')
        self.hasht = PhotoImage(file = '8.png')
        self.noh = PhotoImage(file = '9.png')
        self.zarb = PhotoImage(file = 'x.png')
        self.seven = Button(self,image = self.haft ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.seven7)
        self.eight = Button(self,image = self.hasht ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.eight8)
        self.nine = Button(self,image = self.noh,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.nine9)
        self.multiplication = Button(self,image = self.zarb ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.product)

        self.chahar = PhotoImage(file = '4.png')
        self.panj = PhotoImage(file = '5.png')
        self.shish = PhotoImage(file = '6.png')
        self.menha = PhotoImage(file = '-.png')
        self.four = Button(self,image = self.chahar ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.four4)
        self.five = Button(self,image = self.panj ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.five5)
        self.six = Button(self,image = self.shish ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.six6)
        self.minus  = Button(self,image = self.menha ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.difference)

        self.yek = PhotoImage(file = '1.png')
        self.do = PhotoImage(file = '2.png')
        self.se = PhotoImage(file = '3.png')
        self.jam = PhotoImage(file = '+.png')
        self.one = Button(self,image = self.yek,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.one1)
        self.two = Button(self,image = self.do,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.two2)
        self.three = Button(self,image = self.se,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.three3)
        self.plus = Button(self,image = self.jam,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.sum1)

        self.manfi = PhotoImage(file = 'manfi.png')
        self.sefr = PhotoImage(file = '0.png')
        self.noghte = PhotoImage(file = 'noghte.png')
        self.mosavi = PhotoImage(file = '=.png')
        self.negative = Button(self,image = self.manfi,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Negative)
        self.zero = Button(self,image =self.sefr ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.zero0)
        self.dot = Button(self,image = self.noghte,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.dot1)
        self.equal = Button(self,image = self.mosavi,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.equals)

        self.baz = PhotoImage(file = '(.png')
        self.baste = PhotoImage(file = ').png')
        self.pp = PhotoImage(file = 'p.png')
        self.oparenthesis = Button(self,image = self.baz ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Oparenthesis)
        self.cparenthesis = Button(self,image = self.baste ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Cparenthesis)
        self.p= Button(self,image = self.pp ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.P)

        self.sin2 = PhotoImage(file = 'sin.png')
        self.cos2 = PhotoImage(file = 'cos.png')
        self.tan2 = PhotoImage(file = 'tan.png')
        self.sin = Button(self,image = self.sin2 ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Sin)
        self.cos = Button(self,image = self.cos2 ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Cos)
        self.tan = Button(self,image = self.tan2 ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Tan)

        self.tavan = PhotoImage(file = 'tavan.png')
        self.radi = PhotoImage(file = '√.png')
        self.fac = PhotoImage(file = '!.png')
        self.exponent  = Button(self,image = self.tavan ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Exponent )
        self.radical = Button(self,image = self.radi ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Radical)
        self.factorial = Button(self,image = self.fac ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Factorial)

        self.xdo = PhotoImage(file = 'x2.png')
        self.radi3 = PhotoImage(file = '√3.png')
        self.log = PhotoImage(file = 'log.png')
        self.exponent2 = Button(self,image = self.xdo ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Exponent2)
        self.radical3 = Button(self,image = self.radi3 ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Radical3)
        self.logaritm = Button(self,image = self.log ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Logaritm)

        self.ghadr = PhotoImage(file = 'gh.png')
        self.besad = PhotoImage(file = 'besad.png')
        self.eee = PhotoImage(file = 'e.png')
        self.absolute= Button(self,image =  self.ghadr ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.Absolute)
        self.xx= Button(self,image = self.besad ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.x)
        self.ee= Button(self,image = self.eee ,relief = 'flat',activebackground = '#DEE2E6',bg = '#DEE2E6',command = self.e)

        self.result.grid(row = 1 , column = 1)
        self.his.grid(row = 1 , column = 1 , padx = 20)
        self.res.grid(row = 2 , column = 1 , padx = 20)

        self.keyss.grid(row = 2 , column = 1)
        self.key1.grid(row = 1 , column = 1 , pady = 30 , padx = 5)
        self.key2.grid(row = 1 , column = 2 , pady = 30 , padx = 5)

        self.percent.place(x = 35 , y = 181)
        self.c.place(x = 130 , y = 181)
        self.ce.place(x = 225 , y = 181)
        self.Division.place(x = 320 , y = 181)

        self.seven.place(x = 35 , y = 262)
        self.eight.place(x = 130, y = 262)
        self.nine.place(x = 225 , y = 262)
        self.multiplication.place(x = 320 , y = 262)

        self.four.place(x = 35 , y = 343)
        self.five.place(x = 130 , y = 343)
        self.six.place(x = 225 , y = 343)
        self.minus .place(x = 320 , y = 343)

        self.one.place(x = 35 , y = 424)
        self.two.place(x = 130 , y = 424)
        self.three.place(x = 225 , y = 424)
        self.plus.place(x = 320 , y = 424)

        self.negative.place(x = 35 , y = 505)
        self.zero.place(x = 130 , y = 505)
        self.dot.place(x = 225 , y = 505)
        self.equal.place(x = 320 , y = 505)

        self.oparenthesis.place(x = 439 , y = 181)
        self.cparenthesis.place(x = 534 , y = 181)
        self.p.place(x = 629 , y = 181)

        self.sin.place(x = 439 , y = 262)
        self.cos.place(x = 534 , y = 262)
        self.tan.place(x = 629 , y = 262)

        self.exponent.place(x = 439 , y = 343)
        self.radical.place(x = 534 , y = 343)
        self.factorial.place(x = 629 , y = 343)

        self.exponent2.place(x = 439 , y = 424)
        self.radical3.place(x = 534 , y = 424)
        self.logaritm.place(x = 629 , y = 424)

        self.absolute.place(x = 534 , y = 505)
        self.xx.place(x = 439 , y = 505)
        self.ee.place(x = 629 , y = 505)
        
        
o = GUI()
o.mainloop()
