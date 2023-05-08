'''1. Write a Python class to find a pair of elements (indices
      of the two numbers) from a given array whose sum equals
      a specific target number.'''

class checkSum:  
    def __init__(self, list1, target, length):  
        self.list1 = list1  
        self.target = target
        self.length = length
          
    def solution(self):  
        for i in range(length - 1):  
            for j in range(i + 1, length):  
                if list1[i] + list1[j] == self.target:  
                    new_list = i, j  
                    return list(new_list)  
        return -1  

if __name__ == "__main__" :
    list1 = []
    length = int(input("Enter length of array : "))
    t = length
    while t > 0 :
        l = int(input("Enter array element : "))
        list1.append(l)
        t -= 1
    
    target = int(input("Enter target number : "))
    obj = checkSum(list1, target, length)
    print(obj.solution())
