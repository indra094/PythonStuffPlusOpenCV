ij2="Stay focused bruv. Gurls gonna %s and go. You gotta ensure you don't give them any %s."
fillers=('cum','time')
print (ij2 % fillers)

print ((ij2 % fillers).find('cum'))

sep = 'hoss'

seq=['qwewq','sdfds','rter','wqewq','wut']
print (seq)
glue='_'
print (glue.join(seq))

randstr="I wew wew asdA Grge jij"
print (randstr)
print ("Bpp")

print (randstr.lower())

truth = "O wqewq boom boom"
print (truth.replace('wqewq', 'say'))

#dictionary
dict={'dad':'Bobby boy', 'mom':22, 'bro':'sadio'}
print (dict)

print (dict['dad'])
print (dict['mom'])

dict2=dict.copy()

dict.clear()
print (dict, dict2)

#hashkey deprecated in 3.x python use in
res = 'de' in dict2
print ('dad' in dict2)
#dict2.has_key('dad')
res2=True
if res2==False:
    print ("nup")
    print ("no again")
elif res:
    print ("de not in dict2")
else:
    print ("yolo")

name='charlie'
thing="haas"

if thing=='haas':
    if (name=="choyu"):
        print ('adsadas')
    else:
        print ("charlie haas")
else:
    print ("fi")

print (10>2)

l1 = [2,4,2]
l2 = [1,4,2]
print (l1==l2)
l2[0]=2
print (l1 is l2 , l1==l2, 'w' in 'wus')
cond2="pus"<"wus"
cond1="sus">"lolsdasd"
if cond1 and cond2:
    print ("booomchicka")
else:
    print ("zoom")

cond3=1==2
if cond1 or cond3:
    print ("atlest one corrent")

#loops
b=1
while b<=10:
    print (b)
    b+=1

l1

for var in l1:

    print (var)

def watsname(nm='broly',prn=3):
    while 1:
        name = input("Enter"+nm)
        if name==nm:
            while prn>=1:
                print ("correctname madafaka")
                prn-=1
            break

name = input("enter ref name")
cnt=input("enter count")
print (cnt)
if (not name):
    watsname()
elif not cnt:
    print("in not cnt")
    watsname(prn=10)

def mul(num,pow):
    cnt = 1
    while cnt<pow:
        num +=num
        cnt+=1
    print (num)

mul(6,3)

#unlimited params in func
def multra(name, *list):
    print (list)
    print (name)

multra("bobby",4,'sadio')

def multraDict(**dict):
    print (dict)

multraDict(apps=1)

#tuples immutable v list
def ex(a,b,c):
    print (a+b+c)
t1=(1,2,4)
ex(*t1)

#@understand this dude
def ex2(**dict):
    print (dict)
d1={'a':3,'b':5}
ex2(**d1)

class exampleSaiyan:
    eyes="blue"
    age=26
    hair=2
    def canSuperSaiyan(self, name):
        self.name=name
        return 'hey can go ss'
    def dispName(self):
        print (self.name)
    def sayin(self):
        print ("heyyo %s" % self.name)
print (exampleSaiyan)

exSaiyan=exampleSaiyan()
eS2 = exampleSaiyan()
print (exSaiyan.eyes)
print (exSaiyan.hair)
print (exSaiyan.canSuperSaiyan('broly'))
print(eS2.canSuperSaiyan('xicor'))
print (exSaiyan.dispName())#return none in outer print
eS2.sayin()

class parentClass:
    var1="im var1"
    var2="im var2"

class childClass(parentClass):
    pass#don't do anything wrt what to inherit and what not to-inherit all

parentObject=parentClass()
print (parentObject.var1)

childObj=childClass()
print (childObj.var1)
print (childObj.var2)

class par:
    var1="bacon"
    var2="sausage"

class child(par):
    var2="toast"
pob=par()
cob=child()
print (pob.var1)
print (pob.var2)

print (cob.var1)
print (cob.var2)

class multiChild(par, exampleSaiyan):
    var3="im a new var"

cobj=multiChild()
print (cobj.var1)
print (cobj.eyes)
