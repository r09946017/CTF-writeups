from Crypto.Util.number import *

class Complex:
    baseRe = 1
    baseIm = 0
    p = 8494638672381712426688477470653430477269594977016930662854015708761990399918086769491700011694720852848575947599954053177997043739645079780483579065896793
    q = 7580404339410605275626408632293985390119410811758716323067754026905773097627216054700243523685903084284434158078654472410013702925363551739091210471600391

    n  = p*q
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
        
    def Christmas_gift(self):
        mistletoe =   getPrime(400)
        
        phi = (Complex.p*Complex.q)**2+Complex.p*Complex.q+1+(Complex.p*Complex.q+1)*(Complex.p+Complex.q)+(Complex.p**2+Complex.q**2)
        Querce = inverse(mistletoe,phi)
        return Querce


    def OnePlus(self):
        _re = (self.re*Complex.baseRe - self.im*Complex.baseIm)%Complex.n
        _im = (self.re*Complex.baseIm + self.im*Complex.baseRe)%Complex.n
        Complex.baseRe = _re
        Complex.baseIm = _im
        
    def Double(self):
        _re  = (self.re*self.re - self.im*self.im)%Complex.n
        _im  = (self.re*self.im + self.im*self.re)%Complex.n
        self.re = _re
        self.im = _im

    def val(self):
        return Complex.baseRe,Complex.baseIm
