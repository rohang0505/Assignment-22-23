import multiprocessing
import os

def IsPrime(No):
    if No < 2:
        return False
    
    for i in range(2, int(No ** 0.5)+1):
        if No % i == 0:
            return False
        
    return True

def PrimeCount(N):
    count = 0

    for i in range(1, N + 1):
        if IsPrime(i):
            count += 1

    print("Process ID :",os.getpid)
    print("Input :",N)
    print("Prime count :",count)
    print()

    return count

def main():
    Data = [10000, 20000, 30000, 40000]

    p = multiprocessing.Pool()
    Result = p.map(PrimeCount, Data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()