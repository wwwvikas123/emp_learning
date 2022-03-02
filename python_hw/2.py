import argparse
from tomlkit import integer


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('int', type=int, nargs='+')
    script_arg = parser.parse_args()
    return script_arg
  
def main(mylist):
    temp = []
    for number in mylist:
        if int(number) % 2 == 0 and int(number) != 254:
            temp.append(number)
    [print(i) for i in temp]
    
if __name__ == '__main__':
    script_arg = create_parser()
    main(script_arg.int)