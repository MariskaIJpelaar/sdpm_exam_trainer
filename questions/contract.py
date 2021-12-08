from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionContractDefs(QuestionDefs):
	def __init__(self):
		super(QuestionContractDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Request For Information (RFI)', 'request to suppliers to indicate whether they are able to satisfy the potential request of the customer'),
			('Request For Proposal (RFP)', 'invitation to parties through a tendering process to submit a proposal fo rthe delivery of a specific service or product'),
			('Request For Quote (RFQ)', 'invitation to parties through a tendering process to submit a quotation on the basis of fixed specifications')
		]