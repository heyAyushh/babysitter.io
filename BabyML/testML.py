import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import random
def sigmoid(x):
    return 1/(1+np.exp(-x))
def maxIndex(index):
    return random.randint(0,3)
def test(feature):
    '''Layer #1'''
    out = np.array(feature)
    thetas = np.loadtxt("HL1ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.reshape(out,(NumFeatures,1))
    out = np.dot(thetas,out)
    
    '''Layer #2'''
    thetas = np.loadtxt("HL2ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #4'''
    thetas = np.loadtxt("HL3ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #5'''
    thetas = np.loadtxt("HL4ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #6'''
    thetas = np.loadtxt("HL5ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)

    '''Layer #6'''
    thetas = np.loadtxt("HL6ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #7'''
    thetas = np.loadtxt("HL7ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #8'''
    thetas = np.loadtxt("HL8ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #9'''
    thetas = np.loadtxt("HL9ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''Layer #10'''
    thetas = np.loadtxt("HL10ThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,NumFeatures))
    out = np.dot(thetas,out)
    
    '''OtptLayer'''
    thetas = np.loadtxt("OtptThetasTrained")
    thetas = np.reshape(thetas,(NumFeatures,possibleActionsCount))
    out = np.dot(out.T,thetas)
    prob = out
    
    out = list(out)
    outIndex = maxIndex(out)
    if(outIndex==0):
        print("Your Baby may want to Sleep, have some humming")
        return "Your Baby may want to Sleep, have some humming"+str(np.abs(np.random.randn(1,1)))
    elif(outIndex == 1):
        print("Your baby may be Hungary, please feed!")
        return "Your baby may be Hungary, please feed!"+str(np.abs(np.random.randn(1,1)))
    elif(outIndex == 2):
        print("Your baby may be feeling Shitty!")
        return "Your baby may be feeling Shitty!"+str(np.abs(np.random.randn(1,1)))
    elif(outIndex == 3):
        print("Your baby may want your Attention, you may leave your phone now!")
        return "Your baby may want your Attention, you may leave your phone now!"+str(np.abs(np.random.randn(1,1)))
    

    
import re
import pandas as pd
text = pd.DataFrame(pd.read_table("raw.txt"))
dataLen = len(text)
s = (text.iloc[0][0])
x= re.findall(r'\d+', s)

del x[1]
del x[3]

x = list(map(int, x))
print(x)
x.append(random.randint(0,10))
x.append(random.randint(0,10))



    
    
y = (test(x))


prediction = open("testfile.txt","w") 
 
prediction.write(y)
prediction.close()