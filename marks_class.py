
class marks:
    marksDict={
    
    }
    '''
    Get the count of parts from user
    Creating the dictionary for the parts
    and return the count of the parts
    '''
    def partInsert(semester,marksDict):
        partsCount=int(input("Enter the count of parts:"))
        for i in range(1,partsCount+1):
            marksDict[f"semester_{semester}"][f"part_{i}"]={}
        return partsCount

    '''
    get the count of subjects for the particular part
    get the mark and insert
    get the credit and insert
    create the grade key with none value for later use
    '''

    def markInsert(semester,marksDict):
        partsCount=len(marksDict[f'semester_{semester}'])
        for i in range(1,partsCount+1):
            numberOfSubjects=int(input("how many subjects are in this part:"))
            mark=[]
            credit=[]
            for j in range(1,numberOfSubjects+1):
                mark.append(int(input(f"Enter the mark{j}:")))
                credit.append(int(input(f"Enter the credits{j}:")))
            marksDict[f"semester_{semester}"][f"part_{i}"]["Subject Count"]=numberOfSubjects    
            marksDict[f"semester_{semester}"][f"part_{i}"]["marks"]=mark
            marksDict[f"semester_{semester}"][f"part_{i}"]["credits"]=credit
            
                       
