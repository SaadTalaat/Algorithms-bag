from Queue import *
import __future__
class BST():
    root = None
    class Node():
        __right = None
        __left = None
        __key = None
        __value = None
        def getKey(self):
            return self.__key
        def setKey(self, key):
            self.__key = key
        def getValue(self):
            return self.__value
        def setValue(self, value):
            self.__value = value
        def getRight(self):
            return self.__right
        def setRight(self, node):
            assert node
            self.__right = node
        def getLeft(self):
            return self.__left
        def setLeft(self, node):
            assert node
        def __init__(self, key, value):
            self.__key = key
            self.__value = value
    def Put(self, key, value):
        self.root = self.__put(self.root, key, value)
    def __put(self, parent, key, value):
        if(parent == None):
                parent = self.Node(key, value)
        if( parent.getKey() > key):
                parent.setLeft(self.__put(parent.getLeft(), key, value))
        elif( parent.getKey() < key):
                parent.setRight(self.__put(parent.getRight(), key, value))
        else:
            parent.setValue(value)
        return parent
            
    def Get(self, key, value):
        return self.__get(self.root, key, value)
    def __get(self, parent, key, value):
        if(parent == None):
            return None
        if( parent.getKey() < key):
            self.__get(parent.getRight(), key)
        elif(parent.getKey() > key):
            self.__get(parent.getLeft(), key);
        else:
            return parent.getValue()
             
    def Inorder(self):
        l = []
        self.__inorder(self.root, l)
        return l
        
    def __inorder(self, parent, l):
        if(parent == None):
               return
        self.__inorder(parent.getLeft(), l)
        l.append(parent.getKey())
        self.__inorder(parent.getRight(), l)
        return
        
    def Preorder(self):
        l = []
        self.__preorder(self.root, l)
        return l
    def __preorder(self, parent, l):
       if(parent == None):
           return
       l.append(parent.getKey())
       self.__preorder(parent.getLeft())
       self.__preorder(parent.getRight())
       return
    def Levelorder(self):
       l = []
       self.__levelorder(self.root, l)
       return l
       
    def __levelorder(self,parent, l):
       assert parent
       q = Queue()
       q.put(parent)
       while( not q.empty()):
           p = q.get()
           l.append(p.getKey())
           if p.getLeft() != None:
               q.put(p.getLeft())
           if p.getRight() != None:
               q.put(p.getRight())
    def printx(self):
        level = 1
        cur = 0
        l = self.Levelorder()
        w = len(l)
        for i in range(0,len(l)):
            print l[i],
            cur+=1
            if(cur == level):
		print ""
                level*=2
                cur = 0

b = BST()
b.Put(1,2)
b.Put(2,2)
b.Put(3,2)
b.Put(4,2)
b.Put(5,2)
b.Put(6,2)
b.Put(7,2)
b.Put(8,2)
b.Put(9,2)
b.Put(10,2)
b.Put(11,2)
b.Put(12,2)
b.Put(13,2)
b.Put(14,2)
b.Put(15,2)
b.printx()
