def apriori(SETOFITEMS, minSup, minConf):
    FIRSTITEMSET = getItemSetFromList(SETOFITEMS)
   
    GBFS = dict()
   
    globalItemSetWithSup = defaultdict(int)

    ITEMSET = GET_MIN_SUPPORT(FIRSTITEMSET, SETOFITEMS, minSup, globalItemSetWithSup)
    CURRENTITEMSET = ITEMSET
    k = 2

    
    while(CURRENTITEMSET):
       
        GBFS[k-1] = CURRENTITEMSET
        
        candidateSet = UNION_GET(CURRENTITEMSET, k)
        
        candidateSet = PRUNING(candidateSet, CURRENTITEMSET, k-1)
        
        CURRENTITEMSET = GET_MIN_SUPPORT(candidateSet, SETOFITEMS, minSup, globalItemSetWithSup)
        k += 1

    rules = associationRule(GBFS, globalItemSetWithSup, minConf)
    rules.sort(key=lambda x: x[2])

    return GBFS, rules

SET_ITEM_FREQ, rules = apriori(SETOFITEMS, minSup=2, minConf=0.5)

def UNION_GET(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def PRUNING(candidateSet, prevFreqSet, length):
    TEMP_CAN = candidateSet.copy()
    for item in candidateSet:
        subsets = combinations(item, length)
        for subset in subsets:
            
            if(frozenset(subset) not in prevFreqSet):
                TEMP_CAN.remove(item)
                break
    return TEMP_CAN


def GET_MIN_SUPPORT(itemSet, SETOFITEMS, minSup, globalItemSetWithSup):
    SET_ITEM_FREQ = set()
    LOCALSUP = defaultdict(int)

    for item in itemSet:
        for itemSet in SETOFITEMS:
            if item.issubset(itemSet):
                globalItemSetWithSup[item] += 1
                LOCALSUP[item] += 1

    for item, supCount in LOCALSUP.items():
        support = float(supCount / len(SETOFITEMS))
        if(support >= minSup):
            SET_ITEM_FREQ.add(item)

    return SET_ITEM_FREQ


SETOFITEMS = [['l1', 'l2', 'l5'],
                ['l2', 'l4'],
                ['l2', 'l3'],
                ['l1', 'l2', 'l4'],
                ['l1', 'l3'],
                ['l2', 'l3'],
                 ['l1', 'l3'],
                  ['l1', 'l2','l3','l5'],
                   ['l1', 'l2','l3'],
                ]
SET_ITEM_FREQ, rules = apriori(SETOFITEMS, minSup=2, minConf=0.22)
print(SET_ITEM_FREQ)
print(rules)  
