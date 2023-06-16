#############################################################################################
################################################## DAY 1 #####################################
#############################################################################################
import pandas as pd
import numpy as np

##########################################################################################
########################################### Path Address ############################################
###########################################################################################
########################################################################################################################
########################################### Context Oriented Blocked Day1  #############################################
########################################################################################################################
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//5.Stimulus_Oriented_Blocked_New_Version_Two_Days//Day1//'




##############################################################################################################
################################################# list csv files##############################################
##############################################################################################################

###############################################################################################################
###############################################Contex_Oriented_Blocked_Day1 ###############################
################################################################################################################

 #omit 5cc5aec9ef83da0001cffead.csv
 # 606537639bc40e88e953c584.csv

list_csv_file=['6337cba5cbed8cb3514a6504.csv','5dcf932f3708100b7db43ddd.csv','5e6685e1ffed4c405a4db5d0.csv',
               '60e797b64fca2922f9cd51af.csv','5f0fab5abdec9a1aff2b2744.csv','6101930ddd5330f83b898c61.csv',
               '5fb757520b48c928a9b6e00b.csv','6318f71ece2f523f840e1eee.csv','5c27de12a2b00a00018b2c16.csv',
               '5cec5281dfb2720019961f4d.csv','5f0a5a99dbbf721316f118e2.csv','5ea9fd35de1f1015aea1117a.csv',
               '5e82a76d09f66f9cd3aeb0e7.csv','631636ea6359694a5ae0be31.csv','5d462cd2638dca0001daa57c.csv',
               '5658000ca9872d0011e1ba26.csv','5dbbfa90c486791b1bd03292.csv','5e27868c5cbbcc0b3599574b.csv',
               '5a4f6c4b5f741700018a79a8.csv','5d96eeed1998fb00177f6b71.csv','62b33f729b02ed15713cb73b.csv',
               '5a6fd0626923df0001ef977b.csv','5e8d44819163b611f62d706c.csv','62a733deec84f43ab19f7cca.csv',
               '5fa4f94e535f3b1aa628e0ab.csv','601e13b872774f263d64acac.csv','5f6e36c7f042f033d0f97bc1.csv',
               '5c2dea19d396500001e2b39d.csv','63162e1bbde3c4bb1d9d92a3.csv','614e29a3a354be1de3eb1bc8.csv',
               '62bdad093f129a724c4dd7b2.csv','60fced51e14f51249023972a.csv','6305b8d5ac4df0bfd1e5b335.csv',
               '56b4b565b2de2a000d3316ba.csv','558acd52fdf99b65685f03d9.csv','5ed8cf4782a6eb04ddf9962d.csv',
               '61010400617800821cac834e.csv','5d6f332829c25100188a4a27.csv','610b164074738771ef9acb0a.csv',
               '5c1942e200849900010afdcd.csv','5e45a7e926e79c000bc12a85.csv','603862f99e00971c55fe0874.csv',
               '605fe9680cac2ea943d411ec.csv','5e68b753e203811578c0a521.csv','5a04869ff2e3460001edad2e.csv',
               '5f98fd9bc1d2852287281bdb.csv','5f1273feb9ddf60dd2781b2f.csv','594a964c215cbd000146de75.csv',
               '63275a285d39ed53838654f1.csv','56f59251736c79000c2241f7.csv','6109d15f510e56947f3f1bae.csv',
               '628de6437f61a055721e9c1d.csv','5c6fb7c3c114eb00018b3154.csv','611ab91a00baa062f55b86d8.csv',
               '5a78e410ae9a0b0001a97274.csv','60ff61f892600d5d9c7a9ce5.csv','6278700097208c3f1b717481.csv',
               '5e9749b44592572013c96868.csv','61506f90721dcdeca6e77c2d.csv','5f569e71ae1bf40eae8b5e28.csv',
               '63254db937c17e8e9200fd54.csv','63474e67a5fd298c6103c409.csv','5ee232f2b970662cfa352567.csv',
               '62911ef14fd68295d60ba83b.csv','61452bbe86c21c0347085911.csv','62bdc30224534809032cf056.csv',
               '5e8b89d0afcb1606e761ef7f.csv','616c4a95398b06c2c85b32ed.csv','5dee72917309b950e5262f3a.csv',
               '60da65c630ff4389c297b03c.csv','5b0b3ef830d562000155366f.csv','5b5c8d4e10aec90001ed4bee.csv',
               '631c8e97db06f601f81bd82f.csv']


