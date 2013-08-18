'''
Created on 18.08.2013

@author: SCHRED
'''
import zehntausendp.zehntausend

#returns a hashmap associating noDice to throws to actions
# a action has the same format as a throw plus an additional element for stopping (0=continue, 1=stop)
def liststrategies():
    result={}
    throws=zehntausendp.zehntausend.allthrows()
    for noDice in throws.keys():
        result[noDice]={}
        for throw in throws[noDice]:
            result[noDice][tuple(throw)]=getmoves(throw,noDice)
    return result
    
def getmoves(throw, noDice):
    result=[]
    #max=[1,2,2,2,2,2,2,1,2,2]
    i=0
    current=[0,0,0,0,0,0,0,0,0,0,0]
    while i<len(throw):
        if current[i]<throw[i]:
            current[i]+=1
            i=0
            #add to result: (stop/continue as possible)
            current[-1]=0
            result.append(list(current))
            if isstoppossible(throw, current, noDice):
                current[-1]=1
                result.append(list(current))
        else:
            current[i]=0
            i+=1
    return result
    
def isstoppossible(throw, current, noDice):
    for i in range(len(throw)):
        if current[i]<throw[i]:
            return 0
    if throw[0]*6+sum(throw[1:7])*3+throw[7]*6+sum(throw[8:10])==noDice:
        return 0
    return 1
    
def remainingdice(action, noDice):
    result=noDice
    if action[0][0]==1 or action[0][7]>0:
        return 6
    result-=sum(action[0][1:7])*3
    result-=sum(action[0][8:10])
    if result==0:
        return 6
    return result
    
if __name__=="__main__":
    #output
    allstratsperthrow=liststrategies()
    '''import pickle
    f=open("allthrowstrats.txt","wb")
    pickle.dump(allstratsperthrow,f)
    f.close()'''
    for i in list(allstratsperthrow.keys()):
        print(str(i)+" dice:")
        for j in list(allstratsperthrow[i].keys()):
            print(">["+",".join(str(x) for x in j)+"]")
            for s in allstratsperthrow[i][j]:
                print("  ["+",".join(str(x) for x in s)+"]= ")#+str(points.pointsforaction(s,j)))
                #pass