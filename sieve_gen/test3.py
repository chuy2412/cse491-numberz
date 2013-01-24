################################################################
#Test3: call the function next 3 times in the generator
#       check if the value is equal to 7
################################################################
import sieve

def test3():
    s = sieve.sieve() #create an object of type sieve

    s.next()    #move to the next prime number (3)
    s.next()    #move to the next prime number (5)

    #Check if next value is equal to 7
    #Error would occur if the value is not equal to 7
    assert s.next() == 7


#Call the first test to see if the value is equal to 7
test3()

