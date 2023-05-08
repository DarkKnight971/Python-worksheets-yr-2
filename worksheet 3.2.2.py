'''1. Write a Python class to find a pair of elements (indices
      of the two numbers) from a given array whose sum equals
      a specific target number.'''

class checkSum:  
    def __init__(self, array, target):  
        self.array = array  
        self.target = target  
          
    def solution(self):  
        l = len(list1)  
          
        for i in range(l - 1):  
            for j in range(i+1, l):  
                if array[i] + array[j] == self.target:  
                    new_list = i, j  
                    return list(new_list)  
        return -1  
  
def main():
    list = [1, 2, 4, 5, 11]  
    t = 6  
    obj = checkSum(list, t)  
    print(obj.solution())
  
if __name__ == "__main__" :
    main()
