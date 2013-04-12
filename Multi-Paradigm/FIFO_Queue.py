'''
Created on Mar 27, 2011
a FIFO Queue (First In First Out) which is based on the indexed
double direction LinkedList
@author: saad
'''
from com.structures.LinkedList import LinkedList
from com.exceptions.EmptyQueueException import EmptyQueueException

class FIFOQueue():
    List = None
    def __init__(self):
        self.List = LinkedList()
    def enqueue(self,value):
        self.List.attach(value)
    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException
        return self.List.delete(0)
    def clear(self):
        self.List = LinkedList()
    def isEmpty(self):
        return self.List.isEmpty()
    def size(self):
        return self.List.size()


#from threading import Thread
#
#def method():
#    print "A";
#
#def method2():
#    print "B";        
#h=Thread(None, method);
#j = Thread(None,method2);
#j.start()
#h.start()
#h.join(5000)
#j.join(5000)