
#exactly here I need find stimulus_rule match from the list_csv_file_Day2_Update and 
#go to address day1 for csv files
# we compute the accuracy of stimulus-rule match for 



# Address day1 becuase I want to extract data from day1 CSV s:
Day_1_Address= address = 'D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day1//Data//'

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




df_Stimulu_Response = pd.DataFrame(columns = rule_Stimulus)

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


    for i in range(433): # 288 only train 433 train with test
    
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
    df_Stimulu_Response = df_Stimulu_Response.append(pd.DataFrame(acc_total, columns = rule_Stimulus), ignore_index=True)
    

df_Stimulu_Response['prolificID']=list_csv_file_Day2_Update
day_2_add='D://OneDrive - UGent//Desktop//Mina//Prolific//4.Stimulus_Oriented_Blocked_two_days//Day2//Data//'
df_leg_acc.to_csv(day_2_add+'df_SR_ACC_Stimulus_Blocked_Task_Labeling.csv', index=False) 

######### Plotting stimulus_response seprately and toghether ############
import matplotlib.pyplot as plt 

# list of x axis 
x_axis=['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12']

df.mean(axis=0)
y_111_leg_acc= [df_111_leg_acc['acc_leg_1'].mean(),df_111_leg_acc['acc_leg_2'].mean(),df_111_leg_acc['acc_leg_3'].mean(), 
                df_111_leg_acc['acc_leg_4'].mean(),df_111_leg_acc['acc_leg_5'].mean(),df_111_leg_acc['acc_leg_6'].mean(),
                df_111_leg_acc['acc_leg_7'].mean(),df_111_leg_acc['acc_leg_8'].mean(),df_111_leg_acc['acc_leg_9'].mean(),
                df_111_leg_acc['acc_leg_10'].mean(),df_111_leg_acc['acc_leg_11'].mean(),df_111_leg_acc['acc_leg_12'].mean()]

y_112_leg_acc= [df_112_leg_acc['acc_leg_1'].mean(),df_112_leg_acc['acc_leg_2'].mean(),df_112_leg_acc['acc_leg_3'].mean(), 
                df_112_leg_acc['acc_leg_4'].mean(),df_112_leg_acc['acc_leg_5'].mean(),df_112_leg_acc['acc_leg_6'].mean(),
                df_112_leg_acc['acc_leg_7'].mean(),df_112_leg_acc['acc_leg_8'].mean(),df_112_leg_acc['acc_leg_9'].mean(),
                df_112_leg_acc['acc_leg_10'].mean(),df_112_leg_acc['acc_leg_11'].mean(),df_112_leg_acc['acc_leg_12'].mean()]

y_121_leg_acc= [df_121_leg_acc['acc_leg_1'].mean(),df_121_leg_acc['acc_leg_2'].mean(),df_121_leg_acc['acc_leg_3'].mean(), 
                df_121_leg_acc['acc_leg_4'].mean(),df_121_leg_acc['acc_leg_5'].mean(),df_121_leg_acc['acc_leg_6'].mean(),
                df_121_leg_acc['acc_leg_7'].mean(),df_121_leg_acc['acc_leg_8'].mean(),df_121_leg_acc['acc_leg_9'].mean(),
                df_121_leg_acc['acc_leg_10'].mean(),df_121_leg_acc['acc_leg_11'].mean(),df_121_leg_acc['acc_leg_12'].mean()]

y_122_leg_acc= [df_122_leg_acc['acc_leg_1'].mean(),df_122_leg_acc['acc_leg_2'].mean(),df_122_leg_acc['acc_leg_3'].mean(), 
                df_122_leg_acc['acc_leg_4'].mean(),df_122_leg_acc['acc_leg_5'].mean(),df_122_leg_acc['acc_leg_6'].mean(),
                df_122_leg_acc['acc_leg_7'].mean(),df_122_leg_acc['acc_leg_8'].mean(),df_122_leg_acc['acc_leg_9'].mean(),
                df_122_leg_acc['acc_leg_10'].mean(),df_122_leg_acc['acc_leg_11'].mean(),df_122_leg_acc['acc_leg_12'].mean()]

