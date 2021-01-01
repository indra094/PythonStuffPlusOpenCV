class Covid:
    def isPositive(self):
        print ("is covid+ve")

obj = Covid()
print (obj.isPositive())

class new:
    def __init__(self):
        print ("this is constr")
        print ("in __init__ def constr")

newObjec=new()

import covid
covid.testMod()
# importing again in the same IDLE shell will make no differece
# regardless of the changes in the module except for reload

baby=covid.testMod
baby()

input()
#make changes to module
#covid.reload(testMod)-doesnt work rn for 3.9pythin needs library and stuff
import covid
baby()
covid.testMod()

import math
print (math.sqrt(89))

print (dir(math))#find what info a module contains
help(math)

print (math.__doc__)#summarize, already in dir()

#file stuff
fob=open('C:\\Users\indra094\Documents\scripts\sample.txt','w')
fob.write('boom masalalalalalala land')
fob.close()

fob=open('C:\\Users\indra094\Documents\scripts\_lookAway.bat','r')
print (fob.read(10))
print (fob.read())
fob.close()

fob=open('C:\\Users\indra094\Documents\scripts\_lookAway.bat','r')
print (fob.read())
fob.close()

fob=open('C:\\Users\indra094\Documents\scripts\TimeSaverCommands.txt','r')
print (fob.readline())

print (fob.readlines())#returns as a list
fob.close()

fob=open('C:\\Users\indra094\Documents\scripts\sample.txt','w')
fob.write('Im inserting more shit into this file.\noh yeah yeah\n oh yeah yeah yeah yeah.\n')
fob.close()

fob=open('C:\\Users\indra094\Documents\scripts\TimeSaverCommands.txt','r')
list=fob.readlines()
print (list)
fob.close()

list[2]="hey vegeta nice shrit"
print (list)

fob=open('C:\\Users\indra094\Documents\scripts\sample.txt','w')
fob.writelines(list)#no writeline
fob.close()
