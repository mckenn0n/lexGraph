import re
import numpy as np
import matplotlib.pyplot as plot


print('This is "The EmotionalBobcat\'s" second chalange!')

userIn=input("What is the name of your file:" )
common=[]
inLex=0
nInLex=0
count=0
datFile= open(userIn,"r", encoding='utf-8')
file= open("common.txt","r", encoding='utf-8')
for line in file:
	common.append(line.strip())
common.append('')
common.append(' ')
common.append('i')
string= datFile.read().lower()
newList= re.split(r"[^'\w-]|--|- ", string)
newNewList = [y for y in newList if y not in common]
dic={}
for word in newNewList:
	if word not in dic:
		dic[word]=1
	else:
		dic[word]+=1
	count+=1
otherFile = open("sent_lexicon.csv","r", encoding='utf-8')
otherList=[]
for line in otherFile:
	otherList.append(line.strip())
secondDic={}
for item in otherList:
	temp = item.split(',')
	secondDic[temp[0]]=float(temp[1])
neg=0	
kindaN=0
nutr=0
kindaP=0
pos=0
for things in dic:
	if things not in secondDic:
		continue
	elif secondDic[things] <= -.6:
		neg+=dic[things]
	elif secondDic[things] <= -.2:
		kindaN+=dic[things]
	elif secondDic[things] <= .2:
		nutr+=dic[things]
	elif secondDic[things] <= .6:
		kindaP+=dic[things]
	else:
		pos+=dic[things]
List=[]

jim=sorted(dic,key=dic.get,reverse=False)
for word in dic:
	if word not in secondDic:
		nInLex+=dic[word]
	else:
		inLex+=dic[word]
		dic[word]=dic[word]*secondDic[word]
		#print(word ," = ", dic[word])
for words in newNewList:
	if words in secondDic:
		List.append(float(secondDic[words]))
means=np.mean(List)
vares=np.var(List)
STD=np.std(List)
print("Mean Sentiment Score: ", means)
print("Variance: ", vares)
print("Standard Deviation: ", STD)
print("Total Words: ",count)
print("Words Found in Lexicon: ",inLex)
print("Words Not in Lexicon: ",nInLex)
plot.title("Sentiment Distribution for "+userIn+".txt")
xlabels=["Negative", "Weak Negative", "Neutral", "Weak Positive", "Positive"]
plot.xlabel("Sentiment")
plot.ylabel("Percent of Words")
plot.bar([0.1,1.1,2.1,3.1,4.1], [neg/inLex,kindaN/inLex,nutr/inLex,kindaP/inLex,pos/inLex], color="green")
#plot.axis([0, 5, 0.00, 0.35])
plot.xticks([0.5,1.5,2.5,3.5,4.5],xlabels)
plot.show()
	#r"[^'\w-]|--"