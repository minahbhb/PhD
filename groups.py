import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv

Context_Blocked=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_ACC_Critera_Whole_Train.csv')
Context_Interleaved=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_2_Data_Pilot_Run//df_Total_Context_Interleaved_Two_Days_ACC_Critera_Whole_Train.csv')
Context_Blocked_Labeling=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day2//df_Total_Context_Blocked_NewVersuion_Two_Days_ACC_Critera_Whole_Train.csv')

Stimulus_Blocked=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//df_Total_Stimulus_Blocked_Two_Days_ACC_Critera_Whole_Train.csv')
Stimulus_Interleaved=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_Total_Stimulus_Interleaved_Two_Days_ACC_Critera_Whole_Train.csv')
Stimulus_Blocked_New_Version=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day2//df_Total_Stimulus_Blocked_New_Version_Two_Days_ACC_Critera_Whole_Train.csv')

plt.style.use('seaborn')
#
#plt.xkcd() #comic style

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']
#plt.figure(figsize=(6, 3))


y1= [Context_Blocked['ACC_block_1'].mean(),Context_Blocked['ACC_block_2'].mean(),Context_Blocked['ACC_block_3'].mean(), 
     Context_Blocked['ACC_block_4'].mean(),Context_Blocked['ACC_block_5'].mean(),Context_Blocked['ACC_block_6'].mean(),
     Context_Blocked['ACC_block_7'].mean(),Context_Blocked['ACC_block_8'].mean(),Context_Blocked['ACC_block_9'].mean(),
     Context_Blocked['ACC_block_10'].mean(),Context_Blocked['ACC_block_11'].mean(),Context_Blocked['ACC_block_12'].mean()]

y2= [Context_Interleaved['ACC_block_1'].mean(),Context_Interleaved['ACC_block_2'].mean(),Context_Interleaved['ACC_block_3'].mean(), 
     Context_Interleaved['ACC_block_4'].mean(),Context_Interleaved['ACC_block_5'].mean(),Context_Interleaved['ACC_block_6'].mean(),
     Context_Interleaved['ACC_block_7'].mean(),Context_Interleaved['ACC_block_8'].mean(),Context_Interleaved['ACC_block_9'].mean(),
     Context_Interleaved['ACC_block_10'].mean(),Context_Interleaved['ACC_block_11'].mean(),Context_Interleaved['ACC_block_12'].mean()]

y3= [Stimulus_Blocked['ACC_block_1'].mean(),Stimulus_Blocked['ACC_block_2'].mean(),Stimulus_Blocked['ACC_block_3'].mean(), 
     Stimulus_Blocked['ACC_block_4'].mean(),Stimulus_Blocked['ACC_block_5'].mean(),Stimulus_Blocked['ACC_block_6'].mean(),
     Stimulus_Blocked['ACC_block_7'].mean(),Stimulus_Blocked['ACC_block_8'].mean(),Stimulus_Blocked['ACC_block_9'].mean(),
     Stimulus_Blocked['ACC_block_10'].mean(),Stimulus_Blocked['ACC_block_11'].mean(),Stimulus_Blocked['ACC_block_12'].mean()]


y4= [Stimulus_Interleaved['ACC_block_1'].mean(),Stimulus_Interleaved['ACC_block_2'].mean(),Stimulus_Interleaved['ACC_block_3'].mean(), 
     Stimulus_Interleaved['ACC_block_4'].mean(),Stimulus_Interleaved['ACC_block_5'].mean(),Stimulus_Interleaved['ACC_block_6'].mean(),
     Stimulus_Interleaved['ACC_block_7'].mean(),Stimulus_Interleaved['ACC_block_8'].mean(),Stimulus_Interleaved['ACC_block_9'].mean(),
     Stimulus_Interleaved['ACC_block_10'].mean(),Stimulus_Interleaved['ACC_block_11'].mean(),Stimulus_Interleaved['ACC_block_12'].mean()]

y5=[Stimulus_Blocked_New_Version['ACC_block_1'].mean(),Stimulus_Blocked_New_Version['ACC_block_2'].mean(),Stimulus_Blocked_New_Version['ACC_block_3'].mean(), 
    Stimulus_Blocked_New_Version['ACC_block_4'].mean(),Stimulus_Blocked_New_Version['ACC_block_5'].mean(),Stimulus_Blocked_New_Version['ACC_block_6'].mean(),
    Stimulus_Blocked_New_Version['ACC_block_7'].mean(),Stimulus_Blocked_New_Version['ACC_block_8'].mean(),Stimulus_Blocked_New_Version['ACC_block_9'].mean(),
    Stimulus_Blocked_New_Version['ACC_block_10'].mean(),Stimulus_Blocked_New_Version['ACC_block_11'].mean(),Stimulus_Blocked_New_Version['ACC_block_12'].mean()]

y6=[Context_Blocked_Labeling['ACC_block_1'].mean(),Context_Blocked_Labeling['ACC_block_2'].mean(), Context_Blocked_Labeling['ACC_block_3'].mean(),
    Context_Blocked_Labeling['ACC_block_4'].mean(), Context_Blocked_Labeling['ACC_block_5'].mean(), Context_Blocked_Labeling['ACC_block_6'].mean(),
    Context_Blocked_Labeling['ACC_block_7'].mean(), Context_Blocked_Labeling['ACC_block_8'].mean(), Context_Blocked_Labeling['ACC_block_9'].mean(),
    Context_Blocked_Labeling['ACC_block_10'].mean(), Context_Blocked_Labeling['ACC_block_11'].mean(), Context_Blocked_Labeling['ACC_block_12'].mean(),]




plt.xticks(rotation=45)
plt.plot(x_axis, y1, 'o-',label = "Context_Blocked No Labeling")
#plt.plot(x_axis, y2, '*-',label = "Context_Interleaved")
plt.plot(x_axis, y3, 'o-',label = "Stimulus_Blocked Labeling")
#plt.plot(x_axis, y4, '*-',label = "Stimulus_Interleaved")
plt.plot(x_axis, y5, '^-',label = "Stimulus_Blocked_No Labeling")
plt.plot(x_axis, y6, '^-',label = "Context Blocked Labeling")
plt.title("ACC Criteria Whole Training Blocks",fontsize=16)
plt.legend()
plt.show()

######################################################################################################################
############################################# ACC 456 #################################################################
#######################################################################################################################

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import csv
Context_Blocked_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_ACC_Critera_456_Train.csv')
Context_Interleaved_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_2_Data_Pilot_Run//df_Total_Context_Interleaved_Two_Days_ACC_Critera_456_Train.csv')
Stimulus_Blocked_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//df_Total_Stimulus_Blocked_Two_Days_ACC_Critera_456_Train.csv')
Stimulus_Interleaved_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_Total_Stimulus_Interleaved_Two_Days_ACC_Critera_456_Train.csv')
Stimulus_Blocked_New_Version_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day2//df_Total_Stimulus_Blocked_New_Version_Two_Days_ACC_Critera_456_Train.csv')
Context_Blocked_New_Version_456= pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day2//df_Total_Context_Blocked_NewVersion_Two_Days_ACC_Critera_456_Train.csv')

#plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style

# list of x axis 
#x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9']
#plt.figure(figsize=(6, 3))

'''
y1= [Context_Blocked_456['ACC_block_1'].mean(),Context_Blocked_456['ACC_block_2'].mean(),Context_Blocked_456['ACC_block_3'].mean(), 
     Context_Blocked_456['ACC_block_4'].mean(),Context_Blocked_456['ACC_block_5'].mean(),Context_Blocked_456['ACC_block_6'].mean(),
     Context_Blocked_456['ACC_block_7'].mean(),Context_Blocked_456['ACC_block_8'].mean(),Context_Blocked_456['ACC_block_9'].mean(),
     Context_Blocked_456['ACC_block_10'].mean(),Context_Blocked_456['ACC_block_11'].mean(),Context_Blocked_456['ACC_block_12'].mean()]

y2= [Context_Interleaved_456['ACC_block_1'].mean(),Context_Interleaved_456['ACC_block_2'].mean(),Context_Interleaved_456['ACC_block_3'].mean(), 
     Context_Interleaved_456['ACC_block_4'].mean(),Context_Interleaved_456['ACC_block_5'].mean(),Context_Interleaved_456['ACC_block_6'].mean(),
     Context_Interleaved_456['ACC_block_7'].mean(),Context_Interleaved_456['ACC_block_8'].mean(),Context_Interleaved_456['ACC_block_9'].mean(),
     Context_Interleaved_456['ACC_block_10'].mean(),Context_Interleaved_456['ACC_block_11'].mean(),Context_Interleaved_456['ACC_block_12'].mean()]

y3= [Stimulus_Blocked_456['ACC_block_1'].mean(),Stimulus_Blocked_456['ACC_block_2'].mean(),Stimulus_Blocked_456['ACC_block_3'].mean(), 
     Stimulus_Blocked_456['ACC_block_4'].mean(),Stimulus_Blocked_456['ACC_block_5'].mean(),Stimulus_Blocked_456['ACC_block_6'].mean(),
     Stimulus_Blocked_456['ACC_block_7'].mean(),Stimulus_Blocked_456['ACC_block_8'].mean(),Stimulus_Blocked_456['ACC_block_9'].mean(),
     Stimulus_Blocked_456['ACC_block_10'].mean(),Stimulus_Blocked_456['ACC_block_11'].mean(),Stimulus_Blocked_456['ACC_block_12'].mean()]


y4= [Stimulus_Interleaved_456['ACC_block_1'].mean(),Stimulus_Interleaved_456['ACC_block_2'].mean(),Stimulus_Interleaved_456['ACC_block_3'].mean(), 
     Stimulus_Interleaved_456['ACC_block_4'].mean(),Stimulus_Interleaved_456['ACC_block_5'].mean(),Stimulus_Interleaved_456['ACC_block_6'].mean(),
     Stimulus_Interleaved_456['ACC_block_7'].mean(),Stimulus_Interleaved_456['ACC_block_8'].mean(),Stimulus_Interleaved_456['ACC_block_9'].mean(),
     Stimulus_Interleaved_456['ACC_block_10'].mean(),Stimulus_Interleaved_456['ACC_block_11'].mean(),Stimulus_Interleaved_456['ACC_block_12'].mean()]

y5=[Stimulus_Blocked_New_Version_456['ACC_block_1'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_2'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_3'].mean(), 
    Stimulus_Blocked_New_Version_456['ACC_block_4'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_5'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_6'].mean(),
    Stimulus_Blocked_New_Version_456['ACC_block_7'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_8'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_9'].mean(),
    Stimulus_Blocked_New_Version_456['ACC_block_10'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_11'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_12'].mean()]

y6=[Context_Blocked_New_Version_456['ACC_block_1'].mean(),Context_Blocked_New_Version_456['ACC_block_2'].mean(),Context_Blocked_New_Version_456['ACC_block_3'].mean(), 
    Context_Blocked_New_Version_456['ACC_block_4'].mean(),Context_Blocked_New_Version_456['ACC_block_5'].mean(),Context_Blocked_New_Version_456['ACC_block_6'].mean(),
    Context_Blocked_New_Version_456['ACC_block_7'].mean(),Context_Blocked_New_Version_456['ACC_block_8'].mean(),Context_Blocked_New_Version_456['ACC_block_9'].mean(),
    Context_Blocked_New_Version_456['ACC_block_10'].mean(),Context_Blocked_New_Version_456['ACC_block_11'].mean(),Context_Blocked_New_Version_456['ACC_block_12'].mean()]
'''
y1= [Context_Blocked_456['ACC_block_1'].mean(),Context_Blocked_456['ACC_block_2'].mean(),Context_Blocked_456['ACC_block_3'].mean(), 
     Context_Blocked_456['ACC_block_4'].mean(),Context_Blocked_456['ACC_block_5'].mean(),Context_Blocked_456['ACC_block_6'].mean(),
     Context_Blocked_456['ACC_block_7'].mean(),Context_Blocked_456['ACC_block_8'].mean(),Context_Blocked_456['ACC_block_9'].mean()]

y2= [Context_Interleaved_456['ACC_block_1'].mean(),Context_Interleaved_456['ACC_block_2'].mean(),Context_Interleaved_456['ACC_block_3'].mean(), 
     Context_Interleaved_456['ACC_block_4'].mean(),Context_Interleaved_456['ACC_block_5'].mean(),Context_Interleaved_456['ACC_block_6'].mean(),
     Context_Interleaved_456['ACC_block_7'].mean(),Context_Interleaved_456['ACC_block_8'].mean(),Context_Interleaved_456['ACC_block_9'].mean()]

y3= [Stimulus_Blocked_456['ACC_block_1'].mean(),Stimulus_Blocked_456['ACC_block_2'].mean(),Stimulus_Blocked_456['ACC_block_3'].mean(), 
     Stimulus_Blocked_456['ACC_block_4'].mean(),Stimulus_Blocked_456['ACC_block_5'].mean(),Stimulus_Blocked_456['ACC_block_6'].mean(),
     Stimulus_Blocked_456['ACC_block_7'].mean(),Stimulus_Blocked_456['ACC_block_8'].mean(),Stimulus_Blocked_456['ACC_block_9'].mean()]


