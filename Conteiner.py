class Container:
  
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second
        self.list_1 = self.first,self.second
    
    def __eq__(self,other):
        return self.list_1 == other

    def __str__(self):
        if self.first == None and self.second == None:
            return f"[]"
        if self.second == None:
            self.second = ""
            return f"[{self.first}]"
        else:
            return f"{sorted(self.list_1)}"
            

c1 = Container() 
c2 = Container(10) 
c3 = Container(10,100) 
c4 = Container(100,10)
c5 = Container(10,100)


print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c4 == c5)
print(c3 == c5)