################################################################################################################
############################################ Payment DataFrame ##################################################
##################################################################################################################


column_list_payment=['prolificID', 'session', 'version', 'Age','gender',
                     'RT_block_1','RT_block_2','RT_block_3','RT_block_4','RT_block_5',
                     'RT_block_6','RT_block_7','RT_block_8','RT_block_9',
                     'nun_seq_1','nun_seq_2','nun_seq_3','nun_seq_4','nun_seq_5',
                     'nun_seq_6','nun_seq_7','nun_seq_8','nun_seq_9',
                     'Response_Percentage_block_1','Response_Percentage_block_2','Response_Percentage_block_3',
                     'Response_Percentage_block_4','Response_Percentage_block_5','Response_Percentage_block_6',
                     'Response_Percentage_block_7','Response_Percentage_block_8','Response_Percentage_block_9',
                     'Response_distribution_block_1','Response_distribution_block_2','Response_distribution_block_3',
                     'Response_distribution_block_4','Response_distribution_block_5','Response_distribution_block_6',
                     'Response_distribution_block_7','Response_distribution_block_8','Response_distribution_block_9']

df_payment=pd.DataFrame(columns=column_list_payment)

#df = pd.read_csv(address+'629fec7ad26e41512fe15400.csv')

for i in range(len(list_csv_file)):
    
    df = pd.read_csv(address+list_csv_file[i])
    
    counts_1=df.iloc[0:48]['response'].isnull().astype(int).groupby(df.iloc[0:48]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_1=counts_1.max(axis=0) 
    
    counts_2=df.iloc[48:96]['response'].isnull().astype(int).groupby(df.iloc[48:96]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_2=counts_2.max(axis=0)
    
    counts_3=df.iloc[96:144]['response'].isnull().astype(int).groupby(df.iloc[96:144]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_3=counts_3.max(axis=0)
    
    counts_4=df.iloc[144:192]['response'].isnull().astype(int).groupby(df.iloc[144:192]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_4=counts_4.max(axis=0)
    
    counts_5=df.iloc[192:240]['response'].isnull().astype(int).groupby(df.iloc[192:240]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_5=counts_5.max(axis=0)
    
    counts_6=df.iloc[240:288]['response'].isnull().astype(int).groupby(df.iloc[240:288]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_6=counts_6.max(axis=0)
    
    counts_7=df.iloc[288:336]['response'].isnull().astype(int).groupby(df.iloc[288:336]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_7=counts_7.max(axis=0)
    
    counts_8=df.iloc[336:384]['response'].isnull().astype(int).groupby(df.iloc[336:384]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_8=counts_8.max(axis=0)
    
    counts_9=df.iloc[384:432]['response'].isnull().astype(int).groupby(df.iloc[384:432]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_9=counts_9.max(axis=0)
    
    dict_data={}
    dict_data={'prolificID': df['prolificID'][0], 'session': df['session'][0], 'version': df['version'][0], 
               'Age':df['Age'][0],'gender':df['gender'][0],
               'nun_seq_1':nun_seq_1, 'nun_seq_2':nun_seq_2, 'nun_seq_3':nun_seq_3,
               'nun_seq_4':nun_seq_4, 'nun_seq_5': nun_seq_5, 'nun_seq_6': nun_seq_6,
               'nun_seq_7':nun_seq_7, 'nun_seq_8': nun_seq_8, 'nun_seq_9':nun_seq_9,
               'RT_block_1': df.iloc[0:48]['reaction_time'].mean(),
               'RT_block_2': df.iloc[48:96]['reaction_time'].mean(),
               'RT_block_3': df.iloc[96:144]['reaction_time'].mean(),
               'RT_block_4': df.iloc[144:192]['reaction_time'].mean(),
               'RT_block_5': df.iloc[192:240]['reaction_time'].mean(),
               'RT_block_6': df.iloc[240:288]['reaction_time'].mean(),
               'RT_block_7': df.iloc[288:336]['reaction_time'].mean(),
               'RT_block_8': df.iloc[336:384]['reaction_time'].mean(),
               'RT_block_9': df.iloc[384:432]['reaction_time'].mean(),
               'Response_Percentage_block_1': (df.iloc[0:48]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_2': (df.iloc[48:96]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_3': (df.iloc[96:144]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_4': (df.iloc[144:192]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_5': (df.iloc[192:240]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_6': (df.iloc[240:288]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_7': (df.iloc[288:336]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_8': (df.iloc[336:384]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_9': (df.iloc[384:432]['response'].notnull().sum()/48)*100,
               
               'Response_distribution_block_1': (df.iloc[0:48]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_2': (df.iloc[48:96]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_3': (df.iloc[96:144]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_4': (df.iloc[144:192]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_5': (df.iloc[192:240]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_6': (df.iloc[240:288]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_7': (df.iloc[288:336]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_8': (df.iloc[336:384]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_9': (df.iloc[384:432]['response'].value_counts()['d']/48)*100}
       
    df_payment = df_payment.append(dict_data, ignore_index=True)
#saving df_total to csv
########################################################################################################################
################################## change th addrress and name of the file ############################################
##########################################################################################################################



df_payment.to_csv(address+'df_payment_Stimulus_Blocked_New_Version_Day1.csv', index=False)




# now I make df.payment. Now I want to exclude participants from payment and data analysis.

       
###########################################################################################################
##################################### Exclude from Payment ################################################
############################################################################################################

# 1. Response distribution per block & generally:
    # for example keep pressing D or K for more than 90% of times: here I only count apperance of 'd' so if
    # 'd' count percentage is less than 10% it means they keep pressing 'k' and I will omit them from the 
    # payment and also analysis.
    
# 2. if the mean RT in each (even one block) is less than 300ms I will omit that person from payment and analyis

# 3. null response in one block 30% sequentially.
    
omit_subject_list=[]
for i in range (len( df_payment)):
    #print(i)
    if (df_payment.iloc[i]['RT_block_1']<300 or
        df_payment.iloc[i]['RT_block_2']<300 or
        df_payment.iloc[i]['RT_block_3']<300 or
        df_payment.iloc[i]['RT_block_4']<300 or
        df_payment.iloc[i]['RT_block_5']<300 or
        df_payment.iloc[i]['RT_block_6']<300 or
        df_payment.iloc[i]['RT_block_7']<300 or
        df_payment.iloc[i]['RT_block_8']<300 or
        df_payment.iloc[i]['RT_block_9']<300 or
        df_payment.iloc[i]['nun_seq_1'] > 14 or
        df_payment.iloc[i]['nun_seq_2'] > 14 or
        df_payment.iloc[i]['nun_seq_3'] > 14 or
        df_payment.iloc[i]['nun_seq_4'] > 14 or
        df_payment.iloc[i]['nun_seq_5'] > 14 or
        df_payment.iloc[i]['nun_seq_6'] > 14 or
        df_payment.iloc[i]['nun_seq_7'] > 14 or
        df_payment.iloc[i]['nun_seq_8'] > 14 or
        df_payment.iloc[i]['nun_seq_9'] > 14 or
        df_payment.iloc[i]['Response_distribution_block_1']<10 or
        df_payment.iloc[i]['Response_distribution_block_2']<10 or
        df_payment.iloc[i]['Response_distribution_block_3']<10 or
        df_payment.iloc[i]['Response_distribution_block_4']<10 or
        df_payment.iloc[i]['Response_distribution_block_5']<10 or
        df_payment.iloc[i]['Response_distribution_block_6']<10 or
        df_payment.iloc[i]['Response_distribution_block_7']<10 or
        df_payment.iloc[i]['Response_distribution_block_8']<10 or
        df_payment.iloc[i]['Response_distribution_block_9']<10 ):
        
        omit=1;
        omit_subject_list.append(df_payment.iloc[i]['prolificID'])
        
    else:
        omit=0;


# Save omit_subject_list

import csv
with open(address+"omit_subject_list.csv", "w") as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(omit_subject_list)


# omiting partipant from list_csv_file 
# only participants in df_total from first day would be considered for payment if they pass conditions in second day too        
for i in omit_subject_list:
    print(i)
    i=i+'.csv'
    result = list_csv_file.index(i)
    #result=result+'.csv'
    print(result)
    print(list_csv_file[result])
    list_csv_file.pop(result)
    

#############################################################################################
############################################################################################
# only partiicpants in df_total will be paid

column_list=['prolificID', 'session', 'version', 'Age','gender', 'extra_payment',
             'RT_block_1','RT_block_2','RT_block_3','RT_block_4','RT_block_5',
             'RT_block_6','RT_block_7','RT_block_8','RT_block_9',
             'ACC_block_1', 'ACC_block_2','ACC_block_3','ACC_block_4','ACC_block_5',
             'ACC_block_6','ACC_block_7','ACC_block_8','ACC_block_9']
df_total=pd.DataFrame(columns=column_list)

for i in range(len(list_csv_file)):
    df = pd.read_csv(address+list_csv_file[i])
    print(list_csv_file[i])
    #print(df)
    extra_payment=3*2*((df['accuracy'].sum()/len(df['accuracy']))-0.50)
    dict_data={}
    dict_data={'prolificID': df['prolificID'][0], 'session': df['session'][0], 'version': df['version'][0], 
               'Age':df['Age'][0],'gender':df['gender'][0], 'extra_payment': extra_payment,
               'RT_block_1': df.iloc[0:48]['reaction_time'].mean(),
               'RT_block_2': df.iloc[48:96]['reaction_time'].mean(),
               'RT_block_3': df.iloc[96:144]['reaction_time'].mean(),
               'RT_block_4': df.iloc[144:192]['reaction_time'].mean(),
               'RT_block_5': df.iloc[192:240]['reaction_time'].mean(),
               'RT_block_6':df.iloc[240:288]['reaction_time'].mean(),
               'RT_block_7': df.iloc[288:336]['reaction_time'].mean(),
               'RT_block_8':df.iloc[336:384]['reaction_time'].mean(),
               'RT_block_9':df.iloc[384:432]['reaction_time'].mean(),
               'ACC_block_1':df.iloc[0:48]['accuracy'].sum()/48,
               'ACC_block_2':df.iloc[48:96]['accuracy'].sum()/48,
               'ACC_block_3':df.iloc[96:144]['accuracy'].sum()/48,
               'ACC_block_4':df.iloc[144:192]['accuracy'].sum()/48,
               'ACC_block_5':df.iloc[192:240]['accuracy'].sum()/48,
               'ACC_block_6':df.iloc[240:288]['accuracy'].sum()/48,
               'ACC_block_7':df.iloc[288:336]['accuracy'].sum()/48,
               'ACC_block_8':df.iloc[336:384]['accuracy'].sum()/48,
               'ACC_block_9':df.iloc[384:432]['accuracy'].sum()/48,
               'Response_Percentage_block_1': (df.iloc[0:48]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_2': (df.iloc[48:96]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_3': (df.iloc[96:144]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_4': (df.iloc[144:192]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_5': (df.iloc[192:240]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_6': (df.iloc[240:288]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_7': (df.iloc[288:336]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_8': (df.iloc[336:384]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_9': (df.iloc[384:432]['response'].notnull().sum()/48)*100}
       
    df_total = df_total.append(dict_data, ignore_index=True)
    
    
#################################################################################################################
#define bionomial threshold here for acc of each block then you can remove subjects from df_total before saving    
    
##################################################################################################################    
#saving df_total to csv


df_total.to_csv(address+'df_total_Stimulus_Blocked_New_Version_Day1.csv', index=False)

# Check the outlier based on the Sennes critera only on ACC for Day1 Data:
    
# computing Biomedia Test for making criteria to moit subject:
# another way to use that function is to give it the proportion of success and the number of trials considered
# (it's basically the length of the array or the number of responses you take into account for a participant)
#pvalue = stats.binom_test(accuracy1.sum(), n = len(accuracy1), p=0.5, alternative='greater')
#print('accuracy 1: %.2f, pvalue 1= %.4f' % (accuracy1.mean(), pvalue))


# list csv file that pass the payment criteria. Now I want to check these participants performance 
# whether they can pass the ACC bionomial test criteria or not.
from scipy import stats
csv_list_ACC = df_total['prolificID'].tolist()

# address the first day data to go and check csv file of 6 training session to for ACC

Address_Day1='D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'


# I have df_total that  pass criteria for payment.
# now I want to make another criteria on that df_total to see how much
# consider which participants for ACC analysis.
# only keep csv files from second day that pass criteria from the first day ACC during 
# 6 blocks of training


    
omit_list_ACC_whole_train = []
omit_list_ACC_456_train = []

for i in range(len(csv_list_ACC)):
    
    df = pd.read_csv(Address_Day1+csv_list_ACC[i]+".csv")
    
    ACC_whole = df.iloc[0:288]['accuracy'].sum() #288
    ACC_456 = df.iloc[144:288]['accuracy'].sum()
    
    #print('sum of correct response from 288 trial: ', ACC_Success)
    
    pvalue = stats.binom_test(ACC_whole, n = 287, p=0.5, alternative='greater')
    pvalue_456 = stats.binom_test(ACC_456, n = 144, p=0.5, alternative='greater')
    
    #print('pvalue: ',pvalue)
    #print('-------------------\n')
    if pvalue > 0.05:
        print(csv_list_ACC[i])
        omit_list_ACC_whole_train.append(csv_list_ACC[i])
        
    if pvalue_456 > 0.05:
        print(csv_list_ACC[i])
        omit_list_ACC_456_train.append(csv_list_ACC[i])   
        

import copy

df_whole_train=copy.deepcopy(df_total)
df_456=copy.deepcopy(df_total)
# omit particpants with low
for i in omit_list_ACC_whole_train:
    j=i[0:-4]
    #print(i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if j in df_whole_train['prolificID'].tolist():
        #print('true')
        index=df_whole_train[df_whole_train['prolificID']==j].index.values
        df_whole_train.drop(index, inplace = True )
         
df_whole_train.to_csv(Address_Day1+'_DAY1_df_Total_Context_Blocked_ACC_Critera_Whole_Train.csv', index=False)




# omit particpants with low
for i in omit_list_ACC_456_train:
    j=i[0:-4]
    #print(i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if j in df_456['prolificID'].tolist():
        #print('true')
        index=df_456[df_456['prolificID']==j].index.values
        df_456.drop(index, inplace = True )
        
         
df_456.to_csv(Address_Day1+'DAY1_df_Total_Context_Blocked_ACC_Critera_456_Train.csv', index=False)
####################################################################################################

###################### Task1 Task2 Task3 ##########################################################
# check prolific ID in df_456: for each subject check what is task1 and task2 and task 3
# then extract task1, task2 and task3 from test phase:

csv_list_Task = df_456['prolificID'].tolist()

# address the first day data to go and check csv file of 6 training session to for ACC

Address_Day1 = 'D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'

mean_acc_task={'Task1_1':[], 'Task2_1':[], 'Task3_1':[],
               'Task1_2':[], 'Task2_2':[], 'Task3_2':[],
               'Task1_7':[], 'Task2_7':[], 'Task3_7':[],
               'Task1_8':[], 'Task2_8':[], 'Task3_8':[],
               'Task1_9':[], 'Task2_9':[], 'Task3_9':[]}


for i in range(len(csv_list_Task)): #csv_list_Task
    
    df = pd.read_csv(Address_Day1+csv_list_ACC[i]+".csv")
    #Task1 = df.iloc[0]['Rule']
    #Task2 = df.iloc[48]['Rule']
    #Task3 = df.iloc[96]['Rule']
    mean_acc_task['Task1_1'].append(df.iloc[0:48]['accuracy'].sum()/48)
    mean_acc_task['Task2_1'].append( df.iloc[48:96]['accuracy'].sum()/48)
    mean_acc_task['Task3_1'].append(df.iloc[96:144]['accuracy'].sum()/48)
    
    mean_acc_task['Task1_2'].append(df.iloc[144:192]['accuracy'].sum()/48)
    mean_acc_task['Task2_2'].append( df.iloc[192:240]['accuracy'].sum()/48)
    mean_acc_task['Task3_2'].append(df.iloc[240:288]['accuracy'].sum()/48)
    
    
    
    block_7_task1=[]
    block_7_task2=[]
    block_7_task3=[]
    
    block_8_task1=[]
    block_8_task2=[]
    block_8_task3=[]
    
    block_9_task1=[]
    block_9_task2=[]
    block_9_task3=[]
    for j in range (288,432):
        
        # Block 7
        if df.iloc[j]['block_number']==7:
            
            if df.iloc[j]['context_image']=='img/planet1.png':
                block_7_task1.append(df.iloc[j]['accuracy'])
                
            elif df.iloc[j]['context_image']=='img/planet2.png':
                block_7_task2.append(df.iloc[j]['accuracy'])
                
            elif df.iloc[j]['context_image']=='img/planet3.png':
                block_7_task3.append(df.iloc[j]['accuracy'])
            
        elif df.iloc[j]['block_number']==8:
            if df.iloc[j]['context_image']=='img/planet1.png':
                block_8_task1.append(df.iloc[j]['accuracy'])
                
            elif df.iloc[j]['context_image']=='img/planet2.png':
                block_8_task2.append(df.iloc[j]['accuracy'])
                
            elif df.iloc[j]['context_image']=='img/planet3.png':
                block_8_task3.append(df.iloc[j]['accuracy'])
            
        
        elif df.iloc[j]['block_number']==9:
            if df.iloc[j]['context_image']=='img/planet1.png':
                block_9_task1.append(df.iloc[j]['accuracy'])
                
            elif df.iloc[j]['context_image']=='img/planet2.png':
                block_9_task2.append(df.iloc[j]['accuracy'])
                
            elif df.iloc[j]['context_image']=='img/planet3.png':
                block_9_task3.append(df.iloc[j]['accuracy'])
    

    
    mean_acc_task['Task1_7'].append(pd.notnull(block_7_task1).sum()/16)
    mean_acc_task['Task2_7'].append(pd.notnull(block_7_task2).sum()/16)
    mean_acc_task['Task3_7'].append(pd.notnull(block_7_task3).sum()/16)
    
    mean_acc_task['Task1_8'].append(pd.notnull(block_8_task1).sum()/16)
    mean_acc_task['Task2_8'].append(pd.notnull(block_8_task2).sum()/16)
    mean_acc_task['Task3_8'].append(pd.notnull(block_8_task3).sum()/16)
    
    mean_acc_task['Task1_9'].append(pd.notnull(block_9_task1).sum()/16)
    mean_acc_task['Task2_9'].append(pd.notnull(block_9_task2).sum()/16)
    mean_acc_task['Task3_9'].append(pd.notnull(block_9_task3).sum()/16)
            

# Save CSV fiel to save the dictinary Open a csv file for writing
with open(Address_Day1+"CB_Planet_mean_acc_tasks.csv", "w", newline="") as fp:
    # Create a writer object
    writer = csv.DictWriter(fp, fieldnames=mean_acc_task.keys())

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerow(mean_acc_task)
    print('Done writing dict to a csv file')
  