# -*- coding: UTF-8 -*-
import unittest
import math
def method_liuliang(e1,e2,d1,d2,h,c1,l1,l2,niu):
    lamida1_0=0.02
    lamida2_0=0.02
    lamida1=0.0
    lamida2=0.0
    c2=l1/d1*(d2/d1)**4
    c3=l2/d2
    while abs(lamida1_0-lamida1)/lamida1_0>=0.02 or abs(lamida2_0-lamida2)/lamida2_0>=0.02:#确定精度等级.
        v2=2*9.8*h/(c1+c2*lamida1_0+c3*lamida2_0)
        v1=(d2/d1)**2*v2
        lamida1=lamida1_0
        lamida2=lamida2_0
        lamida1_0=lamida(v1*d1/niu, e1/d1)
        lamida2_0=lamida(v2*d2/niu, e2/d2)
    return v2*3.14*d2**2/4 

def lamida(Re,e):#雷诺数 相对粗糙度e/d 
    if Re<=2000:
        return (64/Re)
    elif Re<=4000:
        return False
    elif Re<=22.2*(1/e)**(8/7):
        return (0.3164/Re**0.25)
    elif Re<=597*(1/e)**(9/8):
        return (0.0055*(1+(20000*e+1e6/Re)**(1/3)))
    else:
        return (1.14+2*math.log(1/e))**(-2)
    
class Test(unittest.TestCase): 
    def testha(self):
        self.assertAlmostEquals(method_liuliang(0.2e-3, 0.2e-3, 200e-3, 100e-3, 5, (0.5*(0.5)**4+4.42), 10, 20, 1.3e-6),0.15,places=1)
    def testl(self):
        self.assertAlmostEquals(method_liuliang(0.2e-3, 0.2e-3, 200e-3, 100e-3, 8, (0.5*(0.5)**4+4.42), 5, 10, 1.3e-6),0.24,places=2)
    def testd(self):
        self.assertAlmostEquals(method_liuliang(0.2e-3, 0.2e-3, 100e-3, 50e-3, 8, (0.5*(0.5)**4+4.42), 10, 20, 1.3e-6),0.04,places=2)
if __name__ == '__main__':
    unittest.main()(defaultTest = 'suite')
        