'''
Created on Mar 27, 2011

@author: saad
'''

class LinkedList():
    class LinkedListElement():
        __value = None
        __prev = None
        __next = None
        
        def __init__(self,value):
            self.__value = value
        
        def setNext(self,next):
            self.__next = next
        
        def setPrev(self,prev):
            self.__prev = prev
        
        def getNext(self):
            return self.__next;
        
        def getPrev(self):
            return self.__prev;
        
        def setValue(self,value):
            old = self.__value
            self.__value = value
            return old;
        
        def getValue(self):
            return self.__value;
        
        def attachAfter(self,element):
            element.setNext(self.__next)
            element.setPrev(self)
            self.__next.setPrev(element)
            self.__next = element
            
            
        def attachBefore(self,element):
            element.setNext(self)
            element.setPrev(self.__prev)
            self.__prev.setNext(element)
            self.__prev = element
            
        def delete(self,element):
            self.__prev.setNext(self.__next)
            self.__next.setPrev(self.__prev)
            self.setNext(None)
            self.setPrev(None)
            return self
        def detach(self):
            self.__prev.setNext(self.__next)
            self.__next.setPrev(self.__prev)
            self.setPrev(None)
            self.setNext(None)
            return self
        
        
    __size = None
    __HeadAndTail = LinkedListElement(None)
    def __init__(self):
        self.clear()
        print ">>> LinkedList Created"
    
    def insert(self,index,value):
        assert value != None , "VALUE CANNOT BE EMPTY"
        if (index < 0) or (index > self.__size):
            raise IndexError("Bad Index")
            return
        element = self.getElement(index)
        element.attachBefore(self.LinkedListElement(value))
        self.__size += 1
    
    def getElement(self,index):
        element = self.__HeadAndTail.getNext()
        if (index < 0) or (index > self.__size):
            raise IndexError
            return
        for i in range(0,index):
            element = element.getNext()
        return element
    
    def attach(self,value):
        self.__HeadAndTail.attachBefore(self.LinkedListElement(value))
        self.__size += 1
    
    def delete(self,index):
        if(index < 0) | (index > self.__size):
            raise IndexError
        self.__size -=1
        return self.getElement(index).detach().getValue();
    
    def clear(self):
        self.__HeadAndTail.setNext(self.__HeadAndTail)
        self.__HeadAndTail.setPrev(self.__HeadAndTail)
        self.__size = 0
    def set(self,index,value):
        return self.getElement(index).setValue(value)
    
    def get(self,index):
        return self.getElement(index).getValue();
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
