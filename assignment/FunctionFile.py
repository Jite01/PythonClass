def largest_element(array: list)->int:
	largest = array[0]
	for i in array:
		if largest < i:
			largest = i
	return largest


stuff = [191, 78, 90, 6, 3]
print(f"The largest element in the array is ",largest_element(stuff))


def list_reversal(array: list)-> list:
	arrayCopy = []
	for i in range(0, len(array)):
		arrayCopy.append(array[(len(array)- 1) - i])
	return arrayCopy

stuff = [191, 78, 90, 6, 3]
print(f"The reverse list is ",list_reversal(stuff))


def element_finder(array: list, element: int)->str:
	for i in range(0, (len(array))):
		if element == array[i]:
			print(element, " found")
			return True
	print(element, "not found")
	return False

stuff = [18, 78, 90, 6, 3]
element = 76
element_finder(stuff, element)

			
def odd_indices_print_function(array: list)->list:
	odd_array = []
	for i in range (1, (len(array)), 2):
		odd_array.append(array[i])
	return odd_array

stuff = [191, 78, 90, 6, 3]
print("The odd indices are ",odd_indices_print_function(stuff))

def even_indices_print_function(array: list)->list:
	even_array = []
	for i in range (2, (len(array)), 2):
		even_array.append(array[i])
	return even_array

stuff = [191, 78, 90, 6, 3]
print("The even indices are ",even_indices_print_function(stuff))


def list_running_total(array: list)->int:
	total = 0
	for i in range(0, (len(array))):
		total += array[i]
	return total

stuff = [191, 78, 90, 6, 3]
print("The running total is",list_running_total(stuff))
	
def palindrome_check_function(string_input: str)->bool:
	clinch = (len(string_input) - 1) // 2
	str1 = string_input[0: clinch]
	str2 = string_input[(len(string_input) - 1):((len(string_input) - 1) - clinch) :-1]
	if str1 == str2:
		print(string_input,"is a palindrome")
		return True
	print(string_input,"is not a palindrome")
	print(str1, str2)
	return False

stuff = "madam"
palindrome_check_function(stuff)



 

	
	
	
	