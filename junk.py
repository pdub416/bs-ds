import pandas as pd

ixlist = ['Patrick','Lindsay','Ivan','Emily','Iva']
df = pd.DataFrame({ 'Assignment 1': pd.Series([72,85,87,94,77],index = ixlist),
                'Assignment 2':pd.Series([82,89,92,92,84],index = ixlist),
                'Assignment 3':pd.Series([80,94,90,99,85],index = ixlist), 
                'Midterm':pd.Series([86,95,92,97,89],index = ixlist),
                'Final Exam':pd.Series([84,92,90,91,92],index = ixlist) })

df['Final Grade'] = df*[0.1, 0.1, 0.1, 0.3, 0.4]
pass
