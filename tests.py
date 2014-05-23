import unittest
import rjson

class RjsonTests(unittest.TestCase):
	def test_failsWhenNone(self):
		# arrange
		# act
		result = list(rjson.parseJson(None))
		
		# assert
		self.assertTrue(len(result) == 0)

	def test_failsWhenNotString(self):
		# arrange
		json = 1
		
		# act
		result = list(rjson.parseJson(1))
		
		# assert
		self.assertTrue(len(result) == 0)

	def test_failsWhenNotCorrectJson(self):
		# arrange
		json = "not json"

		# act
		result = list(rjson.parseJson(json))

		# assert
		self.assertTrue(len(result) == 0)

	def test_succeedsWithSimpleHappyPath(self):
		# arrange
		json = "{ \"what\":\"hello\" }"

		# act
		result = list(rjson.parseJson(json))

		# assert
		self.assertTrue(len(result) == 1)

	def test_succeedsWithDoubleQuote(self):
		# arrange
		json = "{ \"what\":\"hello\\\"\" }"

		# act
		result = list(rjson.parseJson(json))

		# assert
		self.assertTrue(len(result) == 1)

def main():
    unittest.main()

if __name__ == '__main__':
        main()