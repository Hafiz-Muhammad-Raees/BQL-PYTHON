print ('==================================================\n')
print ("\u2740 PYTHON ASSIGNMENT 2 (BANO QABIL) \u2740")
print ('\n==================================================\n')

# Printing Group's Information in the form of Table

print ("Group's Information:\n")
headers = ["S.No.", "Participant's Name", "Father's Name", "Class", "Age", "Challan No.", "Contact No."]
rows = [
[1, "Hafiz Muhammad Raees", "Shamim Akhtar", "XI", "17 years", 252265, "+92 348 3621301"],
[2, "Fuzail Ahmad", "Muhammad Khalid", "XI", "15 years", 254466, "+92 334 3171039"],
[3, "Hafiz Hashir Khan", "Asim Khan", "X", "17 years", '******', "+92 317 8092848"]
]
def info_table(headers, rows):

    col_widths = [max(len(str(item)) for item in col) for col in zip(*[headers] + rows)]
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))
    print(format_str.format(*headers))
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))

    for row in rows:
        print(format_str.format(*row))
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))
info_table(headers, rows)
print ('\n==================================================\n')

# Defining class "Student_Result"

class Student_Result:

    # Defining constructor function
    def __init__(self, sno, name, f_name, cls, rollno):
        # Adding Instance Attributes
        self.sno = sno
        self.name = name  
        self.fname = f_name
        self.cls = cls
        self.rollno = rollno
        self.maxmarks = {}  
        self.obtmarks = {} 
        self.int_percentage = {}
        self.percentage = {}
        self.grade = {}
        self.table_headers = ['Subject', 'Max Marks', 'Obt. Marks', 'Percentage', 'Grade']
        self.table_rows = []
        self.totalmax = 0
        self.totalobt = 0
        self.avgint_percentage = 0
        self.avg_grade = ''  
    
    # Adding Subjects with Max marks, Obt. marks, Percentages and Grades for EACH Subject
    def add_subject(self, subject, m_marks, o_marks):

        # Adding Max marks and Obt. marks
        self.maxmarks[subject] = m_marks
        self.obtmarks[subject] = o_marks

        # Calculating Percentage for each Subject
        self.int_percentage[subject] = (o_marks / m_marks) * 100
        self.percentage[subject] = f'{self.int_percentage[subject]:.2f} %'

        # Finding Grade for each Subject
        self.grade[subject] = (
            'A+' if self.int_percentage[subject] >= 80 else 
            'A' if self.int_percentage[subject] >= 70 else 
            'B' if self.int_percentage[subject] >= 60 else 
            'C' if self.int_percentage[subject] >= 50 else 
            'D' if self.int_percentage[subject] >= 40 else 
            'E' if self.int_percentage[subject] >= 33 else 
            'F')

        # Adding 'Data of All Subjects' into 'self.table_rows'
        existing_subject = next((row for row in self.table_rows if row[0] == subject), None)
        if existing_subject:
            existing_subject[1] = self.maxmarks[subject]
            existing_subject[2] = self.obtmarks[subject]
            existing_subject[3] = self.percentage[subject]
            existing_subject[4] = self.grade[subject]
        else:
            self.table_rows.append([
                subject, self.maxmarks[subject], 
                self.obtmarks[subject], 
                self.percentage[subject], 
                self.grade[subject]
            ])

    # Calculating TOTAL Max and Obt. marks
    def find_total(self):
        self.totalmax = sum(self.maxmarks.values())
        self.totalobt = sum(self.obtmarks.values())
    
    # Calculating Overall Percentage
    def find_percentage(self):
        if self.totalmax > 0:
            self.avgint_percentage = (self.totalobt / self.totalmax) * 100
        else:
            self.avgint_percentage = 0
        self.avg_percentage = f'{self.avgint_percentage:.2f} %'

    # Finding Overall Grade
    def find_grade(self):
        if 80 <= self.avgint_percentage:
            self.avg_grade = 'A+'
        elif 70 <= self.avgint_percentage:
            self.avg_grade = 'A'
        elif 60 <= self.avgint_percentage:
            self.avg_grade = 'B'
        elif 50 <= self.avgint_percentage:
            self.avg_grade = 'C'
        elif 40 <= self.avgint_percentage:
            self.avg_grade = 'D'
        elif 33 <= self.avgint_percentage:
            self.avg_grade = 'E'
        else:
            self.avg_grade = 'F'
    
    # Representing 'Data of All Subjects' using a Table
    def print_table(self):

        # Calculate maximum width for each column
        col_widths = [max(len(str(item)) for item in col) for col in zip(*[self.table_headers] + self.table_rows)]
    
        # Create a format string for each column width
        format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    
        # Create table lines with correct formatting of HEADERS and ROWS
        table_lines = []
        separator = "-" * (sum(col_widths) + len(col_widths) * 3 - 1)
        table_lines.append(separator)
        table_lines.append(format_str.format(*self.table_headers))
        table_lines.append(separator)
        for row in self.table_rows:
            table_lines.append(format_str.format(*row))
        table_lines.append(separator)

        # Return the Table
        return "\n".join(table_lines)
    
    # For String Representation of the class "Student_Result"
    def __str__(self):

        #Call Methods within the Class
        self.find_total()
        self.find_percentage()
        self.find_grade()

        # Return the Mark sheet
        return (f"""
\u273F MARKSHEET FOR STUDENT {self.sno} \u273F
\n------------------------------
\nStudent's Name: {self.name} 
\nFather's Name: {self.fname} 
\nClass: {self.cls}
\nRoll No: {self.rollno}
\n____________________________________________________________
\nSUBJECT-WISE RESULT:
\n{self.print_table()}
\n____________________________________________________________
\nOVERALL RESULT:
\nMaximum Marks: {self.totalmax} 
\nObtained Marks: {self.totalobt} 
\nPercentage: {self.avg_percentage} 
\nGrade: {self.avg_grade} 
\n============================================================
        """)

# Taking Student's Data in the form of list as input

main_list = []
info = int(input('\nEnter Number of Students: '))

for i in range(1, info + 1):
    print(f'\nEnter Data for Student {i}:')
    sno = i
    name = input(f"\nStudent's Name: ")
    f_name = input(f"Father's Name: ")
    cls = input(f"Class: ")
    rollno = input(f"Roll No.: ")
    
    student = Student_Result(sno, name, f_name, cls, rollno)

    n = int(input(f"No. of Subjects: "))
    for j in range(1, n + 1):
        sub = input(f"\nSubject {j} Name: ")
        m_marks = int(input('Max Marks: '))
        o_marks = int(input('Marks Obtained: '))
        student.add_subject(sub, m_marks, o_marks)
    student.find_total()
    student.find_percentage()
    student.find_grade()
    main_list.append(student)

# Printing the Student's Marksheet

print('\n============================================================')
for student in main_list:
    print(student)