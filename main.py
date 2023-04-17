from operator import le
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
    def __it__(self,other):
        if isinstance(other,Student):
            print('Студентов и преподавателей не сравнивают')
            return        
        return self.av_rating() < other.av_rating()
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
#Функция для выставления посещаемости студентом лекций.
    def attendance(self, student, course, availability):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.attendance:
                student.attendance[course] += [availability]
            else:
                student.attendance[course] = [availability]
        else:
            return ('Ошибка')
    
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
    def __it__(self,other):
        if isinstance(other,Lecturer):
            print('Студентов и преподавателей не сравнивают')
            return        
        return self.av_rating() < other.av_rating()
#Функция добавления выговора студенту за невыполнение дз
    def rebuke(self, student, course, rebukes):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.rebuke:
                student.rebuke[course] += [rebukes]
            else:
                student.rebuke[course] = [rebukes]
        else:
            return('Ошибка')
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
some_reviewer1.rate_hw(some_student1, 'Python',  9)
some_reviewer1.rate_hw(some_student1, 'Python',  7)
some_reviewer1.rate_hw(some_student1, 'Python',  8)
some_reviewer2.rate_hw(some_student2, 'Python',  7)
some_reviewer2.rate_hw(some_student2, 'Python',  5)
some_reviewer2.rate_hw(some_student2, 'Python',  10)
some_reviewer2.rate_hw(some_student2, 'Python',  8)

#Выставляем оценки за лекции
some_student1.rate_lec(some_lecturer1, 'Python',  9)
some_student1.rate_lec(some_lecturer1, 'Python',  8)
some_student1.rate_lec(some_lecturer2, 'Python',  6)
some_student1.rate_lec(some_lecturer2, 'Python',  10)
some_student2.rate_lec(some_lecturer1, 'Python',  7)
some_student2.rate_lec(some_lecturer1, 'Python',  5)
some_student2.rate_lec(some_lecturer2, 'Python',  9)
some_student2.rate_lec(some_lecturer2, 'Python',  10)

#Выставляем посещаемость студентам
some_lecturer1.attendance(some_student1, 'Python', 'was')
some_lecturer2.attendance(some_student2, 'Python', 'was')
some_lecturer1.attendance(some_student1, 'Python', 'was')
some_lecturer2.attendance(some_student2, 'Python', 'was')
some_lecturer1.attendance(some_student1, 'Python', 'was')
some_lecturer2.attendance(some_student2, 'Python', 'was')

#Выставляем выговора студентам
some_reviewer2.rebuke(some_student1, 'Python', 'rebuke')
some_reviewer1.rebuke(some_student2, 'Python', 'rebuke')

