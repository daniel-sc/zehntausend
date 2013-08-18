'''
Created on 18.08.2013

@author: SCHRED
'''
import zehntausendp.points
import zehntausendp.liststrategies
from fractions import Fraction
import time

class MyStrat(object):
    def choose(self, throw, noDice, currentPoints, totalPoints):
        #currentPoints are from this round but without this throw
        #noDice is the number if dice currently thrown
        #returns: ([action],stop)
        action=throw
        #print("action=3D"+str(throw))
        if zehntausendp.points.pointsforaction(action,throw)+currentPoints>=350 and zehntausendp.liststrategies.isstoppossible(throw,action,noDice):
            return (action, 1)
        else:
            return (action, 0)

def run():
    start=time.time()
    import zehntausendp.zehntausend
    import zehntausendp.throwprobabilities
    import zehntausendp.evalstrategy
    print("calculating throws..")
    allthrows=zehntausendp.zehntausend.allthrows()
    print("calculating probabilities..")
    probabilities=zehntausendp.throwprobabilities.allprobs(allthrows)
    pointsdist=zehntausendp.evalstrategy.evalstrategy(MyStrat(),probabilities)
    print("output:")
    l=list(pointsdist.keys())
    l.sort()
    for p in l:
        print(str(p).rjust(5)+'{0:.3f}%'.format(float(100*pointsdist[p])).rjust(9))
    total=sum(pointsdist.values())
    print('total: {0:.3f}%'.format(float(total*100)))
    average=sum([Fraction(p)*pointsdist[p] for p in l])
    print("average: "+str(float(average)))
    print("done.mystrat ({0:.2f}sec)".format(time.time()-start))
    
if __name__=="__main__":
    run()