"""
____________________________________________________
How to use: CustomMenu()
Import CustomMenu.py, assuming it's in
another file: from CustomMenu import *
When extending another class from CustomMenu,
( looks like: extendedClassName( CustomMenu ) )
it is reccommended to use this function:
def callCreateMenu( self, menuList, header ):
  self.__menuList = menuList
  self.__header = header
  self.__optionSelected = CustomMenu().createMenu( menuList, header )
Or use a different method.
After creating an object of your extended,
call callCreateMenu with the arguments of
list of options in the menu and the header
of the menu, looking perhaps like this:
menuList = [ "Singleplayer", "Multiplayer", "Zeroplayer" ]
header = "Header of the program\n\n"
objectOfExtended = extendedClassName()
objectOfExtended.callCreateMenu( menuList, header )
Any number of items can be appended to the menuList,
and which option is selected will be stored, if
using the callCreateMenu function, into
self.__optionSelected, as it would index the original
option title in menuList.  Say in the example above
I select "Multiplayer": it will return a 1.
"Singleplayer" would return a 0 and "Zeroplayer",
being the third item in the list and list of options,
would return a 2.  Very much like indexing, but
will nevertheless return what the user inputted.
Header is the second argument that you'll
end up inputting, and it is essentially the title
of the program, to print that at the beginning.
You can choose to include line breaks to improve
the asthestic, however a minimum of 1 is recommended.
The first arguent is menuList, which will create a
menu with options, an option for each item in the list.
What number it returns corresponds to above.
____________________________________________________
"""

from getkey import getkey
import sys
import os

class CustomMenu():
  def __init__( self ):
    self.__optionListToPrint = []
    self.__optionSelected = "[ x ] "
    self.__optionNotSelected = "[   ] "

  def createMenu( self, menuList, header ):
    self.__header = header
    self.__numberOfOptions = len( menuList )
    self.__loopCount = self.__numberOfOptions * 2
    for i in range( self.__loopCount ):
      if i % 2 == 0: # is even
        if i == 0:
          self.__optionListToPrint.append( self.__optionSelected )
        else:
          self.__optionListToPrint.append( self.__optionNotSelected )
      else: # else it is odd
        self.__optionListToPrint.append( menuList[ int( i / 2 ) ] + "\n" )
    self.__selectMenu()
    return self.__optionSelected

  def __selectMenu( self ):
    upArrow = b'\x1b[A'
    downArrow = b'\x1b[B'
    enterKey = b'\n'
    self.__temporaryModeStorage = 0
    lowTempModeStorBound = self.__numberOfOptions - 1
    key = ""
    while key != enterKey and key != upArrow and key != downArrow:
      clear()
      self.__reloadMenu()
      if sys.version_info < (3, 0):
        key = bytes( getkey() )
      else:
        key = bytes( getkey(), "UTF8" )
      if key == upArrow and self.__temporaryModeStorage > 0:
        self.__temporaryModeStorage -= 1
        self.__reloadMenu()
        key = ""
      elif key == downArrow and self.__temporaryModeStorage != lowTempModeStorBound:
        self.__temporaryModeStorage += 1
        self.__reloadMenu()
        key = ""
      elif key == enterKey:
        break
      else:
        key = ""
    self.__optionSelected = self.__temporaryModeStorage
    
  def __reloadMenu( self ):
    modeHeader = self.__header + "Select an option using the arrow keys and press enter:\n"
    clearCycleCount = ( len( self.__optionListToPrint ) - 1 )
    for i in range( 0, clearCycleCount, 2 ):
      self.__optionListToPrint[ i ] = self.__optionNotSelected
    self.__optionListToPrint[ self.__temporaryModeStorage * 2 ] = self.__optionSelected
    print( modeHeader + compileArray( self.__optionListToPrint ))

def compileArray( arr ):
  compiledString = ""
  for i in range( len( arr )):
    compiledString += arr[ i ]
  return compiledString

def clear():
  try: print( "\033c" )
  except: os.sytem( 'cls' )

