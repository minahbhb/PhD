import pandas as pd
import numpy as np
import csv
#################################################################################################################
############################### Load data frame total from the day1 #############################################
#################################################################################################################

# df_total from Day1
df_total = pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day1//Data//df_total_Stimulus_Interleavd_Day1.csv')

# only keep csv files from second day that pass criteria from the first day
# some participants did not pass the criteria from the first day so even though they particiapte in
# the second day test I wont consider them for data analysis and payment
list_csv_file=df_total['prolificID'].tolist()
list_csv_file_Day2=[]
for i in list_csv_file:
    i=i+'.csv'
    list_csv_file_Day2.append(i)
    
    
    
# list csv files in stimulus_Oriented_Interleaved Day2 (appear for the test day2)
csv_list=['5a2dc611390d120001c70ac2.csv','5adef850eb60400001539109.csv','5b905d47e057280001e4af42.csv',
          '5b883986f249560001686872.csv','5b6194251f52240001679001.csv','5bad8fc39c0cc900017a6a28.csv',
          '5bd3454113e7dd0001f21591.csv','5c01d3c509e9c70001500b10.csv','5c85d80dfff8430016e9a418.csv',
          '5cb63178d946580001e4cef4.cvs','5d5af833f35ed70001e17a5c.cvs','5d305152b2cfe00019231a2a.csv',
          '5da6139c002c29001335b5a2.csv','5dc592c6aa431440aa755d5b.csv','5e7aca7dc679490b709c855c.csv',
          '5e65c5b41e30883349a25a61.csv','5e83da30261259130885eebc.csv','5f60d14a4b540f04a9473cb7.csv',
          '5fbd18be2b7651043385b705.csv','5fd9227fbeeb773aa4d6c986.csv','57d02ffb596f5d0001df741f.csv',
          '59c9c8da5535800001a8e434.csv','60b1a6ceb8ed805efaa99650.csv','60d3f9b634e76f8f4b911ad6.csv',
          '60e7a42ebc5356742b8dbf61.csv','60fd640fec893eee4eb8c3a7.csv','62adc4f5fb6abc773729c033.csv',
          '62b20575b356fba8715fae82.csv','62e07b7bce4301b22b769df8.csv','62f7405b197fadddd2b0dd60.csv',
          '62fe409e685f082dce525454.csv','602a8f9033061909d48b1d04.csv','603ecd847a63f50124aa5822.csv',
          '615d051e2366aeb051acb734.csv','631ab96a9f27876b9e4fe4c0.csv','631f36f4a3e9bd18066a7b33.csv',
          '6016be23044b1586fb0fc3fc.csv','6110a371c00388d587922ff1.csv','6159f8134884e2d32f738e4e.csv',
          '6321da5de806efad3e53163f.csv','6336cc276aa0d8c7ca48c95d.csv','58752fed445a5f00019b4a3f.csv',
          '60124cb4154c54274faac7c0.csv','61117cb162ca624c2b2a443c.csv','61292a3404d387db5b0b2a32.csv',
          '610049f981983d371de57fbf.csv','6111234ac8cfa49e38acbfb4.csv','612274842d4805447451f87b.csv',
          '6101667971d68405d105698a.csv','6286588610e848e43598e9d0.csv','5e65061173afb2277765b53b.csv',
          '5ccc60abe787e000167f8143.csv','6307bd3bb93e804d22332b3e.csv','62c41fe598ab94de4d4f021e.csv',
          '6282571cf39cd89341a474e9.csv','62dfdd3c61b792d28de9d0e3.csv','62bd685ac3edc9ad0d77812b.csv',
          '5a70d87e9cdd180001776440.csv','5b32599cc8e94a00018f22a5.csv','5b9fa85b4bca610001d791f3.csv',
          '5e937e8e4d246b6b4162ae72.csv','5ad0f1934d061300011b0a4d.csv','60255901704fd208ecdcf32b.csv',
          '627935c4e5d7e70b502e206e.csv','601d69a993d94008fb2b25dc.csv','5f49f3262a3d07563d14a7f1.csv',
          '6168b61ad8c0d63b37a92109.csv','6029b0e17f3b5d944ab183f1.csv','5baa535fa3c9170001156197.csv',
          '63069f585b35a5ec752fcd30.csv','5ee5e3b02eebe932ee9559c5.csv','59d8ae913e5ea00001e1d05f.csv']


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
address='D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//'
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

