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
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'




##############################################################################################################
################################################# list csv files##############################################
##############################################################################################################

###############################################################################################################
###############################################Contex_Oriented_Blocked_Day1 ###############################
################################################################################################################
# omit list
#'6297567582d2ed2d88ae0450.csv'
# '61104c55afa57c9be5431014.csv']


 
# omit this subject "'61104c55afa57c9be5431014.csv'"before becuase not provide response any response for block 9
list_csv_file=['5a381de00006450001bf2691.csv','5afafdf27245f60001157545.csv','5bc50c8c4b33560001091793.csv',
               '5bca67940f10750001d75f9f.csv','5c2ff645644d5300010c25f3.csv','5d167ddd177e8d0016e60cf6.csv',
               '5d863f244d401800016ece02.csv','5d8793d36c53380015139da9.csv','5d74001d391b6600175f433b.csv',
               '5e8bbb3680cbf20986c677e1.csv','5f3ac1732efa0a74f975b1a8.csv','5f6ffe82dd1c3b5cc2d12649.csv',
               '5f07b62e0e3ac43ea9d490c6.csv','5f49f3262a3d07563d14a7f1.csv','5f202fb60bd98f087818ea51.csv',
               '5f5588eb6fb28c959e202247.csv','5fa9bb93d513d12296138e8f.csv','55a43687fdf99b7da1908e0f.csv',
               '57a2b3e1dcff7d0001c7d0dc.csv','59ffb939517dfb00013dadda.csv','60a7d7b70d3cf8f48a8a490d.csv',
               '60c57903a2db0249ed2779b1.csv','60dbac86b641e23f9bf26260.csv','60ded53d38608c2fa0d1ac4f.csv',
               '60fcc085e84772374cdbb26d.csv','60fcf706f6dfcc4197194efc.csv','60fddeb6dfaa94f6424e0916.csv',
               '60fded771d362f0624a42a38.csv','60fed81a020a69e3bbb6017d.csv','62a0bb5765e6ebd99b2ebe61.csv',
               '62a382f0cbe832bed1d0e575.csv','62ac8d659c88fde55ead0662.csv','62cc751291275617a9c7222f.csv',
               '62d5844a8fcb262f38f5b64c.csv','62e92d95cf6c8f424060db1a.csv','62fb383ce16d6921d1c2c2b8.csv',
               '62fc25ef4ce0d3d169b7a120.csv','550bb70bfdf99b6853dab45e.csv','565bdfcec121fe0012fc3897.csv',
               '604a30e30fa5eba805fc1b51.csv','628deac8711dee5dbda650ae.csv','629f4800dfb8c7c86f69a67e.csv',
               '631b6d4fe26a64d24c946fb1.csv','632aa954e9b6a34171a5e7ed.csv','633b82ab54af035c569082fb.csv',
               '5608a73fd7def20012b7389d.csv','6009f6693bf880114f7bdc99.csv','6101d3dd8a5037f20dfc505f.csv',
               '6101f4093ed452ae3b6d5ab9.csv','6102c81e911700cf7ba5f6bd.csv','6108d6efa698e3dbe3b313d3.csv',
               '6138f7e0ad42e592ca5f2024.csv','6155b9c45f96867d9d9631fd.csv','6238c921bb5d7b3e3b05ab0d.csv',
               '6287a504c4cb277cf781b6bb.csv','61043f36bc2fb31110d2067d.csv','61089ac8867ae303ec5acda5.csv',
               '61664d58d18ca2325a81008e.csv','63260e13957b6901854eed9f.csv','610106becd177b1d8bee303c.csv',
               '6108295fdd0270d7544b5a8a.csv','6111846c736eac63d7930e09.csv','6328817c90a7f703ded34c91.csv',
               '61003045d0f2c8b7ddb40dbd.csv','61180000f554e49f07fd524e.csv','612597436eff2c3e15310f3f.csv',
               '629513753a4424c933282660.csv']


################################################################################################################
############################################ Payment DataFrame ##################################################
##################################################################################################################

# Based on these criterai I decide to keep the subject for payment or not: these three criteria is the least conservative ones that
# told me whether the sbject pay enough attention to the task.

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



df_payment.to_csv(address+'df_payment_Context_Blocked_Day1.csv', index=False)




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
               
               'Sum_ACC_block_1':df.iloc[0:48]['accuracy'].sum(),
               'Sum_ACC_block_2':df.iloc[48:96]['accuracy'].sum(),
               'Sum_ACC_block_3':df.iloc[96:144]['accuracy'].sum(),
               'Sum_ACC_block_4':df.iloc[144:192]['accuracy'].sum(),
               'Sum_ACC_block_5':df.iloc[192:240]['accuracy'].sum(),
               'Sum_ACC_block_6':df.iloc[240:288]['accuracy'].sum(),
               'Sum_ACC_block_7':df.iloc[288:336]['accuracy'].sum(),
               'Sum_ACC_block_8':df.iloc[336:384]['accuracy'].sum(),
               'Sum_ACC_block_9':df.iloc[384:432]['accuracy'].sum(),
               
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


df_total.to_csv(address+'df_total_Context_Blocked_Day1.csv', index=False)



##################################################################################################
# I Want to do my copmutation on data from the first day without considering the data from the second day
# so First I want to remove oulier

# See outlier with BoxPlot
import seaborn as sns
# BoxPlot ACC
sns.boxplot(df_total['ACC_block_1']) # No outlier base on ACC Block1
sns.boxplot(df_total['ACC_block_2']) # No outlier base on ACC Block2
sns.boxplot(df_total['ACC_block_3']) # No outlier base on ACC Block3

sns.boxplot(df_total['ACC_block_4']) # No outlier base on ACC Block4
sns.boxplot(df_total['ACC_block_5']) # No outlier base on ACC Block5
sns.boxplot(df_total['ACC_block_6']) # No outlier base on ACC Block6

sns.boxplot(df_total['ACC_block_7']) # No outlier base on ACC Block 7
sns.boxplot(df_total['ACC_block_8']) # No outlier base on ACC Block 8
sns.boxplot(df_total['ACC_block_9']) # No outlier base on ACC Block 9


# BoxPlot RT
sns.boxplot(df_total['RT_block_1']) # No outlier base on ACC Block1
sns.boxplot(df_total['RT_block_2']) # No outlier base on ACC Block2
sns.boxplot(df_total['RT_block_3']) # No outlier base on ACC Block3

sns.boxplot(df_total['RT_block_4']) # one outlier rt less than 500 ms the same subject has low acc
sns.boxplot(df_total['RT_block_5']) # No outlier base on ACC Block5
sns.boxplot(df_total['RT_block_6']) # No outlier base on ACC Block6

sns.boxplot(df_total['RT_block_7']) # No outlier base on ACC Block 7
sns.boxplot(df_total['RT_block_8']) # No outlier base on ACC Block 8
sns.boxplot(df_total['RT_block_9']) # No outlier base on ACC Block 9


#########################################################################################
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
    

###############################################################################################
# Check stimulus response or task1 task2 task3 ACC


