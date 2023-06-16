import pandas as pd
import numpy as np
import csv
#################################################################################################################
############################### Load data frame total from the day1 #############################################
#################################################################################################################

# df_total from Day1
df_total = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//df_total_Context_Blocked_Day1.csv')

# only keep csv files from second day that pass criteria from the first day
list_csv_file=df_total['prolificID'].tolist()
list_csv_file_Day2=[]
for i in list_csv_file:
    i=i+'.csv'
    list_csv_file_Day2.append(i)
    
## list csv files that participate in the second day
## I want to be sure I can find all the subject in 'list_csv_file_Day2' in the list of csv that I record 
csv_list=['5a381de00006450001bf2691.csv','5afafdf27245f60001157545.csv','5bc50c8c4b33560001091793.csv',
          '5bca67940f10750001d75f9f.csv','5c2ff645644d5300010c25f3.csv','5d167ddd177e8d0016e60cf6.csv',
          '5d863f244d401800016ece02.csv','5d8793d36c53380015139da9.csv','5e8bbb3680cbf20986c677e1.csv',
          '5f3ac1732efa0a74f975b1a8.csv','5f6ffe82dd1c3b5cc2d12649.csv','5f07b62e0e3ac43ea9d490c6.csv',
          '5f202fb60bd98f087818ea51.csv','5f5588eb6fb28c959e202247.csv','5fa9bb93d513d12296138e8f.csv',
          '55a43687fdf99b7da1908e0f.csv','59ffb939517dfb00013dadda.csv','60a7d7b70d3cf8f48a8a490d.csv',
          '60dbac86b641e23f9bf26260.csv','60ded53d38608c2fa0d1ac4f.csv','60fcc085e84772374cdbb26d.csv',
          '60fddeb6dfaa94f6424e0916.csv','60fded771d362f0624a42a38.csv','62a382f0cbe832bed1d0e575.csv',
          '62ac8d659c88fde55ead0662.csv','62cc751291275617a9c7222f.csv','62e92d95cf6c8f424060db1a.csv',
          '62fb383ce16d6921d1c2c2b8.csv','62fc25ef4ce0d3d169b7a120.csv','565bdfcec121fe0012fc3897.csv',
          '604a30e30fa5eba805fc1b51.csv','631b6d4fe26a64d24c946fb1.csv','633b82ab54af035c569082fb.csv',
          '5608a73fd7def20012b7389d.csv','6009f6693bf880114f7bdc99.csv','6101d3dd8a5037f20dfc505f.csv',
          '6101f4093ed452ae3b6d5ab9.csv','6102c81e911700cf7ba5f6bd.csv','6108d6efa698e3dbe3b313d3.csv',
          '6138f7e0ad42e592ca5f2024.csv','6155b9c45f96867d9d9631fd.csv','6287a504c4cb277cf781b6bb.csv',
          '61043f36bc2fb31110d2067d.csv','61664d58d18ca2325a81008e.csv','610106becd177b1d8bee303c.csv',
          '6108295fdd0270d7544b5a8a.csv','6111846c736eac63d7930e09.csv','6328817c90a7f703ded34c91.csv',
          '61180000f554e49f07fd524e.csv','612597436eff2c3e15310f3f.csv','629513753a4424c933282660.csv',
          '6297567582d2ed2d88ae0450.csv','5f49f3262a3d07563d14a7f1.csv','5d74001d391b6600175f433b.csv',
          '550bb70bfdf99b6853dab45e.csv','62d5844a8fcb262f38f5b64c.csv','629f4800dfb8c7c86f69a67e.csv']
          

          

list_csv_file_Day2_Update=[]
omit_from_df_total_day=[]
for i in list_csv_file_Day2:
    if i in csv_list:
        list_csv_file_Day2_Update.append(i)
    if i not in csv_list:
        omit_from_df_total_day.append(i)


# I need to remove the the item in 'omit_from_df_total_day' from df_total fro  the first day

