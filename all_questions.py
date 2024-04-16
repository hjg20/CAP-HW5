#import pytest
import math
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = .9*.2*.8*.2

    # type: float
    # Calculate the probability.
    answers['(b)'] = .1*.2*.1*1

    # type: float
    # Calculate the probability.
    #answers['(c)'] = ((0*.2+.1*.8)*.1)/.1 ###GRADESCOPE FIX
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True ###

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False #A focus on reducing bias leads to reducing UNDERFITTING, not overfitting. Overfitting is the result of high variance.

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.

    error = 0.3
    alpha = (.5)*(math.log((1-error)/error))

    #answers['(c) Weight update'] = alpha ###GRADESCOPE FIX

    answers['(c) Weight update'] = '0.5*math.log((1-p)/p)'

    # type: float
    # the answer should be correct to 3 significant digits

    original_weight = 1
    new_weight = (original_weight)*(math.exp(alpha))

    answers['(d) Weight influence'] = new_weight
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "The base classifiers he is using (flipping a coin 1000 times) have individual error rates of 0.5 (theoretically). Since the base classifiers are random guessing, he will not attain good results using ensemble methods due to the fact that the base classifiers are not leading him to convergence of a specific class after incorporating boosting or bagging."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "(100*p)/100"

    # type: eval_float
    answers['(a) C2-TPR'] = '2*p'

    # type: eval_float
    answers['(a) C1-FPR'] = 'p'

    # type: eval_float
    answers['(a) C2-FPR'] = '2*p'

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "no"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "C1 has a lower true positive rate than C2. However C1 has a lower false positive rate than C2. Based on this, we cannot say that one model is better than the other without knowing what the model is estimating."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = 'TPR/FPR is the same for both classifiers and does not give us much information. We should use precision/recall because the values are different for each classifier.'
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C1'

    # type: explain_string
    answers['(i) Best classifier, explain'] = 'C2 is equally bad at predicting the negative and positive classes, whereas C1 is well at predicting the negative class. We also do not get much information from C2 because it is splitting the data 50/50 for each class.'

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'TPR-FPR'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = 'Using TPR and FPR we can see we get a value of 0.5 for each metric in C2 but get a value of 0.1 for each metric in C1. This shows that C1 is bad at predicting positives but is good at predicting negatives. C2 shows that the data is being randomly assigned. Precision, recall, and F1 are higher for C2, but are not showing how C2 is getting its results.'

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = 'C3 is comparable to C1, except it was better at correctly classifying the positive class. Therefore, I would prefer C3.'
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    #answers['(a) precision for C0'] = 0.1 ###GRADESCOPE FIX
    answers['(a) precision for C0'] = '1/10'

    # type: eval_float
    answers['(a) recall for C0'] = 'p'

    # type: eval_float
    answers['(b) F-measure of C0'] = '(2*p)/((10*p)+1)'

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
        'recall': 80/(80+50),
        'precision': 80/(80+70),
        'F-measure': 160/(160+70+50),
        'accuracy': 880/1000
    }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'This classifier is good at classifying the negative class, but bad at classifying the positive class, so using accuracy is bad because our accuracy is being skewed by the amount of values of the negative class, and not properly showing the errors in classifying the positive class, hence why it is the worst metric. The best metric is F-measure because it is taking in to account the false negatives as well as the false positives. Using missclassifications from both classes helps to see how the model works on all classes it works with and is the best metruc..'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'F1'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'Our test is dealing with cancer detection, therefore we want to focus on our test not identifying people with cancer as being cancer-free. Also, our classes are very imbalanced. Using F1, we can combine precision and recall to get a good sense of how our test identifies smaller classes even when among a larger class.'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'An example scenario in which I would reverse my choice and prefer TPR/FPR over F measure is a scenario in which our classes are well balanced and we equally want to prevent missclassifications for the positive and negative classes.'
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)

print(question1())