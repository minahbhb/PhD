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


########################################################################################################################
########################################### Context Oriented Blocked Day1  #############################################
########################################################################################################################
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'


########################################################################################################################
########################################### Stimulus Oriented Interleaved Day1  ########################################
########################################################################################################################
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day1//Data//'


########################################################################################################################
########################################### Stimulus Oriented Blocked Day1  ########################################
########################################################################################################################
address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day1//Data//'


##############################################################################################################
################################################# list csv files##############################################
##############################################################################################################
## change list of csv files


###############################################################################################################
###############################################Contex_Oriented_Interleaved_Day1 ###############################
################################################################################################################

list_csv_file=['5dd5db1ded7ea4574c7bc996.csv','5dd4074feab0423daf012f92.csv','59a2f6d14d25e800012fcbde.csv',
               '60d13d406f3b34d6791c8831.csv','60f7320f98a037fd7718e698.csv','60fd00abc3abd38c0302fde8.csv',
               '603a700c15614a652832402a.csv','607cce4d28ef1f0561fc93ca.csv','629fec7ad26e41512fe15400.csv',
               '61141391b248527d53b5799c.csv']


###############################################################################################################
###############################################Contex_Oriented_Blocked_Day1 ###############################
################################################################################################################

list_csv_file=['5d167ddd177e8d0016e60cf6.csv','5e8bbb3680cbf20986c677e1.csv','5f3ac1732efa0a74f975b1a8.csv',
               '5f202fb60bd98f087818ea51.csv','60fddeb6dfaa94f6424e0916.csv','60fed81a020a69e3bbb6017d.csv',
               '62ac8d659c88fde55ead0662.csv','62fb383ce16d6921d1c2c2b8.csv','6101d3dd8a5037f20dfc505f.csv',
               '6101f4093ed452ae3b6d5ab9.csv','6238c921bb5d7b3e3b05ab0d.csv','61089ac8867ae303ec5acda5.csv',
               '6111846c736eac63d7930e09.csv','612597436eff2c3e15310f3f.csv']

###############################################################################################################
###############################################Stimulus_Oriented_Interleaved_Day1 ###############################
################################################################################################################

list_csv_file=[]

###############################################################################################################
###############################################Stimulus_Oriented_Blocked_Day1 ###############################
################################################################################################################

list_csv_file=[]



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


df_payment.to_csv(address+'df_payment_Context_Blocked_Day1.csv', index=False)


df_payment.to_csv(address+'df_payment_Stimulus_Interleavd_Day1.csv', index=False)


df_payment.to_csv(address+'df_payment_Stimulus_Blocked_Day1.csv', index=False)

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


df_total.to_csv(address+'df_total_Context_Blocked_Day1.csv', index=False)


df_total.to_csv(address+'df_total_Stimulus_Interleavd_Day1.csv', index=False)


df_total.to_csv(address+'df_total_Stimulus_Blocked_Day1.csv', index=False)


########################################################################################################################
##################################################### Ploting ##########################################################
########################################################################################################################


######################################################################################################################
################################################  ACC plot per person seprately#######################################
######################################################################################################################
import matplotlib.pyplot as plt 
# in the below code I have define ten colors but you can define more colors if you have more subject
color=['b','g','r','c', 'm','y','k','0.8','mediumseagreen','aquamarine']

# list of x axis 
x_axis=['Block_1', 'Block_2', 'Block_3', 'Block_4', 'Block_5', 'Block_6', 'Block_7', 'Block_8', 'Block_9']
plt.figure(figsize=(6, 3))
for i in range (df_total.shape[0]):
    
    y=df_total.iloc[i][['ACC_block_1','ACC_block_2','ACC_block_3','ACC_block_4','ACC_block_5','ACC_block_6','ACC_block_7','ACC_block_8','ACC_block_9']].tolist()
    plt.plot(x_axis,y,color=color[i],label='ACC_'+str(i+1), linewidth=2, marker = 'o',linestyle = 'dashed')
    plt.xticks(rotation='vertical')
    plt.title("Mean Accuracy")
    plt.xlabel('Block') 
    plt.ylabel('Mean ACC')     
   

plt.show()


##############################################################################################################################
####################################################### Mean ACC  for all 9 blocks ############################################
##############################################################################################################################

y1= [df_total['ACC_block_1'].mean(), df_total['ACC_block_2'].mean(), df_total['ACC_block_3'].mean(), df_total['ACC_block_4'].mean(),
     df_total['ACC_block_5'].mean(), df_total['ACC_block_6'].mean(), df_total['ACC_block_7'].mean(), df_total['ACC_block_8'].mean(),
     df_total['ACC_block_9'].mean()]

#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y1,'bo-')
plt.xticks(rotation='vertical')
plt.title("Mean Accuracy")
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
for x,y in zip(x_axis,y1):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()


#################################################################################################################################################
###############################################  RT per person sepratley ############################################################################
#################################################################################################################################################
# Again here I define 10 color since I have 10 subject if you have more you need to define more than 10 colors
#plot for RT seprately for each 
color=['b','g','r','c', 'm','y','k','0.8','mediumseagreen','aquamarine']
x_axis=['Block_1', 'Block_2', 'Block_3', 'Block_4', 'Block_5', 'Block_6', 'Block_7', 'Block_8', 'Block_9']
plt.figure(figsize=(6, 3))
for i in range (df_total.shape[0]):
    
    y2=df_total.iloc[i][['RT_block_1','RT_block_2','RT_block_3','RT_block_4','RT_block_5','RT_block_6','RT_block_7','RT_block_8','RT_block_9']].tolist()
    plt.plot(x_axis,y2,color=color[i],label='RT_'+str(i+1), linewidth=2, marker = 'o',linestyle = 'dashed')
    plt.xticks(rotation='vertical')
    plt.title("Mean Reaction Time")
    plt.xlabel('Block') 
    plt.ylabel('Mean RT')     
   

plt.show()
############################################################################################################################
################################################### Mean RT per ############################################################
###########################################################################################################################


y3= [df_total['RT_block_1'].mean(), df_total['RT_block_2'].mean(), df_total['RT_block_3'].mean(), df_total['RT_block_4'].mean(),
     df_total['RT_block_5'].mean(), df_total['RT_block_6'].mean(), df_total['RT_block_7'].mean(), df_total['RT_block_8'].mean(),
     df_total['RT_block_9'].mean()]

#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y3,'bo-')
plt.xticks(rotation='vertical')
plt.title("Mean RT")
plt.xlabel('Block') 
plt.ylabel('Mean RT')
for x,y in zip(x_axis,y3):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()
    
    
    
    
    
    
    
    
    
    
 
