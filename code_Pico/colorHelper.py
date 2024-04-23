import random

MVA = 80 # max value for color

COLOR_BLACK = (  0,  0,  0)
COLOR_RED   = (MVA,  0,  0)
COLOR_ORANGE= (MVA,140,  0)
COLOR_GREEN = (  0,MVA,  0)
COLOR_BLUE  = (  0,  0,MVA)

#returns a random RGB color
def getRandomColor():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    return (r,g,b)

if __name__ == "__main__":
    print(getRandomColor())
    
    
    