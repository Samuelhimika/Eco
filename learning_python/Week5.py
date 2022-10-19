#
# Object  properties / attributes      Behavior/methods
# # APIE Abstraction, encapsulation, inheritance and polymorphism
# Superclass and lower class

class Person:
    #class variable

    # firstname = 'paul'
    # lastname = 'derick'


#Instance variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


person1 = Person('John', 'Joe')
print(person1.lastname)
print(person1.firstname)