class Math:
    initial_amount = 4
    @staticmethod
    def add(*args): # no need for self
        total = 0
        for num in args:
            total += int(num)
        return total
    @staticmethod  # no need for self
    def subtract(*args):
        total = 0
        for num in args:
            total -= int(num)
        return total

    @classmethod  # exist on the class, no the instance
    def multiply(cls,*args):
        for num in args:
            cls.initial_amount *= num
        return cls.initial_amount  
    
    @property # uses a class like a property (no parentathis needed)
    def power(self):
        return Math.initial_amount ** 4

b = Math()
print(b.power)


a = Math()
a.initial_amount = 5 # not used

print(a.add(1,2,3,4))
print(a.subtract(1,2,3,4))

# takes the class attributes initial amount
print(Math.multiply(1,2,3,4)) # 4 * 1 * 2 * 3 * 4 = 96
print(a.multiply(1,2,3,4)) # 96 * 1 * 2 * 3 * 4 = 2304

