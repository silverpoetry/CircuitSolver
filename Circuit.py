from math import *
def  ModAngToComplex(mod,angle):
    #模长角度转为复数
    return complex(mod*cos(angle/180*pi),mod*sin(angle/180*pi))
class ees(object):
        def __init__(self,a):
            self.complex = a +0j
        def __str__(self):
            if self.complex.imag==0 and self.complex.real==0 :
                return  "0"
            elif self.complex.imag== 0:
                return format(self.complex.real,".3f")
            elif self.complex.real== 0:
                return format(self.complex.imag,".3f")+"j"
            elif  self.complex.imag<0:
                return "{}{}j".format(format(self.complex.real,".3f"),format(self.complex.imag,".3f"))
            else:
                return "{}+{}j".format(format(self.complex.real,".3f"),format(self.complex.imag,".3f"))
        
        def __eq__(self,a):
            self.complex =a 
        def chuan(self,b):
            if type(b) is not ees:
                b= ees(b)
            return ees(self.complex+b.complex)
        def bing(self,b):
            if type(b) is not ees:
                b=ees(b)
            return  ees((self.complex*b.complex)/(self.complex+b.complex))
        def toModAng(self):
            #以模长角度形式输出
            c =self.complex
            mod =sqrt(c.real**2+c.imag**2)
            angle= atan2(c.imag,c.real)/pi*180
            return format(mod,".3f")  +  "∠"+format(angle,".3f") +'°'
        @property  
        def mod(self):
            c =self.complex
            return sqrt(c.real**2+c.imag**2) 
        @property 
        def angle(self):
            c =self.complex
            return  atan2(c.imag,c.real)/pi*180
            
               
                


            

                

        
        
            
