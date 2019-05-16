from CustomMenu import *

def callCreateMenu( menuList, header ):
  optionSelected = CustomMenu().createMenu( menuList, header )
  return optionSelected

menuList = [ "Option 1", "Option 2", "Option 3" ]

header = "Menu Header\n\n"

print( callCreateMenu( menuList, header ))


