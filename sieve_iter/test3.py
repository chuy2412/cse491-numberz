################################################################
#Test3: move the iterator to the next prime number 3 times
#	check if the value is equal to 7
################################################################
import sieve

def test3():
    s = sieve.sieve() #create an object of type sieve
    i = iter(s)       #create an interator for the object sieve

    i.next()    #move to the next value of iterator (3)
    i.next()    #move to the next value of iterator (5)
   
    #Check if next value is equal to 7
    #Error would occur if the value is not equal to 7
    assert i.next() == 7


#Call the first test to see if the value is equal to 7
test3()


