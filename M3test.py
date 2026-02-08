# minutes = 120
# hours = minutes // 60
# mins = minutes%60
# print(f"{minutes} minutes is {hours} hours and {mins} minutes")

# #prime check
# num = 12

# if(num%2==0 and num%3==0):
#     print(f"{num} is divisible by both 2 and 3!")


# x = 8
# y = 8
# if x == y:
#     print(f'{x} and {y} are equal')
# else:
#     if x < y:
#         print(f'{x} is less than {y}')
#     else:
#         print(f'{x} is greater than {y}')




# import time
# def countdown(n):
#     time.sleep(0.5)
#     if n <= 0:
#         print('**BOOM**')
#     else:
#         print(n)
#         countdown(n-1)

# countdown(10)

# text = input("type text\n")

# print(text)

# import math
# def area(radius):
#     a = math.pi * radius**2
#     return a

# print(area(3))

# def compare(x,y):
#     if x<y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1
    
# print(compare(11,10))

# def isbetween(x,y,z):
#     if x<=y<=z:
#         return True
#     else:
#         return False

# print(isbetween(1,3,2))        


numbers = [3, 5, 7, 9]
for i in numbers:
  if i == 7:
    print("Found!")