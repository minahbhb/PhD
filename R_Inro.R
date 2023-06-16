# if you want to see how a command work:
# you have two options using help or ? mark

# restarting Rstadio:
.rs.restartR()

help(read.csv)
? read.csv

# I want to read a file


# we have three option: 
# 1) import data 
# 2) use read.csv(path the file)
# 3) use read.csv(file.choose()) this lets us to brows and choose our file
# example
CBP_Day1=read.csv(file.choose(), header=TRUE)

# we can import the same file as table
CBP_Day1_Data2=read.table(file.choose(), header=TRUE, sep=",")

# when I want to extract a variable from an object I should use $
# in the example below I want to extract Age from CBP_Day1
CBP_Day1$Age

# also I can compute the mean of specific varibale with this 
mean(CBP_Day1$Age)

# Also we can use attach instead of using $ and this command keep the data in R memory
# for example we want to use attach CBP_Day1
attach(CBP_Day1_Data2)

###################################
# we can see type of the varibale and level of variable with the below commands

class(CBP_Day1_Data2$version)
# output "integer"


levels(CBP_Day1_Data2$gender)
# output "female" "male"   "other" 

# we can see the summary of our data:
summary(CBP_Day1_Data2)

# what if we have some data like categorical data 0 and 1
# consider the x include 0 and 1
x =c(1,1,1,0,0,0,1,0,1,0,1)

# when I ask for the class of x and summary. R consider x as numerical not categorical
class(x)
# > class(x)
#[1] "numeric"

summary(x)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#0.0000  0.0000  1.0000  0.5455  1.0000  1.0000 
#

# bit I want to change x in a way that it is categorical
x=as.factor(x)

# now show class and summary
class(x)
# > class(x)
#[1] "factor"

summary(x)

#0 1 
#5 6

# Subseting like list in python
mean(CBP_Day1_Data2$Age[gender=="male"])

# we can make new variable like only male with the age older than 27
male= CBP_Day1_Data2[CBP_Day1_Data2$gender=="male" & CBP_Day1_Data2$Age >27, ]