y4= [Stimulus_Interleaved_456['ACC_block_1'].mean(),Stimulus_Interleaved_456['ACC_block_2'].mean(),Stimulus_Interleaved_456['ACC_block_3'].mean(), 
     Stimulus_Interleaved_456['ACC_block_4'].mean(),Stimulus_Interleaved_456['ACC_block_5'].mean(),Stimulus_Interleaved_456['ACC_block_6'].mean(),
     Stimulus_Interleaved_456['ACC_block_7'].mean(),Stimulus_Interleaved_456['ACC_block_8'].mean(),Stimulus_Interleaved_456['ACC_block_9'].mean()]

y5=[Stimulus_Blocked_New_Version_456['ACC_block_1'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_2'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_3'].mean(), 
    Stimulus_Blocked_New_Version_456['ACC_block_4'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_5'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_6'].mean(),
    Stimulus_Blocked_New_Version_456['ACC_block_7'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_8'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_9'].mean()]

y6=[Context_Blocked_New_Version_456['ACC_block_1'].mean(),Context_Blocked_New_Version_456['ACC_block_2'].mean(),Context_Blocked_New_Version_456['ACC_block_3'].mean(), 
    Context_Blocked_New_Version_456['ACC_block_4'].mean(),Context_Blocked_New_Version_456['ACC_block_5'].mean(),Context_Blocked_New_Version_456['ACC_block_6'].mean(),
    Context_Blocked_New_Version_456['ACC_block_7'].mean(),Context_Blocked_New_Version_456['ACC_block_8'].mean(),Context_Blocked_New_Version_456['ACC_block_9'].mean()]

y1_e= [Context_Blocked_456['ACC_block_1'].sem(),Context_Blocked_456['ACC_block_2'].sem(),Context_Blocked_456['ACC_block_3'].sem(), 
       Context_Blocked_456['ACC_block_4'].sem(),Context_Blocked_456['ACC_block_5'].sem(),Context_Blocked_456['ACC_block_6'].sem(),
       Context_Blocked_456['ACC_block_7'].sem(),Context_Blocked_456['ACC_block_8'].sem(),Context_Blocked_456['ACC_block_9'].sem()]

y2_e= [Context_Interleaved_456['ACC_block_1'].sem(),Context_Interleaved_456['ACC_block_2'].sem(),Context_Interleaved_456['ACC_block_3'].sem(), 
       Context_Interleaved_456['ACC_block_4'].sem(),Context_Interleaved_456['ACC_block_5'].sem(),Context_Interleaved_456['ACC_block_6'].sem(),
       Context_Interleaved_456['ACC_block_7'].sem(),Context_Interleaved_456['ACC_block_8'].sem(),Context_Interleaved_456['ACC_block_9'].sem()]

y3_e= [Stimulus_Blocked_456['ACC_block_1'].sem(),Stimulus_Blocked_456['ACC_block_2'].sem(),Stimulus_Blocked_456['ACC_block_3'].sem(), 
       Stimulus_Blocked_456['ACC_block_4'].sem(),Stimulus_Blocked_456['ACC_block_5'].sem(),Stimulus_Blocked_456['ACC_block_6'].sem(),
       Stimulus_Blocked_456['ACC_block_7'].sem(),Stimulus_Blocked_456['ACC_block_8'].sem(),Stimulus_Blocked_456['ACC_block_9'].sem()]


y4_e= [Stimulus_Interleaved_456['ACC_block_1'].sem(),Stimulus_Interleaved_456['ACC_block_2'].sem(),Stimulus_Interleaved_456['ACC_block_3'].sem(), 
     Stimulus_Interleaved_456['ACC_block_4'].sem(),Stimulus_Interleaved_456['ACC_block_5'].sem(),Stimulus_Interleaved_456['ACC_block_6'].sem(),
     Stimulus_Interleaved_456['ACC_block_7'].sem(),Stimulus_Interleaved_456['ACC_block_8'].sem(),Stimulus_Interleaved_456['ACC_block_9'].sem()]

y5_e=[Stimulus_Blocked_New_Version_456['ACC_block_1'].sem(),Stimulus_Blocked_New_Version_456['ACC_block_2'].sem(),Stimulus_Blocked_New_Version_456['ACC_block_3'].sem(), 
    Stimulus_Blocked_New_Version_456['ACC_block_4'].sem(),Stimulus_Blocked_New_Version_456['ACC_block_5'].sem(),Stimulus_Blocked_New_Version_456['ACC_block_6'].sem(),
    Stimulus_Blocked_New_Version_456['ACC_block_7'].sem(),Stimulus_Blocked_New_Version_456['ACC_block_8'].sem(),Stimulus_Blocked_New_Version_456['ACC_block_9'].sem()]

y6_e=[Context_Blocked_New_Version_456['ACC_block_1'].sem(),Context_Blocked_New_Version_456['ACC_block_2'].sem(),Context_Blocked_New_Version_456['ACC_block_3'].sem(), 
    Context_Blocked_New_Version_456['ACC_block_4'].sem(),Context_Blocked_New_Version_456['ACC_block_5'].sem(),Context_Blocked_New_Version_456['ACC_block_6'].sem(),
    Context_Blocked_New_Version_456['ACC_block_7'].sem(),Context_Blocked_New_Version_456['ACC_block_8'].sem(),Context_Blocked_New_Version_456['ACC_block_9'].sem()]

plt.figure(figsize=(10, 6))

plt.figure(dpi=1200)
plt.xticks(rotation=45) 
plt.errorbar(x_axis, y1, yerr =y1_e, ecolor = '#95baf5', capsize=3,marker='s', markersize=12, linestyle=':', label = "Context-First Without Response-Labeling", color='#95baf5')
#plt.plot(x_axis, y2, 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.errorbar(x_axis, y6, yerr =y6_e , ecolor = 'k', capsize=3,marker='s', markersize=12, linestyle='-', mec = 'k', label = "Context-First With Response-Labeling", color='#95baf5')
plt.errorbar(x_axis, y5, yerr =y5_e, ecolor = '#f09797', capsize=3, marker='s', markersize=12,linestyle=':', label = "Stimulus-First Without Response-Labeling", color='#f09797')
#plt.plot(x_axis, y4, 'o-',label = "Stimulus_Interleaved Task", color='#f09797',markersize=12)
plt.errorbar(x_axis, y3, yerr =y3_e, ecolor = 'k', capsize=3,marker= 's', markersize=12, linestyle='-',mec = 'k',label = "Stimulus-First With Response-Labeling",color='#f09797')
#plt.plot(x_axis, y5, 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy",fontsize=20)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.yticks(np.arange(0.6, 0.95, 0.05))
#plt.savefig(SBP_Path+'SBP_PCA_H2.pdf')
#plt.savefig(SBP_Path+'SBP_PCA_H2.png')
plt.show()



################################################################################################
############################## ACC RT 456 ###############################################

#RT
y1_RT= [Context_Blocked_456['RT_block_1'].mean(),Context_Blocked_456['RT_block_2'].mean(),Context_Blocked_456['RT_block_3'].mean(), 
        Context_Blocked_456['RT_block_4'].mean(),Context_Blocked_456['RT_block_5'].mean(),Context_Blocked_456['RT_block_6'].mean(),
        Context_Blocked_456['RT_block_7'].mean(),Context_Blocked_456['RT_block_8'].mean(),Context_Blocked_456['RT_block_9'].mean(),
        Context_Blocked_456['RT_block_10'].mean(),Context_Blocked_456['RT_block_11'].mean(),Context_Blocked_456['RT_block_12'].mean()]

y2_RT= [Context_Interleaved_456['RT_block_1'].mean(),Context_Interleaved_456['RT_block_2'].mean(),Context_Interleaved_456['RT_block_3'].mean(), 
        Context_Interleaved_456['RT_block_4'].mean(),Context_Interleaved_456['RT_block_5'].mean(),Context_Interleaved_456['RT_block_6'].mean(),
        Context_Interleaved_456['RT_block_7'].mean(),Context_Interleaved_456['RT_block_8'].mean(),Context_Interleaved_456['RT_block_9'].mean(),
        Context_Interleaved_456['RT_block_10'].mean(),Context_Interleaved_456['RT_block_11'].mean(),Context_Interleaved_456['RT_block_12'].mean()]

y3_RT= [Stimulus_Blocked_456['RT_block_1'].mean(),Stimulus_Blocked_456['RT_block_2'].mean(),Stimulus_Blocked_456['RT_block_3'].mean(), 
        Stimulus_Blocked_456['RT_block_4'].mean(),Stimulus_Blocked_456['RT_block_5'].mean(),Stimulus_Blocked_456['RT_block_6'].mean(),
        Stimulus_Blocked_456['RT_block_7'].mean(),Stimulus_Blocked_456['RT_block_8'].mean(),Stimulus_Blocked_456['RT_block_9'].mean(),
        Stimulus_Blocked_456['RT_block_10'].mean(),Stimulus_Blocked_456['RT_block_11'].mean(),Stimulus_Blocked_456['RT_block_12'].mean()]


y4_RT= [Stimulus_Interleaved_456['RT_block_1'].mean(),Stimulus_Interleaved_456['RT_block_2'].mean(),Stimulus_Interleaved_456['RT_block_3'].mean(), 
        Stimulus_Interleaved_456['RT_block_4'].mean(),Stimulus_Interleaved_456['RT_block_5'].mean(),Stimulus_Interleaved_456['RT_block_6'].mean(),
        Stimulus_Interleaved_456['RT_block_7'].mean(),Stimulus_Interleaved_456['RT_block_8'].mean(),Stimulus_Interleaved_456['RT_block_9'].mean(),
        Stimulus_Interleaved_456['RT_block_10'].mean(),Stimulus_Interleaved_456['RT_block_11'].mean(),Stimulus_Interleaved_456['RT_block_12'].mean()]

y5_RT=[Stimulus_Blocked_New_Version_456['RT_block_1'].mean(),Stimulus_Blocked_New_Version_456['RT_block_2'].mean(),Stimulus_Blocked_New_Version_456['RT_block_3'].mean(), 
       Stimulus_Blocked_New_Version_456['RT_block_4'].mean(),Stimulus_Blocked_New_Version_456['RT_block_5'].mean(),Stimulus_Blocked_New_Version_456['RT_block_6'].mean(),
       Stimulus_Blocked_New_Version_456['RT_block_7'].mean(),Stimulus_Blocked_New_Version_456['RT_block_8'].mean(),Stimulus_Blocked_New_Version_456['RT_block_9'].mean(),
       Stimulus_Blocked_New_Version_456['RT_block_10'].mean(),Stimulus_Blocked_New_Version_456['RT_block_11'].mean(),Stimulus_Blocked_New_Version_456['RT_block_12'].mean()]

y6_RT=[Context_Blocked_New_Version_456['RT_block_1'].mean(),Context_Blocked_New_Version_456['RT_block_2'].mean(),Context_Blocked_New_Version_456['RT_block_3'].mean(), 
       Context_Blocked_New_Version_456['RT_block_4'].mean(),Context_Blocked_New_Version_456['RT_block_5'].mean(),Context_Blocked_New_Version_456['RT_block_6'].mean(),
       Context_Blocked_New_Version_456['RT_block_7'].mean(),Context_Blocked_New_Version_456['RT_block_8'].mean(),Context_Blocked_New_Version_456['RT_block_9'].mean(),
       Context_Blocked_New_Version_456['RT_block_10'].mean(),Context_Blocked_New_Version_456['RT_block_11'].mean(),Context_Blocked_New_Version_456['RT_block_12'].mean()]