y_211_leg_acc= [df_211_leg_acc['acc_leg_1'].mean(),df_211_leg_acc['acc_leg_2'].mean(),df_211_leg_acc['acc_leg_3'].mean(), 
                df_211_leg_acc['acc_leg_4'].mean(),df_211_leg_acc['acc_leg_5'].mean(),df_211_leg_acc['acc_leg_6'].mean(),
                df_211_leg_acc['acc_leg_7'].mean(),df_211_leg_acc['acc_leg_8'].mean(),df_211_leg_acc['acc_leg_9'].mean(),
                df_211_leg_acc['acc_leg_10'].mean(),df_211_leg_acc['acc_leg_11'].mean(),df_211_leg_acc['acc_leg_12'].mean()]

y_212_leg_acc= [df_212_leg_acc['acc_leg_1'].mean(),df_212_leg_acc['acc_leg_2'].mean(),df_212_leg_acc['acc_leg_3'].mean(), 
                df_212_leg_acc['acc_leg_4'].mean(),df_212_leg_acc['acc_leg_5'].mean(),df_212_leg_acc['acc_leg_6'].mean(),
                df_212_leg_acc['acc_leg_7'].mean(),df_212_leg_acc['acc_leg_8'].mean(),df_212_leg_acc['acc_leg_9'].mean(),
                df_212_leg_acc['acc_leg_10'].mean(),df_212_leg_acc['acc_leg_11'].mean(),df_212_leg_acc['acc_leg_12'].mean()]

y_221_leg_acc= [df_221_leg_acc['acc_leg_1'].mean(),df_221_leg_acc['acc_leg_2'].mean(),df_221_leg_acc['acc_leg_3'].mean(), 
                df_221_leg_acc['acc_leg_4'].mean(),df_221_leg_acc['acc_leg_5'].mean(),df_221_leg_acc['acc_leg_6'].mean(),
                df_221_leg_acc['acc_leg_7'].mean(),df_221_leg_acc['acc_leg_8'].mean(),df_221_leg_acc['acc_leg_9'].mean(),
                df_221_leg_acc['acc_leg_10'].mean(),df_221_leg_acc['acc_leg_11'].mean(),df_221_leg_acc['acc_leg_12'].mean()]

y_222_leg_acc= [df_222_leg_acc['acc_leg_1'].mean(),df_222_leg_acc['acc_leg_2'].mean(),df_222_leg_acc['acc_leg_3'].mean(), 
                df_222_leg_acc['acc_leg_4'].mean(),df_222_leg_acc['acc_leg_5'].mean(),df_222_leg_acc['acc_leg_6'].mean(),
                df_222_leg_acc['acc_leg_7'].mean(),df_222_leg_acc['acc_leg_8'].mean(),df_222_leg_acc['acc_leg_9'].mean(),
                df_222_leg_acc['acc_leg_10'].mean(),df_222_leg_acc['acc_leg_11'].mean(),df_222_leg_acc['acc_leg_12'].mean()]


y_111_mouth_acc= [df_111_mouth_acc['acc_mouth_1'].mean(),df_111_mouth_acc['acc_mouth_2'].mean(),df_111_mouth_acc['acc_mouth_3'].mean(), 
                  df_111_mouth_acc['acc_mouth_4'].mean(),df_111_mouth_acc['acc_mouth_5'].mean(),df_111_mouth_acc['acc_mouth_6'].mean(),
                  df_111_mouth_acc['acc_mouth_7'].mean(),df_111_mouth_acc['acc_mouth_8'].mean(),df_111_mouth_acc['acc_mouth_9'].mean(),
                  df_111_mouth_acc['acc_mouth_10'].mean(),df_111_mouth_acc['acc_mouth_11'].mean(),df_111_mouth_acc['acc_mouth_12'].mean()]

