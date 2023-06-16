# Context Blocked
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import tensorflow as tf
import tensorflow_datasets as tfds
import random

# Read DATA from CSV file
Context_1_Input= pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Simulation//Context1_Blocked.csv')
Context_2_Input= pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Simulation//Context2_Blocked.csv')
Context_3_Input= pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Simulation//Context3_Blocked.csv')


#Make shuffle each input seprately and then drop output collumn and then concatinate all of them 
#as one input
Context_1_Input = Context_1_Input.sample(frac=1).reset_index(drop=True)
Context_2_Input = Context_2_Input.sample(frac=1).reset_index(drop=True)
Context_3_Input = Context_3_Input.sample(frac=1).reset_index(drop=True)
print(Context_1_Input.shape)
Context_1_Input.head()

num1 = random.randint(1, 8)
num2 = random.randint(1, 8)
num3 = random.randint(1, 8)

Context_1_Test = Context_1_Input[Context_1_Input['stimulus']==num1]
Context_1_Train = Context_1_Input[Context_1_Input['stimulus']!=num1]

Context_2_Test = Context_2_Input[Context_2_Input['stimulus']==num2]
Context_2_Train = Context_2_Input[Context_2_Input['stimulus']!=num2]

Context_3_Test = Context_3_Input[Context_3_Input['stimulus']==num3]
Context_3_Train = Context_3_Input[Context_3_Input['stimulus']!=num3]

