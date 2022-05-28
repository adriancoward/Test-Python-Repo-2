print("Test message from another Python code in a new repository")
print("and another message")
print("this line was added after creating Test Branch 1")
print("this line added after merging back Test Branch 1")

class test_class:
    def __init__(self,prop1,prop2):
        self.prop1=prop1
        self.prop2=prop2

#create an instance of the test_class
test_class1=test_class(1,2)

print(test_class1.prop2)