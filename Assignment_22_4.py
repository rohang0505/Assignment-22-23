import multiprocessing
import os
import time

def PowerSum(N):
    total = 0

    for i in range(1,N + 1):
        total += i ** 5

    print("Process ID :",os.getpid)
    print("Input :", N)
    print("Sum :",total)
    print()

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time =time.time()

    p = multiprocessing.Pool()
    Result = p.map(PowerSum, Data)

    p.close()
    p.join()

    end_time = time.time()

    print(Result)
    print("Execution Time :", end_time - start_time)

if __name__ == "__main__":
    main()