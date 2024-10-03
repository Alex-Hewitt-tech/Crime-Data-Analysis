# Crime-Data-Analysis
## Project Summary
This project analyzes crime data from 2020 to the present from the City of Los Angeles using a comprehensive approach that includes data cleaning, visualization, and statistical analysis. The dataset contains various attributes, including victim age, crime type, weapon used, and geographic location. Key findings reveal trends in crime occurrences over time, seasonal patterns, and relationships between victim demographics and crime statistics. Visualization techniques, such as box plots, line graphs, and heatmaps, effectively illustrate the data insights, highlighting significant patterns like weapon usage and crime counts by area and time of day. Overall, the analysis provides valuable insights into crime dynamics, which can inform policy-making and community safety initiatives.

## Code Setup
You can easily download the crime data from the "data" folder in this repository, specifically the file named Crime_Data_from_2020_to_Present.csv. To use this dataset, simply ensure that you have the necessary packages installed and then read the data into a DataFrame with the following command:
crime_df = pd.read_csv('C:\\Users\\Computer Username\\Downloads\\Crime_Data_from_2020_to_Present.csv')
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

The code counts the frequency of each unique crime status in the Status Desc column of the crime_df DataFrame using the value_counts() function. The output reveals that the most common status is Invest Cont (Investigation Continued), with 781,494 occurrences, indicating that a significant number of crimes remain under investigation. Following this, Adult Other has 107,207 occurrences, suggesting many adult-related cases do not lead to arrests. Adult Arrest accounts for 84,898 instances, reflecting a substantial number of arrests among adult offenders. In contrast, Juvenile Arrest and Juvenile Other show much lower counts at 3,189 and 1,833, respectively, indicating fewer incidents involving juveniles. Lastly, the UNK (Unknown) status is minimal, with only 7 occurrences, suggesting the dataset is largely complete regarding crime status reporting. Overall, these counts provide valuable insights into the outcomes of reported crimes, particularly highlighting the prevalence of ongoing investigations.
What is the frequency distribution of different crime statuses (resolved, pending, etc.)?

