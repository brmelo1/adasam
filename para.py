# a=[]

# for i in range(3):
#     num=float(input(f'manda a nota {i+1}: '))
#     a.append(num)


# for i,a in a:
#     print(f'nota {i+1}= {a}')

li=[1,5,6,2]
a=[1,2,3]
print(li[-1:])
li.insert(2,40)
print(li)
li.extend(a)
print(li)
li.remove(1)
print(li)
li.pop(1)
print(li)
print(li.count(2))
li.sort()
print(len(li))
print(sum(li))
print(max(li))
print(min(li))
