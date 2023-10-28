#with open('csv/python_data1.csv') as data_file:
#    data = data_file.readlines()
#    print(data)

import csv
with open('csv/python_data1.csv') as data_file:
    data = csv.reader(data_file)
    print(data)
    print()
    temperature = []
    for row in data:
        print(row)
        if row[1] != 'temp':
            temperature.append(row[1])
    
    print()
    print(temperature)

file_to_output = open('csv/python_data2.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()

'''
import pandas
data = pandas.read_csv('csv/python_data1.csv')
print(type(data))
print(data)

data_dict = data.to_dict()
print(data_dict)

data_list = data['temp'].to_list()
print(data_list)
print(len(data_list))

avg = sum(data_list) / len(data_list)
print(avg)

# above is same as
print(data['temp'].mean())

print(data['temp'].max())

print(data['condition'])
#print(data.condition)

print(data[data.day == 'Monday'])
'''