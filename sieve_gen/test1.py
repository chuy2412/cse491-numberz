################################################################
#Test1: call the function next 1 time in the generator
#       check if the value is equal to 3
################################################################
import sieve

def test1():
    s = sieve.sieve() #create an object of type sieve

    #Check if next value is equal to 3
    #Error would occur if the value is not equal to 3
    assert s.next() == 3


#Call the first test to see if the value is equal to 3
test1()
