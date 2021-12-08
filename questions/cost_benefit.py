from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionCostBenefitDefs(QuestionDefs):
	def __init__(self):
		super(QuestionCostBenefitDefs, self).__init__()
		self.weight = 0.3

	def generate_pairs(self):
		return [
			('Payback period', 'the exact time duration needed to recover an initial investment as calculated from cash inflows (period when total benefits >= total costs)'),
			('Net present value (NPV)', 'budgeting technique that debates the future value of money based on inflation, etc.'),
			('Internal Rate of Return (IRR)', 'the interest (discount) rate where the present value of the benefits exactly equals the cost'),
			('Bang of buck index', 'net present value divided by the number of human resources'),
			('Opportunity cost', 'the opportunity given up by selecting one project over another'),
			('Sunk cost', 'expended costs')
		]