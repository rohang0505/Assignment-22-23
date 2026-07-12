import multiprocessing
import os

def Factorial(N):
    fact = 1

    for i in range(1, N + 1):
        fact += i

        print("Process ID :", os.getpid)
        print("Input Number :", N)
        print("Factorial :",fact)
        print()

        return fact  
    
def main():
    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()
    Result = p.map(Factorial, Data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()
