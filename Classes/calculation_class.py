
class calculations:
    
    def calculateGPA(marksDict,semester):

        for i in marksDict[f"semester_{semester}"]:
            subCount=marksDict[f"semester_{semester}"][i]['Subject Count']
            mark=marksDict[f"semester_{semester}"][i]['marks']
            credit=marksDict[f"semester_{semester}"][i]['credits']  
            sumOfMandCMultiplied=0
            sumOfCredits=0

            for j in range(subCount):
                sumOfMandCMultiplied+=((mark[j]/10)*credit[j])
                sumOfCredits+=credit[j]
            gpa=sumOfMandCMultiplied/sumOfCredits

            marksDict[f"semester_{semester}"][i]['gpa']=gpa

        
            