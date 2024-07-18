import os
import sys
from importlib import import_module
from random import random

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Appends main project root as importpath.

from sdpm_exam_trainer.core.question import Question
from sdpm_exam_trainer.utils.printer import *
# import sdpm_exam_trainer.questions.product_defs

# https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name/3862957
# only returns 'leaves'
def all_subclasses(cls):
	subclasses = []
	for sub in cls.__subclasses__():
		if not sub.__subclasses__():
			subclasses.append(sub)
		else:
			subclasses.extend(all_subclasses(sub))
	return subclasses

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
	mod = import_module('.'.join(['sdpm_exam_trainer.questions', py]))
	classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), Question)]
	for cls in classes:
		setattr(sys.modules[__name__], cls.__name__, cls)

def main():
	printc(Color.PRP, 'Welcome to the automatic sdpm_exam_trainer')
	printc(Color.PRP, 'This tool provides you with randomized questions for the SDPM exam of december 2021')
	printc(Color.PRP, 'You also receive a grade at the end to see how you performed')
	printc(Color.PRP, 'Please round all your numerical answers to the nearest decimal and use lower-case string-answers, unless stated otherwise')
	printc(Color.PRP, 'Note that these questions are made for personal use, to support the exam-study, we provide no guarantees to the relation of this tool and the exam')

	weights = 0.0
	points = 0.0
	qs = 1
	classes = [ cls for cls in sorted(all_subclasses(Question), key=lambda _: random())]
	for cls in classes:
		printc(Color.YEL, 'Question {}'.format(qs))
		question = cls()
		# if not isinstance(question, sdpm_exam_trainer.questions.product_defs.QuestionProductDefs):
		# 	continue
		weights += question.get_weight()
		points += question.get_weighted_grade()
		qs += 1
	printc(Color.PRP, 'Your grade is: {}'.format((points/weights) * 10))

if __name__ == '__main__':
	main()