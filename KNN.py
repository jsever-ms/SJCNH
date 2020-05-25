class KNN_classify(object):
    pass


KNN_classify()
import numpy as np
from math import sqrt
from collections import Counter

def KNN_classify(k,x_train,y_train,A):
    distances=[sqrt(np.sum((X_train-A)**2)) for X_train in x_train]
    n=np.argsort(distances)

    topk_y=[y_train[i] for i in n[:k]]
    votes=Counter(topk_y)

    return votes.most_common(1)[0][0]