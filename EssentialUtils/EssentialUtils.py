
__version__ = "0.1.0"

__doc__ = """
————————————————————————————————————————————————————————————————————————
EssentialUtils.py -- Useful or random tools that come up every so often.

Import these tools via "from EssentialUtils import eu", and access each
method by doing eu.methodName( [ arg1 ,] [ arg2 ... ] ), so "eu." + name
of needed method + any arguments, if applicable.

There are currently 8 methods.
Here's a list of them:

--> help() -->
Prints this docstring, no arguments.

--> clear() -->
Clears the terminal, no arguments.

--> compileArray( list ) -->
Assembles the parts in a list into a single string, one argument of list
type.

--> splitIntoEqualParts( str, length [ , remainder ] ) -->
Splits a string into parts of n length, starting from the left.  Takes
minimum of two arguments, the string to split, and what size parts to
split it into, str and length, first and second arguments, respectively.
The third optional is a boolean for including the tail end of the split
string if it didn't divide perfectly into equal parts.  Say you have
string "abcde" and length split of three, it returns [ "abc", "de" ] by
default, unless remainder is False.

--> simplifyFraction( list ) -->
Simplifies a fraction in the form of a list.  Takes one argument, a list
the len of which is two, and all parts of the list being integers.  For
example: simplifyFraction( [ 4, 6 ] ) will return [ 2, 3 ].
This method depends on the following function also in Utils:
primeList

--> primeList( int ) -->
Generates a list of prime numbers up to integer i, including it if it is
prime.  Takes one argument of integer type.  For example: primeList( 7 )
will return [ 2, 3, 5, 7 ].
This method depends on the following function also in Utils:
isPrime

--> isPrime( int ) -->
Returns a True or False based on if the inputted integer is prime or
not.  Takes one argument of integer type.  For example: isPrime( 4 )
will return False.

--> whereOccursIn( list, str ) -->
Returns the indexes in order in which the second argument appears in the
first argument.  Takes two arguments, the list ( or string ) to be
searched and the string ( or integer ) to search for in first argument.
For example: whereOccursIn( [ "ap", "ab", "ac", "ap" ], "ap" ) will
return [ 0, 3 ].  And:  whereOccursIn( "seven", "e" ) will return
[ 1, 3 ].  And: whereOccursIn( [ 3, 2, 5, 7 ], 1 ) will return [].  In
the example of lists, unlike strings, they can be searched for an item
with a length over one, while searching a string is limited to one
character searches, as this method was designed for list processing, but
works sometimes for other types.
————————————————————————————————————————————————————————————————————————
"""

import os

class Utils:

    def help():
        print( __doc__ )

    def clear():
        try: os.system( 'clear' ) # print( "\033c" )
        except: os.sytem( 'cls' )

    def compileArray( arr ):
        compiledString = ""
        for i in range( len( arr ) ):
            compiledString += arr[ i ]
        return compiledString

    def splitIntoEqualParts( s, l, r = True ):
        a = []
        for i in range( 0, len( s ), l ):
            a.append( s[ i : i + l ] )
        return a if r else a[ : len( a ) - 1 ]

    def simplifyFraction( frac ):
        for i in eu.primeList( max( frac ) ):
            if frac[ 0 ] % i == 0 and frac[ 1 ] % i == 0:
                frac = [ frac[ 0 ] // i, frac[ 1 ] // i ]
        return frac

    def primeList( i ):
        l = []
        for i in range( 2, i + 1 ):
            if eu.isPrime( i ):
                l.append( i ) 
        return l

    def isPrime( n ):
        for i in range( 2, n // 2 + 1 ):
            if n % i == 0:
                return False
        return True

    def whereOccursIn( l, s ):
        t = []
        for i in range( len( l ) ):
            if l[ i ] == s:
                t.append( i )
        return t

eu = Utils


