

def partInsert(partsCount,marksDict):
    for i in range(1,partsCount+1):
        marksDict[f"part{i}"]={}


def markInsert(partsCount,marksDict):
    for i in range(1,partsCount+1):
        max=int(input("how many subjects are in this part:"))
        for j in range(1,max+1):
            mark=int(input(f"Enter the mark{j}"))
            marksDict[f"part{i}"][f"mark{j}"]=mark


def main():
    marksDict={
    
    }

    semester=int(input("Enter the semester:"))
    marksDict["semester"]=semester

    partsCount=int(input("Enter the count of parts:"))

    partInsert(partsCount,marksDict)
    markInsert(partsCount,marksDict)

    print(marksDict)

main()