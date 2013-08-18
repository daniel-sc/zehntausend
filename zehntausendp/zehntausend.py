'''
Created on 18.08.2013

@author: SCHRED
'''
#returns a list of possible results for throwing noDice many dice. 
# the list elements have the following format:
# [street, 3pair-1, ..., 3pait-6, 6pair, fives, ones]
def listdice(noDice=6):
 result=[]
 #format [street, 3pair-1, ..., 3pait-6, 6pair, fives, ones]
 #street
 if noDice==6:
  result.append([1,0,0,0,0,0,0,0,0,0])
  #6pair
  for i in range(6):
   x=[0,0,0,0,0,0,0,0,0,0]
   x[-3]=1+i
   result.append(x)
  #two 3pair
  for i in range(6):
   x=[0,0,0,0,0,0,0,0,0,0]
   x[i+1]=1
   for j in range(6):
    if j!=i:
     y=list(x) # copy list
     y[j+1]=1
     if y not in result:
      result.append(y)
 #one 3pair plus ones and fifes
 if noDice>=3:
  for i in range(6):
   x=[0,0,0,0,0,0,0,0,0,0]
   x[i+1]=1
   appendonesandfives(result,x,noDice-3)
 #no 3pair - only ones and fifes
 appendonesandfives(result,[0,0,0,0,0,0,0,0,0,0],noDice)
 return result

#does not check if results are already in result! 
def appendonesandfives(result,basis,remainingdice):
 for ones in range(3):
  for fives in range(3):
   if ones+fives<=remainingdice:
    x=list(basis)
    x[-1]=ones
    x[-2]=fives
    result.append(x)
    
#returns an association of noDice -> listdice(noDice)
def allthrows():
 result={}
 for i in (1,2,3,4,5,6):
  result[i]=listdice(i)
 return result

if __name__=="__main__":
    '''import myprint'''
    #print(allthrows())
    total=0
    for i in (1,2,3,4,5,6):
     mydicelist=listdice(i)
     print(str(i)+" dice:")
     #print(myprint.printlist(mydicelist))
     print("no of elements: "+str(len(mydicelist)))
     total+=len(mydicelist)
    print("total possible throws: "+str(total))