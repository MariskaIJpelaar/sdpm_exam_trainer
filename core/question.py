from grader.utils.printer import *

class Question(object):
	"""An abstract Question class which defines the functions to implement by a question"""
	def __init__(self):
		self.weight = None # weight of the question between (0, 1]

	# returns the weight (0, 1]
	def get_weight(self):
		if self.weight == None:
			raise NotImplementedError
		if self.weight <= 0.0 or self.weight > 1.0:
			raise ValueError
		return self.weight

	# returns the weighted grade [0, 1]
	def get_weighted_grade(self):
		grade = self.grade()
		if grade < 0.0 or grade > 1.0:
			raise ValueError
		return grade * self.get_weight()	

	# check if provided answer is correct
	# return 1 if correct 0 else
	# Note: type of 'correct' should be str
	def check(self, correct):
		if not isinstance(correct, str):
			raise ValueError('Expected string value for {}'.format(correct))
		answer = input('answer: ')
		if answer == correct:
			return 1
		printc(Color.RED, 'incorrect, the answer should be: {}'.format(correct))
		return 0

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		raise NotImplementedError