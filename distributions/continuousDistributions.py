import math

class continuousDistr:

   

    def uniform(self, a, b):
        self.b = float(b)
        self.a = float(a)

        uniform_result = float((1 / (self.b - self.a)))
        uniform_mean = float((self.a + self.b) / 2 )
        uniform_var = float(((self.b - self.a) ** 2) / 12)
        
        return print(f'Uniform Distribution is: {uniform_result} \nUniform Distribution mean is : {uniform_mean} \nUniform Distribution variance is : {uniform_var}\n')



    def exponentially(self, lambd, x):
        self.lambd = float(lambd)
        self.x = float(x)

        exp_result = (self.lambd * math.e) ** (- self.lambd * self.x)
        exp_mean = 1 / self.lambd
        exp_var = 1 / (self.lambd ** 2)

        return print(f'Exponentially Distribution result is:{exp_result} \nExponentially Distribution mean is : {exp_mean} \nExponentially Distribution variance is : {exp_var}')




if __name__=='__main__':
    c = continuousDistr()
    c.uniform(2,10)
    c.exponentially(2,3)

