import random

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def chooseNum():
    num1 = random.choice(list1)
    if num1 in [11,12,13]:
        num1 = 10
    if num1 == 1:
        num1 = 11
    return num1


list2 = []
i = 0
while i < 2:
    num1 = chooseNum()
    i = i + 1
    list2.append(num1)

print('Your cards: ',list2)
sum = 0
for num in  list2:
    sum = sum + num
print('Total sum: ', sum)
while True:
    choice = input('You want to continue ? Y or N ')

    if choice == 'Y' or choice == 'y':
        num1 = chooseNum()
        print('Number we got: ', num1)
        sum = sum + num1
        list2.append(num1)
        if sum > 21:
            if 11 in list2:
                sum = sum - 10
                list2.remove(11)
                list2.append(1)
            else:
                print('Your cards: ',list2)
                print('Total sum: ', sum)
                print('You lose')
                break
    else:
        break

    print('Your cards: ',list2)
    print('Total sum: ', sum)
    
user_sum = sum

# for computer

if user_sum <= 21:
    list2 = []
    num1 = chooseNum()
    print('Computer 1st number: ', num1)
    list2.append(num1)
    sum = num1
    while sum <= 17:
        num1 = chooseNum()
        print('Computer number: ', num1)
        sum = sum + num1
        list2.append(num1)
        if sum > 21:
            if 11 in list2:
                sum = sum - 10
                list2.remove(11)
                list2.append(1)
            else:
                print('Computer cards: ',list2)
                print('Computer Total sum: ', sum)
                print('Computer lose')
                break

        print('Computer cards: ',list2)
        print('Computer Total sum: ', sum)

    computer_sum = sum    
    
    if computer_sum < 21:
        if user_sum > computer_sum:
            print('You win')
        elif user_sum < computer_sum:
            print('Computer wins')
        else:
            print('Draw')