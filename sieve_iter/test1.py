################################################################
#Test1: move the iterator to the next prime number 1 time
#       check if the value is equal to 3
################################################################
import sieve

def test1():
    s = sieve.sieve() #create an object of type sieve
    i = iter(s)       #create an interator for the object sieve

    #Check if next value is equal to 3
    #Error would occur if the value is not equal to 3
    assert i.next() == 3


#Call the first test to see if the value is equal to 3
test1()
