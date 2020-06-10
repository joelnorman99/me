"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#This may create a list containing the words: what, does, this, line, do, ?
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #Printed the list

for word in some_words: #this will print the words in list some_words
    print(word) #this printed the words from the list till they were all written

for x in some_words: #an error may occur?
    print(x) #prints the word as a string in some_words

print(some_words) #Prints the strings in the list some_words

if len(some_words) > 3: #will print words from some_words if there are more than 3 words in the list
    print('some_words contains more than 3 words') #printed some_words contains more than 3 words, therefore, some_words has more than 3 entries

def usefulFunction(): #contains tuple (round brackets) of information in my computer and the system
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #prints operating system uname_result(system='Darwin', node='MacBook-Pro', release='19.4.0', version='Darwin Kernel Version 19.4.0: Wed Mar  4 22:28:40 PST 2020; root:xnu-6153.101.6~15/RELEASE_X86_64', machine='x86_64', processor='i386')

usefulFunction()
