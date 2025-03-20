## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Answer: There is a possibility that the device encountered a program error or lost the heartbeat signal during that time, which leads to incomplete data. Those missing data might be happen in some specie condition. The risk of incomplete data is that the margin of error in the dataset will increase, and it may become skewed. This could result in analysis will be misrepresent the true variability of the data.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

Answer: Based on the visualizations and the data set, we can observe that the middle part of the first half of the data, ranging from the 13th to the 25th data points, has a maximum heart rate of 67, and the heart rate remains at a relatively low level overall. Thus, we can conclude that there is a possibility that this range (13th to 25th) corresponds to the sleep phase.

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings.

Answer: Based on the data, the average heart rate is 64.59, the maximum is 93, and the standard deviation is 8.53. Since heart rate usually increase during exercise, we can concluded that heart rate 93 can be corresponds to the exercise time. Also, 93 is more then 3 standard deviation higher than the average 64.59, it can be considered an outlier in the dataset, there is a possibility because of exercise. In addition, the visualizations also show that 93 is located on the very top in the graph.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Answer: Based on the visualizations and data set, we can observe that the middle part of the second half of the data, ranging from 40th to 60th, that's the phases that average(60) heart rate contains in relatively lower level. Also, the heart rate values show greater variation compared to other phases, such as heart rate from 45th to 46th, 50th to 51. Thus, we can conclude that there is a possibility that this range (40th to 60th) corresponds to the regular periods of awake activity phases.