y_112_mouth_acc= [df_112_mouth_acc['acc_mouth_1'].mean(),df_112_mouth_acc['acc_mouth_2'].mean(),df_112_mouth_acc['acc_mouth_3'].mean(), 
                  df_112_mouth_acc['acc_mouth_4'].mean(),df_112_mouth_acc['acc_mouth_5'].mean(),df_112_mouth_acc['acc_mouth_6'].mean(),
                  df_112_mouth_acc['acc_mouth_7'].mean(),df_112_mouth_acc['acc_mouth_8'].mean(),df_112_mouth_acc['acc_mouth_9'].mean(),
                  df_112_mouth_acc['acc_mouth_10'].mean(),df_112_mouth_acc['acc_mouth_11'].mean(),df_112_mouth_acc['acc_mouth_12'].mean()]

y_121_mouth_acc= [df_121_mouth_acc['acc_mouth_1'].mean(),df_121_mouth_acc['acc_mouth_2'].mean(),df_121_mouth_acc['acc_mouth_3'].mean(), 
                  df_121_mouth_acc['acc_mouth_4'].mean(),df_121_mouth_acc['acc_mouth_5'].mean(),df_121_mouth_acc['acc_mouth_6'].mean(),
                  df_121_mouth_acc['acc_mouth_7'].mean(),df_121_mouth_acc['acc_mouth_8'].mean(),df_121_mouth_acc['acc_mouth_9'].mean(),
                  df_121_mouth_acc['acc_mouth_10'].mean(),df_121_mouth_acc['acc_mouth_11'].mean(),df_121_mouth_acc['acc_mouth_12'].mean()]

y_122_mouth_acc= [df_122_mouth_acc['acc_mouth_1'].mean(),df_122_mouth_acc['acc_mouth_2'].mean(),df_122_mouth_acc['acc_mouth_3'].mean(), 
                  df_122_mouth_acc['acc_mouth_4'].mean(),df_122_mouth_acc['acc_mouth_5'].mean(),df_122_mouth_acc['acc_mouth_6'].mean(),
                  df_122_mouth_acc['acc_mouth_7'].mean(),df_122_mouth_acc['acc_mouth_8'].mean(),df_122_mouth_acc['acc_mouth_9'].mean(),
                  df_122_mouth_acc['acc_mouth_10'].mean(),df_122_mouth_acc['acc_mouth_11'].mean(),df_122_mouth_acc['acc_mouth_12'].mean()]

y_211_mouth_acc= [df_211_mouth_acc['acc_mouth_1'].mean(),df_211_mouth_acc['acc_mouth_2'].mean(),df_211_mouth_acc['acc_mouth_3'].mean(), 
                  df_211_mouth_acc['acc_mouth_4'].mean(),df_211_mouth_acc['acc_mouth_5'].mean(),df_211_mouth_acc['acc_mouth_6'].mean(),
                  df_211_mouth_acc['acc_mouth_7'].mean(),df_211_mouth_acc['acc_mouth_8'].mean(),df_211_mouth_acc['acc_mouth_9'].mean(),
                  df_211_mouth_acc['acc_mouth_10'].mean(),df_211_mouth_acc['acc_mouth_11'].mean(),df_211_mouth_acc['acc_mouth_12'].mean()]

y_212_mouth_acc= [df_212_mouth_acc['acc_mouth_1'].mean(),df_212_mouth_acc['acc_mouth_2'].mean(),df_212_mouth_acc['acc_mouth_3'].mean(), 
                  df_212_mouth_acc['acc_mouth_4'].mean(),df_212_mouth_acc['acc_mouth_5'].mean(),df_212_mouth_acc['acc_mouth_6'].mean(),
                  df_212_mouth_acc['acc_mouth_7'].mean(),df_212_mouth_acc['acc_mouth_8'].mean(),df_212_mouth_acc['acc_mouth_9'].mean(),
                  df_212_mouth_acc['acc_mouth_10'].mean(),df_212_mouth_acc['acc_mouth_11'].mean(),df_212_mouth_acc['acc_mouth_12'].mean()]

y_221_mouth_acc= [df_221_mouth_acc['acc_mouth_1'].mean(),df_221_mouth_acc['acc_mouth_2'].mean(),df_221_mouth_acc['acc_mouth_3'].mean(), 
                  df_221_mouth_acc['acc_mouth_4'].mean(),df_221_mouth_acc['acc_mouth_5'].mean(),df_221_mouth_acc['acc_mouth_6'].mean(),
                  df_221_mouth_acc['acc_mouth_7'].mean(),df_221_mouth_acc['acc_mouth_8'].mean(),df_221_mouth_acc['acc_mouth_9'].mean(),
                  df_221_mouth_acc['acc_mouth_10'].mean(),df_221_mouth_acc['acc_mouth_11'].mean(),df_221_mouth_acc['acc_mouth_12'].mean()]

