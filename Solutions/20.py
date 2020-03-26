class Exercise20Handler():
    def __init__(self):
        pass

    def divSeven(self):
        self.n = int(input("> "))
        self.generator = (x for x in range(0,self.n+1) if x%7 == 0)

        for i in self.generator:
            yield i 


def main():
    divGen = Exercise20Handler().divSeven()
    
    for i in divGen:
        print(i)

if __name__ == "__main__":
    main()

"""For more info on generators and yield, see:

https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
"""