for i in omit_from_df_total_day:
    j=i[0:-4]
    print('i is: ',i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if j in df_total['prolificID'].tolist():
        print('hi')
        
        
        print('j is : ',j)
        index=df_total[df_total['prolificID']==j].index.values
        df_total.drop(index, inplace = True )



##################################################################################################################
############################################# Analysing the Second day ###########################################
##################################################################################################################



# Analysing Test Phase 
# List CSV Files to read each time one file and put it as df_test
# read each csv file for each participants sepratly

# address csv files foe day2
address='D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//'
####################################################################################################################
##################################################################################################################

column_list_payment_Day2=['prolificID', 'session', 
                          'RT_block_10','RT_block_11','RT_block_12',
                          'nun_seq_10','nun_seq_11','nun_seq_12',
                          'Response_Percentage_block_10','Response_Percentage_block_11','Response_Percentage_block_12',
                          'Response_distribution_block_10','Response_distribution_block_11','Response_distribution_block_12']

df_payment_Day2=pd.DataFrame(columns=column_list_payment_Day2)

#df = pd.read_csv(address+'629fec7ad26e41512fe15400.csv')

for i in range(len(list_csv_file_Day2_Update)):
    
    df = pd.read_csv(address+list_csv_file_Day2_Update[i])
    
    counts_1=df.iloc[0:48]['response'].isnull().astype(int).groupby(df.iloc[0:48]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_1=counts_1.max(axis=0) 
    
    counts_2=df.iloc[48:96]['response'].isnull().astype(int).groupby(df.iloc[48:96]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_2=counts_2.max(axis=0)
    
    counts_3=df.iloc[96:144]['response'].isnull().astype(int).groupby(df.iloc[96:144]['response'].notnull().astype(int).cumsum()).sum()
    nun_seq_3=counts_3.max(axis=0)
    
    dict_data={}
    dict_data={'prolificID': df['prolificID'][0], 'session': df['session'][0], 
               'nun_seq_10':nun_seq_1, 'nun_seq_11':nun_seq_2, 'nun_seq_12':nun_seq_3,
               
               'RT_block_10': df.iloc[0:48]['reaction_time'].mean(),
               'RT_block_11': df.iloc[48:96]['reaction_time'].mean(),
               'RT_block_12': df.iloc[96:144]['reaction_time'].mean(),
               
               'Response_Percentage_block_10': (df.iloc[0:48]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_11': (df.iloc[48:96]['response'].notnull().sum()/48)*100,
               'Response_Percentage_block_12': (df.iloc[96:144]['response'].notnull().sum()/48)*100,
               
               
               'Response_distribution_block_10': (df.iloc[0:48]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_11': (df.iloc[48:96]['response'].value_counts()['d']/48)*100,
               'Response_distribution_block_12': (df.iloc[96:144]['response'].value_counts()['d']/48)*100}
       
    df_payment_Day2 = df_payment_Day2.append(dict_data, ignore_index=True)
#saving df_total to csv
# change th addrress and name of the file

df_payment_Day2.to_csv(address+'df_payment_Context_Blocked_Day2.csv', index=False)



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
for i in range (len( df_payment_Day2)):
    #print(i)
    if (df_payment_Day2.iloc[i]['RT_block_10']<300 or
        df_payment_Day2.iloc[i]['RT_block_11']<300 or
        df_payment_Day2.iloc[i]['RT_block_12']<300 or
        
        df_payment_Day2.iloc[i]['nun_seq_10'] > 14 or
        df_payment_Day2.iloc[i]['nun_seq_11'] > 14 or
        df_payment_Day2.iloc[i]['nun_seq_12'] > 14 or
        
        df_payment_Day2.iloc[i]['Response_distribution_block_10']<10 or
        df_payment_Day2.iloc[i]['Response_distribution_block_11']<10 or
        df_payment_Day2.iloc[i]['Response_distribution_block_12']<10 ):
        
        omit=1;
        omit_subject_list.append(df_payment_Day2.iloc[i]['prolificID'])
        
    else:
        omit=0;


# Save omit_subject_list
import csv
with open(address+"omit_subject_list.csv", "w") as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(omit_subject_list)
    
# omiting partipant from list_csv_file_Day2_Update
for i in omit_subject_list:
    print(i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if i in df_total['prolificID'].tolist():
        #print('true')
        index=df_total[df_total['prolificID']==i].index.values
        df_total.drop(index, inplace = True )
         
    j=i+'.csv'
    result = list_csv_file_Day2_Update.index(j)
    #result=result+'.csv'
    print(result)
    print(list_csv_file_Day2_Update[result])
    list_csv_file_Day2_Update.pop(result)




##################################################################################################################
##################################################################################################################

#########################################################################################
################### Stimulus_rule accuracy and RT during trainin ########################
#########################################################################################



# Address day1:
Day_1_Address= address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'

# Use updated CSV list about which participants consider
# Csv fiel == list_csv_file_Day2_Update
rule_Stimulus=['SR_1_ACC', 'SR_2_ACC', 'SR_3_ACC', 'SR_4_ACC', 'SR_5_ACC', 'SR_6_ACC',
               'SR_7_ACC', 'SR_8_ACC', 'SR_9_ACC', 'SR_10_ACC', 'SR_11_ACC', 'SR_12_ACC',
               
               'SR_1_RT', 'SR_2_RT', 'SR_3_RT', 'SR_4_RT', 'SR_5_RT', 'SR_6_RT',
               'SR_7_RT', 'SR_8_RT', 'SR_9_RT', 'SR_10_RT', 'SR_11_RT', 'SR_12_RT',
               
               'SR_1_ACC_leg', 'SR_2_ACC_leg', 'SR_3_ACC_leg', 'SR_4_ACC_leg', 'SR_5_ACC_leg', 'SR_6_ACC_leg',
               'SR_7_ACC_leg', 'SR_8_ACC_leg', 'SR_9_ACC_leg', 'SR_10_ACC_leg', 'SR_11_ACC_leg', 'SR_12_ACC_leg',
               
               'SR_1_RT_leg', 'SR_2_RT_leg', 'SR_3_RT_leg', 'SR_4_RT_leg', 'SR_5_RT_leg', 'SR_6_RT_leg',
               'SR_7_RT_leg', 'SR_8_RT_leg', 'SR_9_RT_leg', 'SR_10_RT_leg', 'SR_11_RT_leg', 'SR_12_RT_leg',
               
               'SR_1_ACC_mouth', 'SR_2_ACC_mouth', 'SR_3_ACC_mouth', 'SR_4_ACC_mouth', 'SR_5_ACC_mouth', 'SR_6_ACC_mouth',
               'SR_7_ACC_mouth', 'SR_8_ACC_mouth', 'SR_9_ACC_mouth', 'SR_10_ACC_mouth', 'SR_11_ACC_mouth', 'SR_12_ACC_mouth',
               
               'SR_1_RT_mouth', 'SR_2_RT_mouth', 'SR_3_RT_mouth', 'SR_4_RT_mouth', 'SR_5_RT_mouth', 'SR_6_RT_mouth',
               'SR_7_RT_mouth', 'SR_8_RT_mouth', 'SR_9_RT_mouth', 'SR_10_RT_mouth', 'SR_11_RT_mouth', 'SR_12_RT_mouth',
               
               'SR_1_ACC_antenn', 'SR_2_ACC_antenn', 'SR_3_ACC_antenn', 'SR_4_ACC_antenn', 'SR_5_ACC_antenn', 'SR_6_ACC_antenn',
               'SR_7_ACC_antenn', 'SR_8_ACC_antenn', 'SR_9_ACC_antenn', 'SR_10_ACC_antenn', 'SR_11_ACC_antenn', 'SR_12_ACC_antenn',
               
               'SR_1_RT_antenn', 'SR_2_RT_antenn', 'SR_3_RT_antenn', 'SR_4_RT_antenn', 'SR_5_RT_antenn', 'SR_6_RT_antenn',
               'SR_7_RT_antenn', 'SR_8_RT_antenn', 'SR_9_RT_antenn', 'SR_10_RT_antenn', 'SR_11_RT_antenn', 'SR_12_RT_antenn']




CB_Stimulu_Response = pd.DataFrame(columns = rule_Stimulus)

for j in range(len(list_csv_file_Day2_Update)):
    
    df = pd.read_csv(Day_1_Address + list_csv_file_Day2_Update[j])
    df = df.fillna(0)
    
    #df_Stimulu_Response['prolificID']=df['prolificID'][0]
    insect_111_leg_acc=[]
    insect_111_leg_rt=[]
    
    insect_112_leg_acc=[]
    insect_112_leg_rt=[]
    
    insect_121_leg_acc=[]
    insect_121_leg_rt=[]
    
    insect_122_leg_acc=[]
    insect_122_leg_rt=[]
    
    insect_211_leg_acc=[]
    insect_211_leg_rt=[]
    
    insect_212_leg_acc=[]
    insect_212_leg_rt=[]
    
    insect_221_leg_acc=[]
    insect_221_leg_rt=[]
    
    insect_222_leg_acc=[]
    insect_222_leg_rt=[]
    
    insect_111_antenn_acc=[]
    insect_111_antenn_rt=[]
    
    insect_112_antenn_acc=[]
    insect_112_antenn_rt=[]
    
    insect_121_antenn_acc=[]
    insect_121_antenn_rt=[]
    
    insect_122_antenn_acc=[]
    insect_122_antenn_rt=[]
    
    insect_211_antenn_acc=[]
    insect_211_antenn_rt=[]
    
    insect_212_antenn_acc=[]
    insect_212_antenn_rt=[]
    
    insect_221_antenn_acc=[]
    insect_221_antenn_rt=[]
    
    insect_222_antenn_acc=[]
    insect_222_antenn_rt=[]
    
    insect_111_mouth_acc=[]
    insect_111_mouth_rt=[]
                         
    insect_112_mouth_acc=[]
    insect_112_mouth_rt=[]
                         
    insect_121_mouth_acc=[]
    insect_121_mouth_rt=[]
                         
    insect_122_mouth_acc=[]
    insect_122_mouth_rt=[]
                         
    insect_211_mouth_acc=[]
    insect_211_mouth_rt=[]
    
    insect_212_mouth_acc=[]
    insect_212_mouth_rt=[]
    
    insect_221_mouth_acc=[]
    insect_221_mouth_rt=[]
    
    insect_222_mouth_acc=[]
    insect_222_mouth_rt=[]


    for i in range(288):
    
        ######## insect 111 ########
        if ((df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            
            insect_111_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_111_antenn_rt.append(float(df.iloc[i]['reaction_time']))
                        
        elif ((df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
            
            insect_111_mouth_acc.append(float(df.iloc[i]['accuracy']))
            insect_111_mouth_rt.append(float(df.iloc[i]['reaction_time']))
                           
        elif ((df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
            
                
             insect_111_leg_acc.append(float(df.iloc[i]['accuracy']))
             insect_111_leg_rt.append(float(df.iloc[i]['reaction_time']))
              
 
        ######## insect 112 ########
        if ((df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            
                
            insect_112_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_112_antenn_rt.append(float(df.iloc[i]['reaction_time']))
            
            
        elif ((df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
            

              insect_112_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_112_mouth_rt.append(float(df.iloc[i]['reaction_time']))
              
              
        elif ((df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
            
                
              insect_112_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_112_leg_rt.append(float(df.iloc[i]['reaction_time']))
    
       ############ insect 121 ##########
        if ((df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            
                
            insect_121_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_121_antenn_rt.append(float(df.iloc[i]['reaction_time']))
            
            
        elif ((df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
            

              insect_121_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_121_mouth_rt.append(float(df.iloc[i]['reaction_time']))
              
              
        elif ((df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :

                
              insect_121_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_121_leg_rt.append(float(df.iloc[i]['reaction_time']))
              
        ############ insect 122 ##########
        if ((df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            

            insect_122_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_122_antenn_rt.append(float(df.iloc[i]['reaction_time']))
            

        elif ((df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
            
                
              insect_122_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_122_mouth_rt.append(float(df.iloc[i]['reaction_time']))
              
              
        elif ((df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
            
                
              insect_122_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_122_leg_rt.append(float(df.iloc[i]['reaction_time']))
              
        ########### insect 211 ###########
        if ((df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            

            insect_211_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_211_antenn_rt.append(float(df.iloc[i]['reaction_time']))
            

        elif ((df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
                
              insect_211_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_211_mouth_rt.append(float(df.iloc[i]['reaction_time']))
              
 
        elif ((df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
            
              insect_211_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_211_leg_rt.append(float(df.iloc[i]['reaction_time']))   
 
              
        ########### insect 212 ###########
        if ((df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :

            insect_212_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_212_antenn_rt.append(float(df.iloc[i]['reaction_time']))

            
        elif ((df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
            
                
              insect_212_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_212_mouth_rt.append(float(df.iloc[i]['reaction_time']))
              
  
        elif ((df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
            
                
              insect_212_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_212_leg_rt.append(float(df.iloc[i]['reaction_time']))
              
              
        ########### insect 221 ###########
        if ((df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :            
 
            insect_221_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_221_antenn_rt.append(float(df.iloc[i]['reaction_time']))
            
        elif ((df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
            
              insect_221_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_221_mouth_rt.append(float(df.iloc[i]['reaction_time']))
                            
        elif ((df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
            
              insect_221_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_221_leg_rt.append(float(df.iloc[i]['reaction_time']))
              
        ########### insect 222 ###########
        if ((df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :

            insect_222_antenn_acc.append(float(df.iloc[i]['accuracy']))
            insect_222_antenn_rt.append(float(df.iloc[i]['reaction_time']))
            
        elif ((df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
        
                
              insect_222_mouth_acc.append(float(df.iloc[i]['accuracy']))
              insect_222_mouth_rt.append(float(df.iloc[i]['reaction_time']))
              
              
        elif ((df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :

                
              insect_222_leg_acc.append(float(df.iloc[i]['accuracy']))
              insect_222_leg_rt.append(float(df.iloc[i]['reaction_time']))


    insect_leg_acc = np.array((insect_111_leg_acc, insect_112_leg_acc, insect_121_leg_acc,
                               insect_122_leg_acc, insect_211_leg_acc,insect_212_leg_acc,
                               insect_221_leg_acc, insect_222_leg_acc))
                              
    insect_leg_rt = np.array((insect_111_leg_rt, insect_112_leg_rt, insect_121_leg_rt,
                               insect_122_leg_rt, insect_211_leg_rt, insect_212_leg_rt,
                               insect_221_leg_rt, insect_222_leg_rt))
    
    
    insect_antenn_acc = np.array((insect_111_antenn_acc, insect_112_antenn_acc, insect_121_antenn_acc,
                                  insect_122_antenn_acc, insect_211_antenn_acc, insect_212_antenn_acc, 
                                  insect_221_antenn_acc, insect_222_antenn_acc))
    
    insect_antenn_rt = np.array((insect_111_antenn_rt, insect_112_antenn_rt, insect_121_antenn_rt,
                                 insect_122_antenn_rt, insect_211_antenn_rt, insect_212_antenn_rt, 
                                 insect_221_antenn_rt, insect_222_antenn_rt))
    
    
    insect_mouth_acc = np.array((insect_111_mouth_acc, insect_112_mouth_acc,insect_121_mouth_acc,
                                 insect_122_mouth_acc, insect_211_mouth_acc, insect_212_mouth_acc,
                                 insect_221_mouth_acc,insect_222_mouth_acc))
    
    insect_mouth_rt = np.array((insect_111_mouth_rt, insect_112_mouth_rt,insect_121_mouth_rt,
                                insect_122_mouth_rt, insect_211_mouth_rt, insect_212_mouth_rt,
                                insect_221_mouth_rt,insect_222_mouth_rt))
    
    insect_total_acc = np.array((insect_111_leg_acc, insect_112_leg_acc, insect_121_leg_acc,
                                insect_122_leg_acc, insect_211_leg_acc, insect_212_leg_acc,
                                insect_221_leg_acc, insect_222_leg_acc, insect_111_antenn_acc, 
                                insect_112_antenn_acc, insect_121_antenn_acc, insect_122_antenn_acc,
                                insect_211_antenn_acc, insect_212_antenn_acc, insect_221_antenn_acc,
                                insect_222_antenn_acc, insect_111_mouth_acc, insect_112_mouth_acc,
                                insect_121_mouth_acc, insect_122_mouth_acc, insect_211_mouth_acc,
                                insect_212_mouth_acc, insect_221_mouth_acc, insect_222_mouth_acc))
    
    insect_total_rt = np.array((insect_111_leg_rt, insect_112_leg_rt, insect_121_leg_rt,
                                insect_122_leg_rt, insect_211_leg_rt, insect_212_leg_rt,
                                insect_221_leg_rt, insect_222_leg_rt, insect_111_antenn_rt, 
                                insect_112_antenn_rt, insect_121_antenn_rt, insect_122_antenn_rt,
                                insect_211_antenn_rt, insect_212_antenn_rt, insect_221_antenn_rt,
                                insect_222_antenn_rt, insect_111_mouth_rt, insect_112_mouth_rt,
                                insect_121_mouth_rt, insect_122_mouth_rt, insect_211_mouth_rt,
                                insect_212_mouth_rt, insect_221_mouth_rt,insect_222_mouth_rt))
    
    acc_leg = np.mean(insect_leg_acc, axis = 0).reshape(1,12)
    acc_mouth = np.mean(insect_mouth_acc, axis = 0).reshape(1,12)
    acc_antenn = np.mean(insect_antenn_acc, axis = 0).reshape(1,12)
    
    rt_leg = np.mean(insect_leg_rt, axis = 0).reshape(1,12)
    rt_mouth = np.mean(insect_mouth_rt, axis = 0).reshape(1,12)
    rt_antenn = np.mean(insect_antenn_rt, axis = 0).reshape(1,12)
    
    acc_total = np.mean(insect_leg_acc, axis = 0).reshape(1,12)
    rt_total = np.mean(insect_antenn_rt, axis = 0).reshape(1,12)
    
    acc_total = np.append(acc_total,rt_total)
    acc_total = np.append(acc_total,acc_leg)
    acc_total = np.append(acc_total,rt_leg)
    acc_total = np.append(acc_total,acc_mouth)
    acc_total = np.append(acc_total,rt_mouth)
    acc_total = np.append(acc_total,acc_antenn)
    acc_total = np.append(acc_total,rt_antenn)
    acc_total = acc_total.reshape(1,96)
    CB_Stimulu_Response = CB_Stimulu_Response.append(pd.DataFrame(acc_total, columns = rule_Stimulus), ignore_index=True)
    

CB_Stimulu_Response['prolificID']=list_csv_file_Day2_Update
day_2_add='D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//'
CB_Stimulu_Response.to_csv(day_2_add+'df_SR_ContextBlocked.csv', index=False) 

######### Plotting stimulus_response seprately and toghether ############
import matplotlib.pyplot as plt 

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']


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


############################################################################
############################## Ploting ACC ################################
############################################################################
#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y_mouth_acc,'bo-')
plt.xticks(rotation=45)
plt.title("Stimulus_Blocked (Stimulus_Response Mouth ACC)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.ylim(0.3, 1)

for x,y in zip(x_axis,y_mouth_acc):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center
    #

plt.show() 


#####################################################################
############################## Ploting RT ###########################
#####################################################################


plt.clf()
plt.plot(x_axis,y_mouth_rt,'bo-')
plt.xticks(rotation=45)
plt.title("Stimulu_Blocked (Stimulus_Response RT Mouth Rule)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.ylim([700, 2000])
for x,y in zip(x_axis,y_mouth_rt):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=8,
                 ha='center') # horizontal alignment can be left, right or center

plt.show()




##########################################################################################
###########################################################################################
column_list_switch_cost = ['prolificID_Train', 'prolificID_Test', 'version_Train', 'version_Test', 
                            'ACC_Repeat_Block_7', 'ACC_Alter_Block_7', 'ACC_Repeat_Block_8', 'ACC_Alter_Block_8',
                            'ACC_Repeat_Block_9', 'ACC_Alter_Block_9', 'ACC_Repeat_Block_10', 'ACC_Alter_Block_10',
                            'ACC_Repeat_Block_11', 'ACC_Alter_Block_11', 'ACC_Repeat_Block_12', 'ACC_Alter_Block_12',
                            'RT_Repeat_Block_7', 'RT_Alter_Block_7', 'RT_Repeat_Block_8', 'RT_Alter_Block_8',
                            'RT_Repeat_Block_9', 'RT_Alter_Block_9', 'RT_Repeat_Block_10', 'RT_Alter_Block_10',
                            'RT_Repeat_Block_11', 'RT_Alter_Block_11', 'RT_Repeat_Block_12','RT_Alter_Block_12']

Day_1_Address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'
df_switch_cost = pd.DataFrame(columns=column_list_switch_cost)

for j in range (len(list_csv_file_Day2_Update)):
    
    # Train
    df_train = pd.read_csv(Day_1_Address+ list_csv_file_Day2_Update[j])
    switch_task_train=np.zeros(shape=(432,))
    for m in range (df_train.shape[0]):
        if m!=0:
            if df_train.iloc[m-1]['context_image']!= df_train.iloc[m]['context_image']:
                task_alteration_train=1
                switch_task_train[m]= task_alteration_train;
    
    
    # Test
    df_test = pd.read_csv(address+ list_csv_file_Day2_Update[j])
    version=df_total['version'].where(df_total['prolificID'] == df_test['prolificID'][0]) 
    version=version.dropna().tolist()
    version=version[0]
    print(version)
    df_test['version']=version
    list_acc=np.zeros(shape=(144,))
    switch_task=np.zeros(shape=(144,))                                   

    
### VERSION 1 ###
    if df_test['version'][0]==1:
        for i in range (df_test.shape[0]):
            

### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
        ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
 
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
        ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 2 ###
    if df_test['version'][0]==2:
        for i in range (df_test.shape[0]):
    
            ### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                    
            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                        

    ### VERSION 3 ###
    if df_test['version'][0]==3:
        for i in range (df_test.shape[0]):
            
            ### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )| 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
            ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                        
    ### VERSION 4 ###
    if df_test['version'][0]==4:
        for i in range (df_test.shape[0]):
    
            ### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                                
            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                          
### VERSION 5 ###
    if df_test['version'][0]==5:
        for i in range (df_test.shape[0]):
        
            ### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

                
            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
### VERSION 6 ###
    if df_test['version'][0]==6:
        for i in range (df_test.shape[0]):
    
            ### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                               
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

        
            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                        

            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
### VERSION 7 ###
    if df_test['version'][0]==7:
        for i in range (df_test.shape[0]):
    
            ### Planet 1 ###
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
            ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
            (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                
### VERSION 8 ###
    if df_test['version'][0]==8:
        for i in range (df_test.shape[0]):
    
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                        

                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )| 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
                                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_testiloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
### VERSION 9 ###
    if df_test['version'][0]==9:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                                        

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;

### Version 10 ######
    if df_test['version'][0]==10:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
                        
### VERSION 11 ###
    if df_test['version'][0]==11:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )| 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
        
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;

    
### VERSION 12 ###
    if df_test['version'][0]==12:
        for i in range (df_test.shape[0]):
        
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                                            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################  
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
            ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;


###############################################################################
###############################################################################
### VERSION 13 ###
    if df_test['version'][0]==13:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
    ### VERSION 14 ###
    if df_test['version'][0]==14:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
    
    ### VERSION 15 ###
    if df_test['version'][0]==15:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
### VERSION 16 ###
    if df_test['version'][0]==16:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
        
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
### VERSION 17 ###
    if df_test['version'][0]==17:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png' )&
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
    
### VERSION 18 ###
    if df_test['version'][0]==18:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
        
            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;

    ### VERSION 19 ###
    if df_test['version'][0]==19:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                
    ### VERSION 20 ###
    if df_test['version'][0]==20:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;

    ### VERSION 21 ###
    if df_test['version'][0]==21:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
    ### VERSION 22 ###
    if df_test['version'][0]==22:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 23 ###
    if df_test['version'][0]==23:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                
    ### VERSION 24 ###
    if df_test['version'][0]==24:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

                        
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
    ### VERSION 25 ###
    if df_test['version'][0]==25:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
    ### VERSION 26 ###
    if df_test['version'][0]==26:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
            ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

            
    ### VERSION 27 ###
    if df_test['version'][0]==27:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
            
    ### VERSION 28 ###
    if df_test['version'][0]==28:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
            
    ### VERSION 29 ###
    if df_test['version'][0]==29:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;

    ### VERSION 30 ###
    if df_test['version'][0]==30:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
        
    ### VERSION 31 ###
    if df_test['version'][0]==31:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
            
    ### VERSION 32 ###
    if df_test['version'][0]==32:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 33 ###
    if df_test['version'][0]==33:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
                    
    ### VERSION 34 ###
    if df_test['version'][0]==34:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 35 ###
    if df_test['version'][0]==35:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                (int((df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
            
    ### VERSION 36 ###
    if df_test['version'][0]==36:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png' )&
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
    ### VERSION 37 ###
    if df_test['version'][0]==37:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
    ### VERSION 38 ###
    if df_test['version'][0]==38:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 39 ###
    if df_test['version'][0]==39:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
    ### VERSION 40 ###
    if df_test['version'][0]==40:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
 
            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;

            
    ### VERSION 41 ###
    if df_test['version'][0]==41:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png' )&
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 42 ###
    if df_test['version'][0]==42:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    
    ### VERSION 43 ###
    if df_test['version'][0]==43:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
            ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
        
            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 44 ###
    if df_test['version'][0]==44:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

 
            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy


            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
    ### VERSION 45 ###
    if df_test['version'][0]==45:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
           
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
    ### VERSION 46 ###
    if df_test['version'][0]==46:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    


            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                (int((df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
        
    ### VERSION 47 ###
    if df_test['version'][0]==47:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
                    
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                


            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
                    

    ### VERSION 48 ###
    if df_test['version'][0]==48:
        for i in range (df_test.shape[0]):

            ################### Planet 1 ####################
            if (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet1.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 2########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet2.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    

            ####################Planet 3########################
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                if (df_test.iloc[i]['Press_Button']=="img/NO.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                    
            
            elif (int(df_test.iloc[i]['context_image']=='img/planet3.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                if(df_test.iloc[i]['Press_Button']=="img/YES.png"):
                    accuracy=1;
                    list_acc[i]=accuracy
                
            if i!=0:
                if df_test.iloc[i-1]['context_image']!= df_test.iloc[i]['context_image']:
                    task_alteration=1
                    switch_task[i]= task_alteration;
   
#########Here###########
    df_test['ACC']=list_acc
    df_train['switch_task']=switch_task_train
    df_test['switch_task']=switch_task
    dict_Switch_Cost={}
   
    dict_Switch_Cost={'prolificID_Train': df_train['prolificID'][0], 'prolificID_Test': df_test['prolificID'][0],
                      'version_Train': df_train['version'][0], 'version_Test': df_test['version'][0], 
                      
                      'ACC_Repeat_Block_7': (df_train.iloc[288:336]['accuracy'].where(df_train['switch_task']==0).sum()/df_train.iloc[288:336]['switch_task'].where(df_train['switch_task']==0).count())*100,
                      'ACC_Alter_Block_7': (df_train.iloc[288:336]['accuracy'].where(df_train['switch_task']==1).sum()/df_train.iloc[288:336]['switch_task'].where(df_train['switch_task']==1).count())*100,
                      
                      'ACC_Repeat_Block_8': (df_train.iloc[336:384]['accuracy'].where(df_train['switch_task']==0).sum()/df_train.iloc[336:384]['switch_task'].where(df_train['switch_task']==0).count())*100,
                      'ACC_Alter_Block_8': (df_train.iloc[336:384]['accuracy'].where(df_train['switch_task']==1).sum()/df_train.iloc[336:384]['switch_task'].where(df_train['switch_task']==1).count())*100,
                      
                      'ACC_Repeat_Block_9': (df_train.iloc[384:432]['accuracy'].where(df_train['switch_task']==0).sum()/df_train.iloc[384:432]['switch_task'].where(df_train['switch_task']==0).count())*100,
                      'ACC_Alter_Block_9': (df_train.iloc[384:432]['accuracy'].where(df_train['switch_task']==1).sum()/df_train.iloc[384:432]['switch_task'].where(df_train['switch_task']==1).count())*100,
                      
                      'ACC_Repeat_Block_10': (df_test.iloc[0:48]['ACC'].where(df_test['switch_task']==0).sum()/df_test.iloc[0:48]['switch_task'].where(df_test['switch_task']==0).count())*100,
                      'ACC_Alter_Block_10': (df_test.iloc[0:48]['ACC'].where(df_test['switch_task']==1).sum()/df_test.iloc[0:48]['switch_task'].where(df_test['switch_task']==1).count())*100,
                      
                      'ACC_Repeat_Block_11': (df_test.iloc[48:96]['ACC'].where(df_test['switch_task']==0).sum()/df_test.iloc[48:96]['switch_task'].where(df_test['switch_task']==0).count())*100,
                      'ACC_Alter_Block_11': (df_test.iloc[48:96]['ACC'].where(df_test['switch_task']==1).sum()/df_test.iloc[48:96]['switch_task'].where(df_test['switch_task']==1).count())*100,
                      
                      'ACC_Repeat_Block_12': (df_test.iloc[96:144]['ACC'].where(df_test['switch_task']==0).sum()/df_test.iloc[96:144]['switch_task'].where(df_test['switch_task']==0).count())*100,
                      'ACC_Alter_Block_12': (df_test.iloc[96:144]['ACC'].where(df_test['switch_task']==1).sum()/df_test.iloc[96:144]['switch_task'].where(df_test['switch_task']==1).count())*100,
                      
                      
                      'RT_Repeat_Block_7': df_train.iloc[288:336]['reaction_time'].where(df_train['switch_task']==0).mean(),
                      'RT_Alter_Block_7': df_train.iloc[288:336]['reaction_time'].where(df_train['switch_task']==1).mean(),
                      
                      'RT_Repeat_Block_8': df_train.iloc[336:384]['reaction_time'].where(df_train['switch_task']==0).mean(), 
                      'RT_Alter_Block_8': df_train.iloc[336:384]['reaction_time'].where(df_train['switch_task']==1).mean(),
                      
                      'RT_Repeat_Block_9': df_train.iloc[384:432]['reaction_time'].where(df_train['switch_task']==0).mean(),
                      'RT_Alter_Block_9': df_train.iloc[384:432]['reaction_time'].where(df_train['switch_task']==1).mean(),
                      
                      'RT_Repeat_Block_10': df_test.iloc[0:48]['reaction_time'].where(df_test['switch_task']==0).mean(),
                      'RT_Alter_Block_10': df_test.iloc[0:48]['reaction_time'].where(df_test['switch_task']==1).mean(),
                      
                      'RT_Repeat_Block_11': df_test.iloc[48:96]['reaction_time'].where(df_test['switch_task']==0).mean(), 
                      'RT_Alter_Block_11': df_test.iloc[48:96]['reaction_time'].where(df_test['switch_task']==1).mean(),
                      
                      'RT_Repeat_Block_12': df_test.iloc[96:144]['reaction_time'].where(df_test['switch_task']==0).mean(),
                      'RT_Alter_Block_12': df_test.iloc[96:144]['reaction_time'].where(df_test['switch_task']==1).mean()}
                      
                      

  
    
    df_switch_cost = df_switch_cost.append(dict_Switch_Cost, ignore_index=True)
    df_train.to_csv(address+'df_train_'+ str(j) +'_Context_Blocked_Day1.csv', index=False)
    df_test.to_csv(address+'df_'+ str(j) +'_Context_Blocked_Day2.csv', index=False)
##########################################################################################


list_csv_file_df_test=[]
    
for i in range (len(list_csv_file_Day2_Update)):
    list_csv_file_df_test.append('df_'+ str(i) +'_Context_Blocked_Day2.csv')
    

column_list=['prolificID', 'session', 'version', 
             'RT_block_10','RT_block_11','RT_block_12',
             'ACC_block_10', 'ACC_block_11','ACC_block_12']

df_total_test=pd.DataFrame(columns=column_list)

for i in range(len(list_csv_file_df_test)):
    df = pd.read_csv(address+list_csv_file_df_test[i])

    extra_payment=df_total['extra_payment'].where(df_total['prolificID'] == df['prolificID'][0]) 
    extra_payment=extra_payment.dropna().tolist()
    extra_payment=extra_payment[0]
    print(extra_payment)
    extra_payment_test=1*2*((df['ACC'].sum()/len(df['ACC']))-0.50)
    extra_payment_total=extra_payment+extra_payment_test
    df['extra_payment_total']=extra_payment_total

    dict_data_test={}
    dict_data_test={'prolificID': df['prolificID'][0], 'session': df['session'][0],
                    'version': df['version'][0], 'extra_payment_total': df['extra_payment_total'][0],
                    
                    'RT_block_10': df.iloc[0:48]['reaction_time'].mean(),
                    'RT_block_11': df.iloc[48:96]['reaction_time'].mean(),
                    'RT_block_12': df.iloc[96:144]['reaction_time'].mean(),
    
                    'ACC_block_10':df.iloc[0:48]['ACC'].sum()/48,
                    'ACC_block_11':df.iloc[48:96]['ACC'].sum()/48,
                    'ACC_block_12':df.iloc[96:144]['ACC'].sum()/48,
                    
                    'Sum_ACC_block_10':df.iloc[0:48]['ACC'].sum(),
                    'Sum_ACC_block_11':df.iloc[48:96]['ACC'].sum(),
                    'Sum_ACC_block_12':df.iloc[96:144]['ACC'].sum(),
                    
                    'Response_Percentage_block_10': (df.iloc[0:48]['response'].notnull().sum()/48)*100,
                    'Response_Percentage_block_11': (df.iloc[48:96]['response'].notnull().sum()/48)*100,
                    'Response_Percentage_block_12': (df.iloc[96:144]['response'].notnull().sum()/48)*100,}

    df_total_test = df_total_test.append(dict_data_test, ignore_index=True)


df_total_test.to_csv(address+'df_total_Context_Blocked_Day2.csv', index=False)


##################################################################################################
# now I want to replace 'extra_payment' collumn in df_total from the first day with 
# 'extra_payment_total' collumn in df_test from the second day




# I want to change the index of df_total and df-total_test to prolifc id to have the same index for 
# both datafram
index_list=[]
for i in range(df_total_test.shape[0]):
    index_list.append(i)
    
    
df_total['index']=index_list
df_total_test['index']=index_list
    
df_total_test=df_total_test.set_index('index')
df_total=df_total.set_index('index')




df_total['extra_payment']=df_total_test['extra_payment_total']

df_total['RT_block_10']=df_total_test['RT_block_10']
df_total['RT_block_11']=df_total_test['RT_block_11']
df_total['RT_block_12']=df_total_test['RT_block_12']

df_total['ACC_block_10']=df_total_test['ACC_block_10']
df_total['ACC_block_11']=df_total_test['ACC_block_11']
df_total['ACC_block_12']=df_total_test['ACC_block_12']

df_total['Sum_ACC_block_10']=df_total_test['Sum_ACC_block_10']
df_total['Sum_ACC_block_11']=df_total_test['Sum_ACC_block_11']
df_total['Sum_ACC_block_12']=df_total_test['Sum_ACC_block_12']

df_total['Response_Percentage_block_10']=df_total_test['Response_Percentage_block_10']
df_total['Response_Percentage_block_11']=df_total_test['Response_Percentage_block_11']
df_total['Response_Percentage_block_12']=df_total_test['Response_Percentage_block_12']



##############################################################################################
##################### df_total_required_payment
# saving df_total after removing sunbject based on the performance of the second day
# only subject in this new version of df_total will be paid
# the final amount of extra payment I need to pay them is the collumn of 'extra_payment' in this dataframe
df_total.to_csv(address+'df_Total_Context_Blocked_Two_Days_Required_Payment.csv', index=False)





#####################################################################################################
################################ Computing ACC criteria for data analyisis###########################
#####################################################################################################

# another way to use that function is to give it the proportion of success and the number of trials considered
# (it's basically the length of the array or the number of responses you take into account for a participant)
#pvalue = stats.binom_test(accuracy1.sum(), n = len(accuracy1), p=0.5, alternative='greater')
#print('accuracy 1: %.2f, pvalue 1= %.4f' % (accuracy1.mean(), pvalue))


# list csv file that pass the payment criteria. Now I want to check these participants performance 
# whether they can pass the ACC bionomial test criteria or not.

# I want to read df_total=
import pandas as pd

df_total = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_Required_Payment.csv')

from scipy import stats
csv_list_ACC = df_total['prolificID'].tolist()

# address the first day data to go and check csv file of 6 training session to for ACC

Address_Day1='D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_1//Data//'

# I have df_total that  pass criteria for payment.
# now I want to make another criteria on that df_total to see how much
# consider which participants for ACC analysis.
# only keep csv files from second day that pass criteria from the first day ACC during 
# 6 blocks of training

csv_list_ACC_update=[]
for i in csv_list_ACC:
    i=i+'.csv'
    csv_list_ACC_update.append(i)
    
omit_list_ACC_whole_train = []
omit_list_ACC_456_train = []

for i in range(len(csv_list_ACC_update)):
    
    df = pd.read_csv(Address_Day1+csv_list_ACC_update[i])
    
    ACC_Success=df.iloc[0:288]['accuracy'].sum() #288
    ACC_Success_456= df.iloc[144:288]['accuracy'].sum()
    
    #print('sum of correct response from 288 trial: ', ACC_Success)
    
    pvalue = stats.binom_test(ACC_Success, n = 287, p=0.5, alternative='greater')
    pvalue_456 = stats.binom_test(ACC_Success_456, n = 144, p=0.5, alternative='greater')
    
    #print('pvalue: ',pvalue)
    #print('-------------------\n')
    if pvalue > 0.05:
        print(csv_list_ACC_update[i])
        omit_list_ACC_whole_train.append(csv_list_ACC_update[i])
        
    if pvalue_456 > 0.05:
        print(csv_list_ACC_update[i])
        omit_list_ACC_456_train.append(csv_list_ACC_update[i])   
        

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
         
df_whole_train.to_csv(address+'df_Total_Context_Blocked_Two_Days_ACC_Critera_Whole_Train.csv', index=False)




# omit particpants with low
for i in omit_list_ACC_456_train:
    j=i[0:-4]
    #print(i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if j in df_456['prolificID'].tolist():
        #print('true')
        index=df_456[df_456['prolificID']==j].index.values
        df_456.drop(index, inplace = True )
        
    if j in df_switch_cost['prolificID_Train'].tolist():
        index_switch=df_switch_cost[df_switch_cost['prolificID_Train']==j].index.values
        df_switch_cost.drop(index_switch, inplace = True )
         
df_456.to_csv(address+'df_Total_Context_Blocked_Two_Days_ACC_Critera_456_Train.csv', index=False)
df_switch_cost.to_csv(address+'df_Switch_Cost_Context_Blocked.csv', index=False)


###########################################################################################
#################### Computing ACC Based on the task ######################################
###########################################################################################
mean_acc_task={'Task1_1':[], 'Task2_1':[], 'Task3_1':[],
               'Task1_2':[], 'Task2_2':[], 'Task3_2':[],
               'Task1_7':[], 'Task2_7':[], 'Task3_7':[],
               'Task1_8':[], 'Task2_8':[], 'Task3_8':[],
               'Task1_9':[], 'Task2_9':[], 'Task3_9':[]}

csv_list_Task = df_456['prolificID'].tolist()
for i in range(len(csv_list_Task)): #csv_list_Task
    
    df = pd.read_csv(Address_Day1+csv_list_ACC_update[i])
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
            

Address_Day2='D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//'
# Save CSV fiel to save the dictinary Open a csv file for writing
with open(Address_Day2+"DAY2_CB_Planet_mean_acc_tasks.csv", "w", newline="") as fp:
    # Create a writer object
    writer = csv.DictWriter(fp, fieldnames=mean_acc_task.keys())

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerow(mean_acc_task)
    print('Done writing dict to a csv file')
    


######################################################################################################
################################# Bionomial Test Based on all the block1 from 1 to 12 ###############
######################################################################################################
'''
omit_list_ACC_Whole_Experiment = []
for i in range(df_total.shape[0]):
    #print(i)
    ACC_Success_Whole_Experiment = df_total.iloc[i]['Sum_ACC_block_1']+ df_total.iloc[i]['Sum_ACC_block_2']+\
                                   df_total.iloc[i]['Sum_ACC_block_3']+ df_total.iloc[i]['Sum_ACC_block_4']+\
                                   df_total.iloc[i]['Sum_ACC_block_5']+ df_total.iloc[i]['Sum_ACC_block_6']+\
                                   df_total.iloc[i]['Sum_ACC_block_7']+ df_total.iloc[i]['Sum_ACC_block_8']+\
                                   df_total.iloc[i]['Sum_ACC_block_9']+ df_total.iloc[i]['Sum_ACC_block_10']+\
                                   df_total.iloc[i]['Sum_ACC_block_11']+ df_total.iloc[i]['Sum_ACC_block_12']
    
    pvalue_Whole_Experiment = stats.binom_test(ACC_Success_Whole_Experiment, n = 575, p=0.5, alternative='greater')
    
    
    #print('pvalue: ',pvalue)
    #print('-------------------\n')
    if pvalue_Whole_Experiment > 0.05:
        print(csv_list_ACC_update[i])
        omit_list_ACC_Whole_Experiment.append(csv_list_ACC_update[i])
        
        
import copy

df_Whole_Experiment=copy.deepcopy(df_total)

# omit particpants with low
for i in omit_list_ACC_Whole_Experiment:
    j=i[0:-4]
    #print(i)
    
    ############################ Here I need to remove omit_list from df_total from Day1###########################
    if j in df_Whole_Experiment['prolificID'].tolist():
        #print('true')
        index=df_Whole_Experiment[df_Whole_Experiment['prolificID']==j].index.values
        df_Whole_Experiment.drop(index, inplace = True )
         
df_Whole_Experiment.to_csv(address+'df_Total_Context_Blocked_Two_Days_ACC_Critera_Whole_Experiment.csv', index=False)
'''



################################################################################################################
################################# Find Outlier based on z score 3std above and below mean########################
####################################################################################################
import numpy as np
from scipy import stats

#making a df_outlier to moit all rows if they have outlier value even in one collumn:
df_outlier_copy=copy.deepcopy(df_whole_train)

# now I want to drop irrelevant collumn and only keep relevant collumns:

df_outlier= df_outlier_copy[['ACC_block_1','ACC_block_2','ACC_block_3','ACC_block_4','ACC_block_5','ACC_block_6',
                              'ACC_block_7','ACC_block_8','ACC_block_9','ACC_block_10','ACC_block_11','ACC_block_12']]
### inplace
df_outlier=df_outlier[(np.abs(stats.zscore(df_outlier)) < 3).all(axis=1)]
df_outlier.to_csv(address+'df_Total_Context_Blocked_Two_Days_without_outlier.csv', index=False)

################################################################################################################
###################################### Computing mean ACC of [1,2,3] ,[4,5,6], [7,8,9], [10,11,12] #############
################################################################################################################
from statistics import mean
from statistics import stdev
# use df_whole_train dataframe that consider whole training block for ACC criteria to compute this
Mean_Acc_Blocks_Whole={'ACC(B1B2B3)':round(mean([df_whole_train['ACC_block_1'].mean(),df_whole_train['ACC_block_2'].mean(),df_whole_train['ACC_block_3'].mean()]),3),
                       'ACC(B4B5B6)':round(mean([df_whole_train['ACC_block_4'].mean(),df_whole_train['ACC_block_5'].mean(),df_whole_train['ACC_block_6'].mean()]),3),
                       'ACC(B7B8B9)':round(mean([df_whole_train['ACC_block_7'].mean(),df_whole_train['ACC_block_8'].mean(),df_whole_train['ACC_block_9'].mean()]),3),
                       'ACC(B10B11B12)':round(mean([df_whole_train['ACC_block_10'].mean(),df_whole_train['ACC_block_11'].mean(),df_whole_train['ACC_block_12'].mean()]),3)}

Median_Acc_Blocks_Whole={'ACC(B1B2B3)':round(mean([df_whole_train['ACC_block_1'].median(),df_whole_train['ACC_block_2'].median(),df_whole_train['ACC_block_3'].median()]),3),
                         'ACC(B4B5B6)':round(mean([df_whole_train['ACC_block_4'].median(),df_whole_train['ACC_block_5'].median(),df_whole_train['ACC_block_6'].median()]),3),
                         'ACC(B7B8B9)':round(mean([df_whole_train['ACC_block_7'].median(),df_whole_train['ACC_block_8'].median(),df_whole_train['ACC_block_9'].median()]),3),
                         'ACC(B10B11B12)':round(mean([df_whole_train['ACC_block_10'].median(),df_whole_train['ACC_block_11'].median(),df_whole_train['ACC_block_12'].median()]),3)}

# use df_456 dataframe that consider whole 456s block for ACC criteria to compute this
Mean_Acc_Blocks_456={'ACC(B1B2B3)':round(mean([df_456['ACC_block_1'].mean(),df_456['ACC_block_2'].mean(),df_456['ACC_block_3'].mean()]),3),
                     'ACC(B4B5B6)':round(mean([df_456['ACC_block_4'].mean(),df_456['ACC_block_5'].mean(),df_456['ACC_block_6'].mean()]),3),
                     'ACC(B7B8B9)':round(mean([df_456['ACC_block_7'].mean(),df_456['ACC_block_8'].mean(),df_456['ACC_block_9'].mean()]),3),
                     'ACC(B10B11B12)':round(mean([df_456['ACC_block_10'].mean(),df_456['ACC_block_11'].mean(),df_456['ACC_block_12'].mean()]),3)}

Mean_Acc_Blocks_456_std={'ACC(B1B2B3)':round(stdev([df_456['ACC_block_1'].mean(),df_456['ACC_block_2'].mean(),df_456['ACC_block_3'].mean()]),3),
                         'ACC(B4B5B6)':round(stdev([df_456['ACC_block_4'].mean(),df_456['ACC_block_5'].mean(),df_456['ACC_block_6'].mean()]),3),
                         'ACC(B7B8B9)':round(stdev([df_456['ACC_block_7'].mean(),df_456['ACC_block_8'].mean(),df_456['ACC_block_9'].mean()]),3),
                         'ACC(B10B11B12)':round(stdev([df_456['ACC_block_10'].mean(),df_456['ACC_block_11'].mean(),df_456['ACC_block_12'].mean()]),3)}


# use df_outlier dataframe that consider whole train block for ACC criteria to compute this
Mean_Acc_Blocks_Outlier={'ACC(B1B2B3)':round(mean([df_outlier['ACC_block_1'].mean(),df_outlier['ACC_block_2'].mean(),df_outlier['ACC_block_3'].mean()]),3),
                         'ACC(B4B5B6)':round(mean([df_outlier['ACC_block_4'].mean(),df_outlier['ACC_block_5'].mean(),df_outlier['ACC_block_6'].mean()]),3),
                         'ACC(B7B8B9)':round(mean([df_outlier['ACC_block_7'].mean(),df_outlier['ACC_block_8'].mean(),df_outlier['ACC_block_9'].mean()]),3),
                         'ACC(B10B11B12)':round(mean([df_outlier['ACC_block_10'].mean(),df_outlier['ACC_block_11'].mean(),df_outlier['ACC_block_12'].mean()]),3)}


# use df_whole_train dataframe that consider whole training block for ACC criteria to compute this
Mean_RT_Blocks_Whole={'RT(B1B2B3)':round(mean([df_whole_train['RT_block_1'].mean(),df_whole_train['RT_block_2'].mean(),df_whole_train['RT_block_3'].mean()]),3),
                      'RT(B4B5B6)':round(mean([df_whole_train['RT_block_4'].mean(),df_whole_train['RT_block_5'].mean(),df_whole_train['RT_block_6'].mean()]),3),
                      'RT(B7B8B9)':round(mean([df_whole_train['RT_block_7'].mean(),df_whole_train['RT_block_8'].mean(),df_whole_train['RT_block_9'].mean()]),3),
                      'RT(B10B11B12)':round(mean([df_whole_train['RT_block_10'].mean(),df_whole_train['RT_block_11'].mean(),df_whole_train['RT_block_12'].mean()]),3)}


# use df_456 dataframe that consider whole 456s block for ACC criteria to compute this
Mean_RT_Blocks_456={'RT(B1B2B3)':round(mean([df_456['RT_block_1'].mean(),df_456['RT_block_2'].mean(),df_456['RT_block_3'].mean()]),3),
                    'RT(B4B5B6)':round(mean([df_456['RT_block_4'].mean(),df_456['RT_block_5'].mean(),df_456['RT_block_6'].mean()]),3),
                    'RT(B7B8B9)':round(mean([df_456['RT_block_7'].mean(),df_456['RT_block_8'].mean(),df_456['RT_block_9'].mean()]),3),
                    'RT(B10B11B12)':round(mean([df_456['RT_block_10'].mean(),df_456['RT_block_11'].mean(),df_456['RT_block_12'].mean()]),3)}

Mean_RT_Blocks_456_std={'RT(B1B2B3)':round(stdev([df_456['RT_block_1'].mean(),df_456['RT_block_2'].mean(),df_456['RT_block_3'].mean()]),3),
                        'RT(B4B5B6)':round(stdev([df_456['RT_block_4'].mean(),df_456['RT_block_5'].mean(),df_456['RT_block_6'].mean()]),3),
                        'RT(B7B8B9)':round(stdev([df_456['RT_block_7'].mean(),df_456['RT_block_8'].mean(),df_456['RT_block_9'].mean()]),3),
                        'RT(B10B11B12)':round(stdev([df_456['RT_block_10'].mean(),df_456['RT_block_11'].mean(),df_456['RT_block_12'].mean()]),3)}

# use df_outlier dataframe that consider whole train block for ACC criteria to compute this
'''
Mean_RT_Blocks_Outlier={'RT(B1B2B3)':round(mean([df_outlier['RT_block_1'].mean(),df_outlier['RT_block_2'].mean(),df_outlier['RT_block_3'].mean()]),3),
                        'RT(B4B5B6)':round(mean([df_outlier['RT_block_4'].mean(),df_outlier['RT_block_5'].mean(),df_outlier['RT_block_6'].mean()]),3),
                        'RT(B7B8B9)':round(mean([df_outlier['RT_block_7'].mean(),df_outlier['RT_block_8'].mean(),df_outlier['RT_block_9'].mean()]),3),
                        'RT(B10B11B12)':round(mean([df_outlier['RT_block_10'].mean(),df_outlier['RT_block_11'].mean(),df_outlier['RT_block_12'].mean()]),3)}

'''


df_bar= pd.DataFrame(Mean_Acc_Blocks_Whole.values(),columns =['ACC_Whole'],index=['B1B2B3','B4B5B6','B7B8B9','B10B11B12'])
df_bar['ACC_456']=Mean_Acc_Blocks_456.values()
df_bar['ACC_outlier']= Mean_Acc_Blocks_Outlier.values()
df_bar['Median_Acc_Blocks_Whole']=Median_Acc_Blocks_Whole.values()
df_bar['RT_Whole']= Mean_RT_Blocks_Whole.values()
df_bar['RT_456']= Mean_RT_Blocks_456.values()
#df_bar['RT_outlier']=Mean_RT_Blocks_Outlier.values()

df_bar.to_csv(address+'df_bar_Context_Blocked.csv', index=False)

########################################################################################################################
##################################################### Ploting ##########################################################
########################################################################################################################






##################################################################################################################
################################################ BAR Plots #######################################################
##################################################################################################################

#################################################################################################################
#################################### Bar plot ACC whole trainig criteria ########################################
#################################################################################################################
import matplotlib.pyplot as plt
#plt.figure(figsize=(6, 6))

# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha='center')
        
#plt.style.use('seaborn')
plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style
 

y_whole = list(Mean_Acc_Blocks_Whole.values())
plt.bar(x_axis_bar, y_whole, color='green')
#plt.xticks(rotation='vertical')

plt.title("Context_Blocked (ACC Criteria Whole Training)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.xticks(rotation=45)
plt.ylim(0.5, 1)
# calling the function to add value labels
addlabels(x_axis_bar, y_whole)
plt.show()


#################################################################################################################
#################################### Bar plot ACC 456 training blocks criteria ##################################
#################################################################################################################

x_axis_bar = ['Block\n1,2,3', 'Block\n4,5,6', 'Test1\n(Block6,7,8)', 'Test2\n(Block9,10,11)'] 

y_456=list(Mean_Acc_Blocks_456.values())
y_456_error=list(Mean_Acc_Blocks_456_std.values())

plt.bar(x_axis_bar, y_456,  yerr=y_456_error, align='center', alpha=0.5, ecolor='black', capsize=5, color='green')

plt.title("Context_Blocked Planet",fontsize=20)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.xticks(rotation=45)
plt.ylim(0.5, 1)
# calling the function to add value labels
addlabels(x_axis_bar,y_456)
plt.show()

#################################################################################################################
#################################### Bar plot RT 456 training blocks criteria ##################################
#################################################################################################################

x_axis_bar = ['Block\n1,2,3', 'Block\n4,5,6', 'Test1\n(Block6,7,8)', 'Test2\n(Block9,10,11)'] 

y_456_RT=list(Mean_RT_Blocks_456.values())
y_456_RT_error=list(Mean_RT_Blocks_456_std.values())

plt.bar(x_axis_bar, y_456_RT,  yerr=y_456_RT_error, align='center', alpha=0.5, ecolor='black', capsize=5, color='green')

plt.title("Mean RT Context_Blocked Planet",fontsize=20)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.xticks(rotation=45)
plt.ylim(0, 2000)
# calling the function to add value labels
addlabels(x_axis_bar,y_456_RT)
plt.show()

#################################################################################################################
#################################### Bar plot with omitiing outlier based on ACC criteria whole trianing blocks ##
#################################################################################################################

y_outlier=list(Mean_Acc_Blocks_Outlier.values())
plt.bar(x_axis_bar, y_outlier, color='green')
#plt.xticks(rotation='vertical')

plt.title("Context_Blocked (without outlier)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.xticks(rotation=45)
plt.ylim(0.5, 1)
# calling the function to add value labels
addlabels(x_axis_bar, y_outlier)
plt.show()

#################################################################################################################
#################################### Bar plot with Median  ##
#################################################################################################################

y_median = list(Median_Acc_Blocks_Whole.values())

plt.bar(x_axis_bar, y_median, color='green')
plt.title("Context_Blocked (Median)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Median ACC')
plt.xticks(rotation=45)
plt.ylim(0.5, 1)
# calling the function to add value labels
addlabels(x_axis_bar, y_median)
plt.show()

##############################################################################################################################
##########################################  Mean ACC  Criteria for Whole train ############################################
##############################################################################################################################
#try to plot them with subplot
import matplotlib.pyplot as plt 

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', 
        '7', '8', '9', '10', '11', '12']
#plt.figure(figsize=(6, 3))


y1= [df_whole_train['ACC_block_1'].mean(),df_whole_train['ACC_block_2'].mean(),df_whole_train['ACC_block_3'].mean(), 
     df_whole_train['ACC_block_4'].mean(),df_whole_train['ACC_block_5'].mean(),df_whole_train['ACC_block_6'].mean(),
     df_whole_train['ACC_block_7'].mean(),df_whole_train['ACC_block_8'].mean(),df_whole_train['ACC_block_9'].mean(),
     df_whole_train['ACC_block_10'].mean(),df_whole_train['ACC_block_11'].mean(),df_whole_train['ACC_block_12'].mean()]

#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y1,'bo-')
plt.xticks(rotation=45)
plt.title("Context_Block (ACC Criteria Whole Training)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.ylim(0.5, 1)

for x,y in zip(x_axis,y1):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center
    #

plt.show()

##############################################################################################################################
####################################################### Mean ACC  Criteria for 456 train ############################################
##############################################################################################################################
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import csv

df_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_ACC_Critera_456_Train.csv')

x_axis=['1', '2', '3', '4', '5','6', 
        '7', '8', '9', '10', '11', '12']
y2= [df_456['ACC_block_1'].mean(),df_456['ACC_block_2'].mean(),df_456['ACC_block_3'].mean(), 
     df_456['ACC_block_4'].mean(),df_456['ACC_block_5'].mean(),df_456['ACC_block_6'].mean(),
     df_456['ACC_block_7'].mean(),df_456['ACC_block_8'].mean(),df_456['ACC_block_9'].mean(),
     df_456['ACC_block_10'].mean(),df_456['ACC_block_11'].mean(),df_456['ACC_block_12'].mean()]


plt.clf()
plt.plot(x_axis,y2,'bo-')
plt.xticks(rotation=45)
plt.title("Mean ACC Context_Blocked Planet",fontsize=20)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.ylim(0.5, 1)

for x,y in zip(x_axis,y2):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center
    #

plt.show()



######################################################################################################################
############################################### Mean ACC Based on df_outlier#############################################
######################################################################################################################

y3= [df_outlier['ACC_block_1'].mean(),df_outlier['ACC_block_2'].mean(),df_outlier['ACC_block_3'].mean(), 
     df_outlier['ACC_block_4'].mean(),df_outlier['ACC_block_5'].mean(),df_outlier['ACC_block_6'].mean(),
     df_outlier['ACC_block_7'].mean(),df_outlier['ACC_block_8'].mean(),df_outlier['ACC_block_9'].mean(),
     df_outlier['ACC_block_10'].mean(),df_outlier['ACC_block_11'].mean(),df_outlier['ACC_block_12'].mean()]


plt.clf()
plt.plot(x_axis,y3,'bo-')
plt.xticks(rotation=45)
plt.title("Context_Block (Without Outlier)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.ylim(0.5, 1)

for x,y in zip(x_axis,y3):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center
    #

plt.show()

######################################################################################################################
############################################### Median ACC #############################################
######################################################################################################################
y10= [df_whole_train['ACC_block_1'].median(),df_whole_train['ACC_block_2'].median(),df_whole_train['ACC_block_3'].median(), 
     df_whole_train['ACC_block_4'].median(),df_whole_train['ACC_block_5'].median(),df_whole_train['ACC_block_6'].median(),
     df_whole_train['ACC_block_7'].median(),df_whole_train['ACC_block_8'].median(),df_whole_train['ACC_block_9'].median(),
     df_whole_train['ACC_block_10'].median(),df_whole_train['ACC_block_11'].median(),df_whole_train['ACC_block_12'].median()]



plt.clf()
plt.plot(x_axis,y10,'bo-')
plt.xticks(rotation=45)
plt.title("Context_Block (Median)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Median ACC')
plt.ylim(0.5, 1)

for x,y in zip(x_axis,y10):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center
    #

plt.show()
############################################################################################################################
################################################### Mean RT Whole Training Criteria ############################################################
###########################################################################################################################


y4= [df_whole_train['RT_block_1'].mean(), df_whole_train['RT_block_2'].mean(), df_whole_train['RT_block_3'].mean(), 
     df_whole_train['RT_block_4'].mean(),df_whole_train['RT_block_5'].mean(), df_whole_train['RT_block_6'].mean(), 
     df_whole_train['RT_block_7'].mean(), df_whole_train['RT_block_8'].mean(),df_whole_train['RT_block_9'].mean(),
     df_whole_train['RT_block_10'].mean(), df_whole_train['RT_block_11'].mean(),df_whole_train['RT_block_12'].mean()]

#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y4,'bo-')
plt.xticks(rotation=45)
plt.title("Context_Block (Whole)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.ylim([700, 2000])
for x,y in zip(x_axis,y4):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=8,
                 ha='center') # horizontal alignment can be left, right or center

plt.show()




############################################################################################################################
################################################### Mean RT 4-5-6 Training Criteria ############################################################
###########################################################################################################################


y5= [df_456['RT_block_1'].mean(),df_456['RT_block_2'].mean(), df_456['RT_block_3'].mean(), 
     df_456['RT_block_4'].mean(),df_456['RT_block_5'].mean(), df_456['RT_block_6'].mean(), 
     df_456['RT_block_7'].mean(),df_456['RT_block_8'].mean(), df_456['RT_block_9'].mean(),
     df_456['RT_block_10'].mean(),df_456['RT_block_11'].mean(), df_456['RT_block_12'].mean()]

#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y5,'bo-')
plt.xticks(rotation=45)
plt.title("Mean RT Context_Blocked Planet",fontsize=20)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.ylim([700, 2000])
for x,y in zip(x_axis,y5):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center

plt.show()

##################################################################################################################

#######################################################################
#################### Scatter plot RT vs ACC for each block ##########
#####################################################################
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df_whole_train = pd.read_csv("D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_ACC_Critera_Whole_Train.csv")
df_456= pd.read_csv("D://OneDrive - UGent//Desktop//Mina//Prolific//1.Context_Blocked_Two_Days//Day_2//Data//df_Total_Context_Blocked_Two_Days_ACC_Critera_456_Train.csv")


# df_whole
sns.jointplot(x = "ACC_block_1", y = "RT_block_1",kind = "scatter", data = df_whole_train, xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_2", y = "RT_block_2",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_3", y = "RT_block_3",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_4", y = "RT_block_4",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_5", y = "RT_block_5",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_6", y = "RT_block_6",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_7", y = "RT_block_7",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_8", y = "RT_block_8",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_9", y = "RT_block_9",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_10", y = "RT_block_10",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_11", y = "RT_block_11",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_12", y = "RT_block_12",kind = "scatter", data = df_whole_train,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('Whole Training Criteria', y=1.3, fontsize = 16)


# df_456
sns.jointplot(x = "ACC_block_1", y = "RT_block_1",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_2", y = "RT_block_2",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_3", y = "RT_block_3",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_4", y = "RT_block_4",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_5", y = "RT_block_5",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_6", y = "RT_block_6",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_7", y = "RT_block_7",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_8", y = "RT_block_8",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_9", y = "RT_block_9",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_10", y = "RT_block_10",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_11", y = "RT_block_11",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16)

sns.jointplot(x = "ACC_block_12", y = "RT_block_12",kind = "scatter", data = df_456,xlim = (0.1 ,1), ylim = (1000, 5000))
plt.title('4_5_6 Training Criteria', y=1.3, fontsize = 16) 
    
    
    
    
    
##################################################################################
##################################################################################
# I want to download the df_acc 456 here and extract the mean-acc for each task
df_456=
