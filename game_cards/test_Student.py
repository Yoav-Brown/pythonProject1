from unittest import TestCase,mock
from Student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student=Student(123,'yoav',21)

        self.student_withgrade=Student(123,'ido',23)
        self.student_withgrade.add_grade("english",60)

        self.student_withgrades=Student(1234,'ido',12)
        self.student_withgrades.add_grade("math",70)
        self.student_withgrades.add_grade("python",80)
        self.student_withgrades.add_grade("english",60)

    def test__init__1(self):
        self.assertEqual(self.student.id,123)
        self.assertEqual(self.student.name,'yoav')
        self.assertEqual(self.student.age,21)
        self.assertEqual(self.student.grades,{})


    def test__init__valid_arguments(self):
        student_negative_age=Student(123,'yoav',-6)
        with self.assertRaises(TypeError):
            student_invalid_id = Student('asc', 'yoav', 21)
        with self.assertRaises(TypeError):
            student_invalid_name = Student(123, self.student, 21)
        with self.assertRaises(TypeError):
            student_invalid_age = Student(123, 'yoav', "dfg")

        self.assertTrue(student_negative_age.age==0)


    def test_add_grade(self):
        self.student.add_grade("math",70)
        self.assertTrue(self.student.grades=={"math":70})
        # adding grades to student with grades already
        self.student_withgrades.add_grade('java',75)
        self.assertTrue(self.student_withgrades.grades=={"math":70,"python":80,"english":60,'java':75})

    def test_add_grade_valid_arguments(self):
        # adding subject that isn't string
        with self.assertRaises(TypeError):
           self.student.add_grade(self.student,60)
        #     adding grade that isn't int
        with self.assertRaises(TypeError):
           self.student.add_grade('math','dfg')



    def test_calc_factor_valid_arguments(self):
        # calculating factor when subject isn't string
        with self.assertRaises(TypeError):
            self.student.calc_factor(self.student,60)
        # calculating factor when percentages aren't int
        with self.assertRaises(TypeError):
            self.student.calc_factor('math','dfg')



    def test_calc_factor_functionability(self):
        self.student_withgrade.calc_factor('english',50)
        self.assertTrue({'english': 90},self.student_withgrade.grades)



    def test_calc_factor_exceeds_100(self):
        self.student_withgrade.calc_factor('english',100)
        self.assertTrue({'english': 100},self.student_withgrade.grades)

    def test_average_student_without_grades(self):
        self.assertFalse(self.student.average())

    def test_average(self):
        self.assertEqual(self.student_withgrades.average(),70)
        self.assertEqual(self.student_withgrade.average(),60)


    def test__eq__not_Student(self):
        self.assertFalse(self.student==123)


    def test__eq__functionability(self):
        # comparing students with same id
        self.assertTrue(self.student==self.student_withgrade)
        # comparing students with different id
        self.assertFalse(self.student==self.student_withgrades)


    def test__gt__valid_arguments(self):
        with self.assertRaises(TypeError):
            self.student>8

    def test__gt__functionability(self):
        # comparing bigger student with smaller student
        self.assertTrue(self.student>self.student_withgrades)
        # comparing smaller student with bigger student
        self.assertFalse(self.student>self.student_withgrade)
