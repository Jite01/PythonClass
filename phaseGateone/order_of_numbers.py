print('Enter First number:')  
value1 = int(input())

print('Enter Second number:')  
value2 = int(input())

print('Enter Third number:')  
value3 = int(input())

value1_counter = 0
value2_counter = 0
value3_counter = 0


list = []
list.append(value1)
list.append(value2)
list.append(value3)


for number in list:
	if value1 > number:
		value1_counter += 1
	

for number in list:
	if value2 > number:
		value2_counter += 1

for number in list:
	if value3 > number:
		value3_counter += 1

if value1_counter == 1:
	least = value1
if value1_counter == 2:
	middle = value1
if value1_counter == 3:
	largest = value1

if value2_counter == 1:
	least = value2
if value2_counter == 2:
	middle = value2
if value2_counter == 3:
	largest = value2

if value3_counter == 1:
	least = value3
if value3_counter == 2:
	middle = value3
if value3_counter == 3:
	largest = value3

print(least, middle, largest)


