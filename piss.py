import os 
 

from decr import decr 
from encr import encr 


def main():
    print("1.encr \n2.decr \n")
    val = int(input(">>"))

    if val == 1 :
        encr()

    elif val == 2 :
        decr()

    else:
        print("type 1 or 2 u dumb shit")


main()
