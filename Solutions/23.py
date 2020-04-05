def squareNumber(inpInt):
    print(inpInt**2)

def builtinDocs():
    #Each built-in function has its respective document, which can be drawn out using "__doc__"
    print(abs.__doc__)


if __name__ == "__main__":
    builtinDocs()
    inp = int(input("> "))
    squareNumber(inp)

"""Classes Explanation"""

class Person:
    # Define the class parameter "name"
    name = "Person" #When you call Person() with a parameter, 'name' permenantly stores this for every call.
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print "%s name is %s" % (Person.name, jeffrey.name)