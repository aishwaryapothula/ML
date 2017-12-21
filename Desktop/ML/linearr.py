#AishwaryaPothula
#To apply linear regression

import random
import math

body_weight=[]
brain_weight=[]
#Variables for iteration
i=1
z=0
#Squares of all Body weights for ease of calculation
#Products of all Body weights and Brain weights for ease of calculation
x2=[]
xy=[]

#Making a list of all body weights in the data
#Making a list of all brain weights in the data
while(i<=5):
    a=random.randint(1,101)
    b=a/3
    #b=random.randint(0,a)
    body_weight.append(a)
    brain_weight.append(b)
   
   
    dict={"body":a,"brain":b}
    print("\n{}".format(dict))
    i+=1
print("\nBody weights are {}".format(body_weight))
print("Brain weights are{}".format(brain_weight))

#Iterates as many times as the elements in body_weight
#Made a few calculations in advance to make co-effiencts calculations easier
while(z<len(body_weight)):
    x2.append(body_weight[z]**2)
    xy.append(body_weight[z]*brain_weight[z])
    z+=1
print("\n{} x2".format(x2))
print("{} xy".format(xy))


#Formule to calculate co-effiecients in the linear equation of form y=mx+c.  m=ce1,c=ce2
ce1=((sum(brain_weight)*sum(x2))-(sum(body_weight)*sum(xy)))/((i*sum(x2))-(sum(body_weight)**2))
ce2=((i*sum(xy))-(sum(body_weight)*sum(brain_weight)))/((i*sum(x2))-(sum(body_weight)**2))
print("\n{}".format(ce1))
print(ce2)

#Take input Body weight to give Brain weight according to Linear Regression equation below.
x0=float(input("\nEnter Body weight to find out respective Brain weight: "))
y0=ce1*x0+ce2
print("\nUsing Liner Regression Brain weight : Body weight is: {}\n".format({x0:y0}))






