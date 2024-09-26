#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing needed packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


#Using read_csv pandas function to import the crime data into a pandas dataframe
crime_df = pd.read_csv('C:\\Users\\Alex Hewitt\\Downloads\\Crime_Data_from_2020_to_Present.csv')


# In[4]:


#Gaining information about the data
crime_df.info()


# In[11]:


#Seeing the first 5 rows in the dataset to get a better understanding of the data and how its formatted.
crime_df.head()


# In[8]:


crime_df[['Vict Age', 'LAT', 'LON', 'Crm Cd']].describe()


# In[7]:


#To see the frequency count of what areas have had the most crimes
print(crime_df['AREA NAME'].value_counts())


# In[8]:


#To see the frequency count of the victim sexes 
print(crime_df['Vict Sex'].value_counts())


# In[9]:


#To see the freqeuency count based on the victism decent
print(crime_df['Vict Descent'].value_counts())


# In[6]:



plt.figure(figsize=(8, 6))
sns.boxplot(x='Vict Sex', y='Vict Age', data=crime_df)
plt.title('Box Plot of Victim Age by Sex')
plt.xlabel('Victim Sex')
plt.ylabel('Victim Age')
plt.show()


# In[7]:


plt.figure(figsize=(12, 8))
sns.boxplot(x='Vict Descent', y='Vict Age', data=crime_df)
plt.title('Box Plot of Victim Age by Descent')
plt.xlabel('Victim Descent')
plt.ylabel('Victim Age')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# In[10]:


# Convert date columns to datetime
crime_df['Date Rptd'] = pd.to_datetime(crime_df['Date Rptd'])
crime_df['DATE OCC'] = pd.to_datetime(crime_df['DATE OCC'])


# In[11]:


# Count crimes by year
crimes_per_year = crime_df['Date Rptd'].dt.year.value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(data=crimes_per_year, marker='o')
plt.title('Reported Crimes Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.xticks(crimes_per_year.index)  # Show all year ticks
plt.grid()
plt.show()


# In[16]:


# Count crimes by month for seasonal analysis
crimes_per_month_seasonal = crime_df['DATE OCC'].dt.month.value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=crimes_per_month_seasonal.index, y=crimes_per_month_seasonal.values, palette='coolwarm')
plt.title('Crimes by Month (Seasonal Patterns)')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.xticks(crimes_per_month_seasonal.index, 
           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid()
plt.show()


# In[13]:


# Count crimes by hour
crime_df['Hour'] = (crime_df['TIME OCC'] // 100).astype(int)  # Extract hour from TIME OCC
crimes_by_hour = crime_df['Hour'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=crimes_by_hour.index, y=crimes_by_hour.values, palette='viridis')
plt.title('Crimes by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Crimes')
plt.xticks(crimes_by_hour.index)
plt.grid()
plt.show()


# In[10]:


# Remove any rows with missing weapon data
weapon_data = crime_df[['Weapon Used Cd', 'Weapon Desc']].dropna()

# Count frequency of each weapon type
weapon_counts = weapon_data['Weapon Desc'].value_counts()

# Plotting the top 10 weapons
plt.figure(figsize=(12, 6))
sns.barplot(x=weapon_counts.head(10).index, y=weapon_counts.head(10).values, palette='plasma')
plt.title('Top 10 Weapons Used in Crimes')
plt.xlabel('Weapon Description')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.grid()
plt.show()


# In[18]:


# Create a new column indicating if a weapon was used
crime_df['Weapon Used'] = crime_df['Weapon Used Cd'].notnull()

# Summary statistics for crimes with and without weapons
weapon_stats = crime_df.groupby('Weapon Used')['DR_NO'].count().reset_index(name='Count')
weapon_stats['Weapon Used'] = weapon_stats['Weapon Used'].map({True: 'With Weapon', False: 'No Weapon'})

# Plotting the comparison
plt.figure(figsize=(8, 6))
sns.barplot(x='Weapon Used', y='Count', data=weapon_stats, palette='Set2')
plt.title('Comparison of Crimes With and Without Weapons')
plt.ylabel('Number of Crimes')
plt.grid()
plt.show()


# In[19]:


# Create a box plot to compare victim ages for crimes with and without weapons
plt.figure(figsize=(10, 6))
sns.boxplot(x='Weapon Used', y='Vict Age', data=crime_df)
plt.title('Victim Age Distribution for Crimes With and Without Weapons')
plt.ylabel('Victim Age')
plt.grid()
plt.show()


# In[21]:


# Drop rows with missing premise descriptions
premise_data = crime_df['Premis Desc'].dropna()

# Count frequency of each type of premise
premise_counts = premise_data.value_counts()

# Display the top 10 premises
print(premise_counts.head(10))


# In[23]:


# Plotting the top 10 premises
plt.figure(figsize=(12, 6))
sns.barplot(x=premise_counts.head(10).index, y=premise_counts.head(10).values, palette='viridis')
plt.title('Top 10 Types of Premises Where Crimes Occur')
plt.xlabel('Premise Description')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=60)
plt.grid()
plt.show()


# In[15]:


# Count the frequency of each crime status
status_counts = crime_df['Status Desc'].value_counts()

# Display the counts of crime statuses
print(status_counts)


# In[19]:


# Creating a pie chart for crime status distribution
plt.figure(figsize=(12, 8))
plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Crime Status Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
plt.show()


# In[26]:


# Calculate the time difference
crime_df['Resolution Time'] = crime_df['Date Rptd'] - crime_df['DATE OCC']


# In[27]:


# Filter out any negative time differences (if a crime was reported before it occurred)
resolution_time_data = crime_df[crime_df['Resolution Time'] >= pd.Timedelta(0)]

# Summary statistics for resolution time
print(resolution_time_data['Resolution Time'].describe())


# In[30]:


# Assuming resolution_time_data['Resolution Time'] is your DataFrame column
# Convert to days if not already done
resolution_time_data['Resolution Time'] = resolution_time_data['Resolution Time'].dt.days

# Step 1: Calculate IQR
Q1 = resolution_time_data['Resolution Time'].quantile(0.25)
Q3 = resolution_time_data['Resolution Time'].quantile(0.75)
IQR = Q3 - Q1

# Step 2: Define bounds and filter outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter data to exclude outliers
filtered_data = resolution_time_data[(resolution_time_data['Resolution Time'] >= lower_bound) &
                                     (resolution_time_data['Resolution Time'] <= upper_bound)]

# Step 3: Plotting the histogram with the filtered data
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['Resolution Time'], bins=30, kde=True)
plt.title('Distribution of Crime Resolution Time (Days) - Outliers Removed')
plt.xlabel('Days Between Crime Occurrence and Reporting')
plt.ylabel('Frequency')
plt.grid()
plt.show()


