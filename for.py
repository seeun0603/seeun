'''
test_list = ['one','two','three']
#for i in test_list:
for i in range(0,len(test_list)): -> range는 숫자를 가지고 있는 아이로 인덱싱이 필요
    print(test_list[i])
'''
'''
a = (1,2,3,4,5,6,7,8,9,10)
for i in a:
    if(i %2 !=0):
        print(i)
    else:
        continue
'''
'''
a='안녕하세요. 저는 누구입니다.'
b = a.split(' ')
for i in b:
    print(i)
'''
'''
sum = 0
for i in range(1,11,2):
    sum = sum + i
print(sum)
'''

# for i in range(2,10):
#     for j in range(1,10):
#         print(i,'*',j,'=',i*j)
#     print("\n")   

a='멋쟁이 사자처럼 화이팅 멋쟁이 사자'
b = a.split(' ')
dic={}

for i in b:
    if i in dic:
        dic[i]= dic[i]+1
    else:
        dic[i] =1
print(dic)