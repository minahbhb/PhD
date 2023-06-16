import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv

plt.style.use('seaborn')
x_axis=['7', '8', '9', '10', '11','12']
###################################################################################
################## SWITCH COST IN Context Blocked Planet ##########################
###################################################################################

CB_SW=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Switch_Cost_Context_Blocked.csv')

CB_yR= [round(CB_SW['ACC_Repeat_Block_7'].mean(),2), round(CB_SW['ACC_Repeat_Block_8'].mean(),2) , round(CB_SW['ACC_Repeat_Block_9'].mean(),2), 
        round(CB_SW['ACC_Repeat_Block_10'].mean(),2), round(CB_SW['ACC_Repeat_Block_11'].mean(),2) , round(CB_SW['ACC_Repeat_Block_12'].mean(),2)]

CB_yR_std= [round(CB_SW['ACC_Repeat_Block_7'].std(),2), round(CB_SW['ACC_Repeat_Block_8'].std(),2), round(CB_SW['ACC_Repeat_Block_9'].std(),2), 
            round(CB_SW['ACC_Repeat_Block_10'].std(),2), round(CB_SW['ACC_Repeat_Block_11'].std(),2), round(CB_SW['ACC_Repeat_Block_12'].std(),2)]
    
CB_yA= [round(CB_SW['ACC_Alter_Block_7'].mean(),2), round(CB_SW['ACC_Alter_Block_8'].mean(),2), round(CB_SW['ACC_Alter_Block_9'].mean(),2), 
        round(CB_SW['ACC_Alter_Block_10'].mean(),2), round(CB_SW['ACC_Alter_Block_11'].mean(),2), round(CB_SW['ACC_Alter_Block_12'].mean(),2)]

CB_yA_std= [round(CB_SW['ACC_Alter_Block_7'].std(),2), round(CB_SW['ACC_Alter_Block_8'].std(),2), round(CB_SW['ACC_Alter_Block_9'].std(),2), 
            round(CB_SW['ACC_Alter_Block_10'].std(),2), round(CB_SW['ACC_Alter_Block_11'].std(),2), round(CB_SW['ACC_Alter_Block_12'].std(),2)]

CB_yR_RT= [round(CB_SW['RT_Repeat_Block_7'].mean(),2), round(CB_SW['RT_Repeat_Block_8'].mean(),2), round(CB_SW['RT_Repeat_Block_9'].mean(),2), 
           round(CB_SW['RT_Repeat_Block_10'].mean(),2), round(CB_SW['RT_Repeat_Block_11'].mean(),2), round(CB_SW['RT_Repeat_Block_12'].mean(),2)]

CB_yR_RT_std= [round(CB_SW['RT_Repeat_Block_7'].std(),2), round(CB_SW['RT_Repeat_Block_8'].std(),2), round(CB_SW['RT_Repeat_Block_9'].std(),2), 
               round(CB_SW['RT_Repeat_Block_10'].std(),2), round(CB_SW['RT_Repeat_Block_11'].std(),2), round(CB_SW['RT_Repeat_Block_12'].std(),2)]

CB_yA_RT= [round(CB_SW['RT_Alter_Block_7'].mean(),2), round(CB_SW['RT_Alter_Block_8'].mean(),2), round(CB_SW['RT_Alter_Block_9'].mean(),2), 
           round(CB_SW['RT_Alter_Block_10'].mean(),2), round(CB_SW['RT_Alter_Block_11'].mean(),2), round(CB_SW['RT_Alter_Block_12'].mean(),2)]
         

CB_yA_RT_std= [round(CB_SW['RT_Alter_Block_7'].std(),2), round(CB_SW['RT_Alter_Block_8'].std(),2), round(CB_SW['RT_Alter_Block_9'].std(),2), 
               round(CB_SW['RT_Alter_Block_10'].std(),2), round(CB_SW['RT_Alter_Block_11'].std(),2),round(CB_SW['RT_Alter_Block_12'].std(),2)]
         

