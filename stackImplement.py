class Stacky:
    
    def __init__(self) :
        self._data = []
    
    def len(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self, value):
        self._data.append(value)
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self._data.pop()
        
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self._data[-1]
        
        
        
eric = Stacky()
print(eric.is_empty())
eric.push(2)
print(eric.is_empty())  
eric.pop() 

eric.top() 
print(eric.is_empty())
eric.push(7) 
eric.push(9)
print(eric.top())
print(eric.len())

    
 
        
    
    