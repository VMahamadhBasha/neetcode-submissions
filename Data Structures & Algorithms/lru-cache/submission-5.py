class LRUCache:

    def __init__(self, capacity: int):    
        self.d=[]
        self.c=capacity    

    def get(self, key: int) -> int:
        res=-1
        for i in range(len(self.d)):
            if self.d[i][0]==key:
                res=i
        if res==-1:
            return -1
        value=self.d.pop(res)
        self.d.insert(0,value)
        return value[1]
    
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.d)):
            if self.d[i][0]==key:
                self.d.pop(i)
                break
        self.d.insert(0,[key,value])
        if len(self.d)>self.c:
            self.d.pop()
        

        
