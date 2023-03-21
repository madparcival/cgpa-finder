
class calculations:
    
    def calculateGPA(marksDict,semester):
        for i in marksDict[f"semester_{semester}"]:
            lengthOfPart=len(marksDict[f"semester_{semester}"][i])# TODO: we cant take the length of parts here because part contains mark,credit and grade
            if  lengthOfPart>1:
                for j in range(1,lengthOfPart+1):
                    print(i)
                    mark=marksDict[f"semester_{semester}"][i][f'mark_{j}']
                    credit=marksDict[f"semester_{semester}"][i][f'credit_{j}']
                    grade=marksDict[f"semester_{semester}"][i]['grade']
                    calculatedGrade=(mark*credit)/credit
                    marksDict[f"semester_{semester}"][i]['grade']=grade+calculatedGrade
            else:
                mark=marksDict[f"semester_{semester}"][i]['mark_1']
                credit=marksDict[f"semester_{semester}"][i]['credit_1']
                calculatedGrade=(mark*credit)/credit
                marksDict[f"semester_{semester}"][i]['grade']=calculatedGrade
            
            
            # for i in range(1,numberOfSub+1):
            #     mark=marksDict[f"part_{part}"][f"mark_{i}"]
            #     credit=marksDict[f"part_{part}"][f"credit_{i}"]
            #     grade=(mark*credit)/credit

            #     marksDict[f"part_{part}"][f"mark_{i}"]