plt.xticks(rotation=45)
plt.plot(x_axis, y1_RT, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
#plt.plot(x_axis, y2_RT, 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, y6_RT, 's-',mec = 'k',label = "Context_Blocked_Task", color='#95baf5',markersize=12)
plt.plot(x_axis, y5_RT, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
#plt.plot(x_axis, y4_RT, 'o-',label = "Stimulus_Interleaved Task", color='#f09797',markersize=12)
plt.plot(x_axis, y3_RT, 's-',mec = 'k',label = "Stimulus_Blocked Task", color='#f09797',markersize=12)
#plt.plot(x_axis, y5_RT, 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6_RT, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.title("Mean Reaction Time",fontsize=20)
#plt.legend()
plt.show()


##################################################################################################
##################################### ACC Bar 456 #################################################
####################################################################################################
from statistics import mean
from statistics import stdev

Mean_Acc_Context_Blocked={'ACC(B1B2B3)':round(mean([Context_Blocked_456['ACC_block_1'].mean(),Context_Blocked_456['ACC_block_2'].mean(),Context_Blocked_456['ACC_block_3'].mean()]),3),
                          'ACC(B4B5B6)':round(mean([Context_Blocked_456['ACC_block_4'].mean(),Context_Blocked_456['ACC_block_5'].mean(),Context_Blocked_456['ACC_block_6'].mean()]),3),
                          'ACC(B7B8B9)':round(mean([Context_Blocked_456['ACC_block_7'].mean(),Context_Blocked_456['ACC_block_8'].mean(),Context_Blocked_456['ACC_block_9'].mean()]),3),
                          'ACC(B10B11B12)':round(mean([Context_Blocked_456['ACC_block_10'].mean(),Context_Blocked_456['ACC_block_11'].mean(),Context_Blocked_456['ACC_block_12'].mean()]),3)}


Mean_Acc_Context_Blocked_std={'ACC(B1B2B3)':round(stdev([Context_Blocked_456['ACC_block_1'].mean(),Context_Blocked_456['ACC_block_2'].mean(),Context_Blocked_456['ACC_block_3'].mean()]),3),
                              'ACC(B4B5B6)':round(stdev([Context_Blocked_456['ACC_block_4'].mean(),Context_Blocked_456['ACC_block_5'].mean(),Context_Blocked_456['ACC_block_6'].mean()]),3),
                              'ACC(B7B8B9)':round(stdev([Context_Blocked_456['ACC_block_7'].mean(),Context_Blocked_456['ACC_block_8'].mean(),Context_Blocked_456['ACC_block_9'].mean()]),3),
                              'ACC(B10B11B12)':round(stdev([Context_Blocked_456['ACC_block_10'].mean(),Context_Blocked_456['ACC_block_11'].mean(),Context_Blocked_456['ACC_block_12'].mean()]),3)}



Mean_Acc_Context_Interleaved={'ACC(B1B2B3)':round(mean([Context_Interleaved_456['ACC_block_1'].mean(),Context_Interleaved_456['ACC_block_2'].mean(),Context_Interleaved_456['ACC_block_3'].mean()]),3),
                              'ACC(B4B5B6)':round(mean([Context_Interleaved_456['ACC_block_4'].mean(),Context_Interleaved_456['ACC_block_5'].mean(),Context_Interleaved_456['ACC_block_6'].mean()]),3),
                              'ACC(B7B8B9)':round(mean([Context_Interleaved_456['ACC_block_7'].mean(),Context_Interleaved_456['ACC_block_8'].mean(),Context_Interleaved_456['ACC_block_9'].mean()]),3),
                              'ACC(B10B11B12)':round(mean([Context_Interleaved_456['ACC_block_10'].mean(),Context_Interleaved_456['ACC_block_11'].mean(),Context_Interleaved_456['ACC_block_12'].mean()]),3)}

Mean_Acc_Context_Interleaved_std={'ACC(B1B2B3)':round(stdev([Context_Interleaved_456['ACC_block_1'].mean(),Context_Interleaved_456['ACC_block_2'].mean(),Context_Interleaved_456['ACC_block_3'].mean()]),3),
                                  'ACC(B4B5B6)':round(stdev([Context_Interleaved_456['ACC_block_4'].mean(),Context_Interleaved_456['ACC_block_5'].mean(),Context_Interleaved_456['ACC_block_6'].mean()]),3),
                                  'ACC(B7B8B9)':round(stdev([Context_Interleaved_456['ACC_block_7'].mean(),Context_Interleaved_456['ACC_block_8'].mean(),Context_Interleaved_456['ACC_block_9'].mean()]),3),
                                  'ACC(B10B11B12)':round(stdev([Context_Interleaved_456['ACC_block_10'].mean(),Context_Interleaved_456['ACC_block_11'].mean(),Context_Interleaved_456['ACC_block_12'].mean()]),3)}


Mean_Acc_Stimulus_Blocked={'ACC(B1B2B3)':round(mean([Stimulus_Blocked_456['ACC_block_1'].mean(),Stimulus_Blocked_456['ACC_block_2'].mean(),Stimulus_Blocked_456['ACC_block_3'].mean()]),3),
                           'ACC(B4B5B6)':round(mean([Stimulus_Blocked_456['ACC_block_4'].mean(),Stimulus_Blocked_456['ACC_block_5'].mean(),Stimulus_Blocked_456['ACC_block_6'].mean()]),3),
                           'ACC(B7B8B9)':round(mean([Stimulus_Blocked_456['ACC_block_7'].mean(),Stimulus_Blocked_456['ACC_block_8'].mean(),Stimulus_Blocked_456['ACC_block_9'].mean()]),3),
                           'ACC(B10B11B12)':round(mean([Stimulus_Blocked_456['ACC_block_10'].mean(),Stimulus_Blocked_456['ACC_block_11'].mean(),Stimulus_Blocked_456['ACC_block_12'].mean()]),3)}


Mean_Acc_Stimulus_Blocked_std={'ACC(B1B2B3)':round(stdev([Stimulus_Blocked_456['ACC_block_1'].mean(),Stimulus_Blocked_456['ACC_block_2'].mean(),Stimulus_Blocked_456['ACC_block_3'].mean()]),3),
                              'ACC(B4B5B6)':round(stdev([Stimulus_Blocked_456['ACC_block_4'].mean(),Stimulus_Blocked_456['ACC_block_5'].mean(),Stimulus_Blocked_456['ACC_block_6'].mean()]),3),
                              'ACC(B7B8B9)':round(stdev([Stimulus_Blocked_456['ACC_block_7'].mean(),Stimulus_Blocked_456['ACC_block_8'].mean(),Stimulus_Blocked_456['ACC_block_9'].mean()]),3),
                              'ACC(B10B11B12)':round(stdev([Stimulus_Blocked_456['ACC_block_10'].mean(),Stimulus_Blocked_456['ACC_block_11'].mean(),Stimulus_Blocked_456['ACC_block_12'].mean()]),3)}



Mean_Acc_Stimulus_Interleaved={'ACC(B1B2B3)':round(mean([Stimulus_Interleaved_456['ACC_block_1'].mean(),Stimulus_Interleaved_456['ACC_block_2'].mean(),Stimulus_Interleaved_456['ACC_block_3'].mean()]),3),
                               'ACC(B4B5B6)':round(mean([Stimulus_Interleaved_456['ACC_block_4'].mean(),Stimulus_Interleaved_456['ACC_block_5'].mean(),Stimulus_Interleaved_456['ACC_block_6'].mean()]),3),
                               'ACC(B7B8B9)':round(mean([Stimulus_Interleaved_456['ACC_block_7'].mean(),Stimulus_Interleaved_456['ACC_block_8'].mean(),Stimulus_Interleaved_456['ACC_block_9'].mean()]),3),
                               'ACC(B10B11B12)':round(mean([Stimulus_Interleaved_456['ACC_block_10'].mean(),Stimulus_Interleaved_456['ACC_block_11'].mean(),Stimulus_Interleaved_456['ACC_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Interleaved_std={'ACC(B1B2B3)':round(stdev([Stimulus_Interleaved_456['ACC_block_1'].mean(),Stimulus_Interleaved_456['ACC_block_2'].mean(),Stimulus_Interleaved_456['ACC_block_3'].mean()]),3),
                                    'ACC(B4B5B6)':round(stdev([Stimulus_Interleaved_456['ACC_block_4'].mean(),Stimulus_Interleaved_456['ACC_block_5'].mean(),Stimulus_Interleaved_456['ACC_block_6'].mean()]),3),
                                    'ACC(B7B8B9)':round(stdev([Stimulus_Interleaved_456['ACC_block_7'].mean(),Stimulus_Interleaved_456['ACC_block_8'].mean(),Stimulus_Interleaved_456['ACC_block_9'].mean()]),3),
                                    'ACC(B10B11B12)':round(stdev([Stimulus_Interleaved_456['ACC_block_10'].mean(),Stimulus_Interleaved_456['ACC_block_11'].mean(),Stimulus_Interleaved_456['ACC_block_12'].mean()]),3)}


Mean_Acc_Stimulus_Blocked_New_Version={'ACC(B1B2B3)':round(mean([Stimulus_Blocked_New_Version_456['ACC_block_1'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_2'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_3'].mean()]),3),
                                       'ACC(B4B5B6)':round(mean([Stimulus_Blocked_New_Version_456['ACC_block_4'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_5'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_6'].mean()]),3),
                                       'ACC(B7B8B9)':round(mean([Stimulus_Blocked_New_Version_456['ACC_block_7'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_8'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_9'].mean()]),3),
                                       'ACC(B10B11B12)':round(mean([Stimulus_Blocked_New_Version_456['ACC_block_10'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_11'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Blocked_New_Version_std={'ACC(B1B2B3)':round(stdev([Stimulus_Blocked_New_Version_456['ACC_block_1'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_2'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_3'].mean()]),3),
                                           'ACC(B4B5B6)':round(stdev([Stimulus_Blocked_New_Version_456['ACC_block_4'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_5'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_6'].mean()]),3),
                                           'ACC(B7B8B9)':round(stdev([Stimulus_Blocked_New_Version_456['ACC_block_7'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_8'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_9'].mean()]),3),
                                           'ACC(B10B11B12)':round(stdev([Stimulus_Blocked_New_Version_456['ACC_block_10'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_11'].mean(),Stimulus_Blocked_New_Version_456['ACC_block_12'].mean()]),3)}


import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha='center')
        
plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style
width=0.15
#['Block\n1,2,3', 'Block\n4,5,6', 'Test1\n(Block6,7,8)', 'Test2\n(Block9,10,11)'] 
x_axis= ['Block\n1,2,3', 'Block\n4,5,6', 'Test1\n(Block6,7,8)', 'Test2\n(Block9,10,11)'] 
x_axis_bar = [1,2,3,4]
x_index=np.arange(len(x_axis_bar))

y_1_Bar = list(Mean_Acc_Context_Blocked.values())
yerr_1=list(Mean_Acc_Context_Blocked_std.values())

y_2_Bar = list(Mean_Acc_Context_Interleaved.values())
yerr_2 = list(Mean_Acc_Context_Interleaved_std.values())

y_3_Bar = list(Mean_Acc_Stimulus_Blocked.values())
yerr_3 = list(Mean_Acc_Stimulus_Blocked_std.values())

y_4_Bar = list(Mean_Acc_Stimulus_Interleaved.values())
yerr_4 = list(Mean_Acc_Stimulus_Interleaved_std.values())

y_5_Bar = list(Mean_Acc_Stimulus_Blocked_New_Version.values())
yerr_5 = list(Mean_Acc_Stimulus_Blocked_New_Version_std.values())

#yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)


plt.bar(x_index-(2*width), y_1_Bar, yerr=yerr_1, align='center', alpha=0.5, ecolor='black', capsize=10, width=width, label='Context_Blocked Planet',color='#95baf5',hatch='///')
plt.bar(x_index-width, y_2_Bar, yerr=yerr_2, align='center', alpha=0.5, ecolor='black', capsize=10,  width=width, label='Context_Interleaved Planet',color='#95baf5')
plt.bar(x_index, y_3_Bar, yerr=yerr_3, align='center', alpha=0.5, ecolor='black', capsize=10,width=width, label='Stimulus_Blocked Task',color='#f09797',hatch='///')
plt.bar(x_index+width, y_4_Bar, yerr=yerr_4 , align='center', alpha=0.5, ecolor='black', capsize=10,  width=width, label='Stimulus_Interleaved Task',color='#f09797')
#plt.bar(x_index+(2*width), y_5_Bar, yerr=yerr_5, align='center', alpha=0.5, ecolor='black', capsize=10, width=width, label='Stimulus_Blocked_Planet',color='#f2ba41',hatch='///')


plt.title("Mean Accuracy",fontsize=20)
plt.xlabel('Blocks') 
plt.ylabel('Mean ACC')
plt.xticks(ticks=x_index, labels=x_axis,rotation=45)
plt.ylim(0.5, 1)
#plt.legend()

# calling the function to add value labels
#addlabels(x_axis_bar, y_whole)
plt.show()

##################################################################################################
##################################### RT Bar 456 #################################################
####################################################################################################
Mean_Acc_Context_Blocked_RT={'ACC(B1B2B3)':round(mean([Context_Blocked_456['RT_block_1'].mean(),Context_Blocked_456['RT_block_2'].mean(),Context_Blocked_456['RT_block_3'].mean()]),3),
                             'ACC(B4B5B6)':round(mean([Context_Blocked_456['RT_block_4'].mean(),Context_Blocked_456['RT_block_5'].mean(),Context_Blocked_456['RT_block_6'].mean()]),3),
                             'ACC(B7B8B9)':round(mean([Context_Blocked_456['RT_block_7'].mean(),Context_Blocked_456['RT_block_8'].mean(),Context_Blocked_456['RT_block_9'].mean()]),3),
                             'ACC(B10B11B12)':round(mean([Context_Blocked_456['RT_block_10'].mean(),Context_Blocked_456['RT_block_11'].mean(),Context_Blocked_456['RT_block_12'].mean()]),3)}

Mean_Acc_Context_Blocked_RT_std={'ACC(B1B2B3)':round(stdev([Context_Blocked_456['RT_block_1'].mean(),Context_Blocked_456['RT_block_2'].mean(),Context_Blocked_456['RT_block_3'].mean()]),3),
                                 'ACC(B4B5B6)':round(stdev([Context_Blocked_456['RT_block_4'].mean(),Context_Blocked_456['RT_block_5'].mean(),Context_Blocked_456['RT_block_6'].mean()]),3),
                                 'ACC(B7B8B9)':round(stdev([Context_Blocked_456['RT_block_7'].mean(),Context_Blocked_456['RT_block_8'].mean(),Context_Blocked_456['RT_block_9'].mean()]),3),
                                 'ACC(B10B11B12)':round(stdev([Context_Blocked_456['RT_block_10'].mean(),Context_Blocked_456['RT_block_11'].mean(),Context_Blocked_456['RT_block_12'].mean()]),3)}


Mean_Acc_Context_Interleaved_RT={'ACC(B1B2B3)':round(mean([Context_Interleaved_456['RT_block_1'].mean(),Context_Interleaved_456['RT_block_2'].mean(),Context_Interleaved_456['RT_block_3'].mean()]),3),
                                 'ACC(B4B5B6)':round(mean([Context_Interleaved_456['RT_block_4'].mean(),Context_Interleaved_456['RT_block_5'].mean(),Context_Interleaved_456['RT_block_6'].mean()]),3),
                                 'ACC(B7B8B9)':round(mean([Context_Interleaved_456['RT_block_7'].mean(),Context_Interleaved_456['RT_block_8'].mean(),Context_Interleaved_456['RT_block_9'].mean()]),3),
                                 'ACC(B10B11B12)':round(mean([Context_Interleaved_456['RT_block_10'].mean(),Context_Interleaved_456['RT_block_11'].mean(),Context_Interleaved_456['RT_block_12'].mean()]),3)}


Mean_Acc_Context_Interleaved_RT_std={'ACC(B1B2B3)':round(stdev([Context_Interleaved_456['RT_block_1'].mean(),Context_Interleaved_456['RT_block_2'].mean(),Context_Interleaved_456['RT_block_3'].mean()]),3),
                                     'ACC(B4B5B6)':round(stdev([Context_Interleaved_456['RT_block_4'].mean(),Context_Interleaved_456['RT_block_5'].mean(),Context_Interleaved_456['RT_block_6'].mean()]),3),
                                     'ACC(B7B8B9)':round(stdev([Context_Interleaved_456['RT_block_7'].mean(),Context_Interleaved_456['RT_block_8'].mean(),Context_Interleaved_456['RT_block_9'].mean()]),3),
                                     'ACC(B10B11B12)':round(stdev([Context_Interleaved_456['RT_block_10'].mean(),Context_Interleaved_456['RT_block_11'].mean(),Context_Interleaved_456['RT_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Blocked_RT={'ACC(B1B2B3)':round(mean([Stimulus_Blocked_456['RT_block_1'].mean(),Stimulus_Blocked_456['RT_block_2'].mean(),Stimulus_Blocked_456['RT_block_3'].mean()]),3),
                              'ACC(B4B5B6)':round(mean([Stimulus_Blocked_456['RT_block_4'].mean(),Stimulus_Blocked_456['RT_block_5'].mean(),Stimulus_Blocked_456['RT_block_6'].mean()]),3),
                              'ACC(B7B8B9)':round(mean([Stimulus_Blocked_456['RT_block_7'].mean(),Stimulus_Blocked_456['RT_block_8'].mean(),Stimulus_Blocked_456['RT_block_9'].mean()]),3),
                              'ACC(B10B11B12)':round(mean([Stimulus_Blocked_456['RT_block_10'].mean(),Stimulus_Blocked_456['RT_block_11'].mean(),Stimulus_Blocked_456['RT_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Blocked_RT_std={'ACC(B1B2B3)':round(stdev([Stimulus_Blocked_456['RT_block_1'].mean(),Stimulus_Blocked_456['RT_block_2'].mean(),Stimulus_Blocked_456['RT_block_3'].mean()]),3),
                                  'ACC(B4B5B6)':round(stdev([Stimulus_Blocked_456['RT_block_4'].mean(),Stimulus_Blocked_456['RT_block_5'].mean(),Stimulus_Blocked_456['RT_block_6'].mean()]),3),
                                  'ACC(B7B8B9)':round(stdev([Stimulus_Blocked_456['RT_block_7'].mean(),Stimulus_Blocked_456['RT_block_8'].mean(),Stimulus_Blocked_456['RT_block_9'].mean()]),3),
                                  'ACC(B10B11B12)':round(stdev([Stimulus_Blocked_456['RT_block_10'].mean(),Stimulus_Blocked_456['RT_block_11'].mean(),Stimulus_Blocked_456['RT_block_12'].mean()]),3)}


Mean_Acc_Stimulus_Interleaved_RT={'ACC(B1B2B3)':round(mean([Stimulus_Interleaved_456['RT_block_1'].mean(),Stimulus_Interleaved_456['RT_block_2'].mean(),Stimulus_Interleaved_456['RT_block_3'].mean()]),3),
                                  'ACC(B4B5B6)':round(mean([Stimulus_Interleaved_456['RT_block_4'].mean(),Stimulus_Interleaved_456['RT_block_5'].mean(),Stimulus_Interleaved_456['RT_block_6'].mean()]),3),
                                  'ACC(B7B8B9)':round(mean([Stimulus_Interleaved_456['RT_block_7'].mean(),Stimulus_Interleaved_456['RT_block_8'].mean(),Stimulus_Interleaved_456['RT_block_9'].mean()]),3),
                                  'ACC(B10B11B12)':round(mean([Stimulus_Interleaved_456['RT_block_10'].mean(),Stimulus_Interleaved_456['RT_block_11'].mean(),Stimulus_Interleaved_456['RT_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Interleaved_RT_std={'ACC(B1B2B3)':round(stdev([Stimulus_Interleaved_456['RT_block_1'].mean(),Stimulus_Interleaved_456['RT_block_2'].mean(),Stimulus_Interleaved_456['RT_block_3'].mean()]),3),
                                      'ACC(B4B5B6)':round(stdev([Stimulus_Interleaved_456['RT_block_4'].mean(),Stimulus_Interleaved_456['RT_block_5'].mean(),Stimulus_Interleaved_456['RT_block_6'].mean()]),3),
                                      'ACC(B7B8B9)':round(stdev([Stimulus_Interleaved_456['RT_block_7'].mean(),Stimulus_Interleaved_456['RT_block_8'].mean(),Stimulus_Interleaved_456['RT_block_9'].mean()]),3),
                                      'ACC(B10B11B12)':round(stdev([Stimulus_Interleaved_456['RT_block_10'].mean(),Stimulus_Interleaved_456['RT_block_11'].mean(),Stimulus_Interleaved_456['RT_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Blocked_New_Version_RT={'ACC(B1B2B3)':round(mean([Stimulus_Blocked_New_Version_456['RT_block_1'].mean(),Stimulus_Blocked_New_Version_456['RT_block_2'].mean(),Stimulus_Blocked_New_Version_456['RT_block_3'].mean()]),3),
                                          'ACC(B4B5B6)':round(mean([Stimulus_Blocked_New_Version_456['RT_block_4'].mean(),Stimulus_Blocked_New_Version_456['RT_block_5'].mean(),Stimulus_Blocked_New_Version_456['RT_block_6'].mean()]),3),
                                          'ACC(B7B8B9)':round(mean([Stimulus_Blocked_New_Version_456['RT_block_7'].mean(),Stimulus_Blocked_New_Version_456['RT_block_8'].mean(),Stimulus_Blocked_New_Version_456['RT_block_9'].mean()]),3),
                                          'ACC(B10B11B12)':round(mean([Stimulus_Blocked_New_Version_456['RT_block_10'].mean(),Stimulus_Blocked_New_Version_456['RT_block_11'].mean(),Stimulus_Blocked_New_Version_456['RT_block_12'].mean()]),3)}

Mean_Acc_Stimulus_Blocked_New_Version_RT_std={'ACC(B1B2B3)':round(stdev([Stimulus_Blocked_New_Version_456['RT_block_1'].mean(),Stimulus_Blocked_New_Version_456['RT_block_2'].mean(),Stimulus_Blocked_New_Version_456['RT_block_3'].mean()]),3),
                                              'ACC(B4B5B6)':round(stdev([Stimulus_Blocked_New_Version_456['RT_block_4'].mean(),Stimulus_Blocked_New_Version_456['RT_block_5'].mean(),Stimulus_Blocked_New_Version_456['RT_block_6'].mean()]),3),
                                              'ACC(B7B8B9)':round(stdev([Stimulus_Blocked_New_Version_456['RT_block_7'].mean(),Stimulus_Blocked_New_Version_456['RT_block_8'].mean(),Stimulus_Blocked_New_Version_456['RT_block_9'].mean()]),3),
                                              'ACC(B10B11B12)':round(stdev([Stimulus_Blocked_New_Version_456['RT_block_10'].mean(),Stimulus_Blocked_New_Version_456['RT_block_11'].mean(),Stimulus_Blocked_New_Version_456['RT_block_12'].mean()]),3)}



        
plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style
width=0.15
x_axis=['Block\n1,2,3', 'Block\n4,5,6', 'Test1\n(Block6,7,8)', 'Test2\n(Block9,10,11)'] 
x_axis_bar = [1,2,3,4]
x_index=np.arange(len(x_axis_bar))


y_1_Bar_RT = list(Mean_Acc_Context_Blocked_RT.values())
yerr_1_std = list(Mean_Acc_Context_Blocked_RT_std.values())

y_2_Bar_RT = list(Mean_Acc_Context_Interleaved_RT.values())
yerr_2_std = list(Mean_Acc_Context_Interleaved_RT_std.values())

y_3_Bar_RT = list(Mean_Acc_Stimulus_Blocked_RT.values())
yerr_3_std = list(Mean_Acc_Stimulus_Blocked_RT_std.values())

y_4_Bar_RT = list(Mean_Acc_Stimulus_Interleaved_RT.values())
yerr_4_std = list(Mean_Acc_Stimulus_Interleaved_RT_std.values())

y_5_Bar_RT = list(Mean_Acc_Stimulus_Blocked_New_Version_RT.values())
yerr_5_std = list(Mean_Acc_Stimulus_Blocked_New_Version_RT_std.values())

plt.bar(x_index-(2*width), y_1_Bar_RT, yerr=yerr_1_std, align='center', alpha=0.5, ecolor='black', capsize=10, width=width, label='Context_Blocked Planet',color='#95baf5',hatch='///')
plt.bar(x_index-width, y_2_Bar_RT ,yerr=yerr_2_std, align='center', alpha=0.5, ecolor='black', capsize=10,  width=width, label='Context_Interleaved Planet',color='#95baf5')
plt.bar(x_index, y_3_Bar_RT, yerr=yerr_3_std, align='center', alpha=0.5, ecolor='black', capsize=10, width=width, label='Stimulus_Blocked Task',color='#f09797',hatch='///')
plt.bar(x_index+width, y_4_Bar_RT, yerr=yerr_4_std, align='center', alpha=0.5, ecolor='black', capsize=10,  width=width, label='Stimulus_Interleaved Task',color='#f09797')
#plt.bar(x_index+(2*width), y_5_Bar_RT, yerr=yerr_5_std, align='center', alpha=0.5, ecolor='black', capsize=10, width=width, label='Stimulus_Blocked_Planet',color='#f2ba41',hatch='///')


plt.title("Mean Reaction Time",fontsize=20)
plt.xlabel('Blocks') 
plt.ylabel('Mean RT')
plt.xticks(ticks=x_index, labels=x_axis,rotation=45)
plt.ylim(0, 2000)
#plt.legend()

# calling the function to add value labels
#addlabels(x_axis_bar, y_whole)
plt.show()



########################################################################################################
################################### ACC Without outlier ################################################
########################################################################################################

Context_Blocked_No=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_without_outlier.csv')
Context_Interleaved_No=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_2_Data_Pilot_Run//df_Total_Context_Interleaved_Two_Days_without_outlier.csv')
Stimulus_Blocked_No=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//df_Total_Stimulus_Blocked_Two_Days_without_outlier.csv')
Stimulus_Interleaved_No=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_Total_Stimulus_Interleaved_Two_Days_without_outlier.csv')
Stimulus_Blocked_New_Version_No=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day2//df_Total_Stimulus_Blocked_New_Version_Two_Days_without_outlier.csv')
Context_Blocked_New_Version_No=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day2//df_Total_Context_Blocked_NewVersion_Two_Days_without_outlier.csv')
plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']
#plt.figure(figsize=(6, 3))


y1= [Context_Blocked_No['ACC_block_1'].mean(),Context_Blocked_No['ACC_block_2'].mean(),Context_Blocked_No['ACC_block_3'].mean(), 
     Context_Blocked_No['ACC_block_4'].mean(),Context_Blocked_No['ACC_block_5'].mean(),Context_Blocked_No['ACC_block_6'].mean(),
     Context_Blocked_No['ACC_block_7'].mean(),Context_Blocked_No['ACC_block_8'].mean(),Context_Blocked_No['ACC_block_9'].mean(),
     Context_Blocked_No['ACC_block_10'].mean(),Context_Blocked_No['ACC_block_11'].mean(),Context_Blocked_No['ACC_block_12'].mean()]

y2= [Context_Interleaved_No['ACC_block_1'].mean(),Context_Interleaved_No['ACC_block_2'].mean(),Context_Interleaved_No['ACC_block_3'].mean(), 
     Context_Interleaved_No['ACC_block_4'].mean(),Context_Interleaved_No['ACC_block_5'].mean(),Context_Interleaved_No['ACC_block_6'].mean(),
     Context_Interleaved_No['ACC_block_7'].mean(),Context_Interleaved_No['ACC_block_8'].mean(),Context_Interleaved_No['ACC_block_9'].mean(),
     Context_Interleaved_No['ACC_block_10'].mean(),Context_Interleaved_No['ACC_block_11'].mean(),Context_Interleaved_No['ACC_block_12'].mean()]

y3= [Stimulus_Blocked_No['ACC_block_1'].mean(),Stimulus_Blocked_No['ACC_block_2'].mean(),Stimulus_Blocked_No['ACC_block_3'].mean(), 
     Stimulus_Blocked_No['ACC_block_4'].mean(),Stimulus_Blocked_No['ACC_block_5'].mean(),Stimulus_Blocked_No['ACC_block_6'].mean(),
     Stimulus_Blocked_No['ACC_block_7'].mean(),Stimulus_Blocked_No['ACC_block_8'].mean(),Stimulus_Blocked_No['ACC_block_9'].mean(),
     Stimulus_Blocked_No['ACC_block_10'].mean(),Stimulus_Blocked_No['ACC_block_11'].mean(),Stimulus_Blocked_No['ACC_block_12'].mean()]


y4= [Stimulus_Interleaved_No['ACC_block_1'].mean(),Stimulus_Interleaved_No['ACC_block_2'].mean(),Stimulus_Interleaved_No['ACC_block_3'].mean(), 
     Stimulus_Interleaved_No['ACC_block_4'].mean(),Stimulus_Interleaved_No['ACC_block_5'].mean(),Stimulus_Interleaved_No['ACC_block_6'].mean(),
     Stimulus_Interleaved_No['ACC_block_7'].mean(),Stimulus_Interleaved_No['ACC_block_8'].mean(),Stimulus_Interleaved_No['ACC_block_9'].mean(),
     Stimulus_Interleaved_No['ACC_block_10'].mean(),Stimulus_Interleaved_No['ACC_block_11'].mean(),Stimulus_Interleaved_No['ACC_block_12'].mean()]

y5=[Stimulus_Blocked_New_Version_No['ACC_block_1'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_2'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_3'].mean(), 
    Stimulus_Blocked_New_Version_No['ACC_block_4'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_5'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_6'].mean(),
    Stimulus_Blocked_New_Version_No['ACC_block_7'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_8'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_9'].mean(),
    Stimulus_Blocked_New_Version_No['ACC_block_10'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_11'].mean(),Stimulus_Blocked_New_Version_No['ACC_block_12'].mean()]

y6=[Context_Blocked_New_Version_No['ACC_block_1'].mean(),Context_Blocked_New_Version_No['ACC_block_2'].mean(),Context_Blocked_New_Version_No['ACC_block_3'].mean(), 
    Context_Blocked_New_Version_No['ACC_block_4'].mean(),Context_Blocked_New_Version_No['ACC_block_5'].mean(),Context_Blocked_New_Version_No['ACC_block_6'].mean(),
    Context_Blocked_New_Version_No['ACC_block_7'].mean(),Context_Blocked_New_Version_No['ACC_block_8'].mean(),Context_Blocked_New_Version_No['ACC_block_9'].mean(),
    Context_Blocked_New_Version_No['ACC_block_10'].mean(),Context_Blocked_New_Version_No['ACC_block_11'].mean(),Context_Blocked_New_Version_No['ACC_block_12'].mean()]




plt.xticks(rotation=45)
plt.plot(x_axis, y1, 'o-',label = "Context_Blocked")
plt.plot(x_axis, y2, '*-',label = "Context_Interleaved")
plt.plot(x_axis, y3, 'o-',label = "Stimulus_Blocked")
plt.plot(x_axis, y4, '*-',label = "Stimulus_Interleaved")
plt.plot(x_axis, y5, '^-',label = "Stimulus_Blocked_New_Version")
plt.plot(x_axis, y6, '^-',label = "Context_Blocked_New_Version")
plt.title("ACC WithOut Outlier",fontsize=16)
plt.legend()
plt.show()

###############################################################################################################
################################# ACC Median ##################################################################
###############################################################################################################
Context_Blocked_Median=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_ACC_Critera_Whole_Train.csv')
Context_Interleaved_Median=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_2_Data_Pilot_Run//df_Total_Context_Interleaved_Two_Days_ACC_Critera_Whole_Train.csv')
Stimulus_Blocked_Median=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//df_Total_Stimulus_Blocked_Two_Days_ACC_Critera_Whole_Train.csv')
Stimulus_Interleaved_Median=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_Total_Stimulus_Interleaved_Two_Days_ACC_Critera_Whole_Train.csv')
Stimulus_Blocked_New_Version_Median=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day2//df_Total_Stimulus_Blocked_New_Version_Two_Days_ACC_Critera_Whole_Train.csv')

plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']
#plt.figure(figsize=(6, 3))


y1= [Context_Blocked_Median['ACC_block_1'].median(),Context_Blocked_Median['ACC_block_2'].median(),Context_Blocked_Median['ACC_block_3'].median(), 
     Context_Blocked_Median['ACC_block_4'].median(),Context_Blocked_Median['ACC_block_5'].median(),Context_Blocked_Median['ACC_block_6'].median(),
     Context_Blocked_Median['ACC_block_7'].median(),Context_Blocked_Median['ACC_block_8'].median(),Context_Blocked_Median['ACC_block_9'].median(),
     Context_Blocked_Median['ACC_block_10'].median(),Context_Blocked_Median['ACC_block_11'].median(),Context_Blocked_Median['ACC_block_12'].median()]

y2= [Context_Interleaved_Median['ACC_block_1'].median(),Context_Interleaved_Median['ACC_block_2'].median(),Context_Interleaved_Median['ACC_block_3'].median(), 
     Context_Interleaved_Median['ACC_block_4'].median(),Context_Interleaved_Median['ACC_block_5'].median(),Context_Interleaved_Median['ACC_block_6'].median(),
     Context_Interleaved_Median['ACC_block_7'].median(),Context_Interleaved_Median['ACC_block_8'].median(),Context_Interleaved_Median['ACC_block_9'].median(),
     Context_Interleaved_Median['ACC_block_10'].median(),Context_Interleaved_Median['ACC_block_11'].median(),Context_Interleaved_Median['ACC_block_12'].median()]

y3= [Stimulus_Blocked_Median['ACC_block_1'].median(),Stimulus_Blocked_Median['ACC_block_2'].median(),Stimulus_Blocked_Median['ACC_block_3'].median(), 
     Stimulus_Blocked_Median['ACC_block_4'].median(),Stimulus_Blocked_Median['ACC_block_5'].median(),Stimulus_Blocked_Median['ACC_block_6'].median(),
     Stimulus_Blocked_Median['ACC_block_7'].median(),Stimulus_Blocked_Median['ACC_block_8'].median(),Stimulus_Blocked_Median['ACC_block_9'].median(),
     Stimulus_Blocked_Median['ACC_block_10'].median(),Stimulus_Blocked_Median['ACC_block_11'].median(),Stimulus_Blocked_Median['ACC_block_12'].median()]


y4= [Stimulus_Interleaved_Median['ACC_block_1'].median(),Stimulus_Interleaved_Median['ACC_block_2'].median(),Stimulus_Interleaved_Median['ACC_block_3'].median(), 
     Stimulus_Interleaved_Median['ACC_block_4'].median(),Stimulus_Interleaved_Median['ACC_block_5'].median(),Stimulus_Interleaved_Median['ACC_block_6'].median(),
     Stimulus_Interleaved_Median['ACC_block_7'].median(),Stimulus_Interleaved_Median['ACC_block_8'].median(),Stimulus_Interleaved_Median['ACC_block_9'].median(),
     Stimulus_Interleaved_Median['ACC_block_10'].median(),Stimulus_Interleaved_Median['ACC_block_11'].median(),Stimulus_Interleaved_Median['ACC_block_12'].median()]

y5=[Stimulus_Blocked_New_Version_Median['ACC_block_1'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_2'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_3'].median(), 
    Stimulus_Blocked_New_Version_Median['ACC_block_4'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_5'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_6'].median(),
    Stimulus_Blocked_New_Version_Median['ACC_block_7'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_8'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_9'].median(),
    Stimulus_Blocked_New_Version_Median['ACC_block_10'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_11'].median(),Stimulus_Blocked_New_Version_Median['ACC_block_12'].median()]

plt.xticks(rotation=45)
plt.plot(x_axis, y1, 'o-',label = "Context_Blocked")
plt.plot(x_axis, y2, '*-',label = "Context_Interleaved")
plt.plot(x_axis, y3, 'o-',label = "Stimulus_Blocked")
plt.plot(x_axis, y4, '*-',label = "Stimulus_Interleaved")
plt.plot(x_axis, y5, '^-',label = "Stimulus_Blocked_New_Version")
plt.title("ACC Median",fontsize=16)
plt.legend()
plt.show()

#####################################################################################################
#####################################################################################################
############################################ Stimulus_Response Plotting #############################
#####################################################################################################
#####################################################################################################
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv

CB_Stimulu_Response = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_SR_ContextBlocked.csv')
CI_Stimulu_Response = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_2_Data_Pilot_Run//df_SR_ContextInterleaved.csv')
CBN_Stimulu_Response= pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day2//df_SR_ContextBlockedNewVersion.csv')
SR_Stimulus_Blocked = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//df_SR_StimulusBlocked.csv')
SI_Stimulu_Response = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_SR_StimulusInterleaved.csv')
SBN_Stimulu_Response = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day2//df_SR_StimulusBlockedNewVersion.csv')


x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']

# Stimulus Blocked
SB_y_acc = [SR_Stimulus_Blocked['SR_1_ACC'].mean(), SR_Stimulus_Blocked['SR_2_ACC'].mean(), SR_Stimulus_Blocked['SR_3_ACC'].mean(), 
            SR_Stimulus_Blocked['SR_4_ACC'].mean(), SR_Stimulus_Blocked['SR_5_ACC'].mean(), SR_Stimulus_Blocked['SR_6_ACC'].mean(),
            SR_Stimulus_Blocked['SR_7_ACC'].mean(), SR_Stimulus_Blocked['SR_8_ACC'].mean(), SR_Stimulus_Blocked['SR_9_ACC'].mean(),
            SR_Stimulus_Blocked['SR_10_ACC'].mean(), SR_Stimulus_Blocked['SR_11_ACC'].mean(), SR_Stimulus_Blocked['SR_12_ACC'].mean()]

SB_y_rt = [SR_Stimulus_Blocked['SR_1_RT'].mean(), SR_Stimulus_Blocked['SR_2_RT'].mean(), SR_Stimulus_Blocked['SR_3_RT'].mean(), 
           SR_Stimulus_Blocked['SR_4_RT'].mean(), SR_Stimulus_Blocked['SR_5_RT'].mean(), SR_Stimulus_Blocked['SR_6_RT'].mean(),
           SR_Stimulus_Blocked['SR_7_RT'].mean(), SR_Stimulus_Blocked['SR_8_RT'].mean(), SR_Stimulus_Blocked['SR_9_RT'].mean(),
           SR_Stimulus_Blocked['SR_10_RT'].mean(), SR_Stimulus_Blocked['SR_11_RT'].mean(), SR_Stimulus_Blocked['SR_12_RT'].mean()]

SB_y_leg_acc= [SR_Stimulus_Blocked['SR_1_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_2_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_3_ACC_leg'].mean(), 
               SR_Stimulus_Blocked['SR_4_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_5_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_6_ACC_leg'].mean(),
               SR_Stimulus_Blocked['SR_7_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_8_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_9_ACC_leg'].mean(),
               SR_Stimulus_Blocked['SR_10_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_11_ACC_leg'].mean(), SR_Stimulus_Blocked['SR_12_ACC_leg'].mean()]

SB_y_leg_rt= [SR_Stimulus_Blocked['SR_1_RT_leg'].mean(), SR_Stimulus_Blocked['SR_2_RT_leg'].mean(), SR_Stimulus_Blocked['SR_3_RT_leg'].mean(), 
              SR_Stimulus_Blocked['SR_4_RT_leg'].mean(), SR_Stimulus_Blocked['SR_5_RT_leg'].mean(), SR_Stimulus_Blocked['SR_6_RT_leg'].mean(),
              SR_Stimulus_Blocked['SR_7_RT_leg'].mean(), SR_Stimulus_Blocked['SR_8_RT_leg'].mean(), SR_Stimulus_Blocked['SR_9_RT_leg'].mean(),
              SR_Stimulus_Blocked['SR_10_RT_leg'].mean(), SR_Stimulus_Blocked['SR_11_RT_leg'].mean(), SR_Stimulus_Blocked['SR_12_RT_leg'].mean()]

SB_y_antenn_acc= [SR_Stimulus_Blocked['SR_1_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_2_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_3_ACC_antenn'].mean(), 
                  SR_Stimulus_Blocked['SR_4_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_5_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_6_ACC_antenn'].mean(),
                  SR_Stimulus_Blocked['SR_7_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_8_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_9_ACC_antenn'].mean(),
                  SR_Stimulus_Blocked['SR_10_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_11_ACC_antenn'].mean(), SR_Stimulus_Blocked['SR_12_ACC_antenn'].mean()]

SB_y_antenn_rt= [SR_Stimulus_Blocked['SR_1_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_2_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_3_RT_antenn'].mean(), 
                 SR_Stimulus_Blocked['SR_4_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_5_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_6_RT_antenn'].mean(),
                 SR_Stimulus_Blocked['SR_7_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_8_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_9_RT_antenn'].mean(),
                 SR_Stimulus_Blocked['SR_10_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_11_RT_antenn'].mean(), SR_Stimulus_Blocked['SR_12_RT_antenn'].mean()]

SB_y_mouth_acc= [SR_Stimulus_Blocked['SR_1_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_2_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_3_ACC_mouth'].mean(), 
                 SR_Stimulus_Blocked['SR_4_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_5_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_6_ACC_mouth'].mean(),
                 SR_Stimulus_Blocked['SR_7_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_8_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_9_ACC_mouth'].mean(),
                 SR_Stimulus_Blocked['SR_10_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_11_ACC_mouth'].mean(), SR_Stimulus_Blocked['SR_12_ACC_mouth'].mean()]

SB_y_mouth_rt= [SR_Stimulus_Blocked['SR_1_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_2_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_3_RT_mouth'].mean(), 
                SR_Stimulus_Blocked['SR_4_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_5_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_6_RT_mouth'].mean(),
                SR_Stimulus_Blocked['SR_7_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_8_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_9_RT_mouth'].mean(),
                SR_Stimulus_Blocked['SR_10_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_11_RT_mouth'].mean(), SR_Stimulus_Blocked['SR_12_RT_mouth'].mean()]

############################################################################
############################### Context Blocked ############################
############################################################################
CB_y_acc = [CB_Stimulu_Response['SR_1_ACC'].mean(), CB_Stimulu_Response['SR_2_ACC'].mean(), CB_Stimulu_Response['SR_3_ACC'].mean(), 
            CB_Stimulu_Response['SR_4_ACC'].mean(), CB_Stimulu_Response['SR_5_ACC'].mean(), CB_Stimulu_Response['SR_6_ACC'].mean(),
            CB_Stimulu_Response['SR_7_ACC'].mean(), CB_Stimulu_Response['SR_8_ACC'].mean(), CB_Stimulu_Response['SR_9_ACC'].mean(),
            CB_Stimulu_Response['SR_10_ACC'].mean(), CB_Stimulu_Response['SR_11_ACC'].mean(), CB_Stimulu_Response['SR_12_ACC'].mean()]

CB_y_rt = [CB_Stimulu_Response['SR_1_RT'].mean(), CB_Stimulu_Response['SR_2_RT'].mean(), CB_Stimulu_Response['SR_3_RT'].mean(), 
           CB_Stimulu_Response['SR_4_RT'].mean(), CB_Stimulu_Response['SR_5_RT'].mean(), CB_Stimulu_Response['SR_6_RT'].mean(),
           CB_Stimulu_Response['SR_7_RT'].mean(), CB_Stimulu_Response['SR_8_RT'].mean(), CB_Stimulu_Response['SR_9_RT'].mean(),
           CB_Stimulu_Response['SR_10_RT'].mean(), CB_Stimulu_Response['SR_11_RT'].mean(), CB_Stimulu_Response['SR_12_RT'].mean()]

CB_y_leg_acc= [CB_Stimulu_Response['SR_1_ACC_leg'].mean(), CB_Stimulu_Response['SR_2_ACC_leg'].mean(), CB_Stimulu_Response['SR_3_ACC_leg'].mean(), 
               CB_Stimulu_Response['SR_4_ACC_leg'].mean(), CB_Stimulu_Response['SR_5_ACC_leg'].mean(), CB_Stimulu_Response['SR_6_ACC_leg'].mean(),
               CB_Stimulu_Response['SR_7_ACC_leg'].mean(), CB_Stimulu_Response['SR_8_ACC_leg'].mean(), CB_Stimulu_Response['SR_9_ACC_leg'].mean(),
               CB_Stimulu_Response['SR_10_ACC_leg'].mean(), CB_Stimulu_Response['SR_11_ACC_leg'].mean(), CB_Stimulu_Response['SR_12_ACC_leg'].mean()]

CB_y_leg_rt= [CB_Stimulu_Response['SR_1_RT_leg'].mean(), CB_Stimulu_Response['SR_2_RT_leg'].mean(), CB_Stimulu_Response['SR_3_RT_leg'].mean(), 
              CB_Stimulu_Response['SR_4_RT_leg'].mean(), CB_Stimulu_Response['SR_5_RT_leg'].mean(), CB_Stimulu_Response['SR_6_RT_leg'].mean(),
              CB_Stimulu_Response['SR_7_RT_leg'].mean(), CB_Stimulu_Response['SR_8_RT_leg'].mean(), CB_Stimulu_Response['SR_9_RT_leg'].mean(),
              CB_Stimulu_Response['SR_10_RT_leg'].mean(), CB_Stimulu_Response['SR_11_RT_leg'].mean(), CB_Stimulu_Response['SR_12_RT_leg'].mean()]

CB_y_antenn_acc= [CB_Stimulu_Response['SR_1_ACC_antenn'].mean(), CB_Stimulu_Response['SR_2_ACC_antenn'].mean(), CB_Stimulu_Response['SR_3_ACC_antenn'].mean(), 
                  CB_Stimulu_Response['SR_4_ACC_antenn'].mean(), CB_Stimulu_Response['SR_5_ACC_antenn'].mean(), CB_Stimulu_Response['SR_6_ACC_antenn'].mean(),
                  CB_Stimulu_Response['SR_7_ACC_antenn'].mean(), CB_Stimulu_Response['SR_8_ACC_antenn'].mean(), CB_Stimulu_Response['SR_9_ACC_antenn'].mean(),
                  CB_Stimulu_Response['SR_10_ACC_antenn'].mean(), CB_Stimulu_Response['SR_11_ACC_antenn'].mean(), CB_Stimulu_Response['SR_12_ACC_antenn'].mean()]

CB_y_antenn_rt= [CB_Stimulu_Response['SR_1_RT_antenn'].mean(), CB_Stimulu_Response['SR_2_RT_antenn'].mean(), CB_Stimulu_Response['SR_3_RT_antenn'].mean(), 
                 CB_Stimulu_Response['SR_4_RT_antenn'].mean(), CB_Stimulu_Response['SR_5_RT_antenn'].mean(), CB_Stimulu_Response['SR_6_RT_antenn'].mean(),
                 CB_Stimulu_Response['SR_7_RT_antenn'].mean(), CB_Stimulu_Response['SR_8_RT_antenn'].mean(), CB_Stimulu_Response['SR_9_RT_antenn'].mean(),
                 CB_Stimulu_Response['SR_10_RT_antenn'].mean(), CB_Stimulu_Response['SR_11_RT_antenn'].mean(), CB_Stimulu_Response['SR_12_RT_antenn'].mean()]

CB_y_mouth_acc= [CB_Stimulu_Response['SR_1_ACC_mouth'].mean(), CB_Stimulu_Response['SR_2_ACC_mouth'].mean(), CB_Stimulu_Response['SR_3_ACC_mouth'].mean(), 
                 CB_Stimulu_Response['SR_4_ACC_mouth'].mean(), CB_Stimulu_Response['SR_5_ACC_mouth'].mean(), CB_Stimulu_Response['SR_6_ACC_mouth'].mean(),
                 CB_Stimulu_Response['SR_7_ACC_mouth'].mean(), CB_Stimulu_Response['SR_8_ACC_mouth'].mean(), CB_Stimulu_Response['SR_9_ACC_mouth'].mean(),
                 CB_Stimulu_Response['SR_10_ACC_mouth'].mean(), CB_Stimulu_Response['SR_11_ACC_mouth'].mean(), CB_Stimulu_Response['SR_12_ACC_mouth'].mean()]

CB_y_mouth_rt= [CB_Stimulu_Response['SR_1_RT_mouth'].mean(), CB_Stimulu_Response['SR_2_RT_mouth'].mean(), CB_Stimulu_Response['SR_3_RT_mouth'].mean(), 
                CB_Stimulu_Response['SR_4_RT_mouth'].mean(), CB_Stimulu_Response['SR_5_RT_mouth'].mean(), CB_Stimulu_Response['SR_6_RT_mouth'].mean(),
                CB_Stimulu_Response['SR_7_RT_mouth'].mean(), CB_Stimulu_Response['SR_8_RT_mouth'].mean(), CB_Stimulu_Response['SR_9_RT_mouth'].mean(),
                CB_Stimulu_Response['SR_10_RT_mouth'].mean(), CB_Stimulu_Response['SR_11_RT_mouth'].mean(), CB_Stimulu_Response['SR_12_RT_mouth'].mean()]

###################################################################
################### Context Interleaved ##########################
#################################################################

CI_y_acc = [CI_Stimulu_Response['SR_1_ACC'].mean(), CI_Stimulu_Response['SR_2_ACC'].mean(), CI_Stimulu_Response['SR_3_ACC'].mean(), 
            CI_Stimulu_Response['SR_4_ACC'].mean(), CI_Stimulu_Response['SR_5_ACC'].mean(), CI_Stimulu_Response['SR_6_ACC'].mean(),
            CI_Stimulu_Response['SR_7_ACC'].mean(), CI_Stimulu_Response['SR_8_ACC'].mean(), CI_Stimulu_Response['SR_9_ACC'].mean(),
            CI_Stimulu_Response['SR_10_ACC'].mean(), CI_Stimulu_Response['SR_11_ACC'].mean(), CI_Stimulu_Response['SR_12_ACC'].mean()]

CI_y_rt = [CI_Stimulu_Response['SR_1_RT'].mean(), CI_Stimulu_Response['SR_2_RT'].mean(), CI_Stimulu_Response['SR_3_RT'].mean(), 
           CI_Stimulu_Response['SR_4_RT'].mean(), CI_Stimulu_Response['SR_5_RT'].mean(), CI_Stimulu_Response['SR_6_RT'].mean(),
           CI_Stimulu_Response['SR_7_RT'].mean(), CI_Stimulu_Response['SR_8_RT'].mean(), CI_Stimulu_Response['SR_9_RT'].mean(),
           CI_Stimulu_Response['SR_10_RT'].mean(), CI_Stimulu_Response['SR_11_RT'].mean(), CI_Stimulu_Response['SR_12_RT'].mean()]

CI_y_leg_acc = [CI_Stimulu_Response['SR_1_ACC_leg'].mean(), CI_Stimulu_Response['SR_2_ACC_leg'].mean(), CI_Stimulu_Response['SR_3_ACC_leg'].mean(), 
                CI_Stimulu_Response['SR_4_ACC_leg'].mean(), CI_Stimulu_Response['SR_5_ACC_leg'].mean(), CI_Stimulu_Response['SR_6_ACC_leg'].mean(),
                CI_Stimulu_Response['SR_7_ACC_leg'].mean(), CI_Stimulu_Response['SR_8_ACC_leg'].mean(), CI_Stimulu_Response['SR_9_ACC_leg'].mean(),
                CI_Stimulu_Response['SR_10_ACC_leg'].mean(), CI_Stimulu_Response['SR_11_ACC_leg'].mean(), CI_Stimulu_Response['SR_12_ACC_leg'].mean()]

CI_y_leg_rt = [CI_Stimulu_Response['SR_1_RT_leg'].mean(), CI_Stimulu_Response['SR_2_RT_leg'].mean(), CI_Stimulu_Response['SR_3_RT_leg'].mean(), 
               CI_Stimulu_Response['SR_4_RT_leg'].mean(), CI_Stimulu_Response['SR_5_RT_leg'].mean(), CI_Stimulu_Response['SR_6_RT_leg'].mean(),
               CI_Stimulu_Response['SR_7_RT_leg'].mean(), CI_Stimulu_Response['SR_8_RT_leg'].mean(), CI_Stimulu_Response['SR_9_RT_leg'].mean(),
               CI_Stimulu_Response['SR_10_RT_leg'].mean(), CI_Stimulu_Response['SR_11_RT_leg'].mean(), CI_Stimulu_Response['SR_12_RT_leg'].mean()]

CI_y_antenn_acc = [CI_Stimulu_Response['SR_1_ACC_antenn'].mean(), CI_Stimulu_Response['SR_2_ACC_antenn'].mean(), CI_Stimulu_Response['SR_3_ACC_antenn'].mean(), 
                   CI_Stimulu_Response['SR_4_ACC_antenn'].mean(), CI_Stimulu_Response['SR_5_ACC_antenn'].mean(), CI_Stimulu_Response['SR_6_ACC_antenn'].mean(),
                   CI_Stimulu_Response['SR_7_ACC_antenn'].mean(), CI_Stimulu_Response['SR_8_ACC_antenn'].mean(), CI_Stimulu_Response['SR_9_ACC_antenn'].mean(),
                   CI_Stimulu_Response['SR_10_ACC_antenn'].mean(), CI_Stimulu_Response['SR_11_ACC_antenn'].mean(), CI_Stimulu_Response['SR_12_ACC_antenn'].mean()]

CI_y_antenn_rt = [CI_Stimulu_Response['SR_1_RT_antenn'].mean(), CI_Stimulu_Response['SR_2_RT_antenn'].mean(), CI_Stimulu_Response['SR_3_RT_antenn'].mean(), 
                  CI_Stimulu_Response['SR_4_RT_antenn'].mean(), CI_Stimulu_Response['SR_5_RT_antenn'].mean(), CI_Stimulu_Response['SR_6_RT_antenn'].mean(),
                  CI_Stimulu_Response['SR_7_RT_antenn'].mean(), CI_Stimulu_Response['SR_8_RT_antenn'].mean(), CI_Stimulu_Response['SR_9_RT_antenn'].mean(),
                  CI_Stimulu_Response['SR_10_RT_antenn'].mean(), CI_Stimulu_Response['SR_11_RT_antenn'].mean(), CI_Stimulu_Response['SR_12_RT_antenn'].mean()]

CI_y_mouth_acc = [CI_Stimulu_Response['SR_1_ACC_mouth'].mean(), CI_Stimulu_Response['SR_2_ACC_mouth'].mean(), CI_Stimulu_Response['SR_3_ACC_mouth'].mean(), 
                  CI_Stimulu_Response['SR_4_ACC_mouth'].mean(), CI_Stimulu_Response['SR_5_ACC_mouth'].mean(), CI_Stimulu_Response['SR_6_ACC_mouth'].mean(),
                  CI_Stimulu_Response['SR_7_ACC_mouth'].mean(), CI_Stimulu_Response['SR_8_ACC_mouth'].mean(), CI_Stimulu_Response['SR_9_ACC_mouth'].mean(),
                  CI_Stimulu_Response['SR_10_ACC_mouth'].mean(), CI_Stimulu_Response['SR_11_ACC_mouth'].mean(), CI_Stimulu_Response['SR_12_ACC_mouth'].mean()]

CI_y_mouth_rt = [CI_Stimulu_Response['SR_1_RT_mouth'].mean(), CI_Stimulu_Response['SR_2_RT_mouth'].mean(), CI_Stimulu_Response['SR_3_RT_mouth'].mean(), 
                 CI_Stimulu_Response['SR_4_RT_mouth'].mean(), CI_Stimulu_Response['SR_5_RT_mouth'].mean(), CI_Stimulu_Response['SR_6_RT_mouth'].mean(),
                 CI_Stimulu_Response['SR_7_RT_mouth'].mean(), CI_Stimulu_Response['SR_8_RT_mouth'].mean(), CI_Stimulu_Response['SR_9_RT_mouth'].mean(),
                 CI_Stimulu_Response['SR_10_RT_mouth'].mean(), CI_Stimulu_Response['SR_11_RT_mouth'].mean(), CI_Stimulu_Response['SR_12_RT_mouth'].mean()]

#################################################################################################################
############################### Context Blocked New Version With labeling keys ##################################
##################################################################################################################

CBN_y_acc = [CBN_Stimulu_Response['SR_1_ACC'].mean(), CBN_Stimulu_Response['SR_2_ACC'].mean(), CBN_Stimulu_Response['SR_3_ACC'].mean(), 
             CBN_Stimulu_Response['SR_4_ACC'].mean(), CBN_Stimulu_Response['SR_5_ACC'].mean(), CBN_Stimulu_Response['SR_6_ACC'].mean(),
             CBN_Stimulu_Response['SR_7_ACC'].mean(), CBN_Stimulu_Response['SR_8_ACC'].mean(), CBN_Stimulu_Response['SR_9_ACC'].mean(),
             CBN_Stimulu_Response['SR_10_ACC'].mean(), CBN_Stimulu_Response['SR_11_ACC'].mean(), CBN_Stimulu_Response['SR_12_ACC'].mean()]

CBN_y_rt = [CBN_Stimulu_Response['SR_1_RT'].mean(), CBN_Stimulu_Response['SR_2_RT'].mean(), CBN_Stimulu_Response['SR_3_RT'].mean(), 
            CBN_Stimulu_Response['SR_4_RT'].mean(), CBN_Stimulu_Response['SR_5_RT'].mean(), CBN_Stimulu_Response['SR_6_RT'].mean(),
            CBN_Stimulu_Response['SR_7_RT'].mean(), CBN_Stimulu_Response['SR_8_RT'].mean(), CBN_Stimulu_Response['SR_9_RT'].mean(),
            CBN_Stimulu_Response['SR_10_RT'].mean(), CBN_Stimulu_Response['SR_11_RT'].mean(), CBN_Stimulu_Response['SR_12_RT'].mean()]

CBN_y_leg_acc = [CBN_Stimulu_Response['SR_1_ACC_leg'].mean(), CBN_Stimulu_Response['SR_2_ACC_leg'].mean(), CBN_Stimulu_Response['SR_3_ACC_leg'].mean(), 
                 CBN_Stimulu_Response['SR_4_ACC_leg'].mean(), CBN_Stimulu_Response['SR_5_ACC_leg'].mean(), CBN_Stimulu_Response['SR_6_ACC_leg'].mean(),
                 CBN_Stimulu_Response['SR_7_ACC_leg'].mean(), CBN_Stimulu_Response['SR_8_ACC_leg'].mean(), CBN_Stimulu_Response['SR_9_ACC_leg'].mean(),
                 CBN_Stimulu_Response['SR_10_ACC_leg'].mean(), CBN_Stimulu_Response['SR_11_ACC_leg'].mean(), CBN_Stimulu_Response['SR_12_ACC_leg'].mean()]

CBN_y_leg_rt = [CBN_Stimulu_Response['SR_1_RT_leg'].mean(), CBN_Stimulu_Response['SR_2_RT_leg'].mean(), CBN_Stimulu_Response['SR_3_RT_leg'].mean(), 
                CBN_Stimulu_Response['SR_4_RT_leg'].mean(), CBN_Stimulu_Response['SR_5_RT_leg'].mean(), CBN_Stimulu_Response['SR_6_RT_leg'].mean(),
                CBN_Stimulu_Response['SR_7_RT_leg'].mean(), CBN_Stimulu_Response['SR_8_RT_leg'].mean(), CBN_Stimulu_Response['SR_9_RT_leg'].mean(),
                CBN_Stimulu_Response['SR_10_RT_leg'].mean(), CBN_Stimulu_Response['SR_11_RT_leg'].mean(), CBN_Stimulu_Response['SR_12_RT_leg'].mean()]

CBN_y_antenn_acc = [CBN_Stimulu_Response['SR_1_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_2_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_3_ACC_antenn'].mean(), 
                    CBN_Stimulu_Response['SR_4_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_5_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_6_ACC_antenn'].mean(),
                    CBN_Stimulu_Response['SR_7_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_8_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_9_ACC_antenn'].mean(),
                    CBN_Stimulu_Response['SR_10_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_11_ACC_antenn'].mean(), CBN_Stimulu_Response['SR_12_ACC_antenn'].mean()]

CBN_y_antenn_rt = [CBN_Stimulu_Response['SR_1_RT_antenn'].mean(), CBN_Stimulu_Response['SR_2_RT_antenn'].mean(), CBN_Stimulu_Response['SR_3_RT_antenn'].mean(), 
                   CBN_Stimulu_Response['SR_4_RT_antenn'].mean(), CBN_Stimulu_Response['SR_5_RT_antenn'].mean(), CBN_Stimulu_Response['SR_6_RT_antenn'].mean(),
                   CBN_Stimulu_Response['SR_7_RT_antenn'].mean(), CBN_Stimulu_Response['SR_8_RT_antenn'].mean(), CBN_Stimulu_Response['SR_9_RT_antenn'].mean(),
                   CBN_Stimulu_Response['SR_10_RT_antenn'].mean(), CBN_Stimulu_Response['SR_11_RT_antenn'].mean(), CBN_Stimulu_Response['SR_12_RT_antenn'].mean()]

CBN_y_mouth_acc = [CBN_Stimulu_Response['SR_1_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_2_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_3_ACC_mouth'].mean(), 
                   CBN_Stimulu_Response['SR_4_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_5_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_6_ACC_mouth'].mean(),
                   CBN_Stimulu_Response['SR_7_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_8_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_9_ACC_mouth'].mean(),
                   CBN_Stimulu_Response['SR_10_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_11_ACC_mouth'].mean(), CBN_Stimulu_Response['SR_12_ACC_mouth'].mean()]

CBN_y_mouth_rt = [CBN_Stimulu_Response['SR_1_RT_mouth'].mean(), CBN_Stimulu_Response['SR_2_RT_mouth'].mean(), CBN_Stimulu_Response['SR_3_RT_mouth'].mean(), 
                  CBN_Stimulu_Response['SR_4_RT_mouth'].mean(), CBN_Stimulu_Response['SR_5_RT_mouth'].mean(), CBN_Stimulu_Response['SR_6_RT_mouth'].mean(),
                  CBN_Stimulu_Response['SR_7_RT_mouth'].mean(), CBN_Stimulu_Response['SR_8_RT_mouth'].mean(), CBN_Stimulu_Response['SR_9_RT_mouth'].mean(),
                  CBN_Stimulu_Response['SR_10_RT_mouth'].mean(), CBN_Stimulu_Response['SR_11_RT_mouth'].mean(), CBN_Stimulu_Response['SR_12_RT_mouth'].mean()]

#######################################################################################################
############################## Stimulus Interleaved ###################################################
########################################################################################################

SI_y_acc = [SI_Stimulu_Response['SR_1_ACC'].mean(), SI_Stimulu_Response['SR_2_ACC'].mean(), SI_Stimulu_Response['SR_3_ACC'].mean(), 
            SI_Stimulu_Response['SR_4_ACC'].mean(), SI_Stimulu_Response['SR_5_ACC'].mean(), SI_Stimulu_Response['SR_6_ACC'].mean(),
            SI_Stimulu_Response['SR_7_ACC'].mean(), SI_Stimulu_Response['SR_8_ACC'].mean(), SI_Stimulu_Response['SR_9_ACC'].mean(),
            SI_Stimulu_Response['SR_10_ACC'].mean(), SI_Stimulu_Response['SR_11_ACC'].mean(), SI_Stimulu_Response['SR_12_ACC'].mean()]

SI_y_rt = [SI_Stimulu_Response['SR_1_RT'].mean(), SI_Stimulu_Response['SR_2_RT'].mean(), SI_Stimulu_Response['SR_3_RT'].mean(), 
           SI_Stimulu_Response['SR_4_RT'].mean(), SI_Stimulu_Response['SR_5_RT'].mean(), SI_Stimulu_Response['SR_6_RT'].mean(),
           SI_Stimulu_Response['SR_7_RT'].mean(), SI_Stimulu_Response['SR_8_RT'].mean(), SI_Stimulu_Response['SR_9_RT'].mean(),
           SI_Stimulu_Response['SR_10_RT'].mean(), SI_Stimulu_Response['SR_11_RT'].mean(), SI_Stimulu_Response['SR_12_RT'].mean()]

SI_y_leg_acc = [SI_Stimulu_Response['SR_1_ACC_leg'].mean(), SI_Stimulu_Response['SR_2_ACC_leg'].mean(), SI_Stimulu_Response['SR_3_ACC_leg'].mean(), 
                SI_Stimulu_Response['SR_4_ACC_leg'].mean(), SI_Stimulu_Response['SR_5_ACC_leg'].mean(), SI_Stimulu_Response['SR_6_ACC_leg'].mean(),
                SI_Stimulu_Response['SR_7_ACC_leg'].mean(), SI_Stimulu_Response['SR_8_ACC_leg'].mean(), SI_Stimulu_Response['SR_9_ACC_leg'].mean(),
                SI_Stimulu_Response['SR_10_ACC_leg'].mean(), SI_Stimulu_Response['SR_11_ACC_leg'].mean(), SI_Stimulu_Response['SR_12_ACC_leg'].mean()]

SI_y_leg_rt = [SI_Stimulu_Response['SR_1_RT_leg'].mean(), SI_Stimulu_Response['SR_2_RT_leg'].mean(), SI_Stimulu_Response['SR_3_RT_leg'].mean(), 
               SI_Stimulu_Response['SR_4_RT_leg'].mean(), SI_Stimulu_Response['SR_5_RT_leg'].mean(), SI_Stimulu_Response['SR_6_RT_leg'].mean(),
               SI_Stimulu_Response['SR_7_RT_leg'].mean(), SI_Stimulu_Response['SR_8_RT_leg'].mean(), SI_Stimulu_Response['SR_9_RT_leg'].mean(),
               SI_Stimulu_Response['SR_10_RT_leg'].mean(), SI_Stimulu_Response['SR_11_RT_leg'].mean(), SI_Stimulu_Response['SR_12_RT_leg'].mean()]

SI_y_antenn_acc = [SI_Stimulu_Response['SR_1_ACC_antenn'].mean(), SI_Stimulu_Response['SR_2_ACC_antenn'].mean(), SI_Stimulu_Response['SR_3_ACC_antenn'].mean(), 
                   SI_Stimulu_Response['SR_4_ACC_antenn'].mean(), SI_Stimulu_Response['SR_5_ACC_antenn'].mean(), SI_Stimulu_Response['SR_6_ACC_antenn'].mean(),
                   SI_Stimulu_Response['SR_7_ACC_antenn'].mean(), SI_Stimulu_Response['SR_8_ACC_antenn'].mean(), SI_Stimulu_Response['SR_9_ACC_antenn'].mean(),
                   SI_Stimulu_Response['SR_10_ACC_antenn'].mean(), SI_Stimulu_Response['SR_11_ACC_antenn'].mean(), SI_Stimulu_Response['SR_12_ACC_antenn'].mean()]

SI_y_antenn_rt = [SI_Stimulu_Response['SR_1_RT_antenn'].mean(), SI_Stimulu_Response['SR_2_RT_antenn'].mean(), SI_Stimulu_Response['SR_3_RT_antenn'].mean(), 
                  SI_Stimulu_Response['SR_4_RT_antenn'].mean(), SI_Stimulu_Response['SR_5_RT_antenn'].mean(), SI_Stimulu_Response['SR_6_RT_antenn'].mean(),
                  SI_Stimulu_Response['SR_7_RT_antenn'].mean(), SI_Stimulu_Response['SR_8_RT_antenn'].mean(), SI_Stimulu_Response['SR_9_RT_antenn'].mean(),
                  SI_Stimulu_Response['SR_10_RT_antenn'].mean(), SI_Stimulu_Response['SR_11_RT_antenn'].mean(), SI_Stimulu_Response['SR_12_RT_antenn'].mean()]

SI_y_mouth_acc = [SI_Stimulu_Response['SR_1_ACC_mouth'].mean(), SI_Stimulu_Response['SR_2_ACC_mouth'].mean(), SI_Stimulu_Response['SR_3_ACC_mouth'].mean(), 
                  SI_Stimulu_Response['SR_4_ACC_mouth'].mean(), SI_Stimulu_Response['SR_5_ACC_mouth'].mean(), SI_Stimulu_Response['SR_6_ACC_mouth'].mean(),
                  SI_Stimulu_Response['SR_7_ACC_mouth'].mean(), SI_Stimulu_Response['SR_8_ACC_mouth'].mean(), SI_Stimulu_Response['SR_9_ACC_mouth'].mean(),
                  SI_Stimulu_Response['SR_10_ACC_mouth'].mean(), SI_Stimulu_Response['SR_11_ACC_mouth'].mean(), SI_Stimulu_Response['SR_12_ACC_mouth'].mean()]

SI_y_mouth_rt = [SI_Stimulu_Response['SR_1_RT_mouth'].mean(), SI_Stimulu_Response['SR_2_RT_mouth'].mean(), SI_Stimulu_Response['SR_3_RT_mouth'].mean(), 
                 SI_Stimulu_Response['SR_4_RT_mouth'].mean(), SI_Stimulu_Response['SR_5_RT_mouth'].mean(), SI_Stimulu_Response['SR_6_RT_mouth'].mean(),
                 SI_Stimulu_Response['SR_7_RT_mouth'].mean(), SI_Stimulu_Response['SR_8_RT_mouth'].mean(), SI_Stimulu_Response['SR_9_RT_mouth'].mean(),
                 SI_Stimulu_Response['SR_10_RT_mouth'].mean(), SI_Stimulu_Response['SR_11_RT_mouth'].mean(), SI_Stimulu_Response['SR_12_RT_mouth'].mean()]


####################################################################################################################
############################# Stimulus Blocked New Version with Planet #############################################
#####################################################################################################################

SBN_y_acc = [SBN_Stimulu_Response['SR_1_ACC'].mean(), SBN_Stimulu_Response['SR_2_ACC'].mean(), SBN_Stimulu_Response['SR_3_ACC'].mean(), 
             SBN_Stimulu_Response['SR_4_ACC'].mean(), SBN_Stimulu_Response['SR_5_ACC'].mean(), SBN_Stimulu_Response['SR_6_ACC'].mean(),
             SBN_Stimulu_Response['SR_7_ACC'].mean(), SBN_Stimulu_Response['SR_8_ACC'].mean(), SBN_Stimulu_Response['SR_9_ACC'].mean(),
             SBN_Stimulu_Response['SR_10_ACC'].mean(), SBN_Stimulu_Response['SR_11_ACC'].mean(), SBN_Stimulu_Response['SR_12_ACC'].mean()]

SBN_y_rt = [SBN_Stimulu_Response['SR_1_RT'].mean(), SBN_Stimulu_Response['SR_2_RT'].mean(), SBN_Stimulu_Response['SR_3_RT'].mean(), 
            SBN_Stimulu_Response['SR_4_RT'].mean(), SBN_Stimulu_Response['SR_5_RT'].mean(), SBN_Stimulu_Response['SR_6_RT'].mean(),
            SBN_Stimulu_Response['SR_7_RT'].mean(), SBN_Stimulu_Response['SR_8_RT'].mean(), SBN_Stimulu_Response['SR_9_RT'].mean(),
            SBN_Stimulu_Response['SR_10_RT'].mean(), SBN_Stimulu_Response['SR_11_RT'].mean(), SBN_Stimulu_Response['SR_12_RT'].mean()]

SBN_y_leg_acc= [SBN_Stimulu_Response['SR_1_ACC_leg'].mean(), SBN_Stimulu_Response['SR_2_ACC_leg'].mean(), SBN_Stimulu_Response['SR_3_ACC_leg'].mean(), 
                SBN_Stimulu_Response['SR_4_ACC_leg'].mean(), SBN_Stimulu_Response['SR_5_ACC_leg'].mean(), SBN_Stimulu_Response['SR_6_ACC_leg'].mean(),
                SBN_Stimulu_Response['SR_7_ACC_leg'].mean(), SBN_Stimulu_Response['SR_8_ACC_leg'].mean(), SBN_Stimulu_Response['SR_9_ACC_leg'].mean(),
                SBN_Stimulu_Response['SR_10_ACC_leg'].mean(), SBN_Stimulu_Response['SR_11_ACC_leg'].mean(), SBN_Stimulu_Response['SR_12_ACC_leg'].mean()]

SBN_y_leg_rt= [SBN_Stimulu_Response['SR_1_RT_leg'].mean(), SBN_Stimulu_Response['SR_2_RT_leg'].mean(), SBN_Stimulu_Response['SR_3_RT_leg'].mean(), 
               SBN_Stimulu_Response['SR_4_RT_leg'].mean(), SBN_Stimulu_Response['SR_5_RT_leg'].mean(), SBN_Stimulu_Response['SR_6_RT_leg'].mean(),
               SBN_Stimulu_Response['SR_7_RT_leg'].mean(), SBN_Stimulu_Response['SR_8_RT_leg'].mean(), SBN_Stimulu_Response['SR_9_RT_leg'].mean(),
               SBN_Stimulu_Response['SR_10_RT_leg'].mean(), SBN_Stimulu_Response['SR_11_RT_leg'].mean(), SBN_Stimulu_Response['SR_12_RT_leg'].mean()]

SBN_y_antenn_acc= [SBN_Stimulu_Response['SR_1_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_2_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_3_ACC_antenn'].mean(), 
                   SBN_Stimulu_Response['SR_4_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_5_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_6_ACC_antenn'].mean(),
                   SBN_Stimulu_Response['SR_7_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_8_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_9_ACC_antenn'].mean(),
                   SBN_Stimulu_Response['SR_10_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_11_ACC_antenn'].mean(), SBN_Stimulu_Response['SR_12_ACC_antenn'].mean()]

SBN_y_antenn_rt= [SBN_Stimulu_Response['SR_1_RT_antenn'].mean(), SBN_Stimulu_Response['SR_2_RT_antenn'].mean(), SBN_Stimulu_Response['SR_3_RT_antenn'].mean(), 
                  SBN_Stimulu_Response['SR_4_RT_antenn'].mean(), SBN_Stimulu_Response['SR_5_RT_antenn'].mean(), SBN_Stimulu_Response['SR_6_RT_antenn'].mean(),
                  SBN_Stimulu_Response['SR_7_RT_antenn'].mean(), SBN_Stimulu_Response['SR_8_RT_antenn'].mean(), SBN_Stimulu_Response['SR_9_RT_antenn'].mean(),
                  SBN_Stimulu_Response['SR_10_RT_antenn'].mean(), SBN_Stimulu_Response['SR_11_RT_antenn'].mean(), SBN_Stimulu_Response['SR_12_RT_antenn'].mean()]

SBN_y_mouth_acc= [SBN_Stimulu_Response['SR_1_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_2_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_3_ACC_mouth'].mean(), 
                  SBN_Stimulu_Response['SR_4_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_5_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_6_ACC_mouth'].mean(),
                  SBN_Stimulu_Response['SR_7_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_8_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_9_ACC_mouth'].mean(),
                  SBN_Stimulu_Response['SR_10_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_11_ACC_mouth'].mean(), SBN_Stimulu_Response['SR_12_ACC_mouth'].mean()]

SBN_y_mouth_rt= [SBN_Stimulu_Response['SR_1_RT_mouth'].mean(), SBN_Stimulu_Response['SR_2_RT_mouth'].mean(), SBN_Stimulu_Response['SR_3_RT_mouth'].mean(), 
                 SBN_Stimulu_Response['SR_4_RT_mouth'].mean(), SBN_Stimulu_Response['SR_5_RT_mouth'].mean(), SBN_Stimulu_Response['SR_6_RT_mouth'].mean(),
                 SBN_Stimulu_Response['SR_7_RT_mouth'].mean(), SBN_Stimulu_Response['SR_8_RT_mouth'].mean(), SBN_Stimulu_Response['SR_9_RT_mouth'].mean(),
                 SBN_Stimulu_Response['SR_10_RT_mouth'].mean(), SBN_Stimulu_Response['SR_11_RT_mouth'].mean(), SBN_Stimulu_Response['SR_12_RT_mouth'].mean()]


###########################################################################################
###########################################################################################
####################### Stimulus_Response ACC Plot ########################################
###########################################################################################
###########################################################################################
plt.style.use('Solarize_Light2')
plt.xticks(rotation=45) 
plt.plot(x_axis,CB_y_acc , 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
#plt.plot(x_axis, CI_y_acc, 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_acc, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_acc, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
#plt.plot(x_axis, SI_y_acc, 'o-',label = "Stimulus_Interleaved Keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_acc, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
plt.xlabel('Repetition') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy Stimulus_Response Repetition",fontsize=20)
plt.legend()
plt.show()

###########################################################################################
###########################################################################################
####################### Stimulus_Response RT Plot ########################################
###########################################################################################
###########################################################################################
plt.xticks(rotation=45) 
#plt.style.use('grayscale')
plt.plot(x_axis,CB_y_rt , 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CI_y_rt, 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_rt, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_rt, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_rt, 'o-',label = "Stimulus_Interleaved Keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_rt, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
plt.xlabel('Repetition') 
plt.ylabel('Mean RT')
plt.title("Mean Reaction Time Stimulus_Response Repetition",fontsize=20)
#plt.legend()
plt.show()

###########################################################################################
###########################################################################################
####################### Stimulus_Response ACC  Leg Plot ###################################
###########################################################################################
###########################################################################################
# ACC Leg

plt.xticks(rotation=45) 
plt.plot(x_axis, CB_y_leg_acc, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis,CI_y_leg_acc , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_leg_acc, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_leg_acc, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_leg_acc, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_leg_acc, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Repetition of Stimulus') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy Leg Rule",fontsize=20)
#plt.legend()
plt.show()

###########################################################################################
###########################################################################################
####################### Stimulus_Response RT  Leg Plot ###################################
###########################################################################################
###########################################################################################
# RT Leg
plt.xticks(rotation=45) 
plt.plot(x_axis, CB_y_leg_rt, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis,CI_y_leg_rt , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_leg_rt, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_leg_rt, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_leg_rt, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_leg_rt, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Repetition of Stimulus') 
plt.ylabel('Mean RT')
plt.title("Mean Reaction Time Leg Rule",fontsize=20)
#plt.legend()
plt.show()

###########################################################################################
###########################################################################################
####################### Stimulus_Response ACC  Antenn Plot ###################################
###########################################################################################
###########################################################################################
# ACC Antenn

plt.xticks(rotation=45) 
plt.plot(x_axis, CB_y_antenn_acc, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis,CI_y_antenn_acc , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_antenn_acc, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_antenn_acc, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_antenn_acc, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_antenn_acc, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Repetition of Stimulus') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy Antenn Rule",fontsize=20)
#plt.legend()
plt.show()

###########################################################################################
###########################################################################################
####################### Stimulus_Response RT  Antenn Plot ###################################
###########################################################################################
###########################################################################################
# RT Antenn

plt.xticks(rotation=45) 
plt.plot(x_axis, CB_y_antenn_rt, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis,CI_y_antenn_rt , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_antenn_rt, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_antenn_rt, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_antenn_rt, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_antenn_rt, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Repetition of Stimulus') 
plt.ylabel('Mean RT')
plt.title("Mean Reaction Time Antenn Rule",fontsize=20)
#plt.legend()
plt.show()


###########################################################################################
###########################################################################################
####################### Stimulus_Response ACC Mouth Plot ###################################
###########################################################################################
###########################################################################################
# ACC Mouth

plt.xticks(rotation=45) 
plt.plot(x_axis, CB_y_mouth_acc, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis,CI_y_mouth_acc , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_mouth_acc, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_mouth_acc, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_mouth_acc, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_mouth_acc, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Repetition of Stimulus') 
plt.ylabel('Mean ACC')
plt.title("Mean Accuracy Mouth Rule",fontsize=20)
#plt.legend()
plt.show()

###########################################################################################
###########################################################################################
####################### Stimulus_Response RT Mouth Plot ###################################
###########################################################################################
###########################################################################################
# RT Mouth

plt.xticks(rotation=45) 
plt.plot(x_axis, CB_y_mouth_rt, 's:',label = "Context_Blocked Planet", color='#95baf5',markersize=12)
plt.plot(x_axis,CI_y_mouth_rt , 'o-',label = "Context_Interleaved Planet", color='#95baf5',markersize=12)
plt.plot(x_axis, CBN_y_mouth_rt, 's-', markersize=12, mec = 'k',label = "Context_Blocked Keys", color='#95baf5')
plt.plot(x_axis, SBN_y_mouth_rt, 's:',label = "Stimulus_Blocked_Planet", color='#f09797',markersize=12)
plt.plot(x_axis, SI_y_mouth_rt, 'o-',label = "Stimulus_Interleaved keys", color='#f09797',markersize=12, mec = 'k')
plt.plot(x_axis, SB_y_mouth_rt, 's-',label = "Stimulus_Blocked Keys", color='#f09797',markersize=12,mec = 'k')
#plt.plot(x_axis, , 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Repetition of Stimulus') 
plt.ylabel('Mean RT')
plt.title("Mean Reaction Time Mouth Rule",fontsize=20)
#plt.legend()
plt.show()
