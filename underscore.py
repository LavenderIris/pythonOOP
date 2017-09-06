
class Underscore(object):
    def map(self, numlist, callback):
        # we take the value from each callback and reassign to my original numlist
        for index, num in enumerate(numlist):
            numlist[index] = callback(num)
        return numlist                

    def reduce(self,numlist, callback):
        # it takes a list of numbers and adds thru them one by one and returns overall total
        total=0
        for num in numlist:
            if callback(total, num):
               total+=num
        return total 
    
    def find(self,numlist,callback):
        # returns the first number that is true to the callback
        for num in numlist:
            if callback(num):
                return num
        return -1
        
    def filter(self, numlist, callback):
        # filters a list of numbers based on true criteria
        new_list=[]
        for num in numlist:
            if callback(num):
                new_list.append(num)
        return new_list

    def reject(self,numlist,callback):
        # opposite of filter. Returns a list that is not true of given criteria
        new_list=[]
        for num in numlist:
            if not callback(num):
                new_list.append(num)
        return new_list
 
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print "evens {}".format(evens)

e_index = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "For find, the expected solution is 2 and we have returned {}".format(e_index)

odds_total = _.reduce([1, 2, 3, 4, 5, 6], lambda x, y: x + y )
print "total of all odds: {}".format(odds_total)

odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "Odds are {}".format(odds)

maps= _.map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
print maps