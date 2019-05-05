import sys
import numpy as ny
import matplotlib.pyplot as plt
import math
import BinomialTree
import MonteCarlo

if __name__ == "__main__":
    #1.
    #a)
    T=4
    r=0.02
    h=0.25
    u=math.exp(r*h+0.2*math.sqrt(h))
    d=math.exp(r*h-0.2*math.sqrt(h))
    S0=100
    K=90
    p=(math.exp(r*h)-d)/(u-d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True,0,[])
    bt._setPrice_("Straddle")
    CallPrice = bt.root.C
    print CallPrice

    #b)
    T = 40
    r = 0.02
    h = 0.025
    u = math.exp(r * h + 0.2 * math.sqrt(h))
    d = math.exp(r * h - 0.2 * math.sqrt(h))
    S0 = 100
    K = 90
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True,0,[])
    bt._setPrice_("Straddle")
    CallPrice = bt.root.C
    print CallPrice

    #c)
    T = 4
    r = 0.02
    h = 0.25
    u = math.exp(r * h + 0.2 * math.sqrt(h))
    d = math.exp(r * h - 0.2 * math.sqrt(h))
    S0 = 100
    K = 90
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True,0,[])
    bt._setPrice_("Binary")
    CallPrice = bt.root.C
    print CallPrice

    #2.
    #a)
    T = 250
    r = 0.01
    h = 1.0/365.0
    u = math.exp(r * h + 0.15 * math.sqrt(h))
    d = math.exp(r * h - 0.15 * math.sqrt(h))
    S0 = 10
    K = 10
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True,0,[])
    bt._setPrice_("AmeriCall")
    CallPrice = bt.root.C
    print CallPrice

    #b)
    T = 250
    r = 0.01
    h = 1.0 / 365.0
    u = math.exp(r * h + 0.15 * math.sqrt(h))
    d = math.exp(r * h - 0.15 * math.sqrt(h))
    S0 = 10
    K = 10
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True,0,[])
    bt._setPrice_("AmeriPut")
    CallPrice = bt.root.C
    print CallPrice

    #3.
    #a)
    T = 200
    r = 0.02
    h = 1.0 / 365.0
    u = math.exp(0.2 * math.sqrt(h))
    d = 1.0/u
    S0 = 10
    K = 10
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True, 0.05, [50,100,150])
    bt._setPrice_("AmeriCall")
    CallPrice = bt.root.C
    print CallPrice

    #b)
    T = 200
    r = 0.02
    h = 1.0 / 365.0
    u = math.exp(0.2 * math.sqrt(h))
    d = 1.0 / u
    S0 = 10
    K = 10
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True, 0.05, [50,100,150])
    bt._setPrice_("AmeriPut")
    CallPrice = bt.root.C
    print CallPrice

    #b)
    T = 200
    r = 0.02
    h = 1.0 / 365.0
    u = math.exp(0.2 * math.sqrt(h))
    d = 1.0 / u
    S0 = 10
    K = 10
    p = (math.exp(r * h) - d) / (u - d)
    bt = BinomialTree.BinomialTree(u, d, p, r, h, K, S0, T, True, 0.05, [50, 100, 150])
    bt._setPrice_("Straddle")
    CallPrice = bt.root.C
    print CallPrice

    #4.
    #a)
    T=1.0
    N=365
    K=220.0
    sigma = 0.2
    r=0.02
    S0=200
    paths = 100000
    mc = MonteCarlo.MonteCarlo()
    CallPrice = mc.AsianOptionPricingByMonteCarlo(S0=S0,r=r,sigma=sigma,T=T,N=N,paths=paths,K=K)
    print CallPrice

    #5.
    #a)
    T=1.0
    N=5
    K=220.0
    sigma = 0.2
    r=0.02
    S0=200
    paths = 100000
    mc = MonteCarlo.MonteCarlo()
    CallPrice = mc.AmericanPutOptionPricingByLSMC(S0=S0,r=r,sigma=sigma,T=T,N=N,paths=paths,K=K)
    print CallPrice

    #b)
    T = 1.0
    N = 250
    K = 220.0
    sigma = 0.2
    r = 0.02
    S0 = 200
    paths = [10,100,1000,10000]
    prices = []
    for p in paths:
        mc = MonteCarlo.MonteCarlo()
        Price = mc.AmericanPutOptionPricingByLSMC(S0=S0, r=r, sigma=sigma, T=T, N=N, paths=p, K=K)
        prices.append(Price)
        print Price
    prices.append(CallPrice)
    plt.figure()
    plt.plot([1,2,3,4,5],prices)

    #c)
    T = 1.0
    N = [3,10,100,250,1000]
    K = 220.0
    sigma = 0.2
    r = 0.02
    S0 = 200
    paths = 100000
    prices = []
    for n in N:
        mc = MonteCarlo.MonteCarlo()
        Price = mc.AmericanPutOptionPricingByLSMC(S0=S0, r=r, sigma=sigma, T=T, N=n, paths=paths, K=K)
        prices.append(Price)
        print Price
    plt.figure()
    plt.plot([1, 2, 3, 4, 5], prices)







