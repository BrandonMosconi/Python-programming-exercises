#We can use re.search to find things in strings.
import re

class Exercise18Handler():
    def __init__(self,inpStr):
        self.inpStr = inpStr
    
    def passCheck(self):
        self.passAccept = []

        for x in self.inpStr.split(","):
            if len(x) > 5 and len(x) < 13:
                if not re.search("[a-z]",x):
                    continue #Recall continue moves onto the next iteration, while pass just moves onto the next line of code.
                elif not re.search("[0-9]",x):
                    continue
                elif not re.search("[A-Z]",x):
                    continue
                elif not re.search("[S#@]",x):
                    continue
                else:
                    pass
                self.passAccept.append(x)
        
        print(",".join(self.passAccept))

def main():
    inpVal = input("> ")
    Exercise18Handler(inpVal).passCheck()

if __name__ == "__main__":
    main()
    