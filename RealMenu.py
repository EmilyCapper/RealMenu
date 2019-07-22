
__version__ = "0.5.0"

__doc__ = """
————————————————————————————————————————————————————————————————————————
RealMenu.py -- The customizable menus tool.

Import this tool with "from RealMenu import lm".  The folder with this
file, the __init__ and the dependencies, EssentialUtils and getkey,
should be in the same folder as whatever file is using this library.
If your file is in the same folder, it may not work perfectly.

When executing these methods, ensure that you use the function prefix
"lm", else it may raise an error.  It might look like this:

lm.methodName( [ arg1, ... ] )

Here's how to use the user-oriented methods:

--> setup( list, int ) -->
Takes two arguments ( the second argument being optional ), the list of
options that will be printed next to a checked or unchecked box and and
integer indicating how much indent by space you want between the edge of
the display and the checked or unckecked box.  Look at this bit of code:

options = [ "one", "two", three" ]
lm.setup( options, 4 )
lm.execute()

The user will see this:

    [ x ] one
    [   ] two
    [   ] three

Notice the four spaces between the left side and the checkboxes.

--> customize( list ) -->
One argument of list type.  This function allows putting text before the
selections, so menu information can be displayed to users.  The code:

options = [ "one", "two", three" ]
displayText = [ "Pick a number:" ]
lm.setup( options, 4 )
lm.customize( displayText )
lm.execute()

The user will see this:

Pick a number:
    [ x ] one
    [   ] two
    [   ] three

--> execute() -->
Takes zero arguments, as it processes the data inputted in setup and
customize.  This method allows the menu to "happen."  Upon completion of
its task, it returns the index of the selection made by the user in
reference to the inputted list in setup.  Here's some code:

options = [ "one", "two", three" ]
displayText = [ "Pick a number:" ]
lm.setup( options, 4 )
lm.customize( displayText )
optionSelected = lm.execute()
print( optionSelected )

Assuming the user picks the first option, in this display here:

Pick a number:
    [ x ] one
    [   ] two
    [   ] three

This will be outputted at the end:

0

As zero is the first index, and the first option was selected, zero is
returned.  It might seem counter-intuitive when numbers are the options,
however.

--> reset() -->
Takes zero arguments, as it is completely resetting the object lm in
running the class's __init__().  This means that the menu can be used
again once it has been set up.  In principle, the menu can be used again
before setting it up and having the same options.
————————————————————————————————————————————————————————————————————————
"""

try: from RealMenu.getkey import getkey
except: from getkey import getkey
from EssentialUtils import eu
import sys

class RealMenu:

    def __init__( self ):
        self.choice = []
        self.options = []
        self.selection = 0
        self.lines = []
        self.upArrow = b'\x1b[A'
        self.downArrow = b'\x1b[B'
        self.enterKey = b'\n'
        self.optionRange = []
        self.filled = "[ x ] "
        self.blank = "[   ] "
        self.indent = ""

    def help( self ):
        print( __doc__ )

    def setup( self, options, indent = 0 ):
        self.options = options
        for i in range( len( self.options ) ):
            if i == 0:
                self.choice.append( self.filled )
            else:
                self.choice.append( self.blank )
        self.optionRange = range( len( self.options ) )
        for i in range( indent ):
            self.indent += " "

    def customize( self, lines ):
        self.lines = lines

    def reset( self ):
        self.__init__()

    def execute( self ):
        self.selection = 0
        if self.options == []:
            raise Exception( "Setup not complete before menu execution.\n\
                              Run lm.setup( list ) with a list of options\
                              to choose from." )
        return self.selectionHandler()

    def selectionHandler( self ):
        key = ""
        while True:
            self.reloadDisplay()
            key = self.userKey()
            if key == self.upArrow and ( self.selection - 1 ) in self.optionRange:
                self.doChangeSelected( -1 )
            elif key == self.downArrow and ( self.selection + 1 ) in self.optionRange:
                self.doChangeSelected( 1 )
            elif key == self.enterKey:
                break
        eu.clear()
        return self.selection

    def userKey( self ):
        key = bytes( getkey() ) if sys.version_info < ( 3, 0 )\
                                else bytes( getkey(), "UTF8" )
        return key

    def doChangeSelected( self, change ):
        self.selection += change
        self.choice[ self.choice.index( self.filled ) ] = self.blank
        self.choice[ self.selection ] = self.filled
        self.reloadDisplay()

    def reloadDisplay( self ):
        eu.clear()
        if self.lines != []:
            for i in self.lines:
                print( i )
        for j in range( len( self.options ) ):
            print( self.indent + self.choice[ j ] + self.options[ j ] )

lm = RealMenu()


