import pandas as pd
import numpy as np


# I want to make seprate dataframe for each rule accuracy and Reaction Time

leg_rule_acc=['Insect', 
              'acc_leg_1', 'acc_leg_2', 'acc_leg_3', 'acc_leg_4', 'acc_leg_5', 'acc_leg_6',
              'acc_leg_7', 'acc_leg_8', 'acc_leg_9', 'acc_leg_10', 'acc_leg_11', 'acc_leg_12']

leg_rule_rt=['Insect',                        
             'rt_leg_1', 'rt_leg_2', 'rt_leg_3', 'rt_leg_4', 'rt_leg_5', 'rt_leg_6',
             'rt_leg_7', 'rt_leg_8', 'rt_leg_9', 'rt_leg_10', 'rt_leg_11', 'rt_leg_12']


antenn_rule_acc=['Insect', 
                 'acc_antenn_1', 'acc_antenn_2', 'acc_antenn_3', 'acc_antenn_4', 'acc_antenn_5', 'acc_antenn_6',
                 'acc_antenn_7', 'acc_antenn_8', 'acc_antenn_9', 'acc_antenn_10', 'acc_antenn_11', 'acc_antenn_12']

antenn_rule_rt=['Insect', 
                'rt_antenn_1', 'rt_antenn_2', 'rt_antenn_3', 'rt_antenn_4', 'rt_antenn_5', 'rt_antenn_6',
                'rt_antenn_7', 'rt_antenn_8', 'rt_antenn_9', 'rt_antenn_10', 'rt_antenn_11', 'rt_antenn_12']

mouth_rule_acc=['Insect', 
                'acc_mouth_1', 'acc_mouth_2', 'acc_mouth_3', 'acc_mouth_4', 'acc_mouth_5', 'acc_mouth_6',
                'acc_mouth_7', 'acc_mouth_8', 'acc_mouth_9', 'acc_mouth_10', 'acc_mouth_11', 'acc_mouth_12']

mouth_rule_rt=['Insect', 
               'rt_mouth_1', 'rt_mouth_2', 'rt_mouth_3', 'rt_mouth_4', 'rt_mouth_5', 'rt_mouth_6',
               'rt_mouth_7', 'rt_mouth_8', 'rt_mouth_9', 'rt_mouth_10', 'rt_mouth_11', 'rt_mouth_12']

df_leg_acc=pd.DataFrame(columns= leg_rule_acc)
df_antenn_acc=pd.DataFrame(columns= antenn_rule_acc)
df_mouth_acc=pd.DataFrame(columns= mouth_rule_acc)

df_leg_rt=pd.DataFrame(columns= leg_rule_rt)
df_antenn_rt=pd.DataFrame(columns= antenn_rule_rt)
df_mouth_rt=pd.DataFrame(columns= mouth_rule_rt)


