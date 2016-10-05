# Name: Nate McCain
# Date: 10/06/2014
# Class: CS 142
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: The PersonList class represents a node in a linked list of people.
# The Line class represents a line of people as a linked list. The two classes
# allow the user to add a person to the END of the line, remove a specific person,
# and add a person behind a person currently in line.

# Represents a node in a linked list of people.
class PersonList(object):
    
# Two private variables: the first represent's the person's name, the second
# is a link to the person behind the first.
    def __init__(self, name):
        self.__name = name
        self.__next = None
        
# Returns the name of the person.
    def getName(self):
        return self.__name
    
# Returns a PersonList object with the next person in line.   
    def getNext(self):
        return self.__next
    
# Sets the name of a person.   
    def setName(self, newname):
        self.__name = newname
        
# Sets the next person in line.       
    def setNext(self, newnext):
        self.__next = newnext


# Represents a line of people as a linked list.
class Line(object):
    
# Initializes the private variable that points to the first person in the line.
    def __init__(self):
        self.__head = None
        
# If the object is empty, it will return None.
    def isEmpty(self):
        return self.__head == None
    
# Searches for the input name, returns false if not in list, returns    
    def search(self,name):
        current = self.__head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getName() == name:
                found = True
            else:
                if current.getName() == name:
                    stop = True
                else:
                    current = current.getNext()
        return found

#Adds a person to the END of the linked list.
    def add(self,name):
        current = self.__head
        previous = None
        if name == '':
            print("Error, you did not enter a name for the person to add." + "\n")
        else:
            while current != None:
                previous = current
                current = current.getNext()
            temp = PersonList(name)
            if previous == None:
                temp.setNext(self.__head)
                self.__head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)
                
#Removes a person from the linked list. If the person is not in the line, returns an error message.      
    def remove(self,name):
        current = self.__head
        previous = None
        found = False
        if self.search(name) == False:
            print("Error, person not found. " + "\n")
        else:
            while not found:
                if current.getName() == name:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.__head = current.getNext()
            else:
                previous.setNext(current.getNext())
                
#Allows for the second person to get in line behind the first person. If the first
# person is not in the line, it returns an error message.
    def joinFriend(self, first, second):
        current = self.__head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getName() == first:
                previous = current
                current = current.getNext()
                stop = True
            else:
                previous = current
                current = current.getNext()
        if current == None and stop == False:
            return print("The person referenced is not in line." + "\n")
        else:
            temp = PersonList(second)
            if previous == None:
                temp.setNext(self.head)
                self.__head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)
        
#Overloads str method to print out nicely formatted output. This is how we know
# who is in line, and what the order of the line is.
    def __str__(self):
        current = self.__head
        string = ''
        count = 0
        while current != None:
            count = count + 1 
            string += str(count) + " " + current.getName() + "\n"
            current = current.getNext()
        return string
