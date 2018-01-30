'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase, main


class TestStudentLists(TestCase):
    # https://www.youtube.com/watch?v=6tNS--WetLI
    def setUp(self):
        self.test_class = ClassList(2)

    def tearDown(self):
        # this just has pass in it for now. if there was db handling .
        # or test files to delete, those would go here:
        pass
    
    def test_add_student_check_student_in_list(self):

        self.test_class.add_student('Test Student')
        self.assertIn('Test Student', self.test_class.class_list)

        self.test_class.add_student('Another Test Student')
        self.assertIn('Test Student', self.test_class.class_list)
        self.assertIn('Another Test Student', self.test_class.class_list)

    def test_add_student_already_in_list(self):
        self.test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            self.test_class.add_student('Test Student')

    # a test that adds and removes a student, and asserts the student is removed
    # Use assertNotIn
    def test_remove(self):
        self.test_class.add_student('Test Student3')
        self.test_class.remove_student('Test Student3')
        self.assertNotIn('Test Student3', self.test_class.class_list)

    # a test that removes a student not in the list, and asserts a StudentError is raised
    def test_invalid_remove(self):
        with self.assertRaises(StudentError):
            self.test_class.remove_student('Renee DesCartes')

    # a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_empty_list_remove(self):
        with self.assertRaises(StudentError):
            self.test_class.class_list.clear()
            self.test_class.remove_student('Renee DesCartes')

    def test_enrollment_when_student_present(self):
        self.test_class = ClassList(2)
        self.test_class.add_student('Snoop Dogg')
        self.test_class.add_student('Martha Stewart')
        self.assertTrue(self.test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(self.test_class.is_enrolled('Martha Stewart'))

    # a test that adds some example students to an example class, checks

    def test_enrollment_empty_list(self):
        self.test_class = ClassList(2)
        self.assertFalse(self.test_class.is_enrolled('Snoop Dogg'))

    # a test that adds some example students to a test class, call check_enrolled
    # for a student not enrolled, assert check_enrolled returns false
    def test_check_enrolled(self):
        self.assertFalse(self.test_class.is_enrolled('Lovecraft'))
        self.test_class.add_student('Lovecraft')
        self.assertTrue(self.test_class.is_enrolled('Lovecraft'))

    def test_string_with_students_enrolled(self):
        self.test_class = ClassList(2)
        self.test_class.add_student('Taylor Swift')
        self.test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', self.test_class.__str__())

    def test_string_empty_class(self):
        self.test_class = ClassList(2)
        self.assertEqual('', self.test_class.__str__())

    def test_index_of_student_student_present(self):
        self.test_class = ClassList(3)
        self.test_class.add_student('Harry')
        self.test_class.add_student('Hermione')
        self.test_class.add_student('Ron')

        self.assertEqual(1, self.test_class.index_of_student('Harry'))
        self.assertEqual(2, self.test_class.index_of_student('Hermione'))
        self.assertEqual(3, self.test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(self.test_class.index_of_student('Harry'))

    # However, it would be useful to check that index_of_student returns None if a student isn't present.
    # a test for index_of_student to assert it returns None if the student is not in the list
    # Cover the cases where the list is empty
    # And, when the list is not empty but does not contain the student name.
    def test_index_of_student(self):
        # empty list:
        self.assertEqual(None, self.test_class.index_of_student('test1'))

        # non empty but student not in list:
        self.test_class.add_student('test1')
        self.test_class.index_of_student('test2')

        # list where student is present
        self.test_class.add_student('test2')
        self.assertEqual(1, self.test_class.index_of_student('test1'))

    # a test(s) for new is_class_full method
    # Test a case where the class is full, and when it isn't
    def test_is_class_full(self):
        self.assertFalse(self.test_class.is_class_full())
        self.test_class.add_student('stu1')
        self.test_class.add_student('stu2')
        self.assertTrue(self.test_class.is_class_full())

if __name__ == '__main__':
    main
