# Video 35

# Python command line arguments ----->

import argparse
def sum(a, b):
    return a+b

if __name__ == "__main__":

    # initialize the parser
    parser = argparse.ArgumentParser(description= " Adding two numbers ")

    # Add parameters
    parser.add_argument("num1",type=int, help="First Number")
    parser.add_argument("num2",type=int, help="Second Number")


    # parse the arguments
    args = parser.parse_args()


    print("Sum is: ",sum(args.num1, args.num2))
    