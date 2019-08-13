import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

# unit 1
def test():
    #print(my_mean('sales-*.csv'))
    
    data = pd.DataFrame(np.random.random([2,2]))
    my_heatmap(data)

def my_heatmap(data):
    plt.plot(data)
    plt.show
'''
def my_mean(filestr):
    meanlist = []
    filelist = glob.glob(filestr)

    for f in filelist:
        data = np.loadtxt(f, delimiter=',')
        if np.any(data<0):
            print('missing data in file' +str(f) + '- proceeding anyway')
            # could strip out the missing values instead of proceeding

        meanlist.append(data.mean())

    return meanlist
'''
if __name__ == '__main__':
    test()