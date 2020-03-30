from math import sqrt

class Exercise21Handler():
    def __init__(self):
        pass
    
    #Could also simply use .split(" ") to find this. This just manually does so.
    def spaceCheck(self,inpStr):
        self.area = 0

        for n in range(0,len(inpStr)):
            if inpStr[n] == " ":
                return n+1
        
        return None

    def robotMove(self):
        self.coords = [0,0]

        while True:
            self.inp = input("> ")
            self.n = Exercise21Handler().spaceCheck(self.inp)

            if not self.inp:
                break
            elif self.inp[0].lower() == "l":
                self.coords[0] -= int(self.inp[self.n:])
            elif self.inp[0].lower() == "r":
                self.coords[0] += int(self.inp[self.n:])
            elif self.inp[0].lower() == "u":
                self.coords[1] += int(self.inp[self.n:])
            elif self.inp[0].lower() == "d":
                self.coords[1] -= int(self.inp[self.n:])
        
        print(sqrt(self.coords[0]**2 + self.coords[1]**2))
    
    
        
def main():
    Exercise21Handler().robotMove()

if __name__ == "__main__":
    main()