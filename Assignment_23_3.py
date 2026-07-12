import multiprocessing
import os

def EvenCount(N):
    count = 0

    for i in range(2, N + 1,2):
        count += 1

    print("Process ID :", os.getpid)
    print("Input :", N)
    print("Even Count :", count)
    print()

    return count  

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    Result = p.map(EvenCount, Data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()