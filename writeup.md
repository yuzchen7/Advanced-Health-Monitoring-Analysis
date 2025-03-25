## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Answer: There is a possibility that the device encountered a program error or lost the heartbeat signal during that time, which leads to incomplete data. Those missing data might be happen in some specie condition. The risk of incomplete data is that the margin of error in the dataset will increase, and it may become skewed. This could result in analysis will be misrepresent the true variability of the data.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

Answer: Based on the data set, phase 0 could be the sleep occur. The maximum heart rate of phase 0 is 93, which is the lowest maximum value among with other 4 phases. Also, the average heart rate in phase 0 is 64.59, which means that the heart rate remains consistently low level in this phase. Thus, we can conclude that phase 0 is corresponds to the sleep phase.

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings.

Answer: Based on the data set, phase 2 could be the exercise period. The maximum heart rate in phase 2 data set is 117, that is much higher then phase 1 with 110, phase 3 with 99, and phase 0 with 93. Thus, we can conclude that phase 2 is corresponds to the exercise phase.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Answer: Based on the data set, phase 3 could be the awake activity time period. The average of the phase 3 is 60.65, which is the lowest average of all other phases. The standard deviation is 11.0, even though that is not the highest standard deviation among all 4 phases, it is relatively large compared to the others. Thus, we can conclude that phase 3 is corresponds to the awake activity phase.
