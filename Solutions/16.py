class Exercise16Handler():
    def __init__(self,inpStr):
        self.inpStr = inpStr
    
    def oddFind(self):
        #List comprehension is basically containing everything like so, instead of defining this in a whole for loop.
        self.oddArr = [n for n in self.inpStr.split(",") if int(n)%2 != 0]

        print(",".join(self.oddArr))
    
def main():
    inpVal = input(">")
    handler = Exercise16Handler(inpVal)
    handler.oddFind()

if __name__ == "__main__":
    main()