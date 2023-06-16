import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv

# Stimulus Blocked Planet

SBP_ACC = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Default_SBP_ACC_history.csv')

SBP_LOSS = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Default_SBP_LOSS_history.csv')

SBP_Input_Gussian_Noise = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Input_Gussian_Noise_Injection_on_Default_Model.csv')

SBP_Weight_Gussian_Noise = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Lesion_Gussian_Noise_on_Default_Model_.csv')

SBP_Weight_Drop = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Lesion_wieght_Drop_on_Default_Model_.csv')

SBP_Timo_Noise = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Timo_Noise_on_Default_Model_.csv')

SBP_ACC_History = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Default_SBP_Model_History.csv')


 

# Stimulus Blocked Labeling
SBL_ACC = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Default_SBLabeling_ACC_history.csv')

SBL_LOSS = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Default_SBLabeling_LOSS_history.csv')
SBL_Input_Gussian_Noise  = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Input_Gussian_Noise_Injection_on_Default_Model.csv')

SBL_Weight_Gussian_Noise  = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Lesion_Gussian_Noise_on_Default_Model_.csv')

SBL_Weight_Drop = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Lesion_wieght_Drop_on_Default_Model_.csv')
SBL_Timo_Noise = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Timo_Noise_on_Default_Model_.csv')

SBL_ACC_History = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Default_SBLabeling_Model_History.csv')

                           
# Context Blocked Planet Model1
CBP_ACC_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_1_ACC_history.csv')
CBP_LOSS_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_1_LOSS_history.csv')
CBP_Input_Gussian_Noise_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Input_Gussian_Noise_Injection_on_Default_Model_1.csv')

CBP_Wieght_Gussian_Noise_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Lesion_Gussian_Noise_on_Default_Model_1.csv')

CBP_Wieght_Drop_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Lesion_wieght_Drop_on_Default_Model_1.csv')
CBP_Timo_Noise_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Timo_Noise_on_Default_Model_1.csv')

CBP_ACC_History_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_1_History.csv')



# Context Blocked Planet Model2
'''
CBP_ACC_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_2_ACC_history.csv')
CBP_LOSS_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_2_LOSS_history.csv')
CBP_Input_Gussian_Noise_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Input_Gussian_Noise_Injection_on_Default_Model_2.csv')
CBP_Wieght_Gussian_Noise_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Lesion_Gussian_Noise_on_Default_Model_2.csv')
CBP_Wieght_Drop_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Lesion_wieght_Drop_on_Default_Model_2.csv')
CBP_Timo_Noise_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Timo_Noise_on_Default_Model_2.csv')

CBP_ACC_History_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_2_History.csv')
'''


# Context Blocked Labeling Modle1
CBL_ACC_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_1_ACC_history.csv')
CBL_LOSS_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_1_LOSS_history.csv')
CBL_Input_Gussian_Noise_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Input_Gussian_Noise_Injection_on_Default_Model_1.csv')
CBL_Wieght_Gussian_Noise_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Lesion_Gussian_Noise_on_Default_Model_1.csv')
CBL_Wieght_Drop_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Lesion_wieght_Drop_on_Default_Model_1.csv')
CBL_Timo_Noise_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Timo_Noise_on_Default_Model_1.csv')

CBL_ACC_History_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_1_History.csv')


'''
# Context Blocked Labeling Model2
CBL_ACC_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_2_ACC_history.csv')
CBL_LOSS_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_2_LOSS_history.csv')
CBL_Input_Gussian_Noise_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Input_Gussian_Noise_Injection_on_Default_Model_2.csv')
CBL_Wieght_Gussian_Noise_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Lesion_Gussian_Noise_on_Default_Model_2.csv')
CBL_Wieght_Drop_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Lesion_wieght_Drop_on_Default_Model_2.csv')
#CBL_Timo_Noise_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Timo_Noise_on_Default_Model_2.csv')


CBL_ACC_History_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_2_History.csv')
'''
#################################################################################
########################## PLOTING ###############################################
##################################################################################


###################################################################################
########################## ACC #################################################
#################################################################################


SBP_ACC_y1 = [SBP_ACC_History['ACC_Before'].mean(), SBP_ACC['E1'].mean(),SBP_ACC['E2'].mean(), SBP_ACC['E3'].mean(),
              SBP_ACC['E4'].mean(),SBP_ACC['E5'].mean(), SBP_ACC['E6'].mean(),
              SBP_ACC['E7'].mean(),SBP_ACC['E8'].mean(), SBP_ACC['E9'].mean(),
              SBP_ACC['E10'].mean(),SBP_ACC['E11'].mean(), SBP_ACC['E12'].mean(),
              SBP_ACC['E13'].mean(),SBP_ACC['E14'].mean(), SBP_ACC['E15'].mean(), SBP_ACC_History['ACC_After'].mean()]


SBL_ACC_y1 = [SBL_ACC_History['ACC_Before'].mean(), SBL_ACC['E1'].mean(), SBL_ACC['E2'].mean(), SBL_ACC['E3'].mean(),
              SBL_ACC['E4'].mean(), SBL_ACC['E5'].mean(), SBL_ACC['E6'].mean(),
              SBL_ACC['E7'].mean(), SBL_ACC['E8'].mean(), SBL_ACC['E9'].mean(),
              SBL_ACC['E10'].mean(), SBL_ACC['E11'].mean(), SBL_ACC['E12'].mean(),
              SBL_ACC['E13'].mean(), SBL_ACC['E14'].mean(), SBL_ACC['E15'].mean(), SBL_ACC_History['ACC_After'].mean()]

