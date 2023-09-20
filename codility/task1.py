import math
def task1():
    def task1code(A,B):
        list = [x for x in range(A,B+1)]
        num_integers = 0
        nums = []

        for i in list:
            sqrt_i = (int)(math.sqrt(i))
            num = sqrt_i * (sqrt_i + 1)
            
            if num == i:
                nums.append(num)
                num_integers += 1
        print(nums)
        return num_integers
    return task1code(1, 100)


#####
print(task1())

