# Crime-Data-Analysis
## Project Summary

## Code Setup

## Code Overview
### 1.Loading dataset and data exploration

### 2.Victim Demographic Analysis
The Victim Demographic Analysis examines how crimes impact individuals based on their sex, descent, and age. It explores the distribution of victims by gender and ethnicity, while also analyzing age differences within these groups. This provides key insights into which demographics are most affected by crime, helping identify patterns and potential vulnerabilities.

#### The questions we are trying to answer in this section
What is the distribution of crimes based on victim sex?

What is the distribution of crimes based on victim descent?

How does the age of victims differ by sex?

How does the age of victims differ by descent?
#### The code
What is the distribution of crimes based on victim sex?

The distribution of crimes based on victim sex shows that the majority of victims are male (M) with 395,620 instances, followed closely by female (F) victims, with 351,884 instances. There are also 93,814 victims categorized as X (unknown or not specified). Additionally, 111 victims are listed as H, and there is 1 instance where the victim's sex is unknown or recorded as -. This suggests that both males and females are significantly impacted by crime, with a slightly higher number of male victims

![image](https://github.com/user-attachments/assets/4151761e-4064-4969-a000-c673dcecfea8)

What is the distribution of crimes based on victim descent?

The distribution of crimes based on victim descent reveals that the highest number of victims belong to the H (Hispanic) category, with 291,865 instances. This is followed by W (White) victims, totaling 196,427, and B (Black) victims, with 133,904 instances. The X category, which likely represents unknown or unspecified descent, includes 102,563 victims. Other descent categories include O (Other) with 76,477, A (Asian) with 20,987, and smaller counts for K (Korean), F (Filipino), C (Chinese), J (Japanese), V (Vietnamese), I (Indian), Z, P, U, D, G, L, and S. There are also 2 instances where the victim's descent is not specified. This data indicates a significant representation of Hispanic and White victims in the crime dataset, with a notable number of victims from various other descent backgrounds.

![image](https://github.com/user-attachments/assets/6cea4f8e-464e-492f-8e80-33cfc5b5c8ab)

How does the age of victims differ by sex?

The code begins by cleaning the crime_df DataFrame to remove any rows where the Vict Sex or Vict Descent columns contain the values '-' or 'X'. This filtered DataFrame is stored in boxcrime_df, ensuring that only relevant data is used for analysis. Subsequently, a box plot is generated to visualize the distribution of victim ages by sex.The box plot analysis of victim ages by sex shows that male victims tend to have a median age between 37-39 years, with an interquartile range (IQR) from 28 to 50 years. Males exhibit a minimum age slightly below 0 and a maximum age in the mid-80s, along with numerous outliers above this range. In contrast, female victims have a median age slightly lower, around 36-38 years, with an IQR from 28 to 48 years. Their age distribution similarly shows a minimum of 0 and a maximum of 80, accompanied by several outliers above 80 years. Overall, while both male and female victim ages overlap considerably, males show a wider age range and a higher maximum age, indicating diverse demographics among victims.

![image](https://github.com/user-attachments/assets/ff5f2608-12e1-4ad8-a3ee-539552fafc31)


How does the age of victims differ by descent?

The boxplot analysis reveals that the median ages of victims across different descent groups are generally similar, clustered in the 30s. However, notable variations exist: the Chinese descent group exhibits the lowest median age, while the Japanese group has the highest. The interquartile ranges (IQRs) also differ significantly, with Japanese, White, Asian, and Other descent groups displaying the largest ranges, indicating greater age variability. Conversely, the Desi group has the narrowest IQR. In terms of maximum ages, both the White and Japanese groups reach into the 90s, while the Desi group has the lowest maximum age. Most descent groups have minimum ages around zero, but the Vietnamese, Middle Eastern, Guamanian, Desi, and Latino groups show minimum ages in the teens or twenties. This suggests that these populations may experience a higher incidence of victimization among older individuals, while the presence of younger victims is more common in the other descent groups.

Overall, these findings highlight the importance of understanding demographic nuances in crime data. The varying patterns of victimization among descent groups may reflect differing social, economic, or cultural factors, which can be critical for informing targeted prevention and intervention strategies. Addressing the specific needs of each group could enhance the effectiveness of crime reduction efforts.

![image](https://github.com/user-attachments/assets/9c300b99-ee9c-475d-8804-70cbaa225407)



### 3.Temporal Analysis
The Temporal Analysis of Crime Data examines how crimes vary over time, providing insights into trends and patterns based on different time factors such as years, months, days, or even times of the day. This analysis helps to identify whether there are any increases or decreases in crime rates over certain periods, detect seasonal patterns, or find peak times when crimes are most likely to occur. By studying these temporal aspects, law enforcement and policymakers can better understand when crimes are most prevalent, allowing them to allocate resources more effectively and develop strategies to mitigate crime at specific times.

#### The questions we are trying to answer in this section
How has the number of reported crimes changed over the years?

Are there any seasonal patterns in crime occurrence based on months?

What time of day do crimes most frequently occur?

#### The Code

How has the number of reported crimes changed over the years?

The code provided analyzes crime data by first converting the relevant date columns to a datetime format, allowing for accurate date manipulations. It then counts the number of reported crimes for each year based on the Date Rptd column, sorting the results to reveal trends over time. The plotted line graph illustrates that reported crimes increased from approximately 190,000 in 2020 to around 230,000 in 2022, indicating a significant rise. In 2023, the number remains stable at about 230,000, suggesting a plateau in crime rates. However, for 2024, the reported crimes drop to under 110,000, reflecting only part of the year's data as it is updated only until September 16th. This decrease could indicate a potential reduction in crime, but it's crucial to note that the year is incomplete, and the final figures may rise as additional reports come in. Overall, the analysis highlights changing crime trends that could prompt further investigation into the factors influencing these patterns.

![image](https://github.com/user-attachments/assets/94dcd2a4-50ac-4851-b4df-37284dd845a9)


Are there any seasonal patterns in crime occurrence based on months?

The code snippet performs a seasonal analysis of crime data by counting the number of reported crimes for each month and visualizing these counts with a bar graph. First, the code extracts the month from the DATE OCC column of the crime_df DataFrame, counts the occurrences of crimes per month, and sorts the results in chronological order. The sns.barplot function is then utilized to create a bar graph, where the x-axis represents the months (adjusted to display properly) and the y-axis indicates the number of crimes reported. The coolwarm color palette is used for aesthetic purposes.

The results of this analysis reveal significant patterns in crime occurrence throughout the year. January stands out as the month with the highest crime count, exceeding 90,000 incidents. March follows closely as the second-highest month, with over 85,000 reported crimes, while February ranks as the third-highest, also around 85,000. From April to August, the crime counts are fairly consistent, all hovering slightly above 80,000. However, from September to December, the numbers drop below 80,000, with November recording the lowest count at just over 70,000. This seasonal analysis highlights the fluctuation of crime incidents across the year, with notable peaks at the beginning of the year and a decline towards the end, suggesting that factors influencing crime rates may vary with seasonal changes.

![image](https://github.com/user-attachments/assets/6a0ff427-2557-442f-a0b4-c8e3f09a6719)


What time of day do crimes most frequently occur?

The provided code performs an analysis of crime occurrences based on the hour of the day. It begins by calculating the hour of each crime incident from the TIME OCC column by performing integer division by 100 to isolate the hour portion. This transformed data is then counted to determine how many crimes occurred during each hour, and the results are sorted in ascending order.

The resulting bar graph visualizes the number of crimes reported for each hour of the day, revealing significant trends in crime patterns. The analysis indicates that the hours from 0 to 11 generally have lower crime counts compared to later hours, with the lowest count occurring at hour 5, which has around 18,000 incidents. Starting from hour 5, there is a gradual increase in crime counts, peaking sharply at hour 12, where incidents surge to over 65,000. After this peak, the number of crimes decreases to just under 45,000 at hour 13. However, crime rates then rise again, reaching about 59,000 by hour 18. Following this peak, there is a gradual decline in crime counts throughout the evening and night, ending with approximately 41,000 incidents at hour 23. This analysis suggests that crime rates are notably higher during midday and early evening hours, while incidents decrease significantly during the early morning hours.

![image](https://github.com/user-attachments/assets/d1d408bf-6ae9-4839-9bd1-aad855638566)


### 4.Crime Status Analysis

### 5.Weapon Usage in Crimes

### 6.Crime Locations 

### 7.Crime Resolution Time Analysis

### 8.Correlation Matrix

### 9.Crime Summary by Crime Type and Area
