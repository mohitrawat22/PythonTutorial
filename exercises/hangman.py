import random
import functools

list1 = ["worldw", "earthe", "planetsp"]
choosen_word = random.choice(list1)
print(choosen_word)
list2 = ['_']*len(choosen_word)
print(list2)

lives_left = 6
while '_' in list2 and lives_left > 0:
    user_input = input("Enter the character: ")
    list3 = []
    start_index = 0
    found_index = False
    while True:
        index = choosen_word.find(user_input, start_index)
        print(f'index is: {index}')
        if index == -1:
            break
        else:
            list3.append(index)
            start_index = index + 1
            found_index = True

    if found_index == False:
            lives_left = lives_left - 1

    if len(list3) > 0:
        for i in list3:
            list2[i] = user_input

    print(list2, f', lives left: {lives_left}')

word = functools.reduce(lambda x,y: x+y, list2)
print(word)