CBL_ACC_M1 = [CBL_ACC_History_Model1['ACC_Before'].mean(), CBL_ACC_Model1['E1'].mean(), CBL_ACC_Model1['E2'].mean(), CBL_ACC_Model1['E3'].mean(),
              CBL_ACC_Model1['E4'].mean(), CBL_ACC_Model1['E5'].mean(), CBL_ACC_Model1['E6'].mean(),
              CBL_ACC_Model1['E7'].mean(), CBL_ACC_Model1['E8'].mean(), CBL_ACC_Model1['E9'].mean(),
              CBL_ACC_Model1['E10'].mean(), CBL_ACC_Model1['E11'].mean(), CBL_ACC_Model1['E12'].mean(),
              CBL_ACC_Model1['E13'].mean(), CBL_ACC_Model1['E14'].mean(), CBL_ACC_Model1['E15'].mean(), CBL_ACC_History_Model1['ACC_After'].mean()]

#CBL_ACC_M2 = [CBL_ACC_History_Model2['ACC_Before'].mean(), CBL_ACC_Model2['E1'].mean(), CBL_ACC_Model2['E2'].mean(), CBL_ACC_Model2['E3'].mean(),
#              CBL_ACC_Model2['E4'].mean(), CBL_ACC_Model2['E5'].mean(), CBL_ACC_Model2['E6'].mean(),
#              CBL_ACC_Model2['E7'].mean(), CBL_ACC_Model2['E8'].mean(), CBL_ACC_Model2['E9'].mean(),
#              CBL_ACC_Model2['E10'].mean(), CBL_ACC_Model2['E11'].mean(), CBL_ACC_Model2['E12'].mean(),
#              CBL_ACC_Model2['E13'].mean(), CBL_ACC_Model2['E14'].mean(), CBL_ACC_Model2['E15'].mean(), CBL_ACC_History_Model2['ACC_After'].mean()]


CBP_ACC_M1 = [CBP_ACC_History_Model1['ACC_Before'].mean(), CBP_ACC_Model1['E1'].mean(), CBP_ACC_Model1['E2'].mean(), CBP_ACC_Model1['E3'].mean(),
              CBP_ACC_Model1['E4'].mean(), CBP_ACC_Model1['E5'].mean(), CBP_ACC_Model1['E6'].mean(),
              CBP_ACC_Model1['E7'].mean(), CBP_ACC_Model1['E8'].mean(), CBP_ACC_Model1['E9'].mean(),
              CBP_ACC_Model1['E10'].mean(), CBP_ACC_Model1['E11'].mean(), CBP_ACC_Model1['E12'].mean(),
              CBP_ACC_Model1['E13'].mean(), CBP_ACC_Model1['E14'].mean(), CBP_ACC_Model1['E15'].mean(), CBP_ACC_History_Model1['ACC_After'].mean()]
    
#CBP_ACC_M2 = [CBP_ACC_History_Model2['ACC_Before'].mean(), CBP_ACC_Model2['E1'].mean(), CBP_ACC_Model2['E2'].mean(), CBP_ACC_Model2['E3'].mean(),
#              CBP_ACC_Model2['E4'].mean(), CBP_ACC_Model2['E5'].mean(), CBP_ACC_Model2['E6'].mean(),
#              CBP_ACC_Model2['E7'].mean(), CBP_ACC_Model2['E8'].mean(), CBP_ACC_Model2['E9'].mean(),
#              CBP_ACC_Model2['E10'].mean(), CBP_ACC_Model2['E11'].mean(), CBP_ACC_Model2['E12'].mean(),
#             CBP_ACC_Model2['E13'].mean(), CBP_ACC_Model2['E14'].mean(), CBP_ACC_Model2['E15'].mean(), CBP_ACC_History_Model2['ACC_After'].mean()]
    

####################################################################################################
################################## INPUT GUASSIAN NOISE ############################################
####################################################################################################


SBP_Input_Gussian_Noise_y1 = [SBP_Input_Gussian_Noise['No'].mean(), SBP_Input_Gussian_Noise['0.001'].mean(),SBP_Input_Gussian_Noise['0.004'].mean(),
                              SBP_Input_Gussian_Noise['0.008'].mean(), SBP_Input_Gussian_Noise['0.01'].mean(), SBP_Input_Gussian_Noise['0.04'].mean(),
                              SBP_Input_Gussian_Noise['0.08'].mean(), SBP_Input_Gussian_Noise['0.1'].mean(), SBP_Input_Gussian_Noise['0.4'].mean(),
                              SBP_Input_Gussian_Noise['0.8'].mean(), SBP_Input_Gussian_Noise['1.0'].mean(), SBP_Input_Gussian_Noise['4.0'].mean(),
                              SBP_Input_Gussian_Noise['8.0'].mean()]

SBL_Input_Gussian_Noise_y1 = [SBL_Input_Gussian_Noise['No'].mean(), SBL_Input_Gussian_Noise['0.001'].mean(),SBL_Input_Gussian_Noise['0.004'].mean(),
                              SBL_Input_Gussian_Noise['0.008'].mean(), SBL_Input_Gussian_Noise['0.01'].mean(), SBL_Input_Gussian_Noise['0.04'].mean(),
                              SBL_Input_Gussian_Noise['0.08'].mean(), SBL_Input_Gussian_Noise['0.1'].mean(), SBL_Input_Gussian_Noise['0.4'].mean(),
                              SBL_Input_Gussian_Noise['0.8'].mean(), SBL_Input_Gussian_Noise['1.0'].mean(), SBL_Input_Gussian_Noise['4.0'].mean(),
                              SBL_Input_Gussian_Noise['8.0'].mean()]


CBP_Input_Gussian_Noise_Model1_y1 = [CBP_Input_Gussian_Noise_Model1['No'].mean(), CBP_Input_Gussian_Noise_Model1['0.001'].mean(), CBP_Input_Gussian_Noise_Model1['0.004'].mean(),
                                     CBP_Input_Gussian_Noise_Model1['0.008'].mean(), CBP_Input_Gussian_Noise_Model1['0.01'].mean(), CBP_Input_Gussian_Noise_Model1['0.04'].mean(),
                                     CBP_Input_Gussian_Noise_Model1['0.08'].mean(), CBP_Input_Gussian_Noise_Model1['0.1'].mean(), CBP_Input_Gussian_Noise_Model1['0.4'].mean(),
                                     CBP_Input_Gussian_Noise_Model1['0.8'].mean(), CBP_Input_Gussian_Noise_Model1['1.0'].mean(), CBP_Input_Gussian_Noise_Model1['4.0'].mean(),
                                     CBP_Input_Gussian_Noise_Model1['8.0'].mean()]

