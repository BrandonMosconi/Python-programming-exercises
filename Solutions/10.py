class Exercise8Handler():
    def __init__(self,strInp):
        self.strInp = strInp

    def setSort(self):
        self.strArr = sorted(set(self.strInp.split(" ")))

        print(" ".join(self.strArr))

def main():
    handler = Exercise8Handler("hello world and practice makes perfect and hello world again")
    handler.setSort()

if __name__ == "__main__":
    main()
