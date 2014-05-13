#
# Test harness for COMP10001 Project 3, 2014s1
#
# Author: Tim Baldwin
# based on code by Marco Lui
#
# Date: 11/5/2014



import getpass,sys
from tests import tests


try:
    code = getpass.getuser()  # get the user name
    submission = __import__(code)  # import the file `USERNAME.py`

# exit if one of the above statements doesn't execute properly, presumably because `USERNAME.py` didn't import properly
except ImportError:
    print "ERROR: Make sure you run the code in the directory where your solution is, and that it is named correctly"
    sys.exit()
except Exception, e:
    print "ERROR: Failed to import your code due to the following error:"
    print "{0}".format(e)
    sys.exit()
    
    

####################################################################################
#
# name: test()
#
# synposis: run the tests for the supplied function name, and check the outputs against those in `test`
# input(s): the function name to be tested (str)
# output(s): print the tests that are tried, and if unsuccessful, the correct value vs. returned value
#

def test(funct_name):
    # print out the names of functions which can be tested in `funct_name` is not in `tests`, and exit
    if funct_name not in tests:
        print "ERROR: '{0}' is not a recognised function name; select from: {1}".format(funct_name,str(tests.keys()))
        return -1
    
    # run test (using valid function name)
    print "Testing the {0} function ...\n".format(funct_name)
    correct = 0  # number of tests passed
    
    # run the user-defined function with each of the sets of arguments provided in `tests`, and chech that the
    # output is correct
    for test in tests[funct_name]:
        print "  testing {0} ...".format(test[0]),
        userval = eval(test[0])  # run the function with the supplied set of arguments (take the string and execute it)
        expval = test[1]
        
        if funct_name in ['swap_cards', 'play']:
        # if the returned value is correct, increment `correct` and print a congratulatory print statement
            if test_equivalent_inset(userval,expval):
                correct += 1
                print "passed"
            
            # if the returned value is *in*correct, print diagnostics
            else:
                print "failed"
                print "    * expected val in (type '{0}') {1}".format(type(expval), expval)
                print "    * returned = (type '{0}') {1}".format(type(userval), userval)

        else:
            # if the returned value is correct, increment `correct` and print a congratulatory print statement
            if test_equivalent(userval,expval):
                correct += 1
                print "passed"
            
            # if the returned value is *in*correct, print diagnostics
            else:
                print "failed"
                print "    * expected = (type '{0}') {1}".format(type(expval), expval)
                print "    * returned = (type '{0}') {1}".format(type(userval), userval)
    
    # print the overall number of tests passed vs. attempted    
    print "\n{0}/{1} tests passed for {2}".format(correct,len(tests[funct_name]),funct_name)

#   
# end test()    
####################################################################################
    




####################################################################################
#
# name: test_equivalent()
#
# synposis: test for equivalence between two arguments. In particular, for this project
#   we need to allow for different orders between hands, as well as different orders
#   for the cards in a hand. We do this by converting the a list-of-lists representation
#   into a set-of-sets representation. We use frozenset as the standard set() is mutable,
#   making it unhashable and thus unsuitable for inclusion in a set.
# input(s): two arguments of arbitrary type
# output(s): Boolean evaluation of the equivalence of the two arguments
#

def test_equivalent(a,b):
    # we consider lists of lists to be the same as long as their contents are the same, 
    # ignoring order of both the outer and inner lists
    if isinstance(a, list) and isinstance(b, list):
        try:
            return as_setset(a) == as_setset(b)
        except TypeError:
            # One of the items was not iterable, we fall back to standard equality
            return a == b
            
    # for everything else, we use the built-in notion of equality
    else:
        return a == b

#  
# end test_equivalent()   
####################################################################################




####################################################################################
#
# name: test_equivalent_inset()
#
# synposis: test for equivalence between two arguments. In particular, for this project
#   we need to allow for different orders between hands, as well as different orders
#   for the cards in a hand. We do this by converting the a list-of-lists representation
#   into a set-of-sets representation. We use frozenset as the standard set() is mutable,
#   making it unhashable and thus unsuitable for inclusion in a set.
# input(s): two arguments of arbitrary type
# output(s): Boolean evaluation of the equivalence of the two arguments
#

def test_equivalent_inset(a,b):
    # we consider lists of lists to be the same as long as their contents are the same, 
    # ignoring order of both the outer and inner lists
    match = False
    for b_i in b:
        if isinstance(a, list) and isinstance(b_i, list):
            try:
                match = match or (as_setset(a) == as_setset(b_i))
            except TypeError:
                # One of the items was not iterable, we fall back to standard equality
                match = match or (a == b_i)
            
        # for everything else, we use the built-in notion of equality
        else:
            match = match or (a == b_i)
    return match

#  
# end test_equivalent()   
####################################################################################




####################################################################################
#
# name: as_setset()
#
# synposis: convert a list-of-lists into a set of sets. This is to facilitate
#   order-agnostic checking of output.
# input(s): a list of lists
# output(s): a frozenset of frozensets 
#

def as_setset(seq):
    return frozenset(frozenset(s) for s in seq)

#  
# end as_setset()   
####################################################################################

# A module's __name__ is set to __main__ when it is imported at the top level 
# (i.e. not by another module)
if __name__ == "__main__":
    for fn_name in tests: 
        # if submission implements the given function
        if hasattr(submission, fn_name):
            test(fn_name)
        else:
            print "No implementation for '{0}'".format(fn_name)
