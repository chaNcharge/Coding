#!/usr/bin/python

ethan = {
	"name": "Ethan",
	"homework": [100.0, 95.0, 100.0, 85.0, 100.0, 100.0],
	"quizzes": [85.0, 80.0, 90.0, 95.0, 96.0],
	"tests": [85.0, 100.0, 92.0, 90.0]
}
alice = {
	"name": "Alice",
	"homework": [100.0, 90.0, 95.0, 100.0, 100.0, 100.0],
	"quizzes": [82.0, 83.0, 91.0, 87.0, 100.0],
	"tests": [89.4, 97.0, 91.0, 90.0]
}
tyler = {
	"name": "Tyler",
	"homework": [0.0, 85.0, 75.0, 60.0, 80.0, 90.0],
	"quizzes": [64.0, 75.0, 78.0, 83.0, 86.5],
	"tests": [79.0, 81.0, 85.0, 70.0]
}

students = [ethan, alice, tyler]

def average(n):
	total = sum(n)
	total = float(total)
	total = total / len(n)
	return total
def get_average(student):
	homework = average(student["homework"])
	quizzes = average(student["quizzes"])
	tests = average(student["tests"])
	total = homework * 0.1 + quizzes * .3 + tests * .6
	return total
def get_letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
def get_class_average(students):
	results = []
	for i in students:
		results.append(get_average(i))
	return average(results)

#change name in graded_student to get a specific student's grades
graded_student = alice

print "Grade: " + get_letter_grade(get_average(graded_student)), get_average(graded_student)
print ""
print "Class Average: " + get_letter_grade(get_class_average(students)), get_class_average(students)