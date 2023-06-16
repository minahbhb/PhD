##############################################################################################################
######################## Scatter plot to see if we can see any RT and ACC trade off ##########################
###############################################################################################################

bar graph all 4 groups toghether scatter plot of rt with acc to see trad of between rt and acc
for mean bar graph :
    one for 123
    one for 456
    one for 789
    one for 101112
    
    
ACC Criteria
Payment Criteria


axs[0].set_title('Block1')

axs[0, 0, 1].plot(x, y, 'tab:orange')
axs[0, 0, 1].set_title('Axis [0, 1]')

axs[0, 1, 0].plot(x, -y, 'tab:green')
axs[0, 1, 0].set_title('Axis [1, 0]')

axs[0, 1, 1].plot(x, -y, 'tab:green')
axs[0, 1, 1].set_title('Axis [1, 0]')

axs[1, 0, 0].plot(x, -y, 'tab:green')
axs[1, 0, 0].set_title('Axis [1, 0]')

axs[1, 0, 1].plot(x, -y, 'tab:green')
axs[1, 0, 1].set_title('Axis [1, 0]')

axs[1, 1, 1].plot(x, -y, 'tab:red')
axs[1, 1, 1].set_title('Axis [1, 1]')
# draw jointplot with
# scatter kind
sns.jointplot(x = "ACC_block_6", y = "RT_block_6",
              kind = "scatter", data = df_whole_train)
# show the plot
plt.show()    

fig, axs = plt.subplots(2, 2)


for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()