y_222_mouth_acc= [df_222_mouth_acc['acc_mouth_1'].mean(),df_222_mouth_acc['acc_mouth_2'].mean(),df_222_mouth_acc['acc_mouth_3'].mean(), 
                  df_222_mouth_acc['acc_mouth_4'].mean(),df_222_mouth_acc['acc_mouth_5'].mean(),df_222_mouth_acc['acc_mouth_6'].mean(),
                  df_222_mouth_acc['acc_mouth_7'].mean(),df_222_mouth_acc['acc_mouth_8'].mean(),df_222_mouth_acc['acc_mouth_9'].mean(),
                  df_222_mouth_acc['acc_mouth_10'].mean(),df_222_mouth_acc['acc_mouth_11'].mean(),df_222_mouth_acc['acc_mouth_12'].mean()]


y_111_antenn_acc= [df_111_antenn_acc['acc_antenn_1'].mean(),df_111_antenn_acc['acc_antenn_2'].mean(),df_111_antenn_acc['acc_antenn_3'].mean(), 
                   df_111_antenn_acc['acc_antenn_4'].mean(),df_111_antenn_acc['acc_antenn_5'].mean(),df_111_antenn_acc['acc_antenn_6'].mean(),
                   df_111_antenn_acc['acc_antenn_7'].mean(),df_111_antenn_acc['acc_antenn_8'].mean(),df_111_antenn_acc['acc_antenn_9'].mean(),
                   df_111_antenn_acc['acc_antenn_10'].mean(),df_111_antenn_acc['acc_antenn_11'].mean(),df_111_antenn_acc['acc_antenn_12'].mean()]

y_112_antenn_acc= [df_112_antenn_acc['acc_antenn_1'].mean(),df_112_antenn_acc['acc_antenn_2'].mean(),df_112_antenn_acc['acc_antenn_3'].mean(), 
                   df_112_antenn_acc['acc_antenn_4'].mean(),df_112_antenn_acc['acc_antenn_5'].mean(),df_112_antenn_acc['acc_antenn_6'].mean(),
                   df_112_antenn_acc['acc_antenn_7'].mean(),df_112_antenn_acc['acc_antenn_8'].mean(),df_112_antenn_acc['acc_antenn_9'].mean(),
                   df_112_antenn_acc['acc_antenn_10'].mean(),df_112_antenn_acc['acc_antenn_11'].mean(),df_112_antenn_acc['acc_antenn_12'].mean()]

y_121_antenn_acc= [df_121_antenn_acc['acc_antenn_1'].mean(),df_121_antenn_acc['acc_antenn_2'].mean(),df_121_antenn_acc['acc_antenn_3'].mean(), 
                   df_121_antenn_acc['acc_antenn_4'].mean(),df_121_antenn_acc['acc_antenn_5'].mean(),df_121_antenn_acc['acc_antenn_6'].mean(),
                   df_121_antenn_acc['acc_antenn_7'].mean(),df_121_antenn_acc['acc_antenn_8'].mean(),df_121_antenn_acc['acc_antenn_9'].mean(),
                   df_121_antenn_acc['acc_antenn_10'].mean(),df_121_antenn_acc['acc_antenn_11'].mean(),df_121_antenn_acc['acc_antenn_12'].mean()]

y_122_antenn_acc= [df_122_antenn_acc['acc_antenn_1'].mean(),df_122_antenn_acc['acc_antenn_2'].mean(),df_122_antenn_acc['acc_antenn_3'].mean(), 
                   df_122_antenn_acc['acc_antenn_4'].mean(),df_122_antenn_acc['acc_antenn_5'].mean(),df_122_antenn_acc['acc_antenn_6'].mean(),
                   df_122_antenn_acc['acc_antenn_7'].mean(),df_122_antenn_acc['acc_antenn_8'].mean(),df_122_antenn_acc['acc_antenn_9'].mean(),
                   df_122_antenn_acc['acc_antenn_10'].mean(),df_122_antenn_acc['acc_antenn_11'].mean(),df_122_antenn_acc['acc_antenn_12'].mean()]

