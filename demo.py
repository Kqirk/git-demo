def main ():
    fizzBuzz()

def fizzBuzz():
    print("hi")
    for i in range(0, 100):
        if (i % 5 == 0 and i % 3 == 0):
            print("FizzBuzz")
        elif (i % 5 == 0):
            print("Fizz")
        elif(i % 3 == 0):
            print("Buzz")
        elif(i % 7 == 0):
            print("HI")
        else:
            print(i)

if __name__ == "__main__":
    main()