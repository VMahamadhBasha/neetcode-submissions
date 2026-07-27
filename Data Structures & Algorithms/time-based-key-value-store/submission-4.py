class TimeMap:

    def __init__(self):
        self.st={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.st:
            self.st[key]=[]
        self.st[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.st:
            return ''
        v=self.st[key]
        result=''
        l,r=0,len(v)-1
        while l<=r:
            m=(l+r)//2
            if v[m][0]<=timestamp:
                result=v[m][1]
                l=m+1
            else:
                r=m-1
        return result