for j in range(len(list_csv_file_Day2_Update)):
    
    df= pd.read_csv(Day_1_Address+list_csv_file_Day2_Update[j])
    
    insect_111_leg_acc=['111','leg']
    insect_111_leg_rt=['111','leg']
    
    insect_112_leg_acc=['112','leg',]
    insect_112_leg_rt=['112','leg',]
    
    insect_121_leg_acc=['121','leg',]
    insect_121_leg_rt=['121','leg',]
    
    insect_122_leg_acc=['122','leg',]
    insect_122_leg_rt=['122','leg',]
    
    insect_211_leg_acc=['211','leg',]
    insect_211_leg_rt=['211','leg',]
    
    insect_212_leg_acc=['212','leg',]
    insect_212_leg_rt=['212','leg',]
    
    insect_221_leg_acc=['221','leg',]
    insect_221_leg_rt=['221','leg',]
    
    insect_222_leg_acc=['222','leg',]
    insect_222_leg_rt=['222','leg',]
    
    insect_111_antenn_acc=['111','antenn']
    insect_111_antenn_rt=['111','antenn']
    
    insect_112_antenn_acc=['112','antenn']
    insect_112_antenn_rt=['112','antenn']
    
    insect_121_antenn_acc=['121','antenn']
    insect_121_antenn_rt=['121','antenn']
    
    insect_122_antenn_acc=['122','antenn']
    insect_122_antenn_rt=['122','antenn']
    
    insect_211_antenn_acc=['211','antenn']
    insect_211_antenn_rt=['211','antenn']
    
    insect_212_antenn_acc=['212','antenn']
    insect_212_antenn_rt=['212','antenn']
    
    insect_221_antenn_acc=['221','antenn']
    insect_221_antenn_rt=['221','antenn']
    
    insect_222_antenn_acc=['222','antenn']
    insect_222_antenn_rt=['222','antenn']
    
    insect_111_mouth_acc=['111','mouth']
    insect_111_mouth_rt=['111','mouth']
                         
    insect_112_mouth_acc=[ '112','mouth']
    insect_112_mouth_rt=[ '112','mouth']
                         
    insect_121_mouth_acc=['121','mouth']
    insect_121_mouth_rt=['121','mouth']
                         
    insect_122_mouth_acc=['122','mouth']
    insect_122_mouth_rt=['122','mouth']
                         
    insect_211_mouth_acc=['211','mouth']
    insect_211_mouth_rt=['211','mouth']
    
    insect_212_mouth_acc=['212','mouth']
    insect_212_mouth_rt=['212','mouth']
    
    insect_221_mouth_acc=['221','mouth']
    insect_221_mouth_rt=['221','mouth']
    
    insect_222_mouth_acc=['222','mouth']
    insect_222_mouth_rt=['222','mouth']


    for i in range(288):
    
        ######## insect 111 ########
        if ((df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_111_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_111_antenn_rt.append(df.iloc[i]['reaction_time'])
                     
            
        elif ((df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_111_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_111_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/111.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_111_leg_acc.append(df.iloc[i]['accuracy'])
              insect_111_leg_rt.append(df.iloc[i]['reaction_time'])
              
        
        ######## insect 112 ########
        if ((df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_112_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_112_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_112_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_112_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/112.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_112_leg_acc.append(df.iloc[i]['accuracy'])
              insect_112_leg_rt.append(df.iloc[i]['reaction_time'])
    
    
       ############ insect 121 ##########
        if ((df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_121_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_121_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_121_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_121_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/121.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_121_leg_acc.append(df.iloc[i]['accuracy'])
              insect_121_leg_rt.append(df.iloc[i]['reaction_time'])
              
        
        ############ insect 122 ##########
        if ((df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_122_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_122_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_122_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_122_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/122.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_122_leg_acc.append(df.iloc[i]['accuracy'])
              insect_122_leg_rt.append(df.iloc[i]['reaction_time'])


        ########### insect 211 ###########
        if ((df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_211_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_211_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_211_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_211_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/211.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_211_leg_acc.append(df.iloc[i]['accuracy'])
              insect_211_leg_rt.append(df.iloc[i]['reaction_time'])             
              
              
        ########### insect 212 ###########
        if ((df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_212_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_212_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_212_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_212_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/212.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_212_leg_acc.append(df.iloc[i]['accuracy'])
              insect_212_leg_rt.append(df.iloc[i]['reaction_time'])
              
        ########### insect 221 ###########
        if ((df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_221_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_221_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_221_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_221_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/221.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_221_leg_acc.append(df.iloc[i]['accuracy'])
              insect_221_leg_rt.append(df.iloc[i]['reaction_time'])
              
              
        ########### insect 222 ###########
        if ((df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thin Antenna') or
            (df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thick Antenna')) :
            insect_222_antenn_acc.append(df.iloc[i]['accuracy'])
            insect_222_antenn_rt.append(df.iloc[i]['reaction_time'])
            
        elif ((df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Mandible Mouth') or
              (df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Shovel Mouth')) :
              insect_222_mouth_acc.append(df.iloc[i]['accuracy'])
              insect_222_mouth_rt.append(df.iloc[i]['reaction_time'])
              
        elif ((df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thin Leg') or
              (df.iloc[i]['stimulus_image']=='img/222.jpg' and df.iloc[i]['Rule']=='Thick Leg')) :
              insect_222_leg_acc.append(df.iloc[i]['accuracy'])
              insect_222_leg_rt.append(df.iloc[i]['reaction_time'])
 
    
 
    # 111 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_111_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_111_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_111_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_111_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_111_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_111_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
    # 112 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_112_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_112_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_112_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_112_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_112_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_112_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
    # 121 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_121_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_121_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_121_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_121_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_121_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_121_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
 
    # 122 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_122_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_122_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_122_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_122_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_122_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_122_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
    # 211 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_211_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_211_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_211_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_211_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_211_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_211_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
    # 212 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_212_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_212_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_212_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_212_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_212_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_212_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
    
    # 221 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_221_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_221_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_221_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_221_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_221_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_221_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
    # 222 #
    df_leg_acc = df_leg_acc.append(pd.DataFrame(insect_222_leg_acc, columns = leg_rule_acc, ignore_index = True)                              
    df_antenn_acc = df_antenn_acc.append(pd.DataFrame(insect_222_antenn_acc, columns = antenn_rule_acc, ignore_index = True)
    df_mouth_acc = df_mouth_acc.append(pd.DataFrame(insect_222_mouth_acc, columns = mouth_rule_acc, ignore_index = True)
    
    df_leg_rt = df_leg_rt.append(pd.DataFrame(insect_222_leg_rt, columns = leg_rule_rt, ignore_index = True)                              
    df_antenn_rt = df_antenn_rt.append(pd.DataFrame(insect_222_antenn_rt, columns = antenn_rule_rt, ignore_index = True)
    df_mouth_rt = df_mouth_rt.append(pd.DataFrame(insect_222_mouth_rt, columns = mouth_rule_rt, ignore_index = True)
    
 
    
    
    
            
    
    