import sys, getopt

def fib(stop):
    a, b  = 0, 1
    for _ in range (0,stop):
        a, b = b, a+b
    return a



def main():
    
    try:
        argsWithoutProg = int(sys.argv[1])
        print (fib(argsWithoutProg))
    except:
         print ("Please provide a number")

if __name__ == "__main__":
  main()