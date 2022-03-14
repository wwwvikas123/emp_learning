a = [1, 5454]

not_digit = []

result = []


def IsInt():
    for element in a:
        if str(element).isdigit():
            pass
        else:
            not_digit.append(element)        
    return element
    

def largest_num():
    for x in range(len(a)):
        largeNum = 0
        for y in range(len(a)):
            if a[y] > largeNum:
                largeNum = a[y]
        a.remove(largeNum)
        result.append(largeNum)
    print(result[0:3])

def main():
    element = IsInt()
    if str(element).isdigit() == False:
        print("You've passed some extra elements that I can't parse: ", not_digit)   
    else:
        largest_num()
     
        

if __name__ == '__main__':
    main()  