#CBP_Input_Gussian_Noise_Model2_y1 = [CBP_Input_Gussian_Noise_Model2['No'].mean(), CBP_Input_Gussian_Noise_Model2['0.001'].mean(), CBP_Input_Gussian_Noise_Model2['0.004'].mean(),
#                                     CBP_Input_Gussian_Noise_Model2['0.008'].mean(), CBP_Input_Gussian_Noise_Model2['0.01'].mean(), CBP_Input_Gussian_Noise_Model2['0.04'].mean(),
#                                     CBP_Input_Gussian_Noise_Model2['0.08'].mean(), CBP_Input_Gussian_Noise_Model2['0.1'].mean(), CBP_Input_Gussian_Noise_Model2['0.4'].mean(),
#                                     CBP_Input_Gussian_Noise_Model2['0.8'].mean(), CBP_Input_Gussian_Noise_Model2['1.0'].mean(), CBP_Input_Gussian_Noise_Model2['4.0'].mean(),
#                                     CBP_Input_Gussian_Noise_Model2['8.0'].mean()]

CBL_Input_Gussian_Noise_Model1_y1 = [CBL_Input_Gussian_Noise_Model1['No'].mean(), CBL_Input_Gussian_Noise_Model1['0.001'].mean(), CBL_Input_Gussian_Noise_Model1['0.004'].mean(),
                                     CBL_Input_Gussian_Noise_Model1['0.008'].mean(), CBL_Input_Gussian_Noise_Model1['0.01'].mean(), CBL_Input_Gussian_Noise_Model1['0.04'].mean(),
                                     CBL_Input_Gussian_Noise_Model1['0.08'].mean(), CBL_Input_Gussian_Noise_Model1['0.1'].mean(), CBL_Input_Gussian_Noise_Model1['0.4'].mean(),
                                     CBL_Input_Gussian_Noise_Model1['0.8'].mean(), CBL_Input_Gussian_Noise_Model1['1.0'].mean(), CBL_Input_Gussian_Noise_Model1['4.0'].mean(),
                                     CBL_Input_Gussian_Noise_Model1['8.0'].mean()]

#CBL_Input_Gussian_Noise_Model2_y1 = [CBL_Input_Gussian_Noise_Model2['No'].mean(), CBL_Input_Gussian_Noise_Model2['0.001'].mean(), CBL_Input_Gussian_Noise_Model2['0.004'].mean(),
#                                     CBL_Input_Gussian_Noise_Model2['0.008'].mean(), CBL_Input_Gussian_Noise_Model2['0.01'].mean(), CBL_Input_Gussian_Noise_Model2['0.04'].mean(),
#                                     CBL_Input_Gussian_Noise_Model2['0.08'].mean(), CBL_Input_Gussian_Noise_Model2['0.1'].mean(), CBL_Input_Gussian_Noise_Model2['0.4'].mean(),
#                                     CBL_Input_Gussian_Noise_Model2['0.8'].mean(), CBL_Input_Gussian_Noise_Model2['1.0'].mean(), CBL_Input_Gussian_Noise_Model2['4.0'].mean(),
#                                    CBL_Input_Gussian_Noise_Model2['8.0'].mean()]


#################################################################################################################
################################# Wieght Guassian Noise ########################################################
################################################################################################################


x_lesion=['No','0.001', '0.004', '0.008', '0.01', '0.04', '0.08', '0.1', '0.4', '0.8', '1.0', '4.0', '8.0']

SBP_Weight_Gussian_Noise_y1 = [SBP_Weight_Gussian_Noise['No'].mean(), SBP_Weight_Gussian_Noise['0.001'].mean(), SBP_Weight_Gussian_Noise['0.004'].mean(),
                               SBP_Weight_Gussian_Noise['0.008'].mean(), SBP_Weight_Gussian_Noise['0.01'].mean(), SBP_Weight_Gussian_Noise['0.04'].mean(),
                               SBP_Weight_Gussian_Noise['0.08'].mean(), SBP_Weight_Gussian_Noise['0.1'].mean(), SBP_Weight_Gussian_Noise['0.4'].mean(),
                               SBP_Weight_Gussian_Noise['0.8'].mean(), SBP_Weight_Gussian_Noise['1.0'].mean(), SBP_Weight_Gussian_Noise['4.0'].mean(),
                               SBP_Weight_Gussian_Noise['8.0'].mean()]

SBL_Weight_Gussian_Noise_y1 = [SBL_Weight_Gussian_Noise['No'].mean(), SBL_Weight_Gussian_Noise['0.001'].mean(), SBL_Weight_Gussian_Noise['0.004'].mean(),
                               SBL_Weight_Gussian_Noise['0.008'].mean(), SBL_Weight_Gussian_Noise['0.01'].mean(), SBL_Weight_Gussian_Noise['0.04'].mean(),
                               SBL_Weight_Gussian_Noise['0.08'].mean(), SBL_Weight_Gussian_Noise['0.1'].mean(), SBL_Weight_Gussian_Noise['0.4'].mean(),
                               SBL_Weight_Gussian_Noise['0.8'].mean(), SBL_Weight_Gussian_Noise['1.0'].mean(), SBL_Weight_Gussian_Noise['4.0'].mean(),
                               SBL_Weight_Gussian_Noise['8.0'].mean()]


