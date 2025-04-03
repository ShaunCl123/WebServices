import unittest, requests

class ApiCode(unittest.TestCase):

    def test_sample_endpoint(self):
        url = 'http://localhost:8000/' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample2_endpoint(self):
        url = 'http://localhost:8000/getAll' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample3_endpoint(self):
        url = 'http://localhost:8000/getSingleProduct/AUTO058' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample4_endpoint(self):
        url = 'http://localhost:8000/addNew/AUTO104/Alternator/150.75/30/Durable' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample5_endpoint(self):
        url = 'http://localhost:8000/deleteOne/AUTO104' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample6_endpoint(self):
        url = 'http://localhost:8000/startsWith/a' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample7_endpoint(self):
        url = 'http://localhost:8000/paginate/AUTO020/AUTO058' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_sample8_endpoint(self):
        url = 'http://localhost:8000/convert/AUTO039' # this is the endpoint to call
        # Making a GET request to the /sample endpoint
        response = requests.get(url)
        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)
    

if __name__ == '__main__':

    unittest.main()