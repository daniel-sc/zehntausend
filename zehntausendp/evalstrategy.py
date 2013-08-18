'''
Created on 18.08.2013

@author: SCHRED
'''

import zehntausendp.points
import zehntausendp.liststrategies
from fractions import Fraction

def gotobrother(throws,enumThrows,probabilities):
    #goes to next brother node or if there is no, to parents brother and so on..
    #this is the backtrack step
    #if len(throws)==1:
    #    #print(str(throws))
    #    #print("throw:"+str(throws[0][0]))
    while len(throws)>0:
        last=throws.pop()
        #print("throw:"+str(last[0]))
        #print("enumThrows:\n"+"\n".join([str(x) for x in enumThrows[last[1]-1]]))
        i=enumThrows[last[1]-1].index(last[0])
        #if len(throws)==0:
        #    print("i="+str(i))
        if i+1<len(enumThrows[last[1]-1]):            
        #todo correct probability:
            throw=enumThrows[last[1]-1][i+1]
            if len(throws)>0:
                prob=throws[-1][3]*Fraction(probabilities[last[1]][throw],6**last[1])
            else:
                prob=Fraction(probabilities[6][throw],6**6)
            throws.append((throw,last[1],last[2],prob))
            return
    

def evalstrategy(strategy,probabilities):
    #input: strategy.choose(throw, noDice-1, currentPoints, totalPoints) : action
    #returns: point->probability
    print("init pointsdist..")
    pointsdist={}
    for i in range(350, 10000, 50):
        pointsdist[i]=Fraction(0,1)
    pointsdist[0]=Fraction(0,1)
    print("calculate points distribution..")
    enumThrows=[list(probabilities[x].keys()) for x in range(1,7)]
    #print("enumTrows-size="+str(len(enumThrows)))
    #print("throws with 6 dice:"+str(len(enumThrows[5])))
    throw=enumThrows[5][0]
    noDice=6
    currentPoints=0
    currentProb=Fraction(probabilities[6][throw],6**6)
    totalPoints=0
    #throws-format: (throw,noDice,currPoints,currProb)
    throws=[(throw,noDice,currentPoints,currentProb)]
    while len(throws)>0:
        #print(".o")
        #go to next node:
        throw=throws[-1][0]
        noDice=throws[-1][1]
        currentPoints=throws[-1][2]
        currentProb=throws[-1][3]
        if sum(throw)==0:
            pointsdist[0]+=currentProb
            #go to brother or parents brother
            gotobrother(throws,enumThrows,probabilities)
            continue
        action=strategy.choose(throw, noDice-1, currentPoints, totalPoints)
        pointsForAction=zehntausendp.points.pointsforaction(action[0],throw)
        if action[1]==1 or currentPoints+pointsForAction>=10000: #stop
            pointsdist[currentPoints+pointsForAction]+=currentProb
            #go to brother or parents brother
            gotobrother(throws,enumThrows,probabilities)
            continue
        #go to first child:
        remDice=zehntausendp.liststrategies.remainingdice(action,noDice)
        nextThrow=enumThrows[remDice-1][0]
        #print("nextThrow:"+str(nextThrow))
        #print("remainingdice="+str(remDice))
        throws.append((nextThrow,remDice,currentPoints+pointsForAction,currentProb*Fraction(probabilities[remDice][nextThrow],6**remDice)))
    return pointsdist
        
if __name__=="__main__":
    print("done.")