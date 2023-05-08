#4. Python program to implement selection sort.

def main() :
	data = []
	n = int(input("Enter size of array : "))
	t = n
	
	while t > 0 :
		d = int(input("Enter an integer : "))
		data.append(d)
		t -= 1
	
	insertionSort(data, n)
	print('Sorted Array in Ascending Order:')
	print(data)

def insertionSort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
		
        while (j >= 0) and (key < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key

if __name__ == '__main__' :
	main()
