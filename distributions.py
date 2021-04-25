import math

class discreteDistr:


    def binomial(self, p, n, x):
        self.p = float(p)
        self.n = int(n)
        self.x = int(x)
        if self.n < self.x:
            return print("Value of x can not be greater than n")
        else:
            binom_result = float((self.p ** self.x) * ( ( 1-self.p ) ** (self.n - self.x)))
            return print("Binomial Distribution result is :", binom_result )

    def bernoulli(self, p, x):
        self.p = float(p)
        self.x = int(x)
        berno_result = float( (self.p ** self.x) * ( (1-self.p) **(1-self.x)))
        return print("Bernoulli Distribution result is :", berno_result)

    def geometric(self, p, x):
        self.p = p
        self.x = x
        geo_result = float( self.p * ((1-self.p) ** (self.x-1)))
        return print("Geometric Distribution result is :", geo_result)

    def poisson(self, lambd, x):
        self.lambd = lambd
        self.x = x

        factorial = 1
        if int(x) >= 1:
            for i in range(1, int(x) + 1):
                factorial = factorial * i

        poisson_result = float( (self.lambd ** self.x) * (math.e ** - self.lambd) / factorial )
        return print("Poisson Distribution result is : ", poisson_result)



if __name__ == '__main__':
    d = discreteDistr()
    d.binomial(0.7, 7, 5)
    d.bernoulli(0.5,5)
    d.geometric(0.5,5)
    d.poisson(8, 10)