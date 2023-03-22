import Classes.marks_class as marks_class
import Classes.calculation_class as calculation_class


#main definition

def main():
    #creating the marks object
    marksobj=marks_class.marks
    #creating the calculations object
    calcyObj=calculation_class.calculations
    marksDict=marksobj.marksDict

    semester=int(input("Enter the semester:"))
    marksDict[f"semester_{semester}"]={}

    marksobj.partInsert(semester,marksDict)

    marksobj.markInsert(semester,marksDict)
    
    calcyObj.calculateGPA(marksDict,semester)
    print(marksDict)

main()