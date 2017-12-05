#AishwaryaPothula
#To apply linear regression

import random
import math

body_weight=[]
brain_weight=[]
i=1
z=0
'''
Variables for iteration
'''
x2=[]
'''
Squares of all Body weights for ease of calculation
'''
xy=[]
'''
Products of all Body weights and Brain weights for ease of calculation
'''

while(i<=5):
    a=random.randint(0,101)
    b=random.randint(0,101)
    body_weight.append(a)
    '''
    Making a list of all body weights in the data
    '''
    brain_weight.append(b)
    '''
    Making a list of all brain weights in the data
    '''
    dict={"body":a,"brain":b}
    print("\n{}".format(dict))
    i+=1
print("\nBody weights are {}".format(body_weight))
print("Brain weights are{}".format(brain_weight))

while(z<len(body_weight)):
    '''
    Iterates as many times as the elements in body_weight
    '''
    x2.append(body_weight[z]**2)
    xy.append(body_weight[z]*brain_weight[z])
    '''
    Made a few calculations in advance to make co-effiencts calculations easier
    '''
    z+=1
print("\n{} x2".format(x2))
print("{} xy".format(xy))

ce1=((sum(brain_weight)*sum(x2))-(sum(body_weight)*sum(xy)))/((i*sum(x2))-(sum(body_weight)**2))
ce2=((i*sum(xy))-(sum(body_weight)*sum(brain_weight)))/((i*sum(x2))-(sum(body_weight)**2))
'''
Formule to calculate co-effiecients in the linear equation of form y=mx+c.  m=ce1,c=ce2
'''
print("\n{}".format(ce1))
print(ce2)

x0=float(input("\nEnter Body weight to find out respective Brain weight: "))
'''
Take input Body weight to give Brain weight according to Linear Regression equation below.
'''
y0=ce1*x0+ce2
print("\nUsing Liner Regression Brain weight : Body weight is: {}\n".format({x0:y0}))






