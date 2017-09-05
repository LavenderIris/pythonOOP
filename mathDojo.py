class MathDojo(object):
    def __init__(self):
        self.result=0
    
    def add(self, *args):
        for element in args:
            if isinstance(element, list):
                for n in element:
                    self.result+=n
            elif isinstance(element, int) or isinstance(element, float):
            # if it's an integer or float
                self.result+=element
            elif isinstance(element, tuple):
            #catching for tuples
                for e in element:
                    self.result+=e
        return self

    def subtract(self, *args):
        for element in args:
            if isinstance(element, list):
                for n in element:
                    self.result-=n
            elif isinstance(element, int) or isinstance(element, float):
            # if it's an integer or float
                self.result-=element
            elif isinstance(element, tuple):
                for e in element:
                    self.result-=e
        return self

    def add2(self, *args):
        for n in args:
            self.result+=n
        print self.result

md=MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

ad = MathDojo()
print ad.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).add((1,1),[2],1).subtract(1,(1,1),[1]).result