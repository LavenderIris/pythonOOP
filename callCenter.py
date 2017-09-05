import sys

class Call(object):
    """
    Call class, includes details about the phone call itself
    """
    def __init__(self,id,name,phone,time_of_call,reason):
        self.id=id
        self.name=name
        self.phone=phone
        self.time_of_call=time_of_call  #in military time format
        self.reason=reason
    
    def display(self):
        print "Unique ID:", self.id
        print "Name:", self.name
        print "Phone:", self.phone
        print "Time of call:", self,time_of_call
        print "Reason:", self.reason
        return self

class CallCenter(object):
    """
    Callcenter class, defined as taking a list of call objects and doing various things with them
    """
    def __init__(self, calls):
        self.calls=calls
        self.queue_size=len(calls)
    
    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self):
        if (len(self.calls)==0):
            print "no more calls to remove"
        else :
            # take off the first item from the queue
            self.calls.pop(0)
        return self

    def info(self):
        self.queue_size = len(self.calls)
        print "Queue size is:", self.queue_size
        for element in self.calls:
            print "Name:", element.name,"Phone", element.phone
        return self

    def removeCall(self,phone):
        index = -1
        for i, element in enumerate(self.calls):
            if element.phone == phone:
                index = i
        self.calls.pop(index)
        return self
    
    def sortCalls(self):
        temp=[]
        while (len(self.calls)>0):
            my_min=sys.maxint
            index=-1
            for i, element in enumerate(self.calls):
                if element.time_of_call<my_min:
                    my_min = element.time_of_call
                    index=i
            # find the smallest number and push onto my new temp array
            temp.append(self.calls[index])            
            self.calls.pop(index)
            
        # reassign temp to my now newly sorted list
        self.calls=temp
        return self

call1=Call(1,"Michael Jackson","555-555-1212",1400,"to add a new person to account")
call2=Call(2,"Shelby Yaris","301-345-1234",1360,"activating a new card")
call3=Call(3,"Lucio Abuya","601-345-5432",1350,"going out of country alert")
call4=Call(1,"Optimus Prime","555-555-5555",1200,"to add a new person to account")

callcenter=CallCenter([call1, call2, call3])
callcenter.info()
callcenter.remove().info()
callcenter.add(call4).info()

print "NINJA CHALLENGE: remove call based on phone"
callcenter.removeCall('555-555-5555').info()
callcenter.add(call4).add(call1).info()

print "HACKER CHALLENGE sorted calls"
callcenter.sortCalls().info()