################################################################
#Test2: move the iterator to the next prime number 2 times
#       check if the value is equal to 5
################################################################
import sieve

def test2():
    s = sieve.sieve() #create an object of type sieve
    i = iter(s)       #create an interator for the object sieve

    i.next()	#move to the next value of iterator 3

    #Check if next value is equal to 5
    #Error would occur if the value is not equal to 5
    assert i.next() == 5


#Call the first test to see if the value is equal to 5
test2()

