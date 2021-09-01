numbers = [1, 2, 3, 4, -1, 0, -20, 1]

#numbers.sort()
#numbers.reverse()
#numbers.append(1000)
#print(len(numbers))
#numbers.clear()
#print(4 in numbers)

numbers.pop(1)
del numbers[1:2] #[1,3,4,-1,0,-20,1] as 2 was removed by the previous pop, starting from 1 remove upto BUT NOT INC 2 = [1,4,-1,0,-20,1]
print(numbers)