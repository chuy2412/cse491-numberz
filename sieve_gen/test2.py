################################################################
#Test2: call the function next 2 times in the generator
#       check if the value is equal to 5
################################################################
import sieve

def test2():
    s = sieve.sieve() #create an object of type sieve

    s.next()    #move to the next prime number (3)

    #Check if next value is equal to 5
    #Error would occur if the value is not equal to 5
    assert s.next() == 5


#Call the first test to see if the value is equal to 5
test2()

