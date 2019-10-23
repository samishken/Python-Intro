# # s=input()
# # print(s)
# # s=input("Enter your name: ")
# # print(s)
#
# i=int(input("Enter an integer number"))
# print(i)
# print(type(i))

# 1 Ask users to enter elements
# 2 those entered elements create an array called x
# 3 display that array called x as a list  - <class 'list'>
lst = [x for x in input("Enter three numbers separated by space: ").split()]
print(lst)
print(type(lst))

lst = [x for x in input("Enter three numbers separated by comma: ").split(',')]
print(lst)
print(type(lst))

lst = [float(x) for x in input("Enter three numbers separated by comma: ").split(',')]
print(lst)
print(type(lst))