y_211_antenn_acc= [df_211_antenn_acc['acc_antenn_1'].mean(),df_211_antenn_acc['acc_antenn_2'].mean(),df_211_antenn_acc['acc_antenn_3'].mean(), 
                   df_211_antenn_acc['acc_antenn_4'].mean(),df_211_antenn_acc['acc_antenn_5'].mean(),df_211_antenn_acc['acc_antenn_6'].mean(),
                   df_211_antenn_acc['acc_antenn_7'].mean(),df_211_antenn_acc['acc_antenn_8'].mean(),df_211_antenn_acc['acc_antenn_9'].mean(),
                   df_211_antenn_acc['acc_antenn_10'].mean(),df_211_antenn_acc['acc_antenn_11'].mean(),df_211_antenn_acc['acc_antenn_12'].mean()]

y_212_antenn_acc= [df_212_antenn_acc['acc_antenn_1'].mean(),df_212_antenn_acc['acc_antenn_2'].mean(),df_212_antenn_acc['acc_antenn_3'].mean(), 
                   df_212_antenn_acc['acc_antenn_4'].mean(),df_212_antenn_acc['acc_antenn_5'].mean(),df_212_antenn_acc['acc_antenn_6'].mean(),
                   df_212_antenn_acc['acc_antenn_7'].mean(),df_212_antenn_acc['acc_antenn_8'].mean(),df_212_antenn_acc['acc_antenn_9'].mean(),
                   df_212_antenn_acc['acc_antenn_10'].mean(),df_212_antenn_acc['acc_antenn_11'].mean(),df_212_antenn_acc['acc_antenn_12'].mean()]

y_221_antenn_acc= [df_221_antenn_acc['acc_antenn_1'].mean(),df_221_antenn_acc['acc_antenn_2'].mean(),df_221_antenn_acc['acc_antenn_3'].mean(), 
                   df_221_antenn_acc['acc_antenn_4'].mean(),df_221_antenn_acc['acc_antenn_5'].mean(),df_221_antenn_acc['acc_antenn_6'].mean(),
                   df_221_antenn_acc['acc_antenn_7'].mean(),df_221_antenn_acc['acc_antenn_8'].mean(),df_221_antenn_acc['acc_antenn_9'].mean(),
                   df_221_antenn_acc['acc_antenn_10'].mean(),df_221_antenn_acc['acc_antenn_11'].mean(),df_221_antenn_acc['acc_antenn_12'].mean()]

y_222_antenn_acc= [df_222_antenn_acc['acc_antenn_1'].mean(),df_222_antenn_acc['acc_antenn_2'].mean(),df_222_antenn_acc['acc_antenn_3'].mean(), 
                   df_222_antenn_acc['acc_antenn_4'].mean(),df_222_antenn_acc['acc_antenn_5'].mean(),df_222_antenn_acc['acc_antenn_6'].mean(),
                   df_222_antenn_acc['acc_antenn_7'].mean(),df_222_antenn_acc['acc_antenn_8'].mean(),df_222_antenn_acc['acc_antenn_9'].mean(),
                   df_222_antenn_acc['acc_antenn_10'].mean(),df_222_antenn_acc['acc_antenn_11'].mean(),df_222_antenn_acc['acc_antenn_12'].mean()]

#label = [ "{:.2f}".format(i) for i in y1]
plt.clf()
plt.plot(x_axis,y_222_antenn_acc,'bo-')
plt.xticks(rotation=45)
plt.title("Stimulus_Block (inscet 222_antenn)",fontsize=12)
plt.xlabel('Block') 
plt.ylabel('Mean ACC')
plt.ylim(0.3, 1)

for x,y in zip(x_axis,y_222_antenn_acc):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 size=10,
                 ha='center') # horizontal alignment can be left, right or center
    #

plt.show() 