df_payment_Day2.to_csv(address+'df_payment_Stimulus_Interleaved_Day2.csv', index=False)


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

###############################################################################################
######################### Stimulus Response ###################################################
##############################################################################################

# Address day1:
Day_1_Address= address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day1//Data//'

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




SI_Stimulu_Response = pd.DataFrame(columns = rule_Stimulus)

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
    SI_Stimulu_Response = SI_Stimulu_Response.append(pd.DataFrame(acc_total, columns = rule_Stimulus), ignore_index=True)
    

SI_Stimulu_Response['prolificID']=list_csv_file_Day2_Update
day_2_add='D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//'
SI_Stimulu_Response.to_csv(day_2_add+'df_SR_StimulusInterleaved.csv', index=False) 

######### Plotting stimulus_response seprately and toghether ############
import matplotlib.pyplot as plt 

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']


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


############################################################################
############################## Ploting ACC ################################
############################################################################
#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis, SI_y_mouth_acc,'bo-')
plt.xticks(rotation=45)
plt.title("Stimulus_Interleaved (Stimulus_Response ACC Mouth Rule)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.ylim(0.3, 1)

for x,y in zip(x_axis, SI_y_mouth_acc):

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
plt.plot(x_axis, SI_y_mouth_rt,'bo-')
plt.xticks(rotation=45)
plt.title("Stimulus_Interleaved (Stimulus_Response RT Mouth Rule)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean RT')
plt.ylim([700, 2000])
for x,y in zip(x_axis, SI_y_mouth_rt):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=8,
                 ha='center') # horizontal alignment can be left, right or center

plt.show()


##################################################################################################################
##################################################################################################################
task_1=['img/ok.png','img/pois.png']
task_2=['img/cold.png','img/warm.png']
task_3=['img/rural.png','img/urban.png']

column_list_switch_cost = ['prolificID_Train', 'prolificID_Test', 'version_Train', 'version_Test', 
                            'ACC_Repeat_Block_7', 'ACC_Alter_Block_7', 'ACC_Repeat_Block_8', 'ACC_Alter_Block_8',
                            'ACC_Repeat_Block_9', 'ACC_Alter_Block_9', 'ACC_Repeat_Block_10', 'ACC_Alter_Block_10',
                            'ACC_Repeat_Block_11', 'ACC_Alter_Block_11', 'ACC_Repeat_Block_12', 'ACC_Alter_Block_12',
                            'RT_Repeat_Block_7', 'RT_Alter_Block_7', 'RT_Repeat_Block_8', 'RT_Alter_Block_8',
                            'RT_Repeat_Block_9', 'RT_Alter_Block_9', 'RT_Repeat_Block_10', 'RT_Alter_Block_10',
                            'RT_Repeat_Block_11', 'RT_Alter_Block_11', 'RT_Repeat_Block_12','RT_Alter_Block_12']

Day_1_Address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day1//Data//'
df_switch_cost = pd.DataFrame(columns=column_list_switch_cost)

for j in range (len(list_csv_file_Day2_Update)):
    
    # Train
    df_train = pd.read_csv(Day_1_Address+ list_csv_file_Day2_Update[j])
    switch_task_train=np.zeros(shape=(432,))
    for m in range (df_train.shape[0]):
        if m!=0:
            if (int(df_train.iloc[m-1]['Press_Button'] in task_1)):
                if ((int(df_train.iloc[m]['Press_Button'] in task_2)) |(int(df_train.iloc[m]['Press_Button'] in task_3))):
                    task_alteration=1
                    switch_task_train[m]= task_alteration;
                    
            elif (int(df_train.iloc[m-1]['Press_Button'] in task_2)):
                if ((int(df_train.iloc[m]['Press_Button'] in task_1))| (int(df_train.iloc[m]['Press_Button'] in task_3))):
                    task_alteration=1
                    switch_task_train[m]= task_alteration;
                
            elif (int(df_train.iloc[m-1]['Press_Button'] in task_3)):
                if ((int(df_train.iloc[m]['Press_Button'] in task_2)) |(int(df_train.iloc[m]['Press_Button'] in task_1))):
                    task_alteration=1
                    switch_task_train[m]= task_alteration;
  
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
            

            ############# Task 1 ############### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                
            # data.Press_Button=="img/warm.png"        
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
         
        #################### Task 2 ########################  data.Press_Button=="img/urban.png"
            elif(int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            # data.Press_Button=="img/rural.png"
            elif    (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            
        #################### Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            #data.Press_Button=="img/pois.png"
            elif    (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    
    ### VERSION 2 ###
    if df_test['version'][0]==2:
        for i in range (df_test.shape[0]):
    
            ### Task 1 ###  data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            #data.Press_Button=="img/warm.png"   
            elif    (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                
            #################### Task 2########################  data.Press_Button=="img/urban.png" 
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            #data.Press_Button=="img/rural.png"            
            elif    (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            #################### Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
            #data.Press_Button=="img/pois.png"           
            elif    (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    
    ### VERSION 3 ###
    if df_test['version'][0]==3:
        for i in range (df_test.shape[0]):
            
            ### Task 1 ### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
            #data.Press_Button=="img/warm.png"    
            elif    (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & 
                    ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                    (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                    (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                    
            ####################Task 2########################   data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                
             #data.Press_Button=="img/rural.png"           
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )| 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
                
            ####################Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            # data.Press_Button=="img/pois.png"            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
                        
    ### VERSION 4 ###
    if df_test['version'][0]==4:
        for i in range (df_test.shape[0]):
    
            ### Task 1 ###  data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            # data.Press_Button=="img/warm.png"    
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                    
            ####################Task 2########################   data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
                #data.Press_Button=="img/rural.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        

            ####################Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
                          
### VERSION 5 ###
    if df_test['version'][0]==5:
        for i in range (df_test.shape[0]):
        
            ### Task 1 ### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
        
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') &  #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2########################   data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') &  #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
                
            ####################Task 3########################   data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') &  #data.Press_Button=="img/pois.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
                        
### VERSION 6 ###
    if df_test['version'][0]==6:
        for i in range (df_test.shape[0]):
    
            ### Task 1 ### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
        
                            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') &  #data.Press_Button=="img/warm.png" 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

        
            #################### Task 2########################  
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & #data.Press_Button=="img/urban.png" 
                 ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
        
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        

            ####################Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                          
### VERSION 7 ###
    if df_test['version'][0]==7:
        for i in range (df_test.shape[0]):
    
            ### Task 1 ### data.Press_Button=="img/cold.png" 
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2########################  data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') &  #data.Press_Button=="img/rural.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        

            ####################task 3########################  
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & #data.Press_Button=="img/ok.png"
                  ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                   (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                   (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                   (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                  
### VERSION 8 ###
    if df_test['version'][0]==8:
        for i in range (df_test.shape[0]):
    
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                    
            #################### Task 2########################   data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.pn') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )| 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        

            #################### Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
                                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy


            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                  
### VERSION 9 ###
    if df_test['version'][0]==9:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                    
            #################### Task 2########################   data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & # data.Press_Button=="img/rural.png" 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            #################### Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
### Version 10 ######
    if df_test['version'][0]==10:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                       
            #  data.Press_Button=="img/warm.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2####################### data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
             
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            ####################Planet 3######################## 
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
             
         
            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                          
### VERSION 11 ###
    if df_test['version'][0]==11:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
              ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )| 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
                                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2########################  data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
        
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        

            ####################Task 3########################   data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
      
### VERSION 12 ###
    if df_test['version'][0]==12:
        for i in range (df_test.shape[0]):
        
            ################### Planet 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                                            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') &  #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2########################  data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') & 
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        

            ####################Task 3########################  data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & 
            ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) | 
            (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                    
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.pn') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) | 
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
###############################################################################
###############################################################################
### VERSION 13 ###
    if df_test['version'][0]==13:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            ####################Planet 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
          
    ### VERSION 14 ###
    if df_test['version'][0]==14:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                 ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
      
    ### VERSION 15 ###
    if df_test['version'][0]==15:
        for i in range (df_test.shape[0]):

            ################### Task 1 ####################  data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & # data.Press_Button=="img/pois.png"
                 ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
          
### VERSION 16 ###
    if df_test['version'][0]==16:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') &
                 ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                 (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy


            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
          
### VERSION 17 ###
    if df_test['version'][0]==17:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png' )&
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
      
### VERSION 18 ###
    if df_test['version'][0]==18:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            ####################Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 19 ###
    if df_test['version'][0]==19:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & # data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy


            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                  
    ### VERSION 20 ###
    if df_test['version'][0]==20:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 21 ###
    if df_test['version'][0]==21:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png" 
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & # data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            ####################Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy


            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 22 ###
    if df_test['version'][0]==22:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & # data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & # data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 23 ###
    if df_test['version'][0]==23:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2 ######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif(int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
                
    ### VERSION 24 ###
    if df_test['version'][0]==24:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2 ######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
                        
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png" 
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 25 ###
    if df_test['version'][0]==25:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2########################  data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    
    ### VERSION 26 ###
    if df_test['version'][0]==26:
        for i in range (df_test.shape[0]):
            
            ################### Planet 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
            ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            ####################Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
                
    ### VERSION 27 ###
    if df_test['version'][0]==27:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 28 ###
    if df_test['version'][0]==28:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png"') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif(int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 29 ###
    if df_test['version'][0]==29:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2 ######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 30 ###
    if df_test['version'][0]==30:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 31 ###
    if df_test['version'][0]==31:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif(int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 32 ###
    if df_test['version'][0]==32:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 33 ###
    if df_test['version'][0]==33:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 34 ###
    if df_test['version'][0]==34:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & # data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 35 ###
    if df_test['version'][0]==35:
        for i in range (df_test.shape[0]):

            ################### Planet 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                (int((df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 36 ###
    if df_test['version'][0]==36:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2########################  data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            ####################Planet 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png' )&
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
          
    ### VERSION 37 ###
    if df_test['version'][0]==37:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3######################## data.Press_Button=="img/ok.png" 
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 38 ###
    if df_test['version'][0]==38:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2 ######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
            
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 39 ###
    if df_test['version'][0]==39:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2 ######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy

            
            ####################Planet 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
          
    ### VERSION 40 ###
    if df_test['version'][0]==40:
        for i in range (df_test.shape[0]):
            
            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 41 ###
    if df_test['version'][0]==41:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if  (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png' )&
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 42 ###
    if df_test['version'][0]==42:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2 ######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 3######################## data.Press_Button=="img/pois.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') & #data.Press_Button=="img/ok.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 43 ###
    if df_test['version'][0]==43:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
            ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
            (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy
            
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            ####################Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 44 ###
    if df_test['version'][0]==44:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
 
            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                

            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                

            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
                

            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 45 ###
    if df_test['version'][0]==45:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & # data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            #################### Task 3 ######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
              
    ### VERSION 46 ###
    if df_test['version'][0]==46:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & # data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                (int((df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            ####################Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg') )|
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
          
    ### VERSION 47 ###
    if df_test['version'][0]==47:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            #################### Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            

            ####################Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
  
    ### VERSION 48 ###
    if df_test['version'][0]==48:
        for i in range (df_test.shape[0]):

            ################### Task 1 #################### data.Press_Button=="img/cold.png"
            if (int(df_test.iloc[i]['Press_Button']=='img/cold.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/warm.png') & #data.Press_Button=="img/warm.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')))):
               
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 2######################## data.Press_Button=="img/urban.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/urban.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/rural.png') & #data.Press_Button=="img/rural.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            ####################Task 3######################## data.Press_Button=="img/ok.png"
            elif (int(df_test.iloc[i]['Press_Button']=='img/ok.png') &
                ((int(df_test.iloc[i]['stimulus_image']=='img/211.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/212.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/221.jpgg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/222.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy
            
            elif (int(df_test.iloc[i]['Press_Button']=='img/pois.png') & #data.Press_Button=="img/pois.png"
                ((int(df_test.iloc[i]['stimulus_image']=='img/111.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/112.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/121.jpg')) |
                (int(df_test.iloc[i]['stimulus_image']=='img/122.jpg')))):
                
                accuracy=1;
                list_acc[i]=accuracy

            if i!=0:
                if (int(df_test.iloc[i-1]['Press_Button'] in task_1)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                        
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_2)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_1))| (int(df_test.iloc[i]['Press_Button'] in task_3))):
                        task_alteration=1
                        switch_task[i]= task_alteration;
                    
                elif (int(df_test.iloc[i-1]['Press_Button'] in task_3)):
                    if ((int(df_test.iloc[i]['Press_Button'] in task_2)) |(int(df_test.iloc[i]['Press_Button'] in task_1))):
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
    df_train.to_csv(address+'df_train_'+ str(j) +'_Stimulus_Interleaved_Day1.csv', index=False)
    df_test.to_csv(address+'df_'+ str(j) +'_Stimulus_Interleaved_Day2.csv', index=False)
##########################################################################################


list_csv_file_df_test=[]
    
for i in range (len(list_csv_file_Day2_Update)):
    list_csv_file_df_test.append('df_'+ str(i) +'_Stimulus_Interleaved_Day2.csv')
    

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
                    
                    'Response_Percentage_block_10': (df.iloc[0:48]['response'].notnull().sum()/48)*100,
                    'Response_Percentage_block_11': (df.iloc[48:96]['response'].notnull().sum()/48)*100,
                    'Response_Percentage_block_12': (df.iloc[96:144]['response'].notnull().sum()/48)*100,}

    df_total_test = df_total_test.append(dict_data_test, ignore_index=True)


df_total_test.to_csv(address+'df_total_Stimulus_Interleaved_Day2.csv', index=False)

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

df_total['Response_Percentage_block_10']=df_total_test['Response_Percentage_block_10']
df_total['Response_Percentage_block_11']=df_total_test['Response_Percentage_block_11']
df_total['Response_Percentage_block_12']=df_total_test['Response_Percentage_block_12']



##############################################################################################
##################### df_total_required_payment
# saving df_total after removing sunbject based on the performance of the second day
# only subject in this new version of df_total will be paid
# the final amount of extra payment I need to pay them is the collumn of 'extra_payment' in this dataframe
df_total.to_csv(address+'df_Total_Stimulus_Interleaved_Two_Days_Required_Payment.csv', index=False)


#####################################################################################################
################################ Computing ACC criteria for data analyisis###########################
#####################################################################################################

# another way to use that function is to give it the proportion of success and the number of trials considered
# (it's basically the length of the array or the number of responses you take into account for a participant)
#pvalue = stats.binom_test(accuracy1.sum(), n = len(accuracy1), p=0.5, alternative='greater')
#print('accuracy 1: %.2f, pvalue 1= %.4f' % (accuracy1.mean(), pvalue))


# list csv file that pass the payment criteria. Now I want to check these participants performance 
# whether they can pass the ACC bionomial test criteria or not.
from scipy import stats
csv_list_ACC = df_total['prolificID'].tolist()

# address the first day data to go and check csv file of 6 training session to for ACC

Address_Day1='D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day1//Data//'

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
         
df_whole_train.to_csv(address+'df_Total_Stimulus_Interleaved_Two_Days_ACC_Critera_Whole_Train.csv', index=False)




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
         

df_switch_cost.to_csv(address+'df_Switch_Cost_Stimulus_Interleaved.csv', index=False)

df_456.to_csv(address+'df_Total_Stimulus_Interleaved_Two_Days_ACC_Critera_456_Train.csv', index=False)

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
df_outlier.to_csv(address+'df_Total_Stimulus_Interleaved_Two_Days_without_outlier.csv', index=False)

################################################################################################################
###################################### Computing mean ACC of [1,2,3] ,[4,5,6], [7,8,9], [10,11,12] #############
################################################################################################################
from statistics import mean
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

df_456=pd.read_csv('D://OneDrive - UGent//Desktop//Mina//Prolific//3.Stimulus_Oriented_Interleaved_two_Days//Day2//Data//df_Total_Stimulus_Interleaved_Two_Days_ACC_Critera_456_Train.csv')
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

df_bar.to_csv(address+'df_bar_Stimulus_Interleaved.csv', index=False)

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
 
x_axis_bar = ['B1B2B3', 'B4B5B6', 'B7B8B9', 'B10B11B12']
y_whole = list(Mean_Acc_Blocks_Whole.values())
plt.bar(x_axis_bar, y_whole, color='green')
#plt.xticks(rotation='vertical')

plt.title("Stimulus_Interleaved (ACC Criteria Whole Training)",fontsize=12)
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


y_456=list(Mean_Acc_Blocks_456.values())
plt.bar(x_axis_bar, y_456, color='green')

plt.title("Stimulus_Interleaved (ACC Criteria Blocks 456)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.xticks(rotation=45)
plt.ylim(0.5, 1)
# calling the function to add value labels
addlabels(x_axis_bar,y_456)
plt.show()

#################################################################################################################
#################################### Bar plot with omitiing outlier based on ACC criteria whole trianing blocks ##
#################################################################################################################

y_outlier=list(Mean_Acc_Blocks_Outlier.values())
plt.bar(x_axis_bar, y_outlier, color='green')
#plt.xticks(rotation='vertical')

plt.title("Stimulus_Interleaved (without outlier)",fontsize=12)
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
plt.title("Stimulus_Interleaved (Median)",fontsize=12)
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
plt.title("Stimulus_Interleaved (ACC Criteria Whole Training)",fontsize=12)
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

import matplotlib.pyplot as plt 

y2= [df_456['ACC_block_1'].mean(),df_456['ACC_block_2'].mean(),df_456['ACC_block_3'].mean(), 
     df_456['ACC_block_4'].mean(),df_456['ACC_block_5'].mean(),df_456['ACC_block_6'].mean(),
     df_456['ACC_block_7'].mean(),df_456['ACC_block_8'].mean(),df_456['ACC_block_9'].mean(),
     df_456['ACC_block_10'].mean(),df_456['ACC_block_11'].mean(),df_456['ACC_block_12'].mean()]


plt.clf()
plt.plot(x_axis,y2,'bo-')
plt.xticks(rotation=45)
plt.title("Mean ACC Stimulus_Interleaved Task",fontsize=20)
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
plt.title("Stimulus_Interleaved (Without Outlier)",fontsize=12)
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
plt.title("Stimulus_Interleaved (Median)",fontsize=12)
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
plt.title("Stimulus_Interleaved (Whole)",fontsize=12)
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
plt.title("Mean RT Stimulus_Interleaved Task",fontsize=20)
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

#######################################################################
#################### Scatter plot RT vs ACC for each block ##########
#####################################################################
import seaborn as sns
import matplotlib.pyplot as plt
 
#plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
plt.xkcd() #comic style
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
'''
plt.scatter(x =[0:df_outlier.shape[0]] , y = "ACC_block_1")
sns.jointplot(x = "ACC_block_2", y = "RT_block_2",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_3", y = "RT_block_3",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_4", y = "RT_block_4",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_5", y = "RT_block_5",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_6", y = "RT_block_6",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_7", y = "RT_block_7",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_8", y = "RT_block_8",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_9", y = "RT_block_9",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_10", y = "RT_block_10",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_11", y = "RT_block_11",kind = "scatter", data = df_outlier)
sns.jointplot(x = "ACC_block_12", y = "RT_block_12",kind = "scatter", data = df_outlier)
'''    
    
    
    
