from grader.core.question import Question
from grader.utils.printer import *

class QuestionMaslow(Question):
	def __init__(self):
		super(QuestionMaslow, self).__init__()
		self.weight = 0.5

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		points = 0
		questions = 5
		printc(Color.CAN, 'Provide Maslow\'s hierarchy of needs:')
		printc(Color.BLU, 'Top: 1.')
		points += self.check('self-actualization')
		printc(Color.BLU, '2.')
		points += self.check('esteem')
		printc(Color.BLU, '3.')
		points += self.check('social')
		printc(Color.BLU, '4.')
		points += self.check('safety needs')
		printc(Color.BLU, '5.')
		points += self.check('physiological needs')

		return points / questions
