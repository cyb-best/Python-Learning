"""
定义一个学生类
要求：
1. 属性包括姓名，学号以及语数英三科的成绩
2. 能够设置学生某科目的成绩
3. 能够打印该学生的所有科目成绩
"""
class Student:
    # def __init__(self, student_name, student_no, chinese_grade, math_grade, english_grade):
    #     self.student_name = student_name
    #     self.student_no = student_no
    #     self.chinese_grade = chinese_grade
    #     self.math_grade = math_grade
    #     self.english_grade = english_grade

    # def set_grade(self, tag, grade):
    #     if tag == 1:
    #         self.chinese_grade = grade
    #     elif tag == 2:
    #         self.math_grade = grade
    #     elif tag == 3:
    #         self.english_grade = grade
    #     else:
    #         print("参数异常")
    #
    # def print_student_all_grade(self):
    #     print(f"该学生的语文成绩为：{self.chinese_grade}\n该学生的数学成绩为：{self.math_grade}\n该学生的英语成绩为：{self.english_grade}")
# stud1 = Student("cyb", 1, 100, 100, 100)
# stud1.print_student_all_grade()
# stud1.set_grade(2, 90)
# stud1.print_student_all_grade()
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生姓名：{self.name}, 学号: {self.student_id}")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}分")

stu1 = Student("cyb", "1001")
stu1.set_grade("数学", 90)
stu1.set_grade("历史", 100)
stu1.print_grades()
