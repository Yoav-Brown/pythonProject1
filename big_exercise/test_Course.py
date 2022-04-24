from unittest import TestCase,mock
from unittest.mock import patch
from Course import Course
from Student import Student

class TestCourse(TestCase):
    def setUp(self):
        self.course=Course(123,'QA',3)
        self.course_with_students=Course(111,'school',3)
        self.course_with_students.subjects['english']='orly'

        self.student_withgrade=Student(123,'ido',23)
        self.student_withgrade.add_grade("english",60)

        self.student_withgrades=Student(1234,'roi',12)
        self.student_withgrades.add_grade("math",70)
        self.student_withgrades.add_grade("python",80)
        self.student_withgrades.add_grade("english",90)

        self.student = Student(456, 'yoav', 21)
        self.student1 = Student(111, 'aaa', 11)
        self.student2 = Student(222, 'bbb', 22)
        self.student3 = Student(333, 'ccc', 33)

        self.course_with_students.add_student(self.student)
        self.course_with_students.add_student(self.student_withgrades)
        self.course_with_students.add_student(self.student_withgrade)
    def test__init__valid_arguments(self):
    #     check whether app will run with invalid course num argument
        with self.assertRaises(TypeError):
            course=Course('sdf','sdf',4)
    #     check whether app will run with invalid course name argument
        with self.assertRaises(TypeError):
            course=Course(1234,self.course,4)
    #     check whether app will run with invalid max students argument
        with self.assertRaises(TypeError):
            course=Course(1234,'sdf','dfg')

    #    check what happens when you input negative number in max students
        course_neg=Course(1234,'dgf',-6)
        self.assertEqual(course_neg.max_students,10)


    def test__init__(self):
        self.assertEqual(self.course.num,123)
        self.assertEqual(self.course.name,'QA')
        self.assertEqual(self.course.max_students,3)
        self.assertEqual(self.course.subjects,{})
        self.assertEqual(self.course.students,[])

    def test_add_student_valid_argumnets(self):
        # check whether function will run with invalid student
        with self.assertRaises(TypeError):
            self.course.add_student(8)
    #     runs with valid student
        self.course.add_student(self.student)
        self.assertIn(self.student , self.course.students)


    def test_add_student_max_reached(self):
    # trying to add  student when the course is filled
        self.course.add_student(self.student)
        self.course.add_student(self.student1)
        self.course.add_student(self.student2)
        # function needs to return false if student wasn't added
        self.assertFalse(self.course.add_student(self.student3))
        # course contains max amount of students after added one more than max
        self.course.add_student(self.student3)
        self.assertTrue(len(self.course.students)==3)

    def test_add_student_already_exists(self):
        self.course.add_student(self.student)
        self.course.add_student(self.student)
        print(self.course.students)

    def test_add_factor_valid_arguments(self):
        # adding factor when subject isn't string
        with self.assertRaises(TypeError):
            self.course.add_factor(self.student,60)
        # adding factor when percentages aren't int
        with self.assertRaises(TypeError):
            self.course.add_factor('math','dfg')
        #  adding factor with valid arguments
        self.course_with_students.add_factor('english',50)
        self.assertEqual( {'english':90},self.student_withgrade.grades)

    def test_add_factor_valid_subject_in_course(self):
        with self.assertRaises(ValueError):
            self.course_with_students.add_factor('math',50)


    def test_add_factor_functionality(self):
        self.course_with_students.add_factor('english',50)
        self.assertEqual( {'english':90},self.student_withgrade.grades)
        print(self.student_withgrades.grades)
        self.assertTrue(self.student_withgrades.grades['english']==100)





    # def test_del_student(self):



    def test_averages(self):
    #     average with on student
        self.assertEqual(False,self.course.averages())
        # self.assertEqual(self.course_with_students.averages())
        print(self.course_with_students.averages())

    def test_weak_students(self):
        with patch("Course.Course.averages") as mock_averages:
            mock_averages.return_value=[50,60,70,80]
            self.assertTrue(self.course.weak_students()==0)

            # lowest not at the beginning or end
            mock_averages.return_value=[60,50,80]
            self.assertTrue(self.course.weak_students()==1)

            # two low grades
            mock_averages.return_value=[50,40,90,40,70]
            self.assertTrue(self.course.weak_students()==[1,3])
