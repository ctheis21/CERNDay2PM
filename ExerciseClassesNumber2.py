import pickle
import os.path


class Stack(list): 
    
    __MAX_SIZE=10000 # A class variable
    
    def __init__(self, size):
        super().__init__()
        if isinstance(size, int) and size > 0 and size < Stack.__MAX_SIZE:
            self.__maxSize=size
        else:
            raise Exception("Wrong stack size given")
            
    @property
    def maxSize(self):
        return self.__maxSize
    
    def __repr__(self):
        return f"({len(self)}/{self.maxSize}) {super().__repr__()}"

    def __eq__(self, other):
        return self.maxSize == other.maxSize and super().__eq__(self, other)
    
    def push(self, value):
        if len(self) >= self.maxSize: #The stack is full
            raise Exception("Stack full!")
        else:
            self.append(value)
    def pop(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return super().pop()
    def peek(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self[-1]
    def isEmpty(self):
        return len(self)==0
    def extendMaxSize(self, newSize):
        if isinstance(newSize, int) and newSize > self.maxSize and newSize <= Stack.__MAX_SIZE:
            self.__maxSize=newSize
        else:
            raise Exception("Wrong stack size given")
    def serialize(self,filename):
        with open(filename, "wb") as fic:
            pickle.dump(self,fic)
            
    @staticmethod 
    def deserialize(filename):
        if os.path.exists(filename):
            try:
                with open(filename, "rb") as fic:
                    temp=pickle.load(fic)
                    return temp
            except Exception as ex:
                print("my",ex)
                raise
        else:
            raise Exception(f"{filename} not found!")
            
    @staticmethod 
    def getMaxSize():
        return Stack.__MAX_SIZE   
       
if __name__ == "__main__":
   
    s1=Stack(10) # 10 is the maximum size of the Stack
    s1.push(24)
    s1.push(27)
    s1.push(29) # obj.method(arg1, arg2) -> method(obj, arg1, arg2)

    print(f"Current maxSize of s1 is {s1.maxSize}")
    
    #s1.maxSize=23 # Exception raised here !!!
    
    s1.serialize("data.pick")
    s4=Stack.deserialize("data.pick")
    print(s4)
    print(len(s1)) # 3
    print(len(s1)) # 3
    print(s1) # (3/10) [24,27,29]
    if 56 in s1:
        print("56 is in the Stack")
    else:
        print("56 is not in the Stack")
    top=s1.pop()
    print(top) # 29
    print(s1) # (2/10) [24,27]
    print(len(s1)) # 2
    top=s1.pop()
    print(top) # 27
    print(s1) # (1/10) [24]
    top=s1.peek()
    print(top) # 24
    print(s1) # (1/10) [24]
    s2=Stack(20) # 20 is the maximum size of the Stack
    s2.push(24)
    print(s2)
    print(s1==s2)
    s2.extendMaxSize(25)
    print(s2)
    s2.clear()
    print(s2)
    
    for e in s1:
        print(e)