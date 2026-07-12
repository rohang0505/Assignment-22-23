import multiprocessing
import os

def SumOfSquares(N):
    total = 0

    for i in range(1,N + 1):
        total = total + (i + i)

    print("Process Id :",os.getpid)
    print("Input Number :", N)
    print("Sum of Square :",total)
    print()

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    p = multiprocessing.Pool()
    Result = p.map(SumOfSquares,Data)

    p.close()
    p.join()

    print("Final Output :")
    print(Result)


if __name__ == "__main__":
    main()