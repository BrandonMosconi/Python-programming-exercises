class Exercise8Handler():
    def __init__(self,strInp):
        self.strInp = strInp
    
    def strSort(self):
        self.strArr = sorted(self.strInp.split(","))
        print(','.join(self.strArr))


def main():
    handler = Exercise8Handler("without,hello,bag,world")
    handler.strSort()

if __name__ == "__main__":
    main()