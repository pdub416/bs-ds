import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

shopping_basket = ['cherry','lemon','celery','grapefruit','apricot']
f_dict = {  'citrus':['lemon','lime','grapefruit','orange','pomelo'],\
            'stone fruit':['cherry','apricot','peach'],\
            'pome':['apple','pear','quince']    }

numlist = [25, 54, 27, 54, 23, 47, 23,  4, 27, 36, 26, 12, 25, 29, 41]

ixlist = ['Patrick','Lindsay','Ivan','Emily','Iva']
weights = pd.Series([0.3/3, 0.3/3, 0.3/3, 0.3, 0.4],\
                     index=['Assignment 1','Assignment 2','Assignment 3','Midterm','Final Exam'] )
df_marks = pd.DataFrame({ 'Assignment 1': pd.Series([72,85,87,94,77],index = ixlist),
                'Assignment 2':pd.Series([82,89,92,92,84],index = ixlist),
                'Assignment 3':pd.Series([80,94,90,99,85],index = ixlist), 
                'Midterm':pd.Series([86,95,92,97,89],index = ixlist),
                'Final Exam':pd.Series([84,92,90,91,92],index = ixlist) })

sentence = 'To construct the notion of a Lie group in Dirac geometry, extending the definition of Poisson Lie groups, the Courant algebroids A must themselves carry a multiplicative structure.'

def test():
    print(reverse_list(numlist))
    print(get_citrus(shopping_basket))
    print(get_mean(numlist))
    print(final_grade(df_marks, weights))
    print(get_odd())
    print(find_half_alphabet(sentence))
    print(find_unequal_pairs([1,2,3,4],[2,4,6]))

    return None

def reverse_list(l):
    # l: a list
    reverse_l = []
    for x in reversed(l):
        reverse_l.append(x)
    return reverse_l

def get_citrus(basket):
    # basket: list of strings
    citrus = []
    for item in basket:
        if item in f_dict['citrus']:
            citrus.append(item)
    return citrus

def get_mean(numlist):
    # numlist: a list
    # fn will only include int/float values in calculation, ignores all other types
    numonly = [x for x in numlist if isinstance(x, float) or isinstance(x, int)]
    return np.mean(numonly)

def final_grade(df, weights):
    # df: dataframe with columns as specified in the question
    # weights: series with indexes matching the columns in df, containing assignment weights
    df['Final Grade'] = (df*weights).sum(1)
    return df

def get_odd():
    return [x for x in range(-10,11) if x % 2 == 1]

def find_half_alphabet(sentence):
    return len([l for l in sentence if l.lower() in 'abcdefghijklm'])

def find_unequal_pairs(x, y):
    return [(x,y) for x in range(1,5) for y in [2,4,6] if x != y]

if __name__ == '__main__':
    test()

