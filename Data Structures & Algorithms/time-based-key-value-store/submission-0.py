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
        for i,t in values:
            if i<=timestamp:
                result=t
            else:
                break
        return result
        
