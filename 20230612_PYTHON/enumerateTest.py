a = ["a1",'b2','c3']
print("=====================")
for i in range(len(a)):
    print("i : ",i,a[i])

print("=====================")
j=0
for v in a:
    print("j : ",j,v)
    j += 1
print("=====================")
for k,v in enumerate(a):
    print("k : ",k,v)
print("=====================")

