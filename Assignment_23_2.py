import multiprocessing
import os

def OddSum(N):
    total = 0

    for i in range(1, N + 1, 2):
        total += i

    print("Process ID :",os.getpid)
    print("Input :", N)
    print("Sum of Odd Numbers :",total)
    print()

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    Result = p.map(OddSum, Data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()