plt.clf()
plt.plot(x_axis, CB_yR, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, CB_yA , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean ACC Context_Blocked Planet",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.legend()
plt.ylim((70, 100))
plt.show()


plt.clf()
plt.plot(x_axis, CB_yR_RT, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, CB_yA_RT , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean RT Context_Blocked Planet",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.legend()
plt.ylim((1100, 2000))
plt.show()


#### BAR Plot ##########

import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = CB_yR
women_means = CB_yA


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= CB_yR_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= CB_yA_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Accuracy')
ax.set_title('Context_Blocked Mean ACC by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

######################## RT ######################
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = CB_yR_RT
women_means = CB_yA_RT


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= CB_yR_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= CB_yA_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Reaction Time')
ax.set_title('Context_Blocked Mean RT by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 2250)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

##############################################################################################################
################################# Switch Cost Context Interleaved ############################################
##############################################################################################################

CI_SW=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_2_Data_Pilot_Run//df_Switch_Cost_Context_Interleaved.csv')

CI_yR= [round(CI_SW['ACC_Repeat_Block_7'].mean(),2), round(CI_SW['ACC_Repeat_Block_8'].mean(),2), round(CI_SW['ACC_Repeat_Block_9'].mean(),2), 
        round(CI_SW['ACC_Repeat_Block_10'].mean(),2), round(CI_SW['ACC_Repeat_Block_11'].mean(),2), round(CI_SW['ACC_Repeat_Block_12'].mean(),2)]
    
CI_yA= [round(CI_SW['ACC_Alter_Block_7'].mean(),2), round(CI_SW['ACC_Alter_Block_8'].mean(),2), round(CI_SW['ACC_Alter_Block_9'].mean(),2), 
        round(CI_SW['ACC_Alter_Block_10'].mean(),2), round(CI_SW['ACC_Alter_Block_11'].mean(),2), round(CI_SW['ACC_Alter_Block_12'].mean(),2)]

CI_yR_RT= [round(CI_SW['RT_Repeat_Block_7'].mean(),2), round(CI_SW['RT_Repeat_Block_8'].mean(),2), round(CI_SW['RT_Repeat_Block_9'].mean(),2), 
           round(CI_SW['RT_Repeat_Block_10'].mean(),2), round(CI_SW['RT_Repeat_Block_11'].mean(),2), round(CI_SW['RT_Repeat_Block_12'].mean(),2)]

CI_yA_RT= [round(CI_SW['RT_Alter_Block_7'].mean(),2), round(CI_SW['RT_Alter_Block_8'].mean(),2), round(CI_SW['RT_Alter_Block_9'].mean(),2), 
           round(CI_SW['RT_Alter_Block_10'].mean(),2), round(CI_SW['RT_Alter_Block_11'].mean(),2), round(CI_SW['RT_Alter_Block_12'].mean(),2)]


CI_yR_std= [round(CI_SW['ACC_Repeat_Block_7'].std(),2), round(CI_SW['ACC_Repeat_Block_8'].std(),2), round(CI_SW['ACC_Repeat_Block_9'].std(),2), 
            round(CI_SW['ACC_Repeat_Block_10'].std(),2), round(CI_SW['ACC_Repeat_Block_11'].std(),2), round(CI_SW['ACC_Repeat_Block_12'].std(),2)]
    
CI_yA_std= [round(CI_SW['ACC_Alter_Block_7'].std(),2), round(CI_SW['ACC_Alter_Block_8'].std(),2), round(CI_SW['ACC_Alter_Block_9'].std(),2), 
            round(CI_SW['ACC_Alter_Block_10'].std(),2), round(CI_SW['ACC_Alter_Block_11'].std(),2), round(CI_SW['ACC_Alter_Block_12'].std(),2)]

CI_yR_RT_std= [round(CI_SW['RT_Repeat_Block_7'].std(),2), round(CI_SW['RT_Repeat_Block_8'].std(),2), round(CI_SW['RT_Repeat_Block_9'].std(),2), 
               round(CI_SW['RT_Repeat_Block_10'].std(),2), round(CI_SW['RT_Repeat_Block_11'].std(),2), round(CI_SW['RT_Repeat_Block_12'].std(),2)]

CI_yA_RT_std= [round(CI_SW['RT_Alter_Block_7'].std(),2), round(CI_SW['RT_Alter_Block_8'].std(),2), round(CI_SW['RT_Alter_Block_9'].std(),2), 
               round(CI_SW['RT_Alter_Block_10'].std(),2), round(CI_SW['RT_Alter_Block_11'].std(),2), round(CI_SW['RT_Alter_Block_12'].std(),2)]
              
plt.clf()
plt.plot(x_axis, CI_yR, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_yA , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean ACC Context_Interleaved",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.legend()
plt.ylim((70, 100))
plt.show()


plt.clf()
plt.plot(x_axis, CI_yR_RT, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_yA_RT , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean RT Context_Interleaved",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.legend()
plt.ylim((1100, 2000))
plt.show()



#### BAR Plot ##########

import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = CI_yR
women_means = CI_yA


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= CI_yR_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= CI_yA_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Accuracy')
ax.set_title('Context_Interleaved Mean ACC by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

######################## RT ######################
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = CI_yR_RT
women_means = CI_yA_RT


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= CI_yR_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= CI_yA_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Reaction Time')
ax.set_title('Context_Interleaved Mean RT by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 2250)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
###########################################################################################################
CBN_SW= pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day2//df_Switch_Cost_Context_Blocked_NewVersion.csv')

CBN_yR= [round(CBN_SW['ACC_Repeat_Block_7'].mean(),2), round(CBN_SW['ACC_Repeat_Block_8'].mean(),2), round(CBN_SW['ACC_Repeat_Block_9'].mean(),2), 
         round(CBN_SW['ACC_Repeat_Block_10'].mean(),2), round(CBN_SW['ACC_Repeat_Block_11'].mean(),2), round(CBN_SW['ACC_Repeat_Block_12'].mean(),2)]
    
CBN_yA= [round(CBN_SW['ACC_Alter_Block_7'].mean(),2), round(CBN_SW['ACC_Alter_Block_8'].mean(),2), round(CBN_SW['ACC_Alter_Block_9'].mean(),2), 
         round(CBN_SW['ACC_Alter_Block_10'].mean(),2), round(CBN_SW['ACC_Alter_Block_11'].mean(),2), round(CBN_SW['ACC_Alter_Block_12'].mean(),2)]

CBN_yR_RT= [round(CBN_SW['RT_Repeat_Block_7'].mean(),2), round(CBN_SW['RT_Repeat_Block_8'].mean(),2), round(CBN_SW['RT_Repeat_Block_9'].mean(),2), 
            round(CBN_SW['RT_Repeat_Block_10'].mean(),2), round(CBN_SW['RT_Repeat_Block_11'].mean(),2), round(CBN_SW['RT_Repeat_Block_12'].mean(),2)]

CBN_yA_RT= [round(CBN_SW['RT_Alter_Block_7'].mean(),2), round(CBN_SW['RT_Alter_Block_8'].mean(),2), round(CBN_SW['RT_Alter_Block_9'].mean(),2), 
            round(CBN_SW['RT_Alter_Block_10'].mean(),2), round(CBN_SW['RT_Alter_Block_11'].mean(),2), round(CBN_SW['RT_Alter_Block_12'].mean(),2)]
         

CBN_yR_std= [round(CBN_SW['ACC_Repeat_Block_7'].std(),2), round(CBN_SW['ACC_Repeat_Block_8'].std(),2), round(CBN_SW['ACC_Repeat_Block_9'].std(),2), 
             round(CBN_SW['ACC_Repeat_Block_10'].std(),2), round(CBN_SW['ACC_Repeat_Block_11'].std(),2), round(CBN_SW['ACC_Repeat_Block_12'].std(),2)]
    
CBN_yA_std= [round(CBN_SW['ACC_Alter_Block_7'].std(),2), round(CBN_SW['ACC_Alter_Block_8'].std(),2), round(CBN_SW['ACC_Alter_Block_9'].std(),2), 
             round(CBN_SW['ACC_Alter_Block_10'].std(),2), round(CBN_SW['ACC_Alter_Block_11'].std(),2), round(CBN_SW['ACC_Alter_Block_12'].std(),2)]

CBN_yR_RT_std= [round(CBN_SW['RT_Repeat_Block_7'].std(),2), round(CBN_SW['RT_Repeat_Block_8'].std(),2), round(CBN_SW['RT_Repeat_Block_9'].std(),2), 
                round(CBN_SW['RT_Repeat_Block_10'].std(),2), round(CBN_SW['RT_Repeat_Block_11'].std(),2), round(CBN_SW['RT_Repeat_Block_12'].std(),2)]

CBN_yA_RT_std= [round(CBN_SW['RT_Alter_Block_7'].std(),2), round(CBN_SW['RT_Alter_Block_8'].std(),2), round(CBN_SW['RT_Alter_Block_9'].std(),2), 
                round(CBN_SW['RT_Alter_Block_10'].std(),2), round(CBN_SW['RT_Alter_Block_11'].std(),2), round(CBN_SW['RT_Alter_Block_12'].std(),2)]
         
plt.clf()
plt.plot(x_axis, CBN_yR, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_yA , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean ACC Context_Blocked Labels",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.legend()
plt.ylim((70, 100))
plt.show()


plt.clf()
plt.plot(x_axis, CBN_yR_RT, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_yA_RT , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean RT Context_Blocked Labels",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.legend()
plt.ylim((1100, 2000))
plt.show()


#### BAR Plot ##########

import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = CBN_yR
women_means = CBN_yA


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= CBN_yR_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= CBN_yA_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Accuracy')
ax.set_title('Context_Blocked labels Mean ACC by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

######################## RT ######################
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = CBN_yR_RT
women_means = CBN_yA_RT


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= CBN_yR_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= CBN_yA_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Reaction Time')
ax.set_title('Context_Blocked Labels Mean RT by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 2250)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
#######################################################################################################
############################################ SWitch Cost Stimulus Blocked #############################
#######################################################################################################

SB_SW=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//df_Switch_Cost_Stimulus_Blocked_Labels.csv')

SB_yR= [round(SB_SW['ACC_Repeat_Block_7'].mean(),2), round(SB_SW['ACC_Repeat_Block_8'].mean(),2), round(SB_SW['ACC_Repeat_Block_9'].mean(),2), 
        round(SB_SW['ACC_Repeat_Block_10'].mean(),2), round(SB_SW['ACC_Repeat_Block_11'].mean(),2), round(SB_SW['ACC_Repeat_Block_12'].mean(),2)]
    
SB_yA= [round(SB_SW['ACC_Alter_Block_7'].mean(),2), round(SB_SW['ACC_Alter_Block_8'].mean(),2), round(SB_SW['ACC_Alter_Block_9'].mean(),2), 
        round(SB_SW['ACC_Alter_Block_10'].mean(),2), round(SB_SW['ACC_Alter_Block_11'].mean(),2), round(SB_SW['ACC_Alter_Block_12'].mean(),2)]

SB_yR_RT= [round(SB_SW['RT_Repeat_Block_7'].mean(),2), round(SB_SW['RT_Repeat_Block_8'].mean(),2), round(SB_SW['RT_Repeat_Block_9'].mean(),2), 
           round(SB_SW['RT_Repeat_Block_10'].mean(),2), round(SB_SW['RT_Repeat_Block_11'].mean(),2), round(SB_SW['RT_Repeat_Block_12'].mean(),2)]

SB_yA_RT= [round(SB_SW['RT_Alter_Block_7'].mean(),2), round(SB_SW['RT_Alter_Block_8'].mean(),2), round(SB_SW['RT_Alter_Block_9'].mean(),2), 
           round(SB_SW['RT_Alter_Block_10'].mean(),2), round(SB_SW['RT_Alter_Block_11'].mean(),2), round(SB_SW['RT_Alter_Block_12'].mean(),2)]


SB_yR_std= [round(SB_SW['ACC_Repeat_Block_7'].std(),2), round(SB_SW['ACC_Repeat_Block_8'].std(),2), round(SB_SW['ACC_Repeat_Block_9'].std(),2), 
            round(SB_SW['ACC_Repeat_Block_10'].std(),2), round(SB_SW['ACC_Repeat_Block_11'].std(),2), round(SB_SW['ACC_Repeat_Block_12'].std(),2)]
    
SB_yA_std= [round(SB_SW['ACC_Alter_Block_7'].std(),2), round(SB_SW['ACC_Alter_Block_8'].std(),2), round(SB_SW['ACC_Alter_Block_9'].std(),2), 
            round(SB_SW['ACC_Alter_Block_10'].std(),2), round(SB_SW['ACC_Alter_Block_11'].std(),2), round(SB_SW['ACC_Alter_Block_12'].std(),2)]

SB_yR_RT_std= [round(SB_SW['RT_Repeat_Block_7'].std(),2), round(SB_SW['RT_Repeat_Block_8'].std(),2), round(SB_SW['RT_Repeat_Block_9'].std(),2), 
               round(SB_SW['RT_Repeat_Block_10'].std(),2), round(SB_SW['RT_Repeat_Block_11'].std(),2), round(SB_SW['RT_Repeat_Block_12'].std(),2)]

SB_yA_RT_std= [round(SB_SW['RT_Alter_Block_7'].std(),2), round(SB_SW['RT_Alter_Block_8'].std(),2), round(SB_SW['RT_Alter_Block_9'].std(),2), 
               round(SB_SW['RT_Alter_Block_10'].std(),2), round(SB_SW['RT_Alter_Block_11'].std(),2), round(SB_SW['RT_Alter_Block_12'].std(),2)]
                  
plt.clf()
plt.plot(x_axis, SB_yR, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, SB_yA , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean ACC Stimulus_Blocked Labels",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.legend()
plt.ylim((70, 100))
plt.show()


plt.clf()
plt.plot(x_axis, SB_yR_RT, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, SB_yA_RT , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean RT Stimulus_Blocked Labels",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.legend()
plt.ylim((1100, 2000))
plt.show()



#### BAR Plot ##########
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = SB_yR
women_means = SB_yA


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= SB_yR_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= SB_yA_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Accuracy')
ax.set_title('Stimulus_Blocked labels Mean ACC by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

######################## RT ######################
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = SB_yR_RT
women_means = SB_yA_RT


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= SB_yR_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= SB_yA_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Reaction Time')
ax.set_title('Stimulus_Blocked Labels Mean RT by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 2250)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
###################################################################################################
############################ Switch Cost Stimulus Interleaved ####################################
##################################################################################################

SI_SW=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_Switch_Cost_Stimulus_Interleaved.csv')

SI_yR= [round(SI_SW['ACC_Repeat_Block_7'].mean(),2), round(SI_SW['ACC_Repeat_Block_8'].mean(),2), round(SI_SW['ACC_Repeat_Block_9'].mean(),2), 
        round(SI_SW['ACC_Repeat_Block_10'].mean(),2), round(SI_SW['ACC_Repeat_Block_11'].mean(),2), round(SI_SW['ACC_Repeat_Block_12'].mean(),2)]
    
SI_yA= [round(SI_SW['ACC_Alter_Block_7'].mean(),2), round(SI_SW['ACC_Alter_Block_8'].mean(),2), round(SI_SW['ACC_Alter_Block_9'].mean(),2), 
        round(SI_SW['ACC_Alter_Block_10'].mean(),2), round(SI_SW['ACC_Alter_Block_11'].mean(),2), round(SI_SW['ACC_Alter_Block_12'].mean(),2)]

SI_yR_RT= [round(SI_SW['RT_Repeat_Block_7'].mean(),2), round(SI_SW['RT_Repeat_Block_8'].mean(),2), round(SI_SW['RT_Repeat_Block_9'].mean(),2), 
           round(SI_SW['RT_Repeat_Block_10'].mean(),2), round(SI_SW['RT_Repeat_Block_11'].mean(),2), round(SI_SW['RT_Repeat_Block_12'].mean(),2)]

SI_yA_RT= [round(SI_SW['RT_Alter_Block_7'].mean(),2), round(SI_SW['RT_Alter_Block_8'].mean(),2), round(SI_SW['RT_Alter_Block_9'].mean(),2), 
           round(SI_SW['RT_Alter_Block_10'].mean(),2), round(SI_SW['RT_Alter_Block_11'].mean(),2), round(SI_SW['RT_Alter_Block_12'].mean(),2)]
 
SI_yR_std= [round(SI_SW['ACC_Repeat_Block_7'].std(),2), round(SI_SW['ACC_Repeat_Block_8'].std(),2), round(SI_SW['ACC_Repeat_Block_9'].std(),2), 
            round(SI_SW['ACC_Repeat_Block_10'].std(),2), round(SI_SW['ACC_Repeat_Block_11'].std(),2), round(SI_SW['ACC_Repeat_Block_12'].std(),2)]
    
SI_yA_std= [round(SI_SW['ACC_Alter_Block_7'].std(),2), round(SI_SW['ACC_Alter_Block_8'].std(),2), round(SI_SW['ACC_Alter_Block_9'].std(),2), 
            round(SI_SW['ACC_Alter_Block_10'].std(),2), round(SI_SW['ACC_Alter_Block_11'].std(),2), round(SI_SW['ACC_Alter_Block_12'].std(),2)]

SI_yR_RT_std= [round(SI_SW['RT_Repeat_Block_7'].std(),2), round(SI_SW['RT_Repeat_Block_8'].std(),2), round(SI_SW['RT_Repeat_Block_9'].std(),2), 
               round(SI_SW['RT_Repeat_Block_10'].std(),2), round(SI_SW['RT_Repeat_Block_11'].std(),2), round(SI_SW['RT_Repeat_Block_12'].std(),2)]

SI_yA_RT_std= [round(SI_SW['RT_Alter_Block_7'].std(),2), round(SI_SW['RT_Alter_Block_8'].std(),2), round(SI_SW['RT_Alter_Block_9'].std(),2), 
               round(SI_SW['RT_Alter_Block_10'].std(),2), round(SI_SW['RT_Alter_Block_11'].std(),2), round(SI_SW['RT_Alter_Block_12'].std(),2)]
         
        
plt.clf()
plt.plot(x_axis, SI_yR, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, SI_yA , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean ACC Stimulus_Interleaved Labels",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.legend()
plt.ylim((70, 100))
plt.show()


plt.clf()
plt.plot(x_axis, SI_yR_RT, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, SI_yA_RT , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean RT Stimulus_Interleaved Labels",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.legend()
plt.ylim((1100, 2000))
plt.show()


#### BAR Plot ##########
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = SI_yR
women_means = SI_yA


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= SI_yR_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= SI_yA_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Accuracy')
ax.set_title('Stimulus_Interleaved Mean ACC by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

######################## RT ######################
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = SI_yR_RT
women_means = SI_yA_RT


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= SB_yR_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= SB_yA_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Reaction Time')
ax.set_title('Stimulus_Interleaved Mean RT by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 2250)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
####################################################################################################
####################### SWitch Cost Stimulus Blocked Planet #####################################

SBN_SW=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day2//df_Switch_Cost_Stimulus_Blocked_New_Version.csv')

SBN_yR= [round(SBN_SW['ACC_Repeat_Block_7'].mean(),2), round(SBN_SW['ACC_Repeat_Block_8'].mean(),2), round(SBN_SW['ACC_Repeat_Block_9'].mean(),2), 
         round(SBN_SW['ACC_Repeat_Block_10'].mean(),2), round(SBN_SW['ACC_Repeat_Block_11'].mean(),2), round(SBN_SW['ACC_Repeat_Block_12'].mean(),2)]
    
SBN_yA= [round(SBN_SW['ACC_Alter_Block_7'].mean(),2), round(SBN_SW['ACC_Alter_Block_8'].mean(),2), round(SBN_SW['ACC_Alter_Block_9'].mean(),2), 
         round(SBN_SW['ACC_Alter_Block_10'].mean(),2), round(SBN_SW['ACC_Alter_Block_11'].mean(),2), round(SBN_SW['ACC_Alter_Block_12'].mean(),2)]

SBN_yR_RT= [round(SBN_SW['RT_Repeat_Block_7'].mean(),2), round(SBN_SW['RT_Repeat_Block_8'].mean(),2), round(SBN_SW['RT_Repeat_Block_9'].mean(),2), 
            round(SBN_SW['RT_Repeat_Block_10'].mean(),2), round(SBN_SW['RT_Repeat_Block_11'].mean(),2), round(SBN_SW['RT_Repeat_Block_12'].mean(),2)]

SBN_yA_RT= [round(SBN_SW['RT_Alter_Block_7'].mean(),2), round(SBN_SW['RT_Alter_Block_8'].mean(),2), round(SBN_SW['RT_Alter_Block_9'].mean(),2), 
            round(SBN_SW['RT_Alter_Block_10'].mean(),2), round(SBN_SW['RT_Alter_Block_11'].mean(),2), round(SBN_SW['RT_Alter_Block_12'].mean(),2)]


SBN_yR_std= [round(SBN_SW['ACC_Repeat_Block_7'].std(),2), round(SBN_SW['ACC_Repeat_Block_8'].std(),2), round(SBN_SW['ACC_Repeat_Block_9'].std(),2), 
             round(SBN_SW['ACC_Repeat_Block_10'].std(),2), round(SBN_SW['ACC_Repeat_Block_11'].std(),2), round(SBN_SW['ACC_Repeat_Block_12'].std(),2)]
    
SBN_yA_std= [round(SBN_SW['ACC_Alter_Block_7'].std(),2), round(SBN_SW['ACC_Alter_Block_8'].std(),2), round(SBN_SW['ACC_Alter_Block_9'].std(),2), 
             round(SBN_SW['ACC_Alter_Block_10'].std(),2), round(SBN_SW['ACC_Alter_Block_11'].std(),2), round(SBN_SW['ACC_Alter_Block_12'].std(),2)]

SBN_yR_RT_std= [round(SBN_SW['RT_Repeat_Block_7'].std(),2), round(SBN_SW['RT_Repeat_Block_8'].std(),2), round(SBN_SW['RT_Repeat_Block_9'].std(),2), 
                round(SBN_SW['RT_Repeat_Block_10'].std(),2), round(SBN_SW['RT_Repeat_Block_11'].std(),2), round(SBN_SW['RT_Repeat_Block_12'].std(),2)]

SBN_yA_RT_std= [round(SBN_SW['RT_Alter_Block_7'].std(),2), round(SBN_SW['RT_Alter_Block_8'].std(),2), round(SBN_SW['RT_Alter_Block_9'].std(),2), 
                round(SBN_SW['RT_Alter_Block_10'].std(),2), round(SBN_SW['RT_Alter_Block_11'].std(),2), round(SBN_SW['RT_Alter_Block_12'].std(),2)]
                  
plt.clf()
plt.plot(x_axis, SBN_yR, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, SBN_yA , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean ACC Stimulus_Blocked Planet",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.legend()
plt.ylim((70, 100))
plt.show()


plt.clf()
plt.plot(x_axis, SBN_yR_RT, 's:',label = "Repetition", color='#95baf5',markersize=12)
plt.plot(x_axis, SBN_yA_RT , 'o-',label = "Alteration", color='#95baf5',markersize=12)
plt.xticks(rotation=45)
plt.title("Mean RT Stimulus_Blocked Planet",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.legend()
plt.ylim((1100, 2000))
plt.show()

#### BAR Plot ##########
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = SBN_yR
women_means = SBN_yA


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= SBN_yR_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= SBN_yA_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Accuracy')
ax.set_title('Stimulus_Blocked Planet Mean ACC by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

######################## RT ######################
import matplotlib.pyplot as plt
import numpy as np
#.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
labels = ['Block 7', 'Block 8', 'Block 9', 'Block 10', 'Block 11', 'Block 12']

men_means = SBN_yR_RT
women_means = SBN_yA_RT


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means,  width, label='Repetition', yerr= SBN_yR_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
rects2 = ax.bar(x + width / 2, women_means, width, label='Alteration', yerr= SBN_yA_RT_std, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Reaction Time')
ax.set_title('Stimulus_Blocked Planet Mean RT by Block and Repetition VS Alteration trails')
ax.set_ylim(0, 2250)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()

def autolabel(rects):
   for rect in rects:
      height = rect.get_height()
      ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width() / 2, height),
         xytext=(0, 3), # 3 points vertical offset
         textcoords="offset points",
         ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
#########################################################################################
###################### SWitch Cost Multi Plot ACC #######################################
##########################################################################################


# Repetition ###
plt.xticks(rotation=45) 
plt.plot(x_axis, CB_yR, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_yR , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_yR, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SB_yR, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_yR, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SBN_yR, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Blocks') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy Repetition",fontsize=20)
plt.legend()
plt.show()


# Alteration ###
plt.xticks(rotation=45) 
plt.plot(x_axis, CB_yA, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_yA , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_yA, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SB_yA, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_yA, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SBN_yA, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Blocks') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy Alteration",fontsize=20)
plt.legend()
plt.show()



############################## RT ###################################
# Repetition ###
plt.xticks(rotation=45) 
plt.plot(x_axis, CB_yR_RT, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_yR_RT , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_yR_RT, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SB_yR_RT, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_yR_RT, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SBN_yR_RT, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Blocks') 
plt.ylabel('Mean RT')
plt.title("Mean RT Repetition",fontsize=20)
plt.legend()
plt.show()


# Alteration ###
plt.xticks(rotation=45) 
plt.plot(x_axis, CB_yA_RT, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_yA_RT , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_yA_RT, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SB_yA_RT, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_yA_RT, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SBN_yA_RT, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Blocks') 
plt.ylabel('Mean RT')
plt.title("Mean RT Alteration",fontsize=20)
plt.legend()
plt.show()






