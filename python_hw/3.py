from operator import le, length_hint
import sys
from time import sleep

key = str('key_phrase')

temp = []
for i in range(len(sys.argv)):
    temp.append(sys.argv[i])

         
def search():
    for i in range(len(temp)):
        if temp[i] == key:
            return True
    return False

def main():
    search()
    if search() == True:
        print("Key phrase is found")
    else:
        print("Key phrase does not found")
   
if __name__ == '__main__':
    main()


