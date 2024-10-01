# Crime-Data-Analysis
## Project Summary

## Code Setup

## Code Overview

### 1.Loading packages, loading dataset and data exploration
Importing Necessary Packages
The code begins by importing essential libraries:
NumPy for numerical operations,
Pandas for data manipulation and analysis,
Seaborn and Matplotlib for data visualization

![image](https://github.com/user-attachments/assets/3d156498-ca9b-4c44-83b6-e0c64aa28c89)


The pd.read_csv function is used to read a CSV file containing crime data into a Pandas DataFrame named crime_df. This file is located at a specified path on the user's machine.

![image](https://github.com/user-attachments/assets/59fac361-f954-48ae-b838-bb64a457c4a0)

Using the info() method on the DataFrame provides a summary of the dataset, which includes:

Number of entries: 978,628, indicating the total number of crime records.
Data columns: 28 columns, such as DR_NO (report number), DATE OCC (date of occurrence), Vict Age (victim age), Weapon Desc (weapon used), and others.
Non-null counts: Shows that most columns have no missing values except for a few like Mocodes, Vict Sex, and Vict Descent, indicating some records are incomplete.
Data types: Describes the data types of each column, such as int64, float64, and object, which helps understand how to handle the data.

![image](https://github.com/user-attachments/assets/26a5ee7c-a949-411e-937e-29d71fd79cfb)

The head() method displays the first five rows of the DataFrame. This snapshot allows for a quick look at the data's format and the types of information it contains

![image](https://github.com/user-attachments/assets/6838118a-616e-4ed4-b966-e431bb805294)

The describe() function is applied to specific columns (Vict Age, LAT, LON, Crm Cd) to generate a statistical summary. This summary includes:

Count: Number of non-null entries.
Mean: Average value for each numeric column (e.g., average victim age is approximately 29 years).
Standard Deviation (std): Measures variability; a higher value indicates more spread in the data.
Min/Max Values: Ranges of values for each column (e.g., victim age ranges from -4 to 120 years).
Percentiles: Provides insights into the distribution of the data, indicating that 25% of victims are under age 0, and 75% are under age 44.

![image](https://github.com/user-attachments/assets/3e552bb5-a323-4346-b53b-7b0d92c7af29)


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
The Crime Status Analysis provides an overview of crime trends and patterns within a specific area by analyzing reported crime data over a defined period. It aims to identify the frequency of different crime types, peak periods of criminal activity, and the demographics of victims. Additionally, the analysis evaluates crime resolution rates and hotspots, helping law enforcement agencies allocate resources effectively and inform community safety measures. By utilizing descriptive statistics and data visualization, this analysis offers actionable insights that enhance public safety and support strategic decision-making for stakeholders.

#### The questions we are trying to answer in this section

What is the frequency distribution of different crime statuses (resolved, pending, etc.)?

How do the crime statuses compare visually using a pie chart?

#### The Code

What is the frequency distribution of different crime statuses (resolved, pending, etc.)?

![image](https://github.com/user-attachments/assets/3260ddff-9a40-415a-8b59-494b164c5fbd)

How do the crime statuses compare visually using a pie chart?

![image](https://github.com/user-attachments/assets/e07f82a1-9dbb-4762-8f80-722549e6c370)


### 5.Weapon Usage in Crimes
The Weapon Usage in Crimes analysis examines the types of weapons employed in various criminal activities to identify trends and correlations between weapon usage and specific crime types. By categorizing crimes based on the weapons involved, this analysis helps to uncover patterns that may inform law enforcement strategies and prevention efforts. It utilizes data visualizations, such as heatmaps, to illustrate the relationship between weapon types and crime occurrences, enabling stakeholders to understand the prevalence of certain weapons in criminal offenses. This information is crucial for developing targeted interventions and improving community safety initiatives.

#### The questions we are trying to answer in this section

What are the most common weapons used in crimes?

What types of weapons are most commonly used in different categories of crime?

How many crimes involve the use of a weapon compared to those without?

How does the age of victims differ between crimes involving weapons and those without?

#### The Code

What are the most common weapons used in crimes?

![image](https://github.com/user-attachments/assets/02f4dabe-f3e8-4349-8b14-9b6b05c05eef)

What types of weapons are most commonly used in different categories of crime?

![image](https://github.com/user-attachments/assets/d923a0b0-eea9-48df-bb94-dbd923ae9122)

![image](https://github.com/user-attachments/assets/74d0ba25-417a-40b8-bba4-3ee6798e2293)

How many crimes involve the use of a weapon compared to those without?

![image](https://github.com/user-attachments/assets/4cef472a-124f-49ac-9778-7a8de4c2b71e)


How does the age of victims differ between crimes involving weapons and those without?

![image](https://github.com/user-attachments/assets/882940e6-f978-4c23-9d18-d1a5502a06fb)


### 6.Crime Locations 
The Crime Locations analysis focuses on identifying and visualizing the geographical distribution of criminal activities within various areas. By mapping crime occurrences, this analysis reveals hotspots where certain types of crimes are more prevalent, aiding law enforcement and policymakers in resource allocation and strategic planning. Utilizing spatial data and visual representations, such as choropleth maps or bar charts, the analysis highlights trends in crime distribution across different neighborhoods or regions. This information is vital for community safety initiatives and can inform targeted interventions to reduce crime rates in high-risk areas.

#### The questions we are trying to answer in this section

What are the top 10 locations where crimes are most frequently committed?

How do the number of crimes vary across different premises?

#### The Code
What are the top 10 locations where crimes are most frequently committed?

![image](https://github.com/user-attachments/assets/b4757034-d53d-4b41-b6ca-42eb6d2f5154)

How do the number of crimes vary across different premises?

![image](https://github.com/user-attachments/assets/b1be14cf-41fa-41aa-91c2-eb8bc4df588c)


### 7.Crime Resolution Time Analysis
The Crime Resolution Time Analysis examines the duration it takes for law enforcement agencies to resolve criminal cases from the time they are reported. By analyzing data on case resolution times, this section aims to identify patterns and factors that influence how quickly crimes are solved. Visualizations, such as histograms or box plots, may be employed to illustrate the distribution of resolution times across different crime types and areas. This analysis is crucial for assessing the efficiency of the criminal justice system, identifying potential delays, and highlighting areas where improvements can be made to expedite case resolutions, ultimately enhancing public trust and safety.

#### The questions we are trying to answer in this section

How long does it typically take for a crime to be reported after it occurs?

What is the distribution of the time between crime occurrence and reporting when outliers are removed?

#### The Code

How long does it typically take for a crime to be reported after it occurs?

![image](https://github.com/user-attachments/assets/be2e79a5-7c84-4567-b8cc-e04a43436d63)


What is the distribution of the time between crime occurrence and reporting when outliers are removed?

![image](https://github.com/user-attachments/assets/cd64dc9c-db98-4f86-bd92-2e3dea5afef8)


### 8.Correlation Matrix
The Correlation Matrix section explores the relationships between various factors related to crime data, such as crime types, victim characteristics, weapon usage, and geographic locations. By calculating correlation coefficients, this analysis identifies how strongly different variables are related to one another, helping to uncover underlying patterns and trends in the data. Visual representations, such as heatmaps, may be used to illustrate these correlations, making it easier to spot significant associations. Understanding these correlations can inform law enforcement strategies, resource allocation, and preventive measures by highlighting factors that may contribute to crime patterns and outcomes.

#### The questions we are trying to answer in this section

How are key numerical features (e.g., victim age, latitude, longitude, crime occurrence time) correlated with each other?

#### The Code

How are key numerical features (e.g., victim age, latitude, longitude, crime occurrence time) correlated with each other?

![image](https://github.com/user-attachments/assets/9524c220-4ae6-434a-87db-2d41920f0419)


### 9.Crime Summary by Crime Type and Area
The Crime Summary by Crime Type and Area section provides a comprehensive overview of the frequency and nature of various crime types across different geographical areas. This analysis involves grouping the data by crime type and area to calculate the total number of incidents and the average age of victims associated with each crime category. Additionally, it examines how victim age correlates with total crime counts, offering insights into demographic patterns within crime statistics. By visualizing this information, stakeholders can identify prevalent crime types in specific areas, assess victim demographics, and develop targeted interventions to enhance public safety and address community-specific needs.

#### The questions we are trying to answer in this section

What are the counts of different types of crimes occurring in various areas, and what is the average age of victims for these crimes?

How does the average victim age relate to the total crime count in different areas?

What are the patterns of crime occurrences throughout the day based on the time they occurred, particularly for the most common crime types?

#### The Code

What are the counts of different types of crimes occurring in various areas, and what is the average age of victims for these crimes?

![image](https://github.com/user-attachments/assets/0702b6bf-8ca4-4822-86ae-7aaf8355c734)


How does the average victim age relate to the total crime count in different areas?

![image](https://github.com/user-attachments/assets/e4fad7d7-a76c-4c31-8226-2284c54e1ef9)


What are the patterns of crime occurrences throughout the day based on the time they occurred, particularly for the most common crime types?

![image](https://github.com/user-attachments/assets/78644155-a496-4b4c-8842-761886a56311)

![image](https://github.com/user-attachments/assets/56ea423c-cf9d-4942-8494-708a11af52a2)

