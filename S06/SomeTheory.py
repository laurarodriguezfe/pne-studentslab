class ClassName:
    #Constructor (__int__) method to initialize attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1 #Define instance attributes
        self.attribute2 = attribute2 #Define instance attributes
    #Method to define actions or behaviors
    def method_name(self, parameter):
        #Perform operations on attributes or other tasks
        pass

class Seq:
    """A class for representing sequences"""
    def __init__(self):
        #It's not good practice to print here, but let's make an exception!
        print("new Sequence created!")
# Main program
# Create an object of the class Seq
s1 = Seq()
s2 = Seq()
print("Testing...")

class ParentClass:
    #Parent class code here
    pass
class ChildClass(ParentClass):
    #Child class code here
    pass

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):
        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")
# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")