![image](https://github.com/user-attachments/assets/3260ddff-9a40-415a-8b59-494b164c5fbd)

How do the crime statuses compare visually using a pie chart?

The code generates a pie chart to visually represent the distribution of various crime statuses in the dataset. The plt.pie() function is utilized, where the sizes of the pie slices correspond to the counts of each status derived from the status_counts Series. The chart is designed with a pastel color palette, and the legend is placed on the right side for easy reference. The title "Crime Status Distribution" is added, and the aspect ratio is set to equal to ensure a circular pie chart.

The results of the pie chart reveal a significant dominance of the Invest Cont (Investigation Continued) status, which takes up the majority of the chart, illustrating that most reported crimes are still under investigation. The second largest segment is Adult Other, indicating a substantial number of adult cases that do not result in arrests. Following that, Adult Arrest represents the third largest slice, reflecting a considerable volume of adult arrests. In contrast, the segments for Juvenile Arrest and Juvenile Other are quite small, showing minimal occurrences compared to the other statuses. Lastly, the UNK (Unknown) category is nearly negligible and hardly visible on the pie chart, suggesting that the dataset is largely complete regarding the reporting of crime statuses. Overall, this visualization effectively highlights the trends in crime status distribution, emphasizing the ongoing nature of many investigations.

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

The code processes the crime dataset to analyze the usage of different weapons in reported crimes. Initially, it filters out any rows containing missing weapon data, retaining only those with valid entries for the Weapon Used Cd and Weapon Desc columns. Next, it counts the frequency of each weapon type using the value_counts() function, which organizes the data by the number of occurrences. A bar plot is then generated to visualize the top 10 weapons used in crimes, with the x-axis representing the weapon descriptions and the y-axis indicating the corresponding number of crimes. The plot is formatted for clarity, featuring a title, axis labels, and rotated x-tick labels for better readability.

The results of the analysis reveal that Strong-arm (Hands, Fist, Feet, or Bodily Force) is the most frequently used weapon, accounting for an astonishing 175,000 reported crimes. The second most common weapon is categorized as Unknown Weapon/Other Weapon, with just under 35,000 occurrences, highlighting a significant number of incidents where the weapon type is not specified. Following this, Verbal Threat ranks third, with close to 25,000 counts. The remaining weapons, including Semi-Automatic Pistol, Knife with Blade 6 Inches or Less, Unknown Firearm, Other Knife, Mace/Pepper Spray, and Vehicle, show relatively low frequencies, all hovering around or below 5,000 crimes. This data suggests that physical confrontations are more prevalent than the use of traditional weapons in reported crime incidents.

![image](https://github.com/user-attachments/assets/02f4dabe-f3e8-4349-8b14-9b6b05c05eef)

What types of weapons are most commonly used in different categories of crime?

The provided code analyzes the relationship between weapons used and specific crime types within the dataset. It begins by grouping the data based on Weapon Description and Crime Description, counting occurrences for each combination. To focus on the most frequent weapons and crimes, the top 10 weapons and crime types are selected, and the dataset is filtered accordingly. The resulting data is used to generate a heatmap that visualizes the frequency of each weapon-crime combination.

The results reveal that the most common weapon-crime pair is Strong-Arm (Hands, Fist, Feet, or Bodily Force) used in Battery - Simple Assault, with a significant count of 67,403 incidents. The second most frequent combination is the same weapon type used in Intimate Partner - Simple Assault, with 43,964 cases. Both values are notably higher than other combinations. Other notable pairs include Handgun used in Assault with a Deadly Weapon - Aggravated Assault (7,640) and Strong-Arm used in the same crime type (6,734), indicating these are prominent crime-weapon pairings.

![image](https://github.com/user-attachments/assets/d923a0b0-eea9-48df-bb94-dbd923ae9122)

![image](https://github.com/user-attachments/assets/74d0ba25-417a-40b8-bba4-3ee6798e2293)

How many crimes involve the use of a weapon compared to those without?

The code examines the frequency of crimes committed with and without the use of weapons. First, a new column, Weapon Used, is created, indicating whether a weapon was used by checking for non-null values in the Weapon Used Cd field. The dataset is then grouped by whether a weapon was involved, and the total count of crimes in each category is calculated. The mapping of the Weapon Used column simplifies the labels to "With Weapon" and "No Weapon." Finally, the data is visualized using a bar plot that compares the number of crimes in each category.

The results show that crimes committed without weapons are significantly more common, totaling over 650,000 incidents, while crimes involving weapons are fewer, with around 315,000. This clear discrepancy highlights that the majority of crimes in the dataset did not involve the use of a weapon.

![image](https://github.com/user-attachments/assets/4cef472a-124f-49ac-9778-7a8de4c2b71e)


How does the age of victims differ between crimes involving weapons and those without?

The code generates a box plot to compare the distribution of victim ages between crimes committed with and without weapons. By using a boxplot, the data is visually split based on whether a weapon was used, as determined by the Weapon Used column. The plot displays the median, interquartile range (IQR), minimum, maximum, and outliers for the age of victims in each group. This helps provide insights into the variation in victim ages depending on whether a weapon was involved in the crime.

The results show that for crimes without weapons, the median victim age falls between 28 and 30, with an IQR from 0 to 42, and a wide age range stretching from below 0 (which may indicate data entry errors) to nearly 100 years old. In contrast, for crimes involving weapons, the median victim age is slightly higher, around 31 to 33, with a narrower IQR between 22 and 47. The maximum victim age in weapon-related crimes is around 80, and there are several outliers, unlike the no-weapon cases, which do not show significant outliers. This suggests that crimes involving weapons tend to impact slightly older individuals and display more extreme age values.

![image](https://github.com/user-attachments/assets/882940e6-f978-4c23-9d18-d1a5502a06fb)


### 6.Crime Locations 
The Crime Locations analysis focuses on identifying and visualizing the geographical distribution of criminal activities within various areas. By mapping crime occurrences, this analysis reveals hotspots where certain types of crimes are more prevalent, aiding law enforcement and policymakers in resource allocation and strategic planning. Utilizing spatial data and visual representations, such as choropleth maps or bar charts, the analysis highlights trends in crime distribution across different neighborhoods or regions. This information is vital for community safety initiatives and can inform targeted interventions to reduce crime rates in high-risk areas.

#### The questions we are trying to answer in this section

What are the top 10 locations where crimes are most frequently committed?

How do the number of crimes vary across different premises?

#### The Code
What are the top 10 locations where crimes are most frequently committed?

The code uses the value_counts() function to calculate and display the frequency of crimes for each area in the dataset, based on the 'AREA NAME' column. This function counts the occurrences of each unique value in the column, effectively summarizing the total number of reported crimes for each area. The output is then printed in descending order, with the area having the highest crime count listed first.

The results show that Central leads with the highest crime count at 67,453 incidents, followed by 77th Street with 60,682, and Pacific with 57,510. Other high-crime areas include Southwest and Hollywood, while areas like Foothill, with 32,457 reported incidents, have comparatively fewer crimes. This indicates that certain areas are more prone to criminal activity than others, with a notable concentration of crimes in Central and surrounding regions.

![image](https://github.com/user-attachments/assets/b4757034-d53d-4b41-b6ca-42eb6d2f5154)

How do the number of crimes vary across different premises?

The code creates a bar plot to visualize the top 10 types of premises where crimes most frequently occur, based on their counts. First, the premise_counts.head(10) function selects the 10 most common premises from the dataset, which are plotted using seaborn's barplot() function. The x-axis represents the premises, and the y-axis shows the number of crimes. The chart's appearance is enhanced with gridlines, a rotated x-axis to make the labels readable, and a title to clarify the plot’s purpose.

The results show that Streets are the most common crime location, with just over 250,000 incidents. This is followed by Single Family Dwellings at approximately 160,000 crimes and Multi-Unit Dwellings (such as apartments and duplexes) at around 120,000. The fourth highest is Parking Lots, with around 65,000 crimes. The remaining premises, such as Sidewalks, Vehicles, Garages, and Department Stores, have significantly lower crime counts, each below 50,000 incidents. This data indicates that public and residential areas are the most frequent settings for criminal activity.

![image](https://github.com/user-attachments/assets/b1be14cf-41fa-41aa-91c2-eb8bc4df588c)


### 7.Crime Resolution Time Analysis
The Crime Resolution Time Analysis examines the duration it takes for law enforcement agencies to resolve criminal cases from the time they are reported. By analyzing data on case resolution times, this section aims to identify patterns and factors that influence how quickly crimes are solved. Visualizations, such as histograms or box plots, may be employed to illustrate the distribution of resolution times across different crime types and areas. This analysis is crucial for assessing the efficiency of the criminal justice system, identifying potential delays, and highlighting areas where improvements can be made to expedite case resolutions, ultimately enhancing public trust and safety.

#### The questions we are trying to answer in this section

How long does it typically take for a crime to be reported after it occurs?

What is the distribution of the time between crime occurrence and reporting when outliers are removed?

#### The Code

How long does it typically take for a crime to be reported after it occurs?

The code calculates the time difference between when a crime was reported and when it occurred. First, it creates a new column, Resolution Time, by subtracting the occurrence date (DATE OCC) from the reported date (Date Rptd). To ensure accuracy, the code filters out any negative time differences, where a crime might have been reported before it actually occurred, which would be logically incorrect. This filtering creates a new dataframe, resolution_time_data, containing only valid time differences.

The results show the summary statistics of the resolution times for the dataset. There are 978,628 valid records where crimes were reported either on the same day or after they occurred. The average time it took for a crime to be reported is around 11 days and 19 hours, with a high standard deviation of 66 days, indicating wide variability. The median (50th percentile) resolution time is 1 day, while the 25th percentile (1st quartile) is 0 days, meaning many crimes were reported on the same day they occurred. The maximum time between a crime occurrence and its report is 1,711 days (nearly 5 years), reflecting that some crimes take significantly longer to be reported. The overall distribution suggests that most crimes are reported within a couple of days, but there are a few outliers with much longer reporting times.

![image](https://github.com/user-attachments/assets/be2e79a5-7c84-4567-b8cc-e04a43436d63)


What is the distribution of the time between crime occurrence and reporting when outliers are removed?

The code first converts the Resolution Time column from a time format into days, representing the number of days between when a crime occurred and when it was reported. This allows for an easier understanding of the data. Next, the code calculates the Interquartile Range (IQR) to identify and remove any extreme outliers. The IQR is calculated by finding the difference between the 25th percentile (Q1) and the 75th percentile (Q3), which represents the middle 50% of the data. The code then defines the lower and upper bounds for acceptable values by subtracting and adding 1.5 times the IQR from Q1 and Q3, respectively. Any resolution times outside these bounds are considered outliers and are removed from the data.

After filtering out the outliers, the code plots a histogram showing the distribution of the crime resolution times (in days), with a Kernel Density Estimation (KDE) overlay. The histogram displays the frequency of different resolution times, and the KDE line provides a smooth estimate of the probability distribution of the data.

In terms of results, the histogram shows that a large proportion of crimes are reported on the same day they occur (around 470,000 cases). The number of cases drops sharply for subsequent days, with about 210,000 reported the next day, and fewer for each day thereafter. The KDE curve follows a similar pattern, starting high for same-day reports and peaking within each bin before tapering off. This indicates that crimes are generally reported within a few days of occurrence, with very few being reported much later. The filtering removed any extreme outliers, providing a clearer view of the distribution.

![image](https://github.com/user-attachments/assets/cd64dc9c-db98-4f86-bd92-2e3dea5afef8)


### 8.Correlation Matrix
The Correlation Matrix section explores the relationships between various factors related to crime data, such as crime types, victim characteristics, weapon usage, and geographic locations. By calculating correlation coefficients, this analysis identifies how strongly different variables are related to one another, helping to uncover underlying patterns and trends in the data. Visual representations, such as heatmaps, may be used to illustrate these correlations, making it easier to spot significant associations. Understanding these correlations can inform law enforcement strategies, resource allocation, and preventive measures by highlighting factors that may contribute to crime patterns and outcomes.

#### The questions we are trying to answer in this section

How are key numerical features (e.g., victim age, latitude, longitude, crime occurrence time) correlated with each other?

#### The Code

How are key numerical features (e.g., victim age, latitude, longitude, crime occurrence time) correlated with each other?

The code computes the correlation matrix for selected numerical features in the crime_df DataFrame, which includes victim age (Vict Age), latitude (LAT), longitude (LON), time of occurrence (TIME OCC), and area (AREA). The correlation matrix quantifies the linear relationship between these variables, with values ranging from -1 to 1. A value of 1 indicates a perfect positive correlation, while a value of -1 indicates a perfect negative correlation. A value of 0 indicates no correlation.

Following the computation of the correlation matrix, the code generates a heatmap to visualize these correlations. The heatmap uses a color gradient to represent the strength and direction of correlations, with annotations showing the exact correlation values. The coolwarm color palette helps distinguish between positive and negative correlations.

The results indicate that the correlation values for most features are relatively low, with many values clustering around 0. The correlation of latitude (LAT) with itself is 1.00, which is expected. A significant negative correlation of -1.00 exists between LAT and LON, indicating that as one increases, the other decreases proportionally, which is typical given that latitude and longitude are often inversely related depending on geographical coordinates. Other correlations, such as between Vict Age and AREA (0.02), LAT and AREA (0.02), LON and AREA (-0.01), and TIME OCC and Vict Age (-0.04), suggest weak relationships. These findings imply that the victim's age and the area of occurrence do not have a strong linear relationship, nor do the time of occurrence and victim age show a significant correlation. Overall, the heatmap visually reinforces the lack of strong correlations among the selected variables in this dataset.

![image](https://github.com/user-attachments/assets/9524c220-4ae6-434a-87db-2d41920f0419)


### 9.Crime Summary by Crime Type and Area
The Crime Summary by Crime Type and Area section provides a comprehensive overview of the frequency and nature of various crime types across different geographical areas. This analysis involves grouping the data by crime type and area to calculate the total number of incidents and the average age of victims associated with each crime category. Additionally, it examines how victim age correlates with total crime counts, offering insights into demographic patterns within crime statistics. By visualizing this information, stakeholders can identify prevalent crime types in specific areas, assess victim demographics, and develop targeted interventions to enhance public safety and address community-specific needs.

#### The questions we are trying to answer in this section

What are the counts of different types of crimes occurring in various areas, and what is the average age of victims for these crimes?

How does the average victim age relate to the total crime count in different areas?

What are the patterns of crime occurrences throughout the day based on the time they occurred, particularly for the most common crime types?

#### The Code

What are the counts of different types of crimes occurring in various areas, and what is the average age of victims for these crimes?

The code snippet performs a summary analysis of crimes from the crime_df DataFrame by grouping the data based on two criteria: crime type (Crm Cd Desc) and area name (AREA NAME). It calculates two key metrics for each group: the count of crimes and the average age of victims. This is achieved using the groupby() function to aggregate the data. Specifically, it employs the agg() function to apply both the count and mean operations to the victim age (Vict Age) column. The results are then reset to create a new DataFrame, and the columns are renamed for clarity, changing "count" to "Crime Count" and "mean" to "Average Victim Age".

The resulting summary, displayed as a DataFrame, provides insights into the frequency and victim age associated with various crime types across different areas. The output consists of 2,393 rows, indicating a diverse range of crime types and area combinations. For instance, the data shows that in the 77th Street area, there were 203 reported incidents of arson with an average victim age of approximately 32.76 years. In contrast, the Central area had 231 incidents of arson but a significantly lower average victim age of around 16.04 years. This pattern indicates varying crime frequencies and victim demographics across areas and crime types. The summary thus highlights critical differences in crime occurrence and victim profiles that could inform targeted interventions and resource allocation in law enforcement and community safety efforts.

![image](https://github.com/user-attachments/assets/0702b6bf-8ca4-4822-86ae-7aaf8355c734)


How does the average victim age relate to the total crime count in different areas?

The provided code creates a scatter plot to visualize the relationship between victim age and crime count across different areas. It uses the seaborn library's scatterplot function to plot the Crime Count on the x-axis and Average Victim Age on the y-axis. Each point on the plot represents a unique combination of crime type and area, with the color of the points indicating the specific area using the hue parameter. The plot is enhanced with titles for clarity, labeled axes, and a grid for better readability. A legend is positioned outside the plot area to avoid overlapping with the data points.

The results indicate a significant clustering of crime counts around the age range of 30 to 41, where a noticeable spike in crime occurrences is observed. Additionally, there are various areas with high crime counts reported for victims aged 0, which may suggest incidents involving minors or reporting discrepancies. Notably, the area named Olympic stands out with the highest crime count, exceeding 9,000 incidents, particularly among victims in their late 30s. This visualization highlights the importance of understanding age demographics in relation to crime statistics across different areas, suggesting potential areas for intervention and policy development.

![image](https://github.com/user-attachments/assets/e4fad7d7-a76c-4c31-8226-2284c54e1ef9)


What are the patterns of crime occurrences throughout the day based on the time they occurred, particularly for the most common crime types?

The provided code aims to analyze and visualize the hourly distribution of crime occurrences based on crime types. First, a new column called Hour Occurred is created in the crime_df DataFrame, which extracts the hour from the TIME OCC column by performing integer division by 100. This transformation allows for grouping by hour.

Next, the code groups the data by Hour Occurred and Crm Cd Desc (crime code description) to count the occurrences of each crime type for each hour. The size() function counts the number of occurrences, and the unstack() method reshapes the DataFrame to have hours as rows and crime types as columns. This results in a matrix-like structure, where the values represent the count of crimes for each combination of hour and crime type.

To focus the analysis, the code identifies the top 10 crime types based on their total counts and filters the heatmap data to include only these crime types. Finally, a heatmap is generated using seaborn, visualizing the number of occurrences of the top crime types at each hour of the day. The heatmap includes annotations for the counts and uses a color gradient to represent the intensity of occurrences.

The results from the heatmap indicate that the highest number of occurrences is at 12 PM, specifically for the crime type "Theft of Identity," which had a total of 10,169 reported incidents. This suggests that midday may be a critical time for interventions, such as increased surveillance or law enforcement presence, to deter these crimes. Additionally, a significant trend is observed in the hours between 4 PM and 11 PM, where counts for vehicle theft are notably high, ranging from 5,513 to 8,317 incidents. This evening surge in crime occurrences suggests that criminals may be more active during these hours, possibly due to increased foot traffic or reduced visibility.

Another noteworthy observation is that "Theft of Identity" also has a high count of 6,058 occurrences at 6 PM, indicating that this type of crime is persistent and requires focused prevention efforts throughout the day. The analysis highlights the importance of timing in law enforcement strategies; by allocating resources effectively during peak crime hours, the police can enhance their response to these incidents. Furthermore, the patterns observed may indicate specific behaviors or motivations for these crimes, underscoring the need for public awareness campaigns to educate individuals on vigilance during these critical times. Overall, these insights reveal critical patterns in crime occurrences throughout the day, highlighting peak times and specific crime types that warrant further investigation and potential intervention strategies.

![image](https://github.com/user-attachments/assets/78644155-a496-4b4c-8842-761886a56311)

![image](https://github.com/user-attachments/assets/56ea423c-cf9d-4942-8494-708a11af52a2)

