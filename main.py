class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.attendance = {}
        self.rebuke = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Студентов и преподавателей не сравнивают.")
            return
        return self.av_rating() < other.av_rating()  
    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    grades = {}
    def average_rating(self):
        sum_rate = 0
        count = 0
        for course in self.grades.values():
            sum_rate += sum(course)
            count += len(course)
            av_rating = (round(sum_rate / count, 2))
        return av_rating
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка преподавателя: {self.average_rating()}'
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Студентов и преподавателей не сравнивают.")
            return
        return self.average_rating() < other.average_rating()  
    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res
class Reviewer(Mentor):
    def __str__(self):
        return 'Имя: '+self.name + '\nФамилия: '+self.surname
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
#Студенты
some_student1 = Student('Елена', 'Анатольевна', 'жен')
some_student2 = Student('Сергей', 'Сергеевич', 'муж')
some_student1.courses_in_progress += ['Python','Git']
some_student2.courses_in_progress += ['Python']

#Лекторы
some_lecturer1 = Lecturer('Анатолий', 'Анатольевич')
some_lecturer2 = Lecturer('Александр', 'Александрович')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Python','Git']

#Проверяющие
some_reviewer1 = Reviewer('Алексей', "Алексеевич")
some_reviewer2 = Reviewer('Олег', "Олегович")

#Выставляем оценки за дз
some_reviewer1.rate_hw(some_student1, 'Python',  10)
some_reviewer1.rate_hw(some_student1, 'Python',  8)
some_reviewer1.rate_hw(some_student1, 'Python',  7)
some_reviewer1.rate_hw(some_student1, 'Python',  8)
some_reviewer2.rate_hw(some_student2, 'Python',  7)
some_reviewer2.rate_hw(some_student2, 'Python',  5)
some_reviewer2.rate_hw(some_student2, 'Python',  10)
some_reviewer2.rate_hw(some_student2, 'Python',  8)

#Выставляем оценки за лекции
some_student1.rate_lec(some_lecturer1, 'Python',  9)
some_student1.rate_lec(some_lecturer1, 'Python',  8)
some_student1.rate_lec(some_lecturer2, 'Python',  3)
some_student1.rate_lec(some_lecturer2, 'Python',  11)
some_student2.rate_lec(some_lecturer1, 'Python',  8)
some_student2.rate_lec(some_lecturer1, 'Python',  5)
some_student2.rate_lec(some_lecturer2, 'Python',  4)
some_student2.rate_lec(some_lecturer2, 'Python',  11)

#Сравниваем студентов
print('some_student2 < some_student1', some_student1 < some_student2)

#Сравниваем лекторов
print('some_lecturer1 < some_lecturer2' ,some_lecturer1 < some_lecturer2)

lecturer_list = [some_lecturer1, some_lecturer2]
student_list = [some_student1,some_student2]

def avg_rate_course_stud(course, student_list):
    summm = 0
    cnt = 0
    for stud in student_list:
        for crs in stud.grades:
            std_sum_rate = stud.avg_rate_course(course)
            summm += std_sum_rate
            cnt += 1
    res = round(summm / cnt, 2)
    return res


def avg_rate_course_lect(course, lector_list):
    summmm = 0
    cnt = 0
    for lect in lector_list:
        for crs in lect.grades:
            lect_summ_rate = lect.avg_rate_course(course)
            summmm += lect_summ_rate
            cnt += 1
    res = round(summmm / cnt, 2)
    return res


print(avg_rate_course_lect('Python', lecturer_list))
print(avg_rate_course_stud('Python', student_list))