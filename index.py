from school.student import Student
from school.cohort import Cohort
from school.exercise import Exercise
from school.instructor import Instructor

student_1 = Student("Matt", "Blagg", "MattScott32", 36, ["exercise 1", "exercise 2"])
student_2 = Student("Manila", "Bui", "ManBu", 36, ["exercise 3", "exercise 4"])
student_3 = Student("Corri", "Goldne", "CorGo", 36, ["exercise 1", "exercise 4"])
student_4 = Student("Chase", "Fite", "Chafi", 36, ["exercise 2", "exercise 3"])

cohort_1 = Cohort(36)
cohort_2 = Cohort(37)
cohort_3 = Cohort(38)

exercise_1 = Exercise("UrbanPlanner", "Python")
exercise_2 = Exercise("Chicken Monkey", "JavaScript")
exercise_3 = Exercise("Celebrity Tribute", "HTML")
exercise_4 = Exercise("Nutshell", "React")

instructor_1 = Instructor("Joe", "Shep", "JoeShep", 36, "Python")
instructor_2 = Instructor("Jisie", "David", "JD", 36, "React")
instructor_3 = Instructor("Jenna", "Solis", "JenSo", 36, "JavaScript")

instructor_3.assign_exercise(student_1, exercise_1)

print(student_1.exercises[0].exercise_name)