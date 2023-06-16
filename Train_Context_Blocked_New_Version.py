#############################################################################################
################################################## DAY 1 #####################################
#############################################################################################
import pandas as pd
import numpy as np

##########################################################################################
################################ Path Address ############################################
###########################################################################################
 
########################################################################################################################
########################################### Stimulus Oriented Blocked Day1  ########################################
########################################################################################################################
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day1//'


###############################################################################################################
###############################################Stimulus_Oriented_Blocked_Day1 ###############################
################################################################################################################
 #Omit this '63640eea073c333b9864c09c.csv'
list_csv_file=['6110ab19ba94b5d169311689.csv','5a6ff39ef660ae0001a9837e.csv','610aba9d57e9ccd056ae5d01.csv',
               '610aea8b22775bec9bf559e9.csv','575f6c823fc3ac000611dffa.csv','5ff0f1b0dd8cf14ba8957c5b.csv',
               '5ea624b32b24666209c18941.csv','5be2991826f9ec00013f6f40.csv',
               '630f9d70f86ca1ee77a5b8dd.csv','603fa7d057d382087d66d1c2.csv','6111af1630b35a24a8476060.csv',
               '6147b57356da2c40473e3e06.csv','5ec1c41a1f98090e8c119332.csv','5ec3f58c9c7ec90e33fd1e39.csv',
               '60ffae39406f5e4035c8dea0.csv','5ad012585b53cb0001f33631.csv','5d134be5269dd500012b15fd.csv',
               '61085127e5234dfd63a0c740.csv','5d26aaf4665b0a00174b8f03.csv','5f736eaa35366908ce9145a2.csv',
               '5e13ad514c81b2a01ae4aa9f.csv','61006614d4c56450afce3a6b.csv','62349b2406ea604d296bd69d.csv',
               '5dac4dad5e53cc001499f1f6.csv','6101ef1676d38820d1002ef5.csv','5b3b934edd6af000014d3152.csv',
               '56942483e0c800000c5969d0.csv','5df5262b19232d3a9a52868b.csv','5ca227b36b36c400013ce15a.csv',
               '5d1d0270601cd7000172942f.csv','610820f8cc357db69daa892a.csv','614f571879ee135c5a579e08.csv',
               '6101aae23efe687ec3d4a2eb.csv','5eb6df62c23fbf5e87db6b4b.csv','60d099f849987e86824eedcd.csv',
               '6111457269336cf7c25383de.csv','6323781f75962af097c34b5e.csv','5f985a6faf071810974a32f8.csv',
               '5e1b299528c70235eeed62ef.csv','5c56964991c0ad0001cfa5ae.csv','613aae01f09a52a007cd063e.csv',
               '57b270d576b2ea0001c98812.csv','6340bbbd6d7184613357fc29.csv','63639d3bbd810ed5c307efc3.csv',
               '62bdc13b2c6f73e8769b419a.csv','62841e3601b7cae85fa2565b.csv','62b1ed31eaaaa61b18c69032.csv',
               '5e500ab1ec45d305b6b82d9f.csv','61729e07e7b9b645c1741ca9.csv','601c696f0370f35c7883cf99.csv',
               '6149256f6335b06ade3723e0.csv','60fe176cf09dbffb8b98b640.csv','61006b0f1f3bfddb6b4c5d55.csv',
               '59cf062758b71700019882d4.csv','55ea70c37480920010aa9982.csv','5de7ccc24b7cf973d7b05bfb.csv',
               '5d453e8723a5bb0001492546.csv','5a08663b3b6dfc0001445abe.csv','612e3a120a7d7d6f0bf16f83.csv',
               '61005a9bfd2f14f18ef7ec7d.csv','5e0a2f6377f8652c6fc3f887.csv','5eb5f6d5e38e9f4e6c8dde3f.csv',
               '61502f4029bebb130459f0ff.csv','6331b9456956d880a1e4632f.csv','6345dc3fd19b0554d9d7b533.csv',
               '5c8db07eb1f89a0016777fe0.csv','629e241d171ec6698e05f149.csv','5faeeaf841eec60d49cb9d1d.csv',
               '62df6e55d6e4b5d86aca366b.csv','5f16f559325a640008bb9a07.csv','63403b7f3fd164408c5ad4b0.csv',
               '56cc78e3ccc0e20006b82a7d.csv','611a5fe31213c287a98ca188.csv']


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

