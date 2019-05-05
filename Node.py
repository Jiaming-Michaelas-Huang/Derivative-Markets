import math
class Node:
    def __init__(self, S, level):
        self.S = S
        self.C = None
        self.level = level
        self.up = None
        self.down = None
    def _setup_(self, u, div, divdate):
        if self.level in divdate:
            self.up = Node(S=self.S * u*(1-div), level=self.level + 1)
        else:
            self.up = Node(S=self.S * u, level=self.level + 1)
    def _setdown_(self, d, div, divdate):
        if self.level in divdate:
            self.down = Node(S=self.S * d*(1-div), level=self.level + 1)
        else:
            self.down = Node(S=self.S * d, level=self.level + 1)
    def _setrecombinationup_(self, up):
        self.up = up
    def _setrecombinationdown_(self,down):
        self.down = down
    def _setEuroCallPrice_(self,K,p,r,delta):
        if(self.up == None and self.down == None):
            self.C = max(self.S-K,0)
        else:
            if self.up.C == None:self.up._setEuroCallPrice_(K,p,r,delta)
            if self.down.C == None:self.down._setEuroCallPrice_(K,p,r,delta)
            self.C = math.exp(-r*delta)*(p*self.up.C+(1-p)*self.down.C)

    def _setAmeriCallPrice_(self,K,p,r,delta):
        if (self.up == None and self.down == None):
            self.C = max(self.S - K, 0)
        else:
            if self.up.C == None:self.up._setAmeriCallPrice_(K, p, r, delta)
            if self.down.C == None:self.down._setAmeriCallPrice_(K, p, r, delta)
            self.C = max(math.exp(-r * delta) * (p * self.up.C + (1 - p) * self.down.C),self.S-K)

    def _setEuroPutPrice_(self, K, p, r, delta):
        if (self.up == None and self.down == None):
            self.C = max(-self.S + K, 0)
        else:
            if self.up.C == None:self.up._setEuroPutPrice_(K, p, r, delta)
            if self.down.C == None:self.down._setEuroPutPrice_(K, p, r, delta)
            self.C = math.exp(-r * delta) * (p * self.up.C + (1 - p) * self.down.C)

    def _setAmeriPutPrice_(self, K, p, r, delta):
        if (self.up == None and self.down == None):
            self.C = max(-self.S + K, 0)
        else:
            if self.up.C == None:self.up._setAmeriPutPrice_(K, p, r, delta)
            if self.down.C == None:self.down._setAmeriPutPrice_(K, p, r, delta)
            self.C = max(math.exp(-r * delta) * (p * self.up.C + (1 - p) * self.down.C), -self.S + K)

    def _setStraddlePrice_(self, K, p, r, delta):
        if (self.up == None and self.down == None):
            self.C = max(self.S - K, 0)+max(K-self.S,0)
        else:
            if self.up.C == None:self.up._setStraddlePrice_(K, p, r, delta)
            if self.down.C == None:self.down._setStraddlePrice_(K, p, r, delta)
            self.C = math.exp(-r * delta) * (p * self.up.C + (1 - p) * self.down.C)
    def _setBinaryPrice_(self, K, p, r, delta):
        if (self.up == None and self.down == None):
            self.C = max(self.S - K, 0)/(self.S-K)
        else:
            if self.up.C == None:self.up._setBinaryPrice_(K, p, r, delta)
            if self.down.C == None:self.down._setBinaryPrice_(K, p, r, delta)
            self.C = math.exp(-r * delta) * (p * self.up.C + (1 - p) * self.down.C)