CBP_Wieght_Gussian_Noise_Model1_y1 = [CBP_Wieght_Gussian_Noise_Model1['No'].mean(), CBP_Wieght_Gussian_Noise_Model1['0.001'].mean(), CBP_Wieght_Gussian_Noise_Model1['0.004'].mean(),
                                      CBP_Wieght_Gussian_Noise_Model1['0.008'].mean(), CBP_Wieght_Gussian_Noise_Model1['0.01'].mean(), CBP_Wieght_Gussian_Noise_Model1['0.04'].mean(),
                                      CBP_Wieght_Gussian_Noise_Model1['0.08'].mean(), CBP_Wieght_Gussian_Noise_Model1['0.1'].mean(), CBP_Wieght_Gussian_Noise_Model1['0.4'].mean(),
                                      CBP_Wieght_Gussian_Noise_Model1['0.8'].mean(), CBP_Wieght_Gussian_Noise_Model1['1.0'].mean(), CBP_Wieght_Gussian_Noise_Model1['4.0'].mean(),
                                      CBP_Wieght_Gussian_Noise_Model1['8.0'].mean()]

#CBP_Wieght_Gussian_Noise_Model2_y1 = [CBP_Wieght_Gussian_Noise_Model2['No'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.001'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.004'].mean(),
#                                      CBP_Wieght_Gussian_Noise_Model2['0.008'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.01'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.04'].mean(),
 #                                     CBP_Wieght_Gussian_Noise_Model2['0.08'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.1'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.4'].mean(),
 #                                     CBP_Wieght_Gussian_Noise_Model2['0.8'].mean(), CBP_Wieght_Gussian_Noise_Model2['1.0'].mean(), CBP_Wieght_Gussian_Noise_Model2['4.0'].mean(),
 #                                     CBP_Wieght_Gussian_Noise_Model2['8.0'].mean()]


CBL_Wieght_Gussian_Noise_Model1_y1 = [CBL_Wieght_Gussian_Noise_Model1['No'].mean(), CBL_Wieght_Gussian_Noise_Model1['0.001'].mean(), CBL_Wieght_Gussian_Noise_Model1['0.004'].mean(),
                                      CBL_Wieght_Gussian_Noise_Model1['0.008'].mean(), CBL_Wieght_Gussian_Noise_Model1['0.01'].mean(), CBL_Wieght_Gussian_Noise_Model1['0.04'].mean(),
                                      CBL_Wieght_Gussian_Noise_Model1['0.08'].mean(), CBL_Wieght_Gussian_Noise_Model1['0.1'].mean(), CBL_Wieght_Gussian_Noise_Model1['0.4'].mean(),
                                      CBL_Wieght_Gussian_Noise_Model1['0.8'].mean(), CBL_Wieght_Gussian_Noise_Model1['1.0'].mean(), CBL_Wieght_Gussian_Noise_Model1['4.0'].mean(),
                                      CBL_Wieght_Gussian_Noise_Model1['8.0'].mean()]

#CBL_Wieght_Gussian_Noise_Model2_y1 = [CBP_Wieght_Gussian_Noise_Model2['No'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.001'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.004'].mean(),
#                                      CBP_Wieght_Gussian_Noise_Model2['0.008'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.01'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.04'].mean(),
#                                      CBP_Wieght_Gussian_Noise_Model2['0.08'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.1'].mean(), CBP_Wieght_Gussian_Noise_Model2['0.4'].mean(),
#                                      CBP_Wieght_Gussian_Noise_Model2['0.8'].mean(), CBP_Wieght_Gussian_Noise_Model2['1.0'].mean(), CBP_Wieght_Gussian_Noise_Model2['4.0'].mean(),
#                                      CBP_Wieght_Gussian_Noise_Model2['8.0'].mean()]

###############################################################################################################
######################### Weight Drop ########################################################################
##############################################################################################################
x_lesion=['No','0.01','0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50', '0.55', '0.60']
                             
SBP_Weight_Drop_y1 = [SBP_Weight_Drop['No'].mean(), SBP_Weight_Drop['0.01'].mean(), SBP_Weight_Drop['0.05'].mean(),
                      SBP_Weight_Drop['0.10'].mean(), SBP_Weight_Drop['0.15'].mean(), SBP_Weight_Drop['0.20'].mean(),
                      SBP_Weight_Drop['0.25'].mean(), SBP_Weight_Drop['0.30'].mean(), SBP_Weight_Drop['0.35'].mean(),
                      SBP_Weight_Drop['0.40'].mean(), SBP_Weight_Drop['0.45'].mean(), SBP_Weight_Drop['0.50'].mean(),
                      SBP_Weight_Drop['0.55'].mean(), SBP_Weight_Drop['0.60'].mean()]
                             

SBL_Weight_Drop_y1 = [SBL_Weight_Drop['No'].mean(), SBL_Weight_Drop['0.01'].mean(), SBL_Weight_Drop['0.05'].mean(),
                      SBL_Weight_Drop['0.10'].mean(), SBL_Weight_Drop['0.15'].mean(), SBL_Weight_Drop['0.20'].mean(),
                      SBL_Weight_Drop['0.25'].mean(), SBL_Weight_Drop['0.30'].mean(), SBL_Weight_Drop['0.35'].mean(),
                      SBL_Weight_Drop['0.40'].mean(), SBL_Weight_Drop['0.45'].mean(), SBL_Weight_Drop['0.50'].mean(),
                      SBL_Weight_Drop['0.55'].mean(), SBL_Weight_Drop['0.60'].mean()]
                             

CBP_Wieght_Drop_Model1_y1 = [CBP_Wieght_Drop_Model1['No'].mean(), CBP_Wieght_Drop_Model1['0.01'].mean(), CBP_Wieght_Drop_Model1['0.05'].mean(),
                             CBP_Wieght_Drop_Model1['0.10'].mean(), CBP_Wieght_Drop_Model1['0.15'].mean(), CBP_Wieght_Drop_Model1['0.20'].mean(),
                             CBP_Wieght_Drop_Model1['0.25'].mean(), CBP_Wieght_Drop_Model1['0.30'].mean(), CBP_Wieght_Drop_Model1['0.35'].mean(),
                             CBP_Wieght_Drop_Model1['0.40'].mean(), CBP_Wieght_Drop_Model1['0.45'].mean(), CBP_Wieght_Drop_Model1['0.50'].mean(),
                             CBP_Wieght_Drop_Model1['0.55'].mean(), CBP_Wieght_Drop_Model1['0.60'].mean()]


