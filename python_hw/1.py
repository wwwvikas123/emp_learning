from pip import main

def type_numbers (int):
    input_int = input().split(',') 
    print("array:", list(input_int), tuple(input_int))
    
def main ():
    print ("Type numbers sepateted by ','")
    type_numbers (int)
    
if __name__ == '__main__':
    	 main()  
