class Student:
    def __init__(self, name, grade_level, gpa):
        self._name = name
        self._grade_level = grade_level
        self._gpa = gpa
        
    
    def get_name(self):
        return self._name
    
    
    def set_name(self, name):
        self._name = name
        
    
    def get_grade_level(self):
        return self._grade_level
    
    
    def set_grade_level(self, grade_level):
        self._grade_level = grade_level
        
        
    def get_gpa(self):
        return self._gpa
    
    
    def set_gpa(self, gpa):
        self._gpa = gpa
        

class School:
    def __init__(self):
        self.students = []
        
    
    def add_students(self, student):
        return self.students.append(student)
        
    
    def calc_avg_gpa(self):
        total_gpa = sum(student.get_gpa() for student in self.students)
        average_gpa = round((total_gpa / len(self.students)), 2)
        return average_gpa
    

if __name__ == '__main__':
    student1 = Student('John', 'A', 4.8)
    student2 = Student('Jane', 'B', 3.8)
    student3 = Student('Peter', 'C', 2.8)
    
    school = School()
    school.add_students(student1)
    school.add_students(student2)
    school.add_students(student3)
    
    print(f'The average GPA of the students is {school.calc_avg_gpa()}')