CBP_Wieght_Drop_Model2_y1 = [CBP_Wieght_Drop_Model2['No'].mean(), CBP_Wieght_Drop_Model2['0.01'].mean(), CBP_Wieght_Drop_Model2['0.05'].mean(),
                             CBP_Wieght_Drop_Model2['0.10'].mean(), CBP_Wieght_Drop_Model2['0.15'].mean(), CBP_Wieght_Drop_Model2['0.20'].mean(),
                             CBP_Wieght_Drop_Model2['0.25'].mean(), CBP_Wieght_Drop_Model2['0.30'].mean(), CBP_Wieght_Drop_Model2['0.35'].mean(),
                             CBP_Wieght_Drop_Model2['0.40'].mean(), CBP_Wieght_Drop_Model2['0.45'].mean(), CBP_Wieght_Drop_Model2['0.50'].mean(),
                             CBP_Wieght_Drop_Model2['0.55'].mean(), CBP_Wieght_Drop_Model2['0.60'].mean()]

CBL_Wieght_Drop_Model1_y1 = [CBL_Wieght_Drop_Model1['No'].mean(), CBL_Wieght_Drop_Model1['0.01'].mean(), CBL_Wieght_Drop_Model1['0.05'].mean(),
                             CBL_Wieght_Drop_Model1['0.10'].mean(), CBL_Wieght_Drop_Model1['0.15'].mean(), CBL_Wieght_Drop_Model1['0.20'].mean(),
                             CBL_Wieght_Drop_Model1['0.25'].mean(), CBL_Wieght_Drop_Model1['0.30'].mean(), CBL_Wieght_Drop_Model1['0.35'].mean(),
                             CBL_Wieght_Drop_Model1['0.40'].mean(), CBL_Wieght_Drop_Model1['0.45'].mean(), CBL_Wieght_Drop_Model1['0.50'].mean(),
                             CBL_Wieght_Drop_Model1['0.55'].mean(), CBL_Wieght_Drop_Model1['0.60'].mean()]

CBL_Wieght_Drop_Model2_y1 = [CBL_Wieght_Drop_Model2['No'].mean(), CBL_Wieght_Drop_Model2['0.01'].mean(), CBL_Wieght_Drop_Model2['0.05'].mean(),
                             CBL_Wieght_Drop_Model2['0.10'].mean(), CBL_Wieght_Drop_Model2['0.15'].mean(), CBL_Wieght_Drop_Model2['0.20'].mean(),
                             CBL_Wieght_Drop_Model2['0.25'].mean(), CBL_Wieght_Drop_Model2['0.30'].mean(), CBL_Wieght_Drop_Model2['0.35'].mean(),
                             CBL_Wieght_Drop_Model2['0.40'].mean(), CBL_Wieght_Drop_Model2['0.45'].mean(), CBL_Wieght_Drop_Model2['0.50'].mean(),
                             CBL_Wieght_Drop_Model2['0.55'].mean(), CBL_Wieght_Drop_Model2['0.60'].mean()]



###################################################################################################################
###################################### ACC PLOT ###################################################################
################################################################################################################
x1=['Baseline', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9','E10',
    'E11', 'E12', 'E13', 'E14', 'E15', 'Test1']

plt.xticks(rotation=45) 

# SBL_ACC_y1
plt.plot(x1, SBL_ACC_y1, 's-', markersize=12, mec = 'k', label = "Stimulus Blocked Labeling", color='#95baf5')
plt.plot(x1, SBP_ACC_y1,  's-', markersize=12, label = "Stimulus Blocked No-Labeling", color='#95baf5')

plt.plot(x1, CBL_ACC_M1, 's-', markersize=12, mec = 'k', label = "Context Blocked Labeling", color='#f09797')

plt.plot(x1, CBP_ACC_M1, 's-',label = "Context Blocked No-Labeling", color='#f09797',markersize=12)

plt.xlabel('Epochs') 
plt.ylabel('Mean ACC')
plt.title("Simulation Mean Accuracy",fontsize=20)
plt.legend()
plt.yticks(np.arange(0.4, 1, 0.05))
plt.show()


###################################### Input Noise injection PLOT ###################################################################
################################################################################################################
x_lesion=['No','0.001', '0.004', '0.008', '0.01', '0.04', '0.08', '0.1', '0.4', '0.8', '1.0', '4.0', '8.0']

plt.xticks(rotation=45) 

# SBP_ACC_y1

# SBL_ACC_y1
plt.plot(x_lesion, SBL_Input_Gussian_Noise_y1, 'o-',label = "Stimulus Blocked Labeling", color='#95baf5',markersize=12)

plt.plot(x_lesion, SBP_Input_Gussian_Noise_y1, '*:', markersize=12, label = "Stimulus Blocked No-Labeling", color='#95baf5')

plt.plot(x_lesion, CBP_Input_Gussian_Noise_Model1_y1, 's-', markersize=12, mec = 'k', label = "Context Blocked Labeling Model1", color='#f09797')

plt.plot(x_lesion, CBP_Input_Gussian_Noise_Model2_y1, 's:', markersize=12, label = "Context Blocked Labeling Model2", color='#f09797')

plt.plot(x_lesion, CBL_Input_Gussian_Noise_Model1_y1, 'o-',label = "Context Blocked Planet Model1", color='#f09797',markersize=12)

plt.plot(x_lesion, CBL_Input_Gussian_Noise_Model2_y1, 'o-', markersize=12, mec = 'k',label = "Context Blocked Planet Model2",color='#f09797')
#plt.plot(x_axis, y5, 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Lesion') 
plt.ylabel('Mean ACC')
plt.title("Input Noise injection",fontsize=20)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


