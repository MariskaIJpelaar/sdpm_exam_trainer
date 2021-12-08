from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionQualityDefs(QuestionDefs):
	def __init__(self):
		super(QuestionQualityDefs, self).__init__()
		self.weight = 0.3

	def generate_pairs(self):
		return [
			('Planning', 'Determine which quality standards are relevant and how to measure them'), 
			('Assurance', 'Making sure you are doing the right things, the right way'),
			('Control', 'Making sure the results of what you have done are what you expected'),
			('Cost of Quality (COQ)', 'Refers to the total cost of all efforts to achieve product-/ service quality, and includes all the work to ensure conformance to requirements, as well as all work resulting from non-conformance to requirements'),
			('Plan Quality Management', 'Process of identifying quality requirements / standards for the project and product AND documenting how th eproject will demonstrate compliance'),
			('Perform Quality Control (QC)', 'Monitoring results to determine if they comply with relevant quality standards and identifying ways to eliminate causes of unsatisfactory results'), 
			('Quality Audit', 'A structured review of the managment activities, performed by trained in-house auditors or by third parties')
		]