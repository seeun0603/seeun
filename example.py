#print("Hello")

#a = 1
#b = 2
#print(a+b)
#print(a-b)
#print(a*b)
#print(a**b)
#print(a/b) 몫+나머지
#print(a//b) 몫
#print(a%b) 나머지

# a = input('입력:')
# print(a)

# my_list =[1, 2, 3]
# print(my_list)

# for m in my_list:
#     print(m)

# a = [1,2,3]
# print(a[2])
# print('-'*30)
# for b in a:
#     print(b)
# print(a[0:2])

# sum=0

# for i in range(3,11):
#     sum=sum+i
# print(sum)

# marks = [90, 25, 67, 45, 80]
# for number in range(1,len(marks)):
#     print("%d번 학생 축하합니다." % (number+1))

'''
a =(1,2,3)
print(a[1])
#a[1] =10 -> 튜플이라서 고치면 에러...
print(a[1])
print('-'*30)
for b in a:
    print(b)
'''

# for i in range(2,10):
#     for j in range(1,10):
#         print(i,'*',j,'=',i*j)
#     print("\n")   

'''
my_dict ={1:'자동차',2:'냉장고',3:'휴대폰'}

print(my_dict)
print('-'*30)
for i in my_dict:
    print(i) #key값이 출력된다
print('-'*30)
for i in my_dict: 
    print(my_dict[i],end='') #value값을 출력된다
'''
a='1 2 3 4 5 6 7 8 9 10'
b = a.split(' ')
for i in b:
    print(i)
