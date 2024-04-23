SAME   =((0,0,0,0,0,0,0,0),
         (0,0,0,0,0,0,0,0),
         (0,0,0,0,0,0,0,0),
         (0,1,1,1,1,1,1,0),
         (0,0,0,0,0,0,0,0),
         (0,1,1,1,1,1,1,0),
         (0,0,0,0,0,0,0,0),
         (0,0,0,0,0,0,0,0)
         )

ARROW_U=((0,0,0,0,1,0,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,1,1,1,1,1,0),
         (0,1,1,1,1,1,1,1),
         (0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,0,0,0,0,0)
         )

ARROW_D=((0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,1,1,1,1,1,1,1),
         (0,0,1,1,1,1,1,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,0,1,0,0,0),
         (0,0,0,0,0,0,0,0)
         )

SAME_LCD=((0,0,0,0,0),
         (0,0,0,0,0),
         (0,0,0,0,0),
         (0,1,1,1,0),
         (0,0,0,0,0),
         (0,1,1,1,0),
         (0,0,0,0,0),
         (0,0,0,0,0)
         )

ARROW_U_LCD=((0,0,1,0,0),
             (0,1,1,1,0),
             (1,1,1,1,1),
             (0,1,1,1,0),
             (0,1,1,1,0),
             (0,1,1,1,0),
             (0,1,1,1,0),
             (0,0,0,0,0)
             )

ARROW_D_LCD=((0,1,1,1,0),
             (0,1,1,1,0),
             (0,1,1,1,0),
             (0,1,1,1,0),
             (1,1,1,1,1),
             (0,1,1,1,0),
             (0,0,1,0,0),
             (0,0,0,0,0)
            )

characters = {1 : ARROW_U,
              2 : ARROW_D,
              3 : SAME
             }
characters_LCD={1 : ARROW_U_LCD,
                2 : ARROW_D_LCD,
                3 : SAME_LCD
              }
def getCharaterbyteArray(character):
    newChar = []
    for row in character:
        row = list(row)
        value = 0x00
        for pixel in row:
            value = value << 1
            if pixel == 1:
                value |= 0x01
        newChar.append(value)
    return bytearray(newChar)
 
#y <= 0
def getScrollingChar(character, y = 0):
    newChar = []
    height = len(character)
    y = y % height
    for row in character[y:]:
        newChar.append( row )
           
    for row in character[:y]:
        newChar.append( row )
    return newChar
                
def _printCharacter(character):
    for row in character:
        for pixel in row:
            if pixel == 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()
        
if __name__ == "__main__":
    _printCharacter(ARROW_U_LCD)
    print(getCharaterbyteArray(ARROW_U_LCD))
#     print("--------------")
#     for key in characters:
#         _printCharacter(characters[key])
#         print("--------------")
#     for key in characters_LCD:
#         _printCharacter(characters_LCD[key])
#         print("--------------")
#         
#     print("--------------")
#     for y in range(0, 9,1):
#         _printCharacter(getScrollingChar(ARROW_U, y))
#         print("--------------")
#     
#     print("--------------")
#     for y in range(8,-5,-1):
#         _printCharacter(getScrollingChar(ARROW_D, y))
#         print("--------------")
# 
