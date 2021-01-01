ex=list('adssa')
print ex
ex[3:] = list('bumsd')
print ex
ex[4:] = list('dasdsadas')
print ex
ex2=[1,2,3]
ex2[1:1]=[2,4,1]#doesn't delete anthing
print ex2
ex2[1:3]=[3,43,1]#deletes 2 elements
print ex2
ex2[1:4]=[]#delete 1,2,3
print ex2
