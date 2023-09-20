########## TASK 3 ############

def task3():
    def task3code(N):
        tempN = N
        negative = False
        if N < 0:
            negative = True
            tempN *= -1
        strN = str(tempN)
        variations = []
        positions = [i for i, ltr in enumerate(strN) if ltr == '5']
        
        for i in positions:
            if i == len(strN)-1:
                varN = (int)(strN[:i])
            else:
                varN = (int)(strN[:i]+strN[i+1:])
            if negative:
                varN *= -1
            variations.append(varN)

        print(variations)    
        return max(variations)


    return task3code(-1545)



##############
print(task3())