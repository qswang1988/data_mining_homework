import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
RANDOM_STATE = 12345 #Do not change it!
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

def check_scores(accuracy, precision, recall, f1):
    a = np.array([1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0])
    b = np.array([1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1])

    print("1. Accuracy test")
    try:
        assert accuracy(a, b) == accuracy_score(a, b)
        print("Correct!")
    except:
        print("Accuracy test failed! You should have got {0} but you got {1}".format(accuracy_score(a, b), accuracy(a, b)) )

    print("2. Precision test")
    try:
        assert precision(a, b) == precision_score(b, a)
        print("Correct!")
    except:
        print("Precision test failed! You should have got {0} but you got {1}".format(precision_score(b, a), precision(a, b)) )

    print("3. Recall test")
    try:
        assert recall(a, b) == recall_score(b, a)
        print("Correct!")
    except:
        print("Recall test failed! You should have got {0} but you got {1}".format(recall_score(b, a), recall(a, b)) )

    print("4. F1-score test")
    try:
        assert f1(a, b) == f1_score(a, b)
        print("Correct!")
    except:
        print("F1 test failed! You should have got {0} but you got {1}".format(f1_score(a, b), f1(a, b)) )
