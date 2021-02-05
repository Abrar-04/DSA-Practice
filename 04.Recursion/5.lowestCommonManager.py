# based on tree : 
# check book/video


#main driver
def getLowestCommonManager(topManager,reportOne,reportTwo):
    return getOrgInfo(topManager,reportOne,reportTwo).LowestCommonManager


def getOrgInfo(manager,reportOne,reportTwo):
    #manager is any node
    #.directReport is predefined as its childNodes

    numImportantReports=0 #init 0
    for directReports in manager.directReports:

        # Recursive call to this method for every child
        # of every manager node to identify the reportOne,reportTwo
        orgInfo=getOrgInfo(directReports,reportOne,reportTwo)


        if orgInfo.LowestCommonManager is not None: # keep going to next manager node if R1,R2 not found
            return orgInfo
        
        numImportantReports+=orgInfo.numImportantReports #the whole manager subtree if there is R1,R2


    
    if manager== reportOne or manager==reportTwo: 
        numImportantReports+=1 # increase if R1 or R2 is found as the manager node itslef
        LowestCommonManager=manager if numImportantReports==2 else None # return LowestCommonManager if both found

    return orgInfo(LowestCommonManager,numImportantReports)



class ORGINFO:
    def __init__(self,LowestCommonManager,numImportantReports):
        self.LowestCommonManager=LowestCommonManager
        self.numImportantReports=numImportantReports