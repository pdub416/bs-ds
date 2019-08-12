import pandas as pd
import numpy as np
import glob
import matplotlib as plt

# unit 1
def test():
    print(my_mean('sales-*.csv'))

    return None

def my_mean(filestr):
    meanlist = {}
    filelist = glob.glob(filestr)

    for f in filelist:
        data = np.loadtxt(f, delimiter=',')
        if np.any(data<0):
            print('missing data in file' +str(f) + '- watch out!')
        meanlist[f] = data.mean()

    return meanlist

def my_heatmap(data):
    plt.imshow(data)
    plot.show

if __name__ == '__main__':
    test()