#
# Example file for working with classes
# python classes_start.py
#

class myClass():
    def method1(self):
        print("myClass method1")
        
    def method2(self, someString):
        print("myClass method2" + someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
        
    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2(" This is a string")
    
    # call another class
    c2 = anotherClass()
    c2.method1()
    # even though we are adding a argument, the argument is not being used
    c2.method2("This is a string")
    # method2 overrides 

if __name__ == "__main__":
  main()
