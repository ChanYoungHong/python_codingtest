array = [3, 5, 1, 2, 4]
sum = 0

for x in array:
    sum += x

print(sum)

for i in array:
    for j in array:
        temp = i*j
        print(temp)

a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

a = 1e9
print(a)

a = 0.3 + 0.6
print(a)

a = 5
b = 3
print(a ** b)

a = [1,2,3,4,5,6,7,8,9]
print(a)

print(a[3])

n = 10
a = [100] * n
print(a)

a = [4,3,2,1]

a.reverse()
print(a)

# 특정 인덱스에 데이터 추가
# 인덱스 2에 3 추
a.insert(2, 3)
print(a)

b = [1,2,3,3,3,4,5,6,6,6,6]
print(b.count(6))

b.remove(1)
b.remove(2)
print(b)

