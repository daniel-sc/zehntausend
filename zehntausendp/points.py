'''
Created on 18.08.2013

@author: SCHRED
'''
#assumes a 5 is counted as 100, if a 5 remains
def pointsforaction(action, throw):
 #street
 if action[0]==1:
  return 1500
 #6pair
 if action[7]>0:
  if action[7]==1:
   return 2000
  else:
   return action[7]*2*100
 #rest
 result=0
 #3pair-1:
 if action[1]==1:
     result+=1000
 #3pair-other:
 for i in (2,3,4,5,6):
  result+=100*action[i]
 #fives:
 result+=action[8]*50
 if action[8]==1 and throw[8]==2:
  result+=50
 #ones:
 result+=action[9]*100
 return result
 
'''print("asf")
import sciphy
print(str(sciphy.misc.comb(6,3)))'''