class Exercise2Handler():
    def __init__(self,strInp):
        self.strInp = strInp

    def commaSplitter(self):
        self.inpSplit = self.strInp.split(",")
        #Use this to turn a list into a tuple
        self.splitTuple = tuple(self.inpSplit)

        print(self.inpSplit)
        print(self.splitTuple)

def main():
    handler = Exercise2Handler("2,3,4,56,7,5")
    handler.commaSplitter()

if __name__ == "__main__":
    main()