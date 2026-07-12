import multiprocessing
import os

def OddCount(N):
    count = 0

    for i in range(1, N + 1,2):
        count += 1

    print("Process ID :", os.getpid)
    print("Input :", N)
    print("Odd Count :", count)
    print()

    return count  

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    Result = p.map(OddCount, Data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()