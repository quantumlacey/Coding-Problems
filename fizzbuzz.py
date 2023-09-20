

# def nameSort(names):
#     names.sort(key=lambda x: (x[0], x[2]))
#     print(names)
#     return names


# # names = [["bharath", "Ku", 30],["Kumar", "bu", 30], ["Bharath","MU",20], ["Kumar","NU",10],["Kumar","SU",20],["Bharath","Pu",10]]

# # sortedNames = nameSort(names)
# # print(sortedNames)



def FizzBuzz(low,high):
    for i in range(low,high+1):
        num = ""
        if (i % 3 != 0) and (i % 5 != 0):
            print(i)
        else:
            if i % 3 == 0:
                num += "Fizz"
            if i % 5 == 0:
                num += "Buzz"
            print(num)
    return

FizzBuzz(2,30)