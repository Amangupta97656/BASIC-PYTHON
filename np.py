import numpy as np

a=np.array([(1,2,3),(4,5,6)])
b=np.array([(6,5,4),(9,7,6)])

print(a)

print(a.ndim)
print(a.max())
print(a.min())
print(a.sum())

print(np.sqrt(a))
print(np.std(a))
print("_________________________________________________________")



print(a+b)
print(a-b)
print(a*b)
print(a/b)


print(a.ravel())
