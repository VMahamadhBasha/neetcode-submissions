class TimeMap:

    def __init__(self):
        self.st={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.st:
            self.st[key]=[]
        self.st[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.st:
            return ""
        values=self.st[key]
        result=''
        l=0
        h=len(values)-1
        while l<=h:
            m=(l+h)//2
            if values[m][0]<=timestamp:
                result=values[m][1]
                l=m+1
            else:
                h=m-1
        return result
        
