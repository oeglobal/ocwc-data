from rest_framework.test import APITestCase

class testCoursesAPI(APITestCase):
	fixtures = ['test-fixtures.json']

	def testCourses(self):
		from data.models import Course
		
		latest_course = Course.objects.latest('id')

		response = self.client.get('/api/v1/courses/latest/')
		self.assertEqual(response.data[0]['linkhash'], latest_course.linkhash)

		response = self.client.get('/api/v1/courses/view/%s/' % latest_course.linkhash)
		self.assertEqual(response.data.get('linkhash'), latest_course.linkhash)

	