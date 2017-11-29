from scipy import stats as st
import numpy as np
import sqlite3
import sys

pergunta = [0.183,0.318,-0.104,-0.068,-0.061,0.103,-0.061,0.014,-0.238,-0.095,-0.025,-0.115,-0.284,-0.049,-0.104,-0.065,-0.064]
setas = [0.318,-0.181,0.179,-0.038,-0.100,-0.130,-0.055,0.108,-0.112,0.005,0.055,0.145,0.067,-0.050,-0.042]
sexual = [0.443,0.381,0.269,0.231,0.224,0.177,0.144,-0.037,-0.108,-0.134,-0.292]
hiperbole = [-0.060,-0.039,0.127,-0.096,-0.021,-0.097,0.127,0.304,-0.073,0.157,-0.004,-0.041,0.051,0.177]
cliffhanger = [-0.061,0.200,0.139,-0.130,-0.051,0.335,0.628,-0.021,-0.353,-0.076,0.240,0.037,-0.119,-0.031,-0.063,0.156,0.044,-0.175,-0.086]
totalaval = [0.955,0.949,0.947,0.935,0.915,0.885,0.715,0.558,0.910,0.913,0.995,0.632,0.752,0.756,0.972,0.999,0.741,0.961,0.898]
porcenpos = [-0.174,-0.826,-0.091,0.493,-0.355,-0.106,-0.128,-0.841,0.042,-0.796,-0.124,-0.041,0.149,-0.508,0.005,-0.379,-0.007,0.353,-0.124]
coments = [0.848,0.934,0.201,0.527,0.362,0.157,0.336,0.449,0.471,0.829,0.873,0.089,0.215,0.514,0.603,0.990,0.515,0.908,0.759]



print("Pergunta:")  
print (np.mean(pergunta))
print (st.t.interval(0.95, len(pergunta)-1, loc=np.mean(pergunta), scale=st.sem(pergunta)))

print("setas:")  
print (np.mean(setas))
print (st.t.interval(0.95, len(setas)-1, loc=np.mean(setas), scale=st.sem(setas)))

print("sexual:")  
print (np.mean(sexual))
print (st.t.interval(0.95, len(sexual)-1, loc=np.mean(sexual), scale=st.sem(sexual)))


print("hiperbole:")  
print (np.mean(hiperbole))
print (st.t.interval(0.95, len(hiperbole)-1, loc=np.mean(hiperbole), scale=st.sem(hiperbole)))

print("cliffhanger:")  
print (np.mean(cliffhanger))
print (st.t.interval(0.95, len(cliffhanger)-1, loc=np.mean(cliffhanger), scale=st.sem(cliffhanger)))

print("totalaval:")  
print (np.mean(totalaval))
print (st.t.interval(0.95, len(totalaval)-1, loc=np.mean(totalaval), scale=st.sem(totalaval)))

print("porcenpos:")  
print (np.mean(porcenpos))
print (st.t.interval(0.95, len(porcenpos)-1, loc=np.mean(porcenpos), scale=st.sem(porcenpos)))

print("coments:")  
print (np.mean(coments))
print (st.t.interval(0.95, len(coments)-1, loc=np.mean(coments), scale=st.sem(coments)))