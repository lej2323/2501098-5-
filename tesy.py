#----------------25

keys = input('키 alpha,delta를 꼭 포함해주세요!!!!: ').split()
values = input().split()

a = dict(zip(keys, values))
del a['alpha']
del a['delta']
print(a)

#-----------26

park ={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}

print('전체 점수는여: ', park)
print('영어점수 : ',park['english'], '/', '과학 점수 :', park['science'])


#-------------27

kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}

kim['korean']=100
kim['english']=100
kim['mathematics']=100
kim['science']=100

print(kim)

#27-1(다른 방식)

# kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}

# for i in kim:
#     kim[i] = 100
# print(kim)

#------------28

lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
if 'english' in lee:
    del lee['english']

print(lee)

# 28-1

# lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}

# x = {key: value for key, value in lee.items()if key !='english'}
# print(x)

# ------------29

lim={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
for keys, values in lim.items():
    print('과목과 점수를 모두 출력 : ', keys, values)

# 29-1(다른방식)

# lim={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
# x ={keys: values for keys, values in lim.items()}
# print(x)

#----------30

choi ={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
x = {key for key, value in choi.items() if value >= 90}
print('90점 이상인 과목 :', x)

# 30-1(다른방법~)
# choi ={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
# for key, value in choi.items():
#     if value >= 90:
#         print(key)

#---------- 31

yoo ={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
x = {value for key, value in yoo.items()}
print('평균은 :', sum(x)/len(yoo))

# 31-1
# yoo ={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
# total = 0
# for keys, values in yoo.items():
#     total += values
# print(total/len(yoo))

#31-2
# yoo ={'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}

# print(sum(yoo.values())/len(yoo))