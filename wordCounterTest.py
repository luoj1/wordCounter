import sys
from wordCounter import wordCounter

print ('please enter in source of txt file')
src = sys.stdin.readline()
src = src[:-1]
print ('please enter in output file of result')
target = sys.stdin.readline()
target = target[:-1]
wordCounter(src, target)
print ('finish')