###################################### Weight Noise injection PLOT ###################################################################
################################################################################################################
x_lesion=['No','0.001', '0.004', '0.008', '0.01', '0.04', '0.08', '0.1', '0.4', '0.8', '1.0', '4.0', '8.0']

plt.xticks(rotation=45) 

#plt.plot(x_lesion, SBL_Weight_Gussian_Noise_y1, 's-',markersize=8, mec = 'k',label = "Stimulus Blocked Labeling", color='#95baf5')

#plt.plot(x_lesion, SBP_Weight_Gussian_Noise_y1, 's-', label = "Stimulus Blocked No-Labeling", color='#95baf5',markersize=8)

plt.plot(x_lesion, CBL_Wieght_Gussian_Noise_Model1_y1, 's-', markersize=8, mec = 'k', label = "Context Blocked Labeling", color='#f09797')

plt.plot(x_lesion, CBP_Wieght_Gussian_Noise_Model1_y1, 's-', label = "Context Blocked No-Labeling", color='#f09797', markersize=8)

plt.xlabel('Standard Deviation') 
plt.ylabel('Mean ACC')
plt.title("Parameters Noise Injection",fontsize=20)
plt.legend()
plt.yticks(np.arange(0.2, 1, 0.05))
plt.show()


###################################### Weight DROP PLOT ###################################################################
################################################################################################################
x_lesion=['No','0.01','0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50', '0.55', '0.60']
plt.xticks(rotation=45) 

# SBP_ACC_y1
plt.plot(x_lesion, SBP_Weight_Drop_y1, '*:', markersize=12, label = "Stimulus Blocked Planet", color='#95baf5')

# SBL_ACC_y1
plt.plot(x_lesion, SBL_Weight_Drop_y1, 'o-',label = "Stimulus Blocked Labeling", color='#95baf5',markersize=12)

plt.plot(x_lesion, CBL_Wieght_Drop_Model1_y1, 's-', markersize=12, mec = 'k', label = "Context Blocked Labeling Model1", color='#f09797')

plt.plot(x_lesion, CBL_Wieght_Drop_Model2_y1, 's:', markersize=12, label = "Context Blocked Labeling Model2", color='#f09797')

plt.plot(x_lesion, CBP_Wieght_Drop_Model1_y1, 'o-',label = "Context Blocked Planet Model1", color='#f09797',markersize=12)

plt.plot(x_lesion, CBP_Wieght_Drop_Model2_y1, 'o-', markersize=12, mec = 'k',label = "Context Blocked Planet Model2",color='#f09797')
#plt.plot(x_axis, y5, 's:',label = "Stimulus_Blocked_Planet",color='#f2ba41',markersize=12)
#plt.plot(x_axis, y6, 's:',label = "Context_Blocked_Task",color='#06a135',markersize=12)
plt.xlabel('Lesion') 
plt.ylabel('Mean ACC')
plt.title("Input Noise injection",fontsize=20)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()





























plt.style.use('seaborn')
from matplotlib.pyplot import figure
x_lesion=['No','0.01','0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50', '0.55', '0.60']
e = np.array(y2) #std
figure(figsize=(10, 10), dpi=80)
#plt.plot(x_lesion, y1, linestyle='--', marker='^', color='b', label='E15')

plt.errorbar(x_lesion, y1,e, linestyle='--', marker='^', color='b', label='E15')
plt.ylabel('Accuracy')
plt.xlabel('Lesion Percentage')
plt.legend(loc='upper right')
plt.ylim (0.1, 1.0)
plt.title('Context Blocked Labeling Model 1 Lesion\n (weight drop)',fontsize = 16 )
for x,y in zip(x_lesion,y1):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.show()

ecolor = 'lightgreen', elinewidth = 5, capsize=10



########################################################################################
########################## Ploting the first Run Model ####################################
#####################################################################################
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv

# Stimulus Blocked Planet

SBP_ACC = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Default_SBP_ACC_history.csv')

SBP_LOSS = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Default_SBP_LOSS_history.csv')

SBP_ACC_History = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Planet//Default_SBP_Model_History.csv')


 

# Stimulus Blocked Labeling
SBL_ACC = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Default_SBLabeling_ACC_history.csv')

SBL_LOSS = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Default_SBLabeling_LOSS_history.csv')

SBL_ACC_History = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Stimulus_Blocked_Labeling//Default_SBLabeling_Model_History.csv')

                           
# Context Blocked Planet Model1
CBP_ACC_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_1_ACC_history.csv')

CBP_LOSS_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_1_LOSS_history.csv')

CBP_ACC_History_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_1_History.csv')



# Context Blocked Planet Model2
'''
CBP_ACC_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_2_ACC_history.csv')

CBP_LOSS_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_2_LOSS_history.csv')

CBP_ACC_History_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Planet//Default_CBP_Model_2_History.csv')
'''


# Context Blocked Labeling Modle1
CBL_ACC_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_1_ACC_history.csv')

CBL_LOSS_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_1_LOSS_history.csv')

CBL_ACC_History_Model1 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_1_History.csv')


'''
# Context Blocked Labeling Model2
CBL_ACC_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_2_ACC_history.csv')

CBL_LOSS_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_2_LOSS_history.csv')


CBL_ACC_History_Model2 = pd.read_csv('D://OneDrive - UGent//Desktop//coursera//Udacity//ML with tensorflow//Neural Network//4. Deep learning with Tensorflow//Simulation_Results//Context_Blocked_Labeling//Default_CBL_Model_2_History.csv')
'''

###################################################################################
########################## Mean ACC #################################################
#################################################################################


