import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import random



dictKeys = ["Temp","Humidity","LightIntensity","CO2Levels","SoundIntensity","BX","BY","BZ","Vibrations"]
NumFeatures = len(dictKeys)
dataLen = 1000
TrainingData = pd.DataFrame(np.random.randn(len(dictKeys),dataLen)).T
TrainingLabels = []
for i in range(dataLen):
    TrainingLabels.append(random.randint(0,len(dictKeys)))
    
    
TrainingLabels = pd.DataFrame(np.array(TrainingLabels))


BatchSize = 100
HiddenLayerNeurons = NumFeatures


DataIn = tf.placeholder(tf.float64,[BatchSize,NumFeatures])

TrueLabels = tf.placeholder(tf.float64,[BatchSize,1])


possibleActionsCount = 4


HL1Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL1Out = tf.sigmoid(tf.matmul(DataIn,HL1Thetas))
HL2Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL2Out = tf.sigmoid(tf.matmul(HL1Out,HL2Thetas))
HL3Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL3Out = tf.sigmoid(tf.matmul(HL2Out,HL3Thetas))
HL4Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL4Out = tf.sigmoid(tf.matmul(HL3Out,HL4Thetas))
HL5Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL5Out = tf.sigmoid(tf.matmul(HL4Out,HL5Thetas))
HL6Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL6Out = tf.sigmoid(tf.matmul(HL5Out,HL5Thetas))
HL7Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL7Out = tf.sigmoid(tf.matmul(HL6Out,HL7Thetas))
HL8Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL8Out = tf.sigmoid(tf.matmul(HL7Out,HL8Thetas))
HL9Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL9Out = tf.sigmoid(tf.matmul(HL8Out,HL9Thetas))
HL10Thetas = tf.Variable(np.random.randn(NumFeatures,HiddenLayerNeurons))
HL10Out = tf.sigmoid(tf.matmul(HL9Out,HL10Thetas))
OtptThetas = tf.Variable(np.random.randn(NumFeatures,possibleActionsCount))
Otpt = tf.sigmoid(tf.matmul(HL10Out,OtptThetas))


CostFunction = tf.reduce_mean(tf.square(Otpt - TrueLabels))


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000000001)
MinimizeError = optimizer.minimize(CostFunction)


Init = tf.global_variables_initializer()


with tf.Session() as S:
    TotalEpochs = 100000
    
    S.run(Init)
    for i in range(TotalEpochs):
        
        RandomIndices = np.random.randint(0,len(TrainingData),size = BatchSize)
        
        Data2Feed = {DataIn:np.array(TrainingData.iloc[RandomIndices]),
                    TrueLabels:np.array(TrainingLabels.iloc[RandomIndices]).reshape(100,1)}
        
        S.run(MinimizeError,feed_dict=Data2Feed)
        
        
        CFErrorInCurrentEpoch = S.run([CostFunction],feed_dict = Data2Feed)
        if(i%100==0):
            print("The CF Error in Epoch: ",i," is: ",np.sqrt(CFErrorInCurrentEpoch))
            
#     HL1ThetasActual = S.run([HL1Thetas])
    Thetas = []
    Thetas.append(S.run([HL1Thetas]))
    Thetas.append(S.run([HL2Thetas]))
    Thetas.append(S.run([HL3Thetas]))
    Thetas.append(S.run([HL4Thetas]))
    Thetas.append(S.run([HL5Thetas]))
    Thetas.append(S.run([HL6Thetas]))
    Thetas.append(S.run([HL7Thetas]))
    Thetas.append(S.run([HL8Thetas]))
    Thetas.append(S.run([HL9Thetas]))
    Thetas.append(S.run([HL10Thetas]))
    Thetas.append(S.run([OtptThetas]))
    

    


TrainedThetas = []
for i in range(len(Thetas)):
    TrainedThetas.append(Thetas[i][0])

TrainedThetas = np.array(TrainedThetas)

np.savetxt("HL1ThetasTrained", TrainedThetas[0], newline=" ")
np.savetxt("HL2ThetasTrained", TrainedThetas[1], newline=" ")
np.savetxt("HL3ThetasTrained", TrainedThetas[2], newline=" ")
np.savetxt("HL4ThetasTrained", TrainedThetas[3], newline=" ")
np.savetxt("HL5ThetasTrained", TrainedThetas[4], newline=" ")
np.savetxt("HL6ThetasTrained", TrainedThetas[5], newline=" ")
np.savetxt("HL7ThetasTrained", TrainedThetas[6], newline=" ")
np.savetxt("HL8ThetasTrained", TrainedThetas[7], newline=" ")
np.savetxt("HL9ThetasTrained", TrainedThetas[8], newline=" ")
np.savetxt("HL10ThetasTrained", TrainedThetas[9], newline=" ")
np.savetxt("OtptThetasTrained", TrainedThetas[10], newline=" ")


    
