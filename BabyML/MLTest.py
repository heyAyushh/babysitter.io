print("No Of Layer",len(Thetas))
def sigmoid(x):
    return (1/(1+np.exp(-x)))
def test(features):
    global Thetas
    print("Testing on Feature",features)
    print("============================")
    out = (np.array(features))
    # Thetas = (pd.DataFrame(pd.read_table('test.txt')))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL1ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL2ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL3ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL4ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL5ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL6ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL7ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL8ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL9ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('HL10ThetasTrained.txt')))))
    out = sigmoid(np.dot(out,(pd.DataFrame(pd.read_table('OtptThetasTrained.txt')))))

    print("Output of Layer",out)
    return out

        
print(test([6]*len(dictKeys)))
    
#     
# import random
# import numpy as np 

# x = []
# for i in range(0,100):
# 	x.append(random.randint(0,100))


# np.savetxt("test.txt",x)
# import pandas as pd 

# mainData = (pd.DataFrame(pd.read_table('test.txt')))

# print(mainData)