SBP_ACC_y1 = [SBP_ACC_History['ACC_Before'].mean(), SBP_ACC['E1'].mean(),SBP_ACC['E2'].mean(), SBP_ACC['E3'].mean(),
              SBP_ACC['E4'].mean(),SBP_ACC['E5'].mean(), SBP_ACC['E6'].mean(),
              SBP_ACC['E7'].mean(),SBP_ACC['E8'].mean(), SBP_ACC['E9'].mean(),
              SBP_ACC['E10'].mean(),SBP_ACC['E11'].mean(), SBP_ACC['E12'].mean(),
              SBP_ACC['E13'].mean(),SBP_ACC['E14'].mean(), SBP_ACC['E15'].mean(), SBP_ACC_History['ACC_After'].mean()]


SBL_ACC_y1 = [SBL_ACC_History['ACC_Before'].mean(), SBL_ACC['E1'].mean(), SBL_ACC['E2'].mean(), SBL_ACC['E3'].mean(),
              SBL_ACC['E4'].mean(), SBL_ACC['E5'].mean(), SBL_ACC['E6'].mean(),
              SBL_ACC['E7'].mean(), SBL_ACC['E8'].mean(), SBL_ACC['E9'].mean(),
              SBL_ACC['E10'].mean(), SBL_ACC['E11'].mean(), SBL_ACC['E12'].mean(),
              SBL_ACC['E13'].mean(), SBL_ACC['E14'].mean(), SBL_ACC['E15'].mean(), SBL_ACC_History['ACC_After'].mean()]

CBL_ACC_M1 = [CBL_ACC_History_Model1['ACC_Before'].mean(), CBL_ACC_Model1['E1'].mean(), CBL_ACC_Model1['E2'].mean(), CBL_ACC_Model1['E3'].mean(),
              CBL_ACC_Model1['E4'].mean(), CBL_ACC_Model1['E5'].mean(), CBL_ACC_Model1['E6'].mean(),
              CBL_ACC_Model1['E7'].mean(), CBL_ACC_Model1['E8'].mean(), CBL_ACC_Model1['E9'].mean(),
              CBL_ACC_Model1['E10'].mean(), CBL_ACC_Model1['E11'].mean(), CBL_ACC_Model1['E12'].mean(),
              CBL_ACC_Model1['E13'].mean(), CBL_ACC_Model1['E14'].mean(), CBL_ACC_Model1['E15'].mean(), CBL_ACC_History_Model1['ACC_After'].mean()]

#CBL_ACC_M2 = [CBL_ACC_History_Model2['ACC_Before'].mean(), CBL_ACC_Model2['E1'].mean(), CBL_ACC_Model2['E2'].mean(), CBL_ACC_Model2['E3'].mean(),
#              CBL_ACC_Model2['E4'].mean(), CBL_ACC_Model2['E5'].mean(), CBL_ACC_Model2['E6'].mean(),
#              CBL_ACC_Model2['E7'].mean(), CBL_ACC_Model2['E8'].mean(), CBL_ACC_Model2['E9'].mean(),
#              CBL_ACC_Model2['E10'].mean(), CBL_ACC_Model2['E11'].mean(), CBL_ACC_Model2['E12'].mean(),
#              CBL_ACC_Model2['E13'].mean(), CBL_ACC_Model2['E14'].mean(), CBL_ACC_Model2['E15'].mean(), CBL_ACC_History_Model2['ACC_After'].mean()]


CBP_ACC_M1 = [CBP_ACC_History_Model1['ACC_Before'].mean(), CBP_ACC_Model1['E1'].mean(), CBP_ACC_Model1['E2'].mean(), CBP_ACC_Model1['E3'].mean(),
              CBP_ACC_Model1['E4'].mean(), CBP_ACC_Model1['E5'].mean(), CBP_ACC_Model1['E6'].mean(),
              CBP_ACC_Model1['E7'].mean(), CBP_ACC_Model1['E8'].mean(), CBP_ACC_Model1['E9'].mean(),
              CBP_ACC_Model1['E10'].mean(), CBP_ACC_Model1['E11'].mean(), CBP_ACC_Model1['E12'].mean(),
              CBP_ACC_Model1['E13'].mean(), CBP_ACC_Model1['E14'].mean(), CBP_ACC_Model1['E15'].mean(), CBP_ACC_History_Model1['ACC_After'].mean()]
    
#CBP_ACC_M2 = [CBP_ACC_History_Model2['ACC_Before'].mean(), CBP_ACC_Model2['E1'].mean(), CBP_ACC_Model2['E2'].mean(), CBP_ACC_Model2['E3'].mean(),
#              CBP_ACC_Model2['E4'].mean(), CBP_ACC_Model2['E5'].mean(), CBP_ACC_Model2['E6'].mean(),
#              CBP_ACC_Model2['E7'].mean(), CBP_ACC_Model2['E8'].mean(), CBP_ACC_Model2['E9'].mean(),
#              CBP_ACC_Model2['E10'].mean(), CBP_ACC_Model2['E11'].mean(), CBP_ACC_Model2['E12'].mean(),
#             CBP_ACC_Model2['E13'].mean(), CBP_ACC_Model2['E14'].mean(), CBP_ACC_Model2['E15'].mean(), CBP_ACC_History_Model2['ACC_After'].mean()]
    

##############################################################################################
####################### Standard Error #######################################################
##############################################################################################



SBP_ACC_e = [SBP_ACC_History['ACC_Before'].sem(), 
              SBP_ACC['E1'].sem(), SBP_ACC['E2'].sem(), SBP_ACC['E3'].sem(),
              SBP_ACC['E4'].sem(), SBP_ACC['E5'].sem(), SBP_ACC['E6'].sem(),
              SBP_ACC['E7'].sem(), SBP_ACC['E8'].sem(), SBP_ACC['E9'].sem(),
              SBP_ACC['E10'].sem(), SBP_ACC['E11'].sem(), SBP_ACC['E12'].sem(),
              SBP_ACC['E13'].sem(), SBP_ACC['E14'].sem(), SBP_ACC['E15'].sem(), 
              SBP_ACC_History['ACC_After'].sem()]


