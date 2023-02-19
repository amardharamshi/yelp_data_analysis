#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Yelp dataset into a Pandas DataFrame
df = pd.read_csv("yelp_business.csv")
df



# In[8]:


df2 = pd.read_csv("yelp_review.csv")
df2


# In[14]:


# Group the data by business name and calculate the mean rating for each business
business_ratings = df.groupby('name').mean()['review_count']

# Sort the business ratings in descending order
business_ratings = business_ratings.sort_values(ascending=False)

# Plot the top 10 businesses with the highest average ratings
business_ratings[:10].plot(kind='bar', x='name', y='review_count', color='orange')
plt.title("Top 10 Popular Businesses on Yelp")
plt.xlabel("Business Name")
plt.ylabel("Average Review count")
plt.show()


# How has the average user rating of businesses changed over time on Yelp?

# In[12]:


# Convert the review_date column to a datetime data type
df2['date'] = pd.to_datetime(df2['date'])

# Group the data by review date and calculate the mean rating for each date
date_ratings = df2.groupby(df2['date'].dt.year).mean()['stars']

# Plot the mean rating by review date
date_ratings.plot(kind='line', color='orange')
plt.title("Average User Rating of Businesses on Yelp over Time")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.show()


# In[4]:


import pandas as pd
# Popular business categories: Identify the most popular business categories and their distribution across neighborhoods and cities.
# load the Yelp dataset


# extract the relevant columns
businesses = df[['business_id', 'name', 'neighborhood', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'categories']]

# create a new dataframe to store the category and count information
category_counts = pd.DataFrame(columns=['category', 'count', 'neighborhood', 'city'])

# iterate over each business
for index, row in businesses.iterrows():
    # extract the categories for the current business
    categories = row['categories'].split(';')
    # iterate over each category for the current business
    for category in categories:
        # check if the category is already in the category_counts dataframe
        if category in category_counts['category'].tolist():
            # if the category is already in the dataframe, update the count
            category_counts.loc[category_counts['category'] == category, 'count'] += 1
            category_counts.loc[category_counts['category'] == category, 'neighborhood'] = row['neighborhood']
            category_counts.loc[category_counts['category'] == category, 'city'] = row['city']
        else:
            # if the category is not in the dataframe, add a new row with count 1
            category_counts = category_counts.append({'category': category, 'count': 1, 'neighborhood': row['neighborhood'], 'city': row['city']}, ignore_index=True)

# sort the category_counts dataframe by count in descending order
category_counts = category_counts.sort_values(by='count', ascending=False)

# print the top 10 categories and their counts
print(category_counts.head(10))


# In[ ]:


import pandas as pd
import folium
#Geospatial analysis: Use latitude and longitude data to visualize the distribution of businesses across cities and neighborhoods.
# load the Yelp dataset


# extract the relevant columns
businesses = df
businesses = businesses.dropna()
# group businesses by city
businesses_by_city = businesses.groupby('city')

# create a map object centered on the first city in the dataset
m = folium.Map(location=[businesses['latitude'].iloc[0], businesses['longitude'].iloc[0]], zoom_start=10)

# iterate over each city
for city, group in businesses_by_city:
    # create a feature group for the current city
    feature_group = folium.FeatureGroup(name=city)
    # iterate over each business in the current city
    for index, row in group.iterrows():
        # add a marker for the current business
        feature_group.add_child(folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']))
    # add the feature group for the current city to the map
    m.add_child(feature_group)

# add a layer control to the map
folium.LayerControl().add_to(m)

# save the map as an HTML file
m.save('businesses_map.html')


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


# extract the categories column and split the categories into a list
categories = df['categories'].str.split(';')

# count the frequency of each category and create a dataframe
category_counts = pd.Series([category for sublist in categories for category in sublist]).value_counts().to_frame('count')

# plot the top 20 categories as a horizontal bar chart
top_categories = category_counts.head(20)
top_categories.plot(kind='barh', legend=None, color='steelblue', figsize=(10, 6))
plt.xlabel('Count')
plt.title('Distribution of Categories in Yelp Dataset')
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt


# 1. How many companies are in the data set
n_companies = df['business_id'].nunique()
print(f"There are {n_companies} unique companies in the data set.")


# 3. How is the distribution of states
states = df['state'].value_counts()
print("Distribution of states:")
print(states)

# 4. Which state has the most restaurants/businesses
most_businesses = states.idxmax()
print(f"{most_businesses} has the most restaurants/businesses.")


# In[7]:


import pandas as pd


# calculate the mean star rating
mean_stars = df['stars'].mean()

print("The average star rating is:", round(mean_stars, 2))


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

# load the Yelp dataset


# create a scatter plot of star rating vs review count
plt.scatter(df['stars'], df['review_count'], alpha=0.1)
plt.xlabel('Star rating')
plt.ylabel('Review count')
plt.show()


# In[9]:


import pandas as pd

# Load Yelp dataset


# Filter for restaurants only
restaurants = df[df["categories"].str.contains("Restaurants")]

# Group by business name and calculate the mean review count
restaurant_review_counts = restaurants.groupby("name")["review_count"].mean()

# Sort by review count in descending order and take the top 10
top_10_restaurants = restaurant_review_counts.sort_values(ascending=False)

top_10_restaurants.head(10)