# In[32]:


# Assuming your DataFrame is named crime_df
# Step 1: Compute the correlation matrix
correlation_matrix = crime_df[['Vict Age', 'LAT', 'LON', 'TIME OCC', 'AREA']].corr()

# Step 2: Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()


# In[33]:


# Grouping by crime type and calculating the count of crimes and average victim age
crime_summary = crime_df.groupby(['Crm Cd Desc', 'AREA NAME'])['Vict Age'].agg(['count', 'mean']).reset_index()
crime_summary.rename(columns={'count': 'Crime Count', 'mean': 'Average Victim Age'}, inplace=True)

# Display the summary
print(crime_summary)


# In[34]:


# Scatter plot: Victim Age vs. Crime Count, colored by Area Name
plt.figure(figsize=(12, 8))
sns.scatterplot(data=crime_summary, x='Crime Count', y='Average Victim Age', hue='AREA NAME', palette='deep')
plt.title('Victim Age vs. Crime Count by Area Name')
plt.xlabel('Crime Count')
plt.ylabel('Average Victim Age')
plt.grid()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)  # Move legend outside of the plot
plt.show()


# In[12]:


# Grouping by Weapon Used and Crime Type to get counts
weapon_crime_summary = crime_df.groupby(['Weapon Desc', 'Crm Cd Desc']).size().unstack(fill_value=0)

# Get the top N weapons and crime types based on counts
top_n_weapons = crime_df['Weapon Desc'].value_counts().nlargest(10).index
top_n_crimes = crime_df['Crm Cd Desc'].value_counts().nlargest(10).index

# Filter the summary to include only top N categories
filtered_weapon_crime_summary = crime_df[crime_df['Weapon Desc'].isin(top_n_weapons) & crime_df['Crm Cd Desc'].isin(top_n_crimes)]
weapon_crime_summary = filtered_weapon_crime_summary.groupby(['Weapon Desc', 'Crm Cd Desc']).size().unstack(fill_value=0)

# Heatmap of Weapons vs. Crime Types
plt.figure(figsize=(12, 8))
sns.heatmap(weapon_crime_summary, cmap='Blues', annot=True, fmt='d')
plt.title('Heatmap of Weapons Used vs. Crime Types')
plt.xlabel('Crime Type')
plt.ylabel('Weapon Used')
#plt.xticks(rotation=35)
plt.show()


# In[13]:


# Create a new column for the hour of occurrence
crime_df['Hour Occurred'] = (crime_df['TIME OCC'] // 100).astype(int)

# Group by hour and crime type to count occurrences
time_crime_summary = crime_df.groupby(['Hour Occurred', 'Crm Cd Desc']).size().unstack(fill_value=0)

# Get the top 10 crime types based on counts
top_n_crimes = crime_df['Crm Cd Desc'].value_counts().nlargest(10).index

# Filter the time_crime_summary to include only top 10 crime types
filtered_time_crime_summary = time_crime_summary.loc[:, top_n_crimes]

# Heatmap of Crime Occurrences by Hour and Top Crime Types
plt.figure(figsize=(12, 8))
sns.heatmap(filtered_time_crime_summary, cmap='viridis', annot=True, fmt='d')
plt.title('Heatmap of Crime Occurrences by Hour and Top Crime Types')
plt.xlabel('Crime Type')
plt.ylabel('Hour of Occurrence')
#plt.xticks(rotation=45)
plt.show()


# In[ ]:




