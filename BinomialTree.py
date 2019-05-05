import Node
import math

class BinomialTree:
    def __init__(self, u, d, p, r, delta, K, S0, N, recommbination,div,div_time):
        self.u = u
        self.d = d
        self.p = p
        self.r = r
        self.delta = delta
        self.K = K
        self.S0 = S0
        self.N = N
        self.root = Node.Node(S0,0)
        temp = []
        temp.append(self.root)
        i = N
        if not recommbination:
            while i > 0:
                temp1 = []
                for n in temp:
                    n._setup_(u,div=div,divdate=div_time)
                    n._setdown_(d,div=div,divdate=div_time)
                    temp1.append(n.up)
                    temp1.append(n.down)
                temp = temp1
                i = i-1
        else:
            while i > 0:
                temp1 = []
                j = 1
                prv_n = None
                for n in temp:
                    if j == 1:
                        n._setup_(u,div=div,divdate=div_time)
                        temp1.append(n.up)
                    else:
                        n._setrecombinationup_(prv_n.down)
                    n._setdown_(d,div=div,divdate=div_time)
                    temp1.append(n.down)
                    j = j + 1
                    prv_n = n
                temp = temp1
                i = i - 1
    def _setPrice_(self, type):
        if type == "EuroCall":
            self.root._setEuroCallPrice_(self.K,self.p,self.r,self.delta)
        if type == "AmeriCall":
            self.root._setAmeriCallPrice_(self.K, self.p, self.r, self.delta)
        if type == "EuroPut":
            self.root._setEuroPutPrice_(self.K,self.p,self.r,self.delta)
        if type == "AmeriPut":
            self.root._setAmeriPutPrice_(self.K,self.p,self.r,self.delta)
        if type == "Straddle":
            self.root._setStraddlePrice_(self.K,self.p,self.r,self.delta)
        if type == "Binary":
            self.root._setBinaryPrice_(self.K,self.p,self.r,self.delta)