SBL_ACC_e = [SBL_ACC_History['ACC_Before'].sem(),
             SBL_ACC['E1'].sem(), SBL_ACC['E2'].sem(), SBL_ACC['E3'].sem(),
              SBL_ACC['E4'].sem(), SBL_ACC['E5'].sem(), SBL_ACC['E6'].sem(),
              SBL_ACC['E7'].sem(), SBL_ACC['E8'].sem(), SBL_ACC['E9'].sem(),
              SBL_ACC['E10'].sem(), SBL_ACC['E11'].sem(), SBL_ACC['E12'].sem(),
              SBL_ACC['E13'].sem(), SBL_ACC['E14'].sem(), SBL_ACC['E15'].sem(), 
              SBL_ACC_History['ACC_After'].sem()]

CBL_ACC_M1_e = [CBL_ACC_History_Model1['ACC_Before'].sem(),
                CBL_ACC_Model1['E1'].sem(), CBL_ACC_Model1['E2'].sem(), CBL_ACC_Model1['E3'].sem(),
                CBL_ACC_Model1['E4'].sem(), CBL_ACC_Model1['E5'].sem(), CBL_ACC_Model1['E6'].sem(),
                CBL_ACC_Model1['E7'].sem(), CBL_ACC_Model1['E8'].sem(), CBL_ACC_Model1['E9'].sem(),
                CBL_ACC_Model1['E10'].sem(), CBL_ACC_Model1['E11'].sem(), CBL_ACC_Model1['E12'].sem(),
                CBL_ACC_Model1['E13'].sem(), CBL_ACC_Model1['E14'].sem(), CBL_ACC_Model1['E15'].sem(), CBL_ACC_History_Model1['ACC_After'].sem()]

#CBL_ACC_M2_e = [CBL_ACC_History_Model2['ACC_Before'].mean(), CBL_ACC_Model2['E1'].mean(), CBL_ACC_Model2['E2'].mean(), CBL_ACC_Model2['E3'].mean(),
#              CBL_ACC_Model2['E4'].mean(), CBL_ACC_Model2['E5'].mean(), CBL_ACC_Model2['E6'].mean(),
#              CBL_ACC_Model2['E7'].mean(), CBL_ACC_Model2['E8'].mean(), CBL_ACC_Model2['E9'].mean(),
#              CBL_ACC_Model2['E10'].mean(), CBL_ACC_Model2['E11'].mean(), CBL_ACC_Model2['E12'].mean(),
#              CBL_ACC_Model2['E13'].mean(), CBL_ACC_Model2['E14'].mean(), CBL_ACC_Model2['E15'].mean(), CBL_ACC_History_Model2['ACC_After'].mean()]


CBP_ACC_M1_e = [CBP_ACC_History_Model1['ACC_Before'].sem(), CBP_ACC_Model1['E1'].sem(), CBP_ACC_Model1['E2'].sem(),
                CBP_ACC_Model1['E3'].sem(), CBP_ACC_Model1['E4'].sem(), CBP_ACC_Model1['E5'].sem(), CBP_ACC_Model1['E6'].sem(),
                CBP_ACC_Model1['E7'].sem(), CBP_ACC_Model1['E8'].sem(), CBP_ACC_Model1['E9'].sem(),
                CBP_ACC_Model1['E10'].sem(), CBP_ACC_Model1['E11'].sem(), CBP_ACC_Model1['E12'].sem(),
                CBP_ACC_Model1['E13'].sem(), CBP_ACC_Model1['E14'].sem(), CBP_ACC_Model1['E15'].sem(), 
                CBP_ACC_History_Model1['ACC_After'].sem()]
    
#CBP_ACC_M2_e = [CBP_ACC_History_Model2['ACC_Before'].mean(), CBP_ACC_Model2['E1'].mean(), CBP_ACC_Model2['E2'].mean(), CBP_ACC_Model2['E3'].mean(),
#              CBP_ACC_Model2['E4'].mean(), CBP_ACC_Model2['E5'].mean(), CBP_ACC_Model2['E6'].mean(),
#              CBP_ACC_Model2['E7'].mean(), CBP_ACC_Model2['E8'].mean(), CBP_ACC_Model2['E9'].mean(),
#              CBP_ACC_Model2['E10'].mean(), CBP_ACC_Model2['E11'].mean(), CBP_ACC_Model2['E12'].mean(),
#             CBP_ACC_Model2['E13'].mean(), CBP_ACC_Model2['E14'].mean(), CBP_ACC_Model2['E15'].mean(), CBP_ACC_History_Model2['ACC_After'].mean()]
    

#######################################################################################################
x1=['Base', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9','E10',
    'E11', 'E12', 'E13', 'E14', 'E15', 'Test1']

plt.figure(figsize=(10, 6))

plt.figure(dpi=1200)
plt.xticks(rotation=45) 

# SBL_ACC_y1
plt.errorbar(x1, SBL_ACC_y1, yerr = SBL_ACC_e, ecolor = 'k', capsize=10, marker='s', linestyle='-',markersize=8, mec = 'k', label = "Stimulus First Labeling", color='#95baf5')
plt.errorbar(x1, SBP_ACC_y1, yerr =  SBP_ACC_e , ecolor = 'k', capsize=10, marker='s',linestyle=':', markersize=8, label = "Stimulus First No_Labeling", color='#95baf5')

plt.errorbar(x1, CBL_ACC_M1, yerr = CBL_ACC_M1_e, ecolor = 'k', capsize=10, marker='s', linestyle='-',markersize=8, mec = 'k', label = "Context First Labeling", color='#f09797')

plt.errorbar(x1, CBP_ACC_M1, yerr = CBP_ACC_M1_e, ecolor = 'k', capsize=10, marker='s',linestyle=':',label = "Context First No_Labeling", color='#f09797',markersize=8)

plt.xlabel('Epochs') 
plt.ylabel('Mean ACC')
plt.title("Simulation Mean Accuracy",fontsize=20)
plt.legend()
plt.yticks(np.arange(0.45, 1.05, 0.05))
plt.show()
