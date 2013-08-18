'''
Created on 18.08.2013

@author: SCHRED
'''

'''def prob(throw,noDice):
    #street
    if throw[0]==1:
        return float(math.factorial(5))/6**5 #= math.factorial(6)/6**6
    #6pair
    if throw[7]>0:
        return 1.0/6**5 #=6/6^6
    #two 3pair
    if sum(throw[1:7])==2:
        return #=(6*combin(6;3)*5)/6^6
    #todo'''
    
def allprobs(allthrows):
#input: noDice->throws
#reurns: noDice->throw->count
    result={}
    for noDice in allthrows.keys():
        result[noDice]={}
        for throw in allthrows[noDice]:
            result[noDice][tuple(throw)]=0
        i=0
        current=[1 for x in range(noDice)]
        #store
        result[noDice][throwfordice(current)]+=1
        while i<noDice:     
            if current[i]<6:
                current[i]+=1
                i=0
                #store
                result[noDice][throwfordice(current)]+=1
            else:
                current[i]=1
                i+=1
    return result
        
def throwfordice(dice):
    #print(dice)
    #input: [valuefirstdice, ..., valueoflastdice]
    #output: throw in known format
    result = [0 for i in range(10)]
    dicedist = [0 for i in range(6)]
    for d in dice:
        dicedist[d-1]+=1
    if dicedist==[1,1,1,1,1,1]:
        result[0]=1
        #print(result)
        return tuple(result)
    if 6 in dicedist:
        result[7]=dicedist.index(6)+1
        #print(result)
        return tuple(result)
    for index, value in enumerate(dicedist):
        if value>=3:
            result[index+1]=1
    result[8]=dicedist[4]%3
    result[9]=dicedist[0]%3
    #print(result)
    return tuple(result)
    
if __name__=="__main__":
    import zehntausendp. zehntausend
    print("calculating throws..")
    allthrows=zehntausendp.zehntausend.allthrows()
    print("calculating probabilities..")
    result=allprobs(allthrows)
    print("output:")
    for noDice in result.keys():
        print(str(noDice)+" dice:")
        for throw in result[noDice].keys():
            print("["+",".join([str(x) for x in throw])+']{0:.3f}%'.format(float(result[noDice][throw]*100)/6**noDice).rjust(6))
        total=float(sum(result[noDice].values()))/6**noDice
        print("total="+str(total))