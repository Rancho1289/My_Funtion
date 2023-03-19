# 한줄 짜리 주석

"""
주석
여러줄
적는 방법
"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


def gugudan(x):
    for i in range(9):
        print((i+1)*x)

