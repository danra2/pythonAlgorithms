#Object serialization, persistence means that you saved to a disk a python Object
#Pickle simplest way to pythonic objects.

#PDB
#import pdb
#You can stop through the code step and step, using pdb.set_trace()
#Press n to go through line by line, and c to continue.
#Trace the value of variables throughout each instance, you could even just use a general IDE
#Or you can use a console.log notifications on each instance.
#Let us go through statement through statement through other passing to other contexts and frames it's called step#
#We use s for that.
#Next vs step, next keeps you in current context, won't go into any functions that are called.
#Why use next anyways? Often using libraries we didn't write, we are making calls to functions that we don't know about
#Don't want to enter functions we don't know anything about.
#Chances are probably your own fault in your code.
#list l shows us where we are atm
#We can type h to see the commands that are available Pdb h debugger.
#Pycharm IDE for debugging as well Visual debugger.

# BenchMarking with Timeit

#pip instlal pytest
#Essentially a script that you can use to call other scripts, and test
#Unit based testing is essentially to test each individual module / functions and modularize testing


# if __name__ == '__main__':
#This is the gate of the program, essentially if you call this program directly
#It will run this program as well, however if you do a import, and specify this gate it won't run it even when you import and call a function within the module.

    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print "the value of {0} is {1}. format(input_val, doubled_val)"

#Run pytest in your terminal then use the assert method to test functions.
#Concept of unit testing

def test_doublit():
    asset myprogram.doubleit(10) == 20

#Basically pytest will test the function with the given input, and then check to if you get 20 once 10 is inputted
#If it doesn't then it will show an error message, and you keep doing this with each new methods / function.


def test_doubleit_type():
    with pytest.raises(TypeError):
        myprogram.doubleit('Hello')

#If there is a type error than print this statement out, essentially you are going to run test on both of these functions
#And it will go through each one and tell you what fail and what doesn't
#Test driven environment is making these tests before creating the functions so you know that this caters to the test.
#Set up and tear down routines for testing.
#Tests should be operating on a temporary data set, so called fixtures.
#Set up routines create an envinronment to run things, we use a tear down routine for other things.

fh.write('\n'.join(newList))
#this writes the instance into a file. 
