import numpy as ny
import math

def Monomial(x,n):
    if n == 0:
        x = (x+1)/(x+1)
        return x
    else:
        return x*Monomial(x,n-1)

class MonteCarlo:
    def MonteCarloSimulation(self,S0,r,sigma,T,N,paths):
        bm = sigma*math.sqrt(T/N)*ny.random.randn(paths,N)+(r-sigma*sigma/2)*T/N
        bm = bm.cumsum(1)
        bm = S0*ny.exp(bm)
        return bm
    def AsianOptionPricingByMonteCarlo(self,S0,r,sigma,T,N,paths,K):
        bm = self.MonteCarloSimulation(S0=S0,r=r,sigma=sigma,T=T,N=N,paths=paths)
        payoff = ny.mean(bm,axis=1)
        payoff = payoff-K
        PV = math.exp(-r*T)*payoff
        su = 0
        for pv in PV:
            if pv > 0:
                su = su + pv
        Price = su/len(PV)
        return Price
    def AmericanPutOptionPricingByLSMC(self,S0,r,sigma,T,N,paths,K):
        S = self.MonteCarloSimulation(S0=S0,r=r,sigma=sigma,T=T,N=N,paths=paths)
        index = ny.zeros((paths,N))
        EVs = ny.where(K-S>0,K-S,0)
        time = N-1
        while time>=0:
            EV = EVs[:,time]
            if time == N-1:
                ECV = ny.zeros((paths,1))
                index[:,time] = ny.where(EV>0,1.0,0.0)
            else:
                ECV = self.LeastSquared(S=S[:,time:N],index=index[:,time+1:N],type=0,k=4,r=r,T=T,N=N)
                index[:,time] = ny.where(EV>=ECV,1.0,0.0)
            time = time - 1
        V0 = 0.0

        for i in range(0,paths):
            maxi = 0
            for j in range(0,N):
                if maxi >0 :
                    index[i,j] = 0
                if index[i,j]>0:
                    maxi = maxi+1

        for i in range(0,N):
            for j in range(0,paths):
                if(index[j,i]!=0):
                    print math.exp(-r*i*T/N)
                    print EVs[j,i]
                V0 = V0+index[j,i]*math.exp(-r*i*T/N)*EVs[j,i]
        V0 = V0/paths
        return V0






    def LeastSquared(self,S,index,type,k,r,T,N):
        X = S[:,0]
        Y = S[:,1:]
        Y = Y*index
        for c in range(0,Y.shape[1]):
            Y[:,c] = Y[:,c]*math.exp(-r*c*T/N)
        Y=ny.sum(Y,axis=1)
        A=ny.zeros((4,4))
        b=ny.zeros((4,1))
        for i in range(0,4):
            for j in range(0,4):
                A[i,j] = sum(Monomial(X,i)*Monomial(X,j))
            b[i,0] = sum(Y*Monomial(X,i))
        print A
        A = ny.mat(A)
        b = ny.mat(b)
        a = A.I.dot(b)
        a = a.tolist()
        Ye = a[0]*Monomial(X,0)+a[1]*Monomial(X,1)+a[2]*Monomial(X,2)+a[3]*Monomial(X,3)
        return Ye





