#############################################################################################
################################################## DAY 1 #####################################
#############################################################################################
import pandas as pd
import numpy as np

##########################################################################################
################################ Path Address ############################################
###########################################################################################
 
# change the path
############################################################################################################### 
########################################### Context Oriented Interleaved Day1  ################################
###############################################################################################################
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//2.Contex_Oriented_Interleaved_Two_Days//Day_1_Data_Pilot_Run//'



##############################################################################################################
################################################# list csv files##############################################
##############################################################################################################
## change list of csv files


###############################################################################################################
###############################################Contex_Oriented_Interleaved_Day1 ###############################
################################################################################################################

list_csv_file=['5a2add709408dc00016f57d3.csv','5a89cc2c000dab00018cbd38.csv','5ae090dadee8590001b078c8.csv',
               '5aea71b9b779850001926fa0.csv','5b7cbe9db630cf000125dffe.csv','5bf5aa89d944c300012634cc.csv',
               '5c4e14a80467570001252ce1.csv','5c5c7f9cdff4b30001aa79a5.csv','5c23c03889f035000173d7d7.csv',
               '5c55c45f53fba80001bcf323.csv','5c675fad8f100a000107e249.csv','5c39849b19ceb400010c62a1.csv',
               '5ccc60abe787e000167f8143.csv','5cf91ace3bb7c4000162318c.csv','5d8b32e664ac880018630273.csv',
               '5d63f9cd26a2ac001758c70d.csv','5d127351768ee30019d6231f.csv','5dd5db1ded7ea4574c7bc996.csv',
               '5dd4074feab0423daf012f92.csv','5deb3c192235ad24f4a21826.csv','5e6ef5fbf14d264ae2ef3867.csv',
               '5e70bf61017e070009a8a738.csv','5e76896ffb3c70208d6e2f41.csv','5ed0091bd374190b9b04045d.csv',
               '5ed543442db0060a955d12e1.csv','5efef32a88bb6a01c8087591.csv','5f0a0df6490a690d6418913d.csv',
               '5f8f0ae15fe9e60fbbbaead9.csv','5f888f1504ea37030833e9ec.csv','5f4813c94e8b081877fb26a6.csv',
               '5f90581950d8520e8c7d3890.csv','5fbd057ea95c7102638685d5.csv','5fc2c0cfdb80f9025c6b4810.csv',
               '5fee2749ad8fba1104bd0f5b.csv','5ffe97d636fe8d54580c662e.csv','59a2f6d14d25e800012fcbde.csv',
               '60ace56a83e45642b22d9954.csv','60d13d406f3b34d6791c8831.csv','60f7320f98a037fd7718e698.csv',
               '60fd00abc3abd38c0302fde8.csv','60fe2250d29c942d97aadd8b.csv','60fec21e36a05990cfa8a715.csv',
               '60ff81237a31ac64e3f71450.csv','60ffa146784103f75aadb045.csv','62a885d5b6af18b3d4579e1b.csv',
               '62b0d24d95bc72be2f45c720.csv','62bb2410591b34a4cf62ecc5.csv','62c5fbbb796500bb5406d772.csv',
               '62cd9290653f1ada1c0575e7.csv','62cf3efe6b75b1e4ee3c372f.csv','62e120bf4d1adef728ddf97a.csv',
               '603a700c15614a652832402a.csv','607cce4d28ef1f0561fc93ca.csv','610c0307782b54307339d806.csv',
               '627a7fc214142c6f228e84fb.csv','628d78a2ccf4a41f24c2d2d8.csv','628f827eeb876ed2617881e7.csv',
               '629fec7ad26e41512fe15400.csv','631b7e747ad94015bc372ca4.csv','6045e5cdb5547f7347302e2b.csv',
               '6091ebb375f9f6e9e1acaef8.csv','6130d9fdf4574ff3e2143b36.csv','611692a4e50bab52864b978f.csv',
               '615327ab3d238b032366a545.csv','633753ce3c8019c829e7ee33.csv','6154973c69da7c97996a19f6.csv',
               '6309045d7355790eefe2ce1b.csv','61141391b248527d53b5799c.csv','603312955f6c243adbe8761e.csv',
               '603470186bba1c26a354c27e.csv']




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

df_payment.to_csv(address+'df_payment_Context_Interleavd_Day1.csv', index=False)

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
df_total.to_csv(address+'df_total_Context_Interleavd_Day1.csv', index=False)


