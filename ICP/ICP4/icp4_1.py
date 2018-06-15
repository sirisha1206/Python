class Employee():
    empCount = 0 #initialize the data member
    empSal = [];
    def __init__(self,name,family,salary,department): #default constructor
        self.ename = name
        self.efamily = family
        self.esalary = salary
        self.edepartment = department
        Employee.empCount +=1
        Employee.empSal.append(salary)

    def get_avg_salary(self):
        print('inside the average salary function')
        sumSal = 0;
        for sal in Employee.empSal:
            sumSal = sumSal+ int(sal);
        return sumSal/len(Employee.empSal)

class FulltimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)


emp1 = FulltimeEmployee('sirisha','sunkara','5000','CS');
emp2 = FulltimeEmployee('vinay','santhosham','4000','CS');
emp3 = FulltimeEmployee('sree','n','3000','CS');
print(FulltimeEmployee.empCount)
print(FulltimeEmployee.empSal)
avgSal = FulltimeEmployee.get_avg_salary(Employee);
print(avgSal)