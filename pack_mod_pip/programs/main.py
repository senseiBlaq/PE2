# ModuleNotFoundError even thoght the parent directory poath is correct.
import sys
import module

sys.path.append('/Users/sensei_blaq/Desktop/dōjō/repos/PE2/py/modules/')

zeroes = [0 for i in range(5)]  # list comprehension to create a list of zeroes
ones = [1 for i in range(5)]  # list comprehension to create a list of ones

print(module.sum1(zeroes))
print(module.prod1(ones))
print(module.__counter)


print("\nEnd of program!!")
