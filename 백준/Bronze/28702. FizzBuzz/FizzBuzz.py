def FizzBuzz(x):
    if x % 15 == 0:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return x

lst = [input() for i in range(3)]

for i in range(3):
    if lst[i] == 'Fizz' or lst[i] == 'Buzz' or lst[i] == 'FizzBuzz':
        lst[i] = 1
    else:
        lst[i] = int(lst[i])
sum = 0
for i in range(3):
    if sum == 0 and lst[i] == 1:
        pass
    elif lst[i] != 1:
        sum = lst[i]
    else:
        sum += 1
print(FizzBuzz(sum+1))