# First I want to see if I have outelier in each column of ACC for all Blocked groups:
# Clear Console ctr+l

# delete variables rm(variable name)
# delete all variables rm(list=ls()) 

########################################################################################
################################ DAY1 ##################################################
########################################################################################



########################################################################################
##################### Context Blocked Planet Day1 ACC from 456 criteria ################
########################################################################################

# read csv files
CBP_Day1 = read.csv(file.choose(), header=TRUE)

boxplot(CBP_Day1$ACC_block_1,CBP_Day1$ACC_block_2,CBP_Day1$ACC_block_3,CBP_Day1$ACC_block_4,
        CBP_Day1$ACC_block_5,CBP_Day1$ACC_block_6,names=c("1","2","3","4","5","6"),
        main="Context_Blocked_Planet Training DAY1 Only",
        ylim=c(0,1), ylab="Accuracy", xlab= "Blocks")

# we can have stat from Boxplot to show us if we have outliere
boxplot.stats(CBP_Day1$ACC_block_1)$out

CBP_accuracy_list=list(CBP_Day1$ACC_block_1,CBP_Day1$ACC_block_2,CBP_Day1$ACC_block_3,
                       CBP_Day1$ACC_block_4,CBP_Day1$ACC_block_5,CBP_Day1$ACC_block_6)

# also we can extract which variables are outlier
CBP_Outlier=list()
for (acc in CBP_accuracy_list)

  out = boxplot.stats(acc)$out
  print(out)
  CBP_Outlier= append(CBP_Outlier,out)
  
# show who was outlier in this block 
out_ind = which(CBP_Day1$ACC_block_1 %in% c(out))
out_ind
CBP_Day1$out_ind

# even we can show which data was outlier on the plot 
boxplot(dat$hwy,
        ylab = "hwy",
        main = "Boxplot of highway miles per gallon"
)
mtext(paste("Outliers: ", paste(out, collapse = ", ")))



##############################################################################################
################### Context Blocked Labeling Day1 ACC from 456 criteria ######################
##############################################################################################

CBL_Day1 = read.csv(file.choose(), header=TRUE)

boxplot(CBL_Day1$ACC_block_1,CBL_Day1$ACC_block_2,CBL_Day1$ACC_block_3,CBL_Day1$ACC_block_4,
        CBL_Day1$ACC_block_5,CBL_Day1$ACC_block_6,names=c("1","2","3","4","5","6"),
        main="Context_Blocked_Labeling Training DAY1 Only",
        ylim=c(0,1), ylab="Accuracy", xlab= "Blocks")


##############################################################################################
################### Stimulus Blocked Labeling Day1 ACC from 456 criteria ######################
##############################################################################################

SBL_Day1 = read.csv(file.choose(), header=TRUE)

boxplot(SBL_Day1$ACC_block_1,SBL_Day1$ACC_block_2,SBL_Day1$ACC_block_3,SBL_Day1$ACC_block_4,
        SBL_Day1$ACC_block_5,SBL_Day1$ACC_block_6,names=c("1","2","3","4","5","6"),
        main="Stimulus_Blocked_Labeling Training DAY1 Only",
        ylim=c(0,1), ylab="Accuracy", xlab= "Blocks")


##############################################################################################
################### Stimulus Blocked Planet Day1 ACC from 456 criteria ######################
##############################################################################################

SBP_Day1 = read.csv(file.choose(), header=TRUE)

boxplot(SBP_Day1$ACC_block_1,SBP_Day1$ACC_block_2,SBP_Day1$ACC_block_3,SBP_Day1$ACC_block_4,
        SBP_Day1$ACC_block_5,SBP_Day1$ACC_block_6,names=c("1","2","3","4","5","6"),
        main="Stimulus_Blocked_Planet Training DAY1 Only",
        ylim=c(0,1), ylab="Accuracy", xlab= "Blocks")


#############################################################################
####################### Save ALL the Plot ##################################
###########################################################################

plots.dir.path <- list.files(tempdir(), pattern="rs-graphics", full.names = TRUE); 
plots.png.paths <- list.files(plots.dir.path, pattern=".png", full.names = TRUE)

file.copy(from=plots.png.paths, to="D:/OneDrive - UGent/Desktop/Mina/Behaviral_Analysis")


###################################################################################
###################################################################################
############################## Mixed ANOVA #######################################

# 1. comparing the mean acc of block 4, 5 and 6 with the mean acc of block 7,8,9

# Cimpute the mean of block 4, 5, 6 for CBP
CBP_Mean_456=mean(mean(CBP_Day1$ACC_block_4),mean(CBP_Day1$ACC_block_5),mean(CBP_Day1$ACC_block_6 ))

# Cimpute the mean of block 7, 8, 9 for CBP
CBP_Mean_789=mean(mean(CBP_Day1$ACC_block_7),mean(CBP_Day1$ACC_block_8),mean(CBP_Day1$ACC_block_9))

# Compute the mean of block 4, 5, 6 for CBL
CBL_Mean_456=mean(mean(CBL_Day1$ACC_block_4),mean(CBL_Day1$ACC_block_5),mean(CBL_Day1$ACC_block_6 ))

# Compute the mean of block 7, 8, 9 for CBP
CBL_Mean_789=mean(mean(CBL_Day1$ACC_block_7),mean(CBL_Day1$ACC_block_8),mean(CBL_Day1$ACC_block_9))

# Compute the mean of block 4, 5, 6 for CBL
SBL_Mean_456=mean(mean(SBL_Day1$ACC_block_4),mean(SBL_Day1$ACC_block_5),mean(SBL_Day1$ACC_block_6 ))

# Compute the mean of block 7, 8, 9 for CBP
SBL_Mean_789=mean(mean(SBL_Day1$ACC_block_7),mean(SBL_Day1$ACC_block_8),mean(SBL_Day1$ACC_block_9))

# Compute the mean of block 4, 5, 6 for CBL
SBP_Mean_456=mean(mean(SBP_Day1$ACC_block_4),mean(SBP_Day1$ACC_block_5),mean(SBP_Day1$ACC_block_6 ))

# Compute the mean of block 7, 8, 9 for CBP
SBP_Mean_789=mean(mean(SBP_Day1$ACC_block_7),mean(SBP_Day1$ACC_block_8),mean(SBP_Day1$ACC_block_9))

# CBP has more collumns than Others
CBP_Day1 = CBP_Day1[,1:34]

# now I want to combine my table vertically
Total_Table=rbind(CBP_Day1, CBL_Day1, SBP_Day1, SBL_Day1)

# lets drop collumns that we do not need
names(Total_Table)

# this table of Total_Table_New has Groups and accuracy of blocks from block 1 to block 9
Total_Table_New = Total_Table[, c(1:2, 17:25)]

# Now I want to add two columns to my data frame "Total_Table_New"
# from collumn (mean of block4,5,6) and collumn(mean 7,8,9)

# Add a collumn to Total_Table_New that compute the mean of ACC_4, ACC_5, ACC_6
Total_Table_New$mean_456 = apply(Total_Table_New[,5:7],1,mean)

# Add a collumn to Total_Table_New that compute the mean of ACC_7, ACC_8, ACC_9
Total_Table_New$mean_789 = apply(Total_Table_New[,8:10],1,mean)

library(tidyverse)
library(ggpubr)
library(rstatix)



# see the data 
head(Total_Table_New)
# drop Extra Collumn
Total_Table_New_drop=Total_Table_New[ -c(3:11) ]

# we have wide format which means we have one row for each person in R we need to have long 
# format which means have one observation in each row
# LONG Format
Long_Table <- Total_Table_New_drop %>%
  gather(key = "time", value = "Accuracy", mean_456,mean_789) %>%
  convert_as_factor(prolificID, time)


Long_Table %>% sample_n_by(Group, time, size = 1)

head(Long_Table)
########################################################################
#################### Summary #########################################
#########################################################################
Long_Table %>%
  group_by(time, Group) %>%
  get_summary_stats(Accuracy, type = "mean_sd")

##################
# Visualization 
bxp <- ggboxplot(
  Long_Table, x = "time", y = "Accuracy",
  color = "Group", palette = "jco"
)
bxp

#####################################################
################### Finding Outlier #################
######################################################

Long_Table %>%
  group_by(time, Group) %>%
  identify_outliers(Accuracy)


###############################################################################
###############################################################################
####################### Normality assumption ###################################

# The normality assumption can be checked by computing Shapiro-Wilk test for
# each combinations of factor levels. If the data is normally distributed, 
# the p-value should be greater than 0.05.

Long_Table %>%
  group_by(time, Group) %>%
  shapiro_test(Accuracy)

# My data is not normally distributed I should go for Robust ANOVA

summary(Long_Table)

######################################################################################
################### QQPLOT ###########################################################
######################################################################################
# Note that, if your sample size is greater than 50, the normal QQ plot is preferred
# because at larger sample sizes the Shapiro-Wilk test becomes very sensitive even to
# a minor deviation from normality.

# QQ plot draws the correlation between a given data and the normal distribution.

ggqqplot(Long_Table, "Accuracy", ggtheme = theme_bw()) +
  facet_grid(time ~ Group)


######################################################################################
############################## Homogenity of Variance ################################
######################################################################################
# Homogneity of variance assumption
# The homogeneity of variance assumption of the between-subject factor (group) can
# be checked using the Levene’s test. The test is performed at each level of time variable:
  
Long_Table %>%
  group_by(time) %>%
  levene_test(Accuracy ~ Group)

# There was homogeneity of variances, as assessed by Levene’s test (p > 0.05).

######################################################################################
#######################Homogenity of CoVariance #################################
#####################################################################################
 #Homogeneity of covariances assumption
# The homogeneity of covariances of the between-subject factor (group) can be 
# evaluated using the Box’s M-test implemented in the rstatix package. 
# If this test is statistically significant (i.e., p < 0.001), you do not have equal 
# covariances, but if the test is not statistically significant (i.e., p > 0.001), 
# you have equal covariances and you have not violated the assumption of homogeneity 
# of covariances.

#Note that, the Box’s M is highly sensitive, so unless p < 0.001 and your 
#sample sizes are unequal, ignore it. However, if significant and you have unequal 
#sample sizes, the test is not robust 
# (https://en.wikiversity.org/wiki/Box%27s_M, Tabachnick & Fidell, 2001).

# Compute Box’s M-test:

box_m(Long_Table[, "Accuracy", drop = FALSE], Long_Table$Group)

##############################################################################################
#############################################################################################
######################### Assumption of sphericity ###########################################

# As mentioned in previous sections, the assumption of sphericity will be automatically
# checked during the computation of the ANOVA test using the R function 
# anova_test() [rstatix package]. 
# The Mauchly’s test is internally used to assess the sphericity assumption.

# By using the function get_anova_table() [rstatix] to extract the ANOVA table, 
# the Greenhouse-Geisser sphericity correction is automatically applied to factors
# violating the sphericity assumption.


# Two-way mixed ANOVA test
res.aov <- anova_test(
  data = Long_Table, dv = Accuracy, wid = id,
  between = group, within = time
)
get_anova_table(res.aov)

Computation