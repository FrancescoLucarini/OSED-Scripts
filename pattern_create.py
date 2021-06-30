import random
import argparse
data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

pattern = ''

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lenght", type=int, required=True)

args = parser.parse_args()

for i in range(0, args.lenght):
    pattern += data[random.randint(0, len(data)-1)]

print(pattern)
x = input("Enter pattern to be searched: ")
lenght2 = len(x)
indexes = []

for i in range(0, len(pattern)):
    temp = pattern[i:i+lenght2]
    if temp == x:
        indexes.append(pattern.index(temp))

for i in indexes:
    print(i)
