'''
.) Programs creats a list of dices
.) ProbailityInfo is used to keep track of the positions of dices
   which will be used to re rolled in future
.) probability contais the list of probanilities

'''
from decimal import Decimal
from random import randint
import sys 

j,k=0,0
dices,ProbabilityInfo,probaility=[],[],[]

for i in range(3):
	dices.append(int(sys.argv[i+1]))

def roll_one(x):
	return (6-x)/float(6)

def roll_two(x,y):
	return ((6-x)/float(6))*((6-y)/float(6))

def roll_three(x,y,z):
	return (6-x)/float(6)*(6-y)/float(6)*(6-z)/float(6)
		

if dices[0]==dices[1]==dices[2]:
	print "Its a yahtzee!!\nNo dice needs to be re-rolled\nScore:25"
	exit()
else:
	for i in range(3):
		if dices[i]==dices[(i+1)%3]:                                          #If two dices have same value
			k=1
			ProbabilityInfo.append([(i+2)%3])
			probaility.append(roll_one(dices[(i+2)%3]))
			ProbabilityInfo.append([(i+1)%3,(i+2)%3])
			probaility.append(roll_two(dices[(i+1)%3],dices[(i+2)%3]))
			ProbabilityInfo.append([i,(i+1)%3])
			probaility.append(roll_two(dices[i],dices[(i+1)%3]))
			ProbabilityInfo.append([i,(i+1)%3,(i+2)%3])
			probaility.append(roll_three(dices[i],dices[(i+1)%3],dices[(i+2)%3]))
if k!=1:
	for i in range(7):
		if i<3:
			ProbabilityInfo.append([i])
			probaility.append(roll_one(dices[(i)]))
		elif i<6:
			ProbabilityInfo.append([j,(j+1)%3])
			probaility.append(roll_two(dices[j],dices[(j+1)%3]))
			j=j+1
		else:
			ProbabilityInfo.append([0,1,2])
			probaility.append(roll_three(dices[0],dices[1],dices[2]))


for i in range(len(ProbabilityInfo)):
	print "Position=%s Probability=%f"%(ProbabilityInfo[i],probaility[i])

MaxProbablityPosition=probaility.index(max(probaility))                     

if max(probaility)>0.33333333:                                               # Setting a Threshold for probability                                       
	print "\n%d dice can be re-rolled\n"%len(ProbabilityInfo[MaxProbablityPosition])
	for i in ProbabilityInfo[MaxProbablityPosition]:
		print "dice number %d" % (i+1)

	for i in ProbabilityInfo[MaxProbablityPosition]:
		dices[i]=randint(0,6)

	print "New Roll:%s"%(dices)
	if dices[0]==dices[1]==dices[2]:
		print "Its a yahtzee!!\nNo dice needs to be rolled\nScore:25"
	else:
		print "Score:%d" % (dices[0]+dices[1]+dices[2])
else:
	print "\nRe rolling not required, less gain probability\n"
	print "Score:%d" % (dices[0]+dices[1]+dices[2])