for i in range(len(list_csv_file)): #
    
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

df_payment.to_csv(address+'df_payment_Context_Blocked_NewVersion_Day1.csv', index=False)


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

df_total.to_csv(address+'df_total_Context_Blocked_NewVersion_Day1.csv', index=False)

#####################################################################################
##################### Mean ACC Task1 Task2 Task3 ####################################
#####################################################################################
#########################################################################################
# I want to consider all the data from day1 to because I will have more dataset in comparsion
# to if I only consider the data from Day2

# On all the data from DAY1 I want to define criteria on ACC

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

Address_Day1='D://OneDrive - UGent//Desktop//Mina//Prolific//6. Context_Oriented_Blocked_New_Version_WithTask_Two_Days//Day1//'


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
         
df_whole_train.to_csv(Address_Day1+'_DAY1_df_Total_Context_Blocked_Labeling_ACC_Critera_Whole_Train.csv', index=False)




# omit particpants with low
for i in omit_list_ACC_456_train:
    j=i[0:-4]
    #print(i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if j in df_456['prolificID'].tolist():
        #print('true')
        index=df_456[df_456['prolificID']==j].index.values
        df_456.drop(index, inplace = True )
        
         
df_456.to_csv(Address_Day1+'DAY1_df_Total_Context_Blocked_Labeling_ACC_Critera_456_Train.csv', index=False)
####################################################################################################

###################### Task1 Task2 Task3 ##########################################################
# check prolific ID in df_456: for each subject check what is task1 and task2 and task 3
# then extract task1, task2 and task3 from test phase:

csv_list_Task = df_456['prolificID'].tolist()

# address the first day data to go and check csv file of 6 training session to for ACC


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
            
            if ((df.iloc[j]['left_button']=='img/cold.png') |
               (df.iloc[j]['right_button']=='img/cold.png')):
                   
                block_7_task1.append(df.iloc[j]['accuracy'])
                
            elif ((df.iloc[j]['left_button']=='img/rural.png') |
                 (df.iloc[j]['right_button']=='img/urban.png')):
                     
                  block_7_task2.append(df.iloc[j]['accuracy'])
                
            elif ((df.iloc[j]['left_button']=='img/pois.png') |
                 (df.iloc[j]['right_button']=='img/ok.png')):
                
                 block_7_task3.append(df.iloc[j]['accuracy'])
            
        elif df.iloc[j]['block_number']==8:
            
            if ((df.iloc[j]['left_button']=='img/cold.png') |
               (df.iloc[j]['right_button']=='img/cold.png')):
                   
                block_8_task1.append(df.iloc[j]['accuracy'])
                
            elif ((df.iloc[j]['left_button']=='img/rural.png') |
                 (df.iloc[j]['right_button']=='img/urban.png')):
                     
                 block_8_task2.append(df.iloc[j]['accuracy'])
                
            elif ((df.iloc[j]['left_button']=='img/pois.png') |
                 (df.iloc[j]['right_button']=='img/ok.png')):
                     
                 block_8_task3.append(df.iloc[j]['accuracy'])
            
        
        elif df.iloc[j]['block_number']==9:
            
            if ((df.iloc[j]['left_button']=='img/cold.png') |
               (df.iloc[j]['right_button']=='img/cold.png')):
                   
                 block_9_task1.append(df.iloc[j]['accuracy'])
                
            elif ((df.iloc[j]['left_button']=='img/rural.png') |
                 (df.iloc[j]['right_button']=='img/urban.png')):
                     
                 block_9_task2.append(df.iloc[j]['accuracy'])
                
            elif ((df.iloc[j]['left_button']=='img/pois.png') |
                 (df.iloc[j]['right_button']=='img/ok.png')):
                     
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
with open(Address_Day1+"CB_Labeling_mean_acc_tasks.csv", "w", newline="") as fp:
    # Create a writer object
    writer = csv.DictWriter(fp, fieldnames=mean_acc_task.keys())

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerow(mean_acc_task)
    print('Done writing dict to a csv file')
    

###############################################################################################
# Check stimulus response or task1 task2 task3 ACC
