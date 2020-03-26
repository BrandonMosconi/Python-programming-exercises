"""itemgetter simply, as it suggests, fetches the object at the provided index of the provided array/
tuple/etc. Combining this with sorted gets the object at each tuple/array/etc. and sorts them. Providing 
several different indexes constructs a hierarchy of sorting levels, so if two entries are equal, it moves
onto the next comparision."""
from operator import itemgetter, attrgetter

class Exercise19Handler():
    def __init__(self):
        pass

    def tupleSort(self):
        self.tuples = []
        
        while True:
            self.s = input("> ")
            if not self.s:
                break
            else:
                self.tuples.append(tuple(self.s.split(",")))
            
        print(sorted(self.tuples,key = itemgetter(0,1,2)))

def main():
    Exercise19Handler().tupleSort()

if __name__ == "__main__":
    main()