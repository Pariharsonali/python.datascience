#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Supress Warnings

import warnings
warnings.filterwarnings('ignore')


# In[23]:


# Import the numpy and pandas packages

import numpy as np
import pandas as pd


# ## Task 1: Reading and Inspection
# 
# -  ### Subtask 1.1: Import and read
# 
# Import and read the movie database. Store it in a variable called `movies`.

# In[62]:


# Write your code for importing the csv file here
import pandas as pd
import numpy as np
movies = pd.read_csv("C:\\Users\\sonal\\Downloads\\Movie+Assignment+Data.csv")
movies


# -  ### Subtask 1.2: Inspect the dataframe
# 
# Inspect the dataframe's columns, shapes, variable types etc.

# In[25]:


# Write your code for inspection here
movies.head()


# In[26]:


movies.info


# In[27]:


movies.shape


# In[64]:


movies.columns


# In[7]:


movies.describe()


# In[28]:


movies.isnull()


# ## Task 2: Cleaning the Data
# 
# -  ### Subtask 2.1: Inspect Null values
# 
# Find out the number of Null values in all the columns and rows. Also, find the percentage of Null values in each column. Round off the percentages upto two decimal places.

# In[65]:


movies.isnull().sum(axis=0)


# In[71]:


# Write your code for column-wise null count
movies.isnull().sum(axis=1)
#we use any()


# In[11]:


# Write your code for row-wise null counmovues
movies.isnull().sum(axis = 1)


# In[12]:


# Write your code for column-wise null percentages here
movies.isnull().mean()*100


# -  ### Subtask 2.2: Drop unecessary columns
# 
# For this assignment, you will mostly be analyzing the movies with respect to the ratings, gross collection, popularity of movies, etc. So many of the columns in this dataframe are not required. So it is advised to drop the following columns.
# -  color
# -  director_facebook_likes
# -  actor_1_facebook_likes
# -  actor_2_facebook_likes
# -  actor_3_facebook_likes
# -  actor_2_name
# -  cast_total_facebook_likes
# -  actor_3_name
# -  duration
# -  facenumber_in_poster
# -  content_rating
# -  country
# -  movie_imdb_link
# -  aspect_ratio
# -  plot_keywords

# In[30]:


# Write your code for dropping the columns here. It is advised to keep inspecting the dataframe after each set of operations 

# Assuming you have a DataFrame called 'df' containing your data
# Replace 'df' with the actual name of your DataFrame

# Inspect the DataFrame before dropping columns
print(movies.head())

# List of columns to drop
columns_to_drop = ['color', 'director_facebook_likes', 'actor_1_facebook_likes',
                   'actor_2_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name',
                   'cast_total_facebook_likes', 'actor_3_name', 'duration',
                   'facenumber_in_poster', 'content_rating', 'country','movie_imdb_link','aspect_ratio','plot_keywords']

# Drop the unnecessary columns
movies.drop(columns_to_drop, axis=1, inplace=True)

# Inspect the DataFrame after dropping columns
print(movies.head())


# In[73]:


movies.head()


# -  ### Subtask 2.3: Drop unecessary rows using columns with high Null percentages
# 
# Now, on inspection you might notice that some columns have large percentage (greater than 5%) of Null values. Drop all the rows which have Null values for such columns.

# In[76]:


import pandas as pd

# Assuming you have a DataFrame called 'df' containing your data
# Replace 'df' with the actual name of your DataFrame

# Calculate null percentages for each column
#null_percentages = movies.isnull().mean()

# Set the threshold for null percentages
#threshold = 0.5

# Identify rows to drop based on the threshold
#rows_to_drop = null_percentages[null_percentages > threshold].index

# Drop the identified rows from the DataFrame
#movies.drop(rows_to_drop, inplace=True)

print(movies.isna().sum(axis=0)/movies.shape[0] > 0.05)
movies.dropna(subset=['gross', 'budget'], inplace=True)


# In[77]:


movies.head()


# -  ### Subtask 2.4: Drop unecessary rows
# 
# Some of the rows might have greater than five NaN values. Such rows aren't of much use for the analysis and hence, should be removed.

# In[78]:


# Write your code for dropping the rows here
movies.drop(rows_to_drop, inplace = True)


# In[79]:


movies.head()


# -  ### Subtask 2.5: Fill NaN values
# 
# You might notice that the `language` column has some NaN values. Here, on inspection, you will see that it is safe to replace all the missing values with `'English'`.

# In[80]:


# Write your code for filling the NaN values in the 'language' column here
import pandas as pd

# Assuming you have loaded your dataset into a pandas DataFrame called 'df'
movies['language'] = movies['language'].fillna('English')

# Now all the NaN values in the 'language' column will be replaced with 'English'


# In[81]:


movies.head()


# -  ### Subtask 2.6: Check the number of retained rows
# 
# You might notice that two of the columns viz. `num_critic_for_reviews` and `actor_1_name` have small percentages of NaN values left. You can let these columns as it is for now. Check the number and percentage of the rows retained after completing all the tasks above.

# In[82]:


# Write your code for checking number of retained rows here
retained_rows = len(movies)  # Number of rows after replacing missing values

print("Number of retained rows:", retained_rows)


# **Checkpoint 1:** You might have noticed that we still have around `77%` of the rows!

# ## Task 3: Data Analysis
# 
# -  ### Subtask 3.1: Change the unit of columns
# 
# Convert the unit of the `budget` and `gross` columns from `$` to `million $`.

# In[83]:


# Write your code for unit conversion here

import pandas as pd

# Assuming you have loaded your dataset into a pandas DataFrame called 'df'
movies['budget'] = movies['budget'] / 1000000  
movies['gross'] = movies['gross'] / 1000000  


# -  ### Subtask 3.2: Find the movies with highest profit
# 
#     1. Create a new column called `profit` which contains the difference of the two columns: `gross` and `budget`.
#     2. Sort the dataframe using the `profit` column as reference.
#     3. Extract the top ten profiting movies in descending order and store them in a new dataframe - `top10`

# In[91]:


# Write your code for creating the profit column  
movies['profit']= movies['budget']- movies['gross']


# In[93]:


# Write your code for sorting the dataframe here
sorted_movies = movies.sort_values( by = 'profit', ascending = True).head(10)


# In[92]:


top_10_profit_movies = movies.nlargest(10, 'profit')

# Write your code to get the top 10 profiting movies here


# In[87]:


movies.head()


# -  ### Subtask 3.3: Drop duplicate values
# 
# After you found out the top 10 profiting movies, you might have notice a duplicate value. So, it seems like the dataframe has duplicate values as well. Drop the duplicate values from the dataframe and repeat `Subtask 3.2`.

# In[94]:


# Write your code for dropping duplicate values here
movies.drop_duplicates(keep = False ,inplace = True)


# In[98]:


# Write code for repeating subtask 2 here
top10 = movies.sort_values('profit', ascending=False).head(10)
top10


# In[100]:


movies.head(10)


# **Checkpoint 2:** You might spot two movies directed by `James Cameron` in the list.

# -  ### Subtask 3.4: Find IMDb Top 250
# 
#     1. Create a new dataframe `IMDb_Top_250` and store the top 250 movies with the highest IMDb Rating (corresponding to the column: `imdb_score`). Also make sure that for all of these movies, the `num_voted_users` is greater than 25,000.
# Also add a `Rank` column containing the values 1 to 250 indicating the ranks of the corresponding films.
#     2. Extract all the movies in the `IMDb_Top_250` dataframe which are not in the English language and store them in a new dataframe named `Top_Foreign_Lang_Film`.

# In[102]:


# Write your code for extracting the top 250 movies as per the IMDb score here. Make sure that you store it in a new dataframe 
# and name that dataframe as 'IMDb_Top_250'
IMDb_Top_250 = movies.loc[movies['num_voted_users']> 25000].sort_values('imdb_score', ascending=False).head(250)
IMDb_Top_250['Rank'] = IMDb_Top_250['imdb_score'].rank(ascending=False, method='first')


# In[103]:


IMDb_Top_250.head(250)


# In[105]:


Top_Foreign_Lang_Film = IMDb_Top_250.loc[IMDb_Top_250['language'] != 'English']
# Write your code to extract top foreign language films from 'IMDb_Top_250' here


# In[106]:


Top_Foreign_Lang_Film.head(10)


# **Checkpoint 3:** Can you spot `Veer-Zaara` in the dataframe?

# - ### Subtask 3.5: Find the best directors
# 
#     1. Group the dataframe using the `director_name` column.
#     2. Find out the top 10 directors for whom the mean of `imdb_score` is the highest and store them in a new dataframe `top10director`. 

# In[107]:


# Write your code for extracting the top 10 directors here
director_score = movies.groupby('director_name').agg({'imdb_score': np.mean}).reset_index()
director_score.columns = ['director_name', 'mean_imdb_score']
top10director = director_score.sort_values('mean_imdb_score', ascending=False).head(10)
top10director


# **Checkpoint 4:** No surprises that `Damien Chazelle` (director of Whiplash and La La Land) is in this list.

# -  ### Subtask 3.6: Find popular genres
# 
# You might have noticed the `genres` column in the dataframe with all the genres of the movies seperated by a pipe (`|`). Out of all the movie genres, the first two are most significant for any film.
# 
# 1. Extract the first two genres from the `genres` column and store them in two new columns: `genre_1` and `genre_2`. Some of the movies might have only one genre. In such cases, extract the single genre into both the columns, i.e. for such movies the `genre_2` will be the same as `genre_1`.
# 2. Group the dataframe using `genre_1` as the primary column and `genre_2` as the secondary column.
# 3. Find out the 5 most popular combo of genres by finding the mean of the gross values using the `gross` column and store them in a new dataframe named `PopGenre`.

# In[108]:


# Write your code for extracting the first two genres of each movie here
movies['genre_1'] = movies['genres'].str.split('|').str[0]
movies['genre_2'] = movies['genres'].apply(lambda x: x.split('|')[1] if len(x.split('|')) > 1 else x.split('|')[0])


# In[109]:


movies_by_segment = movies.groupby(['genre_1', 'genre_2']) 
# Write your code for grouping the dataframe here


# In[110]:


Genre_group = movies_by_segment.agg({'gross': np.mean}).reset_index()# Write your code for getting the 5 most popular combo of genres here
Genre_group.columns = ['genre_1', 'genre_2', 'mean_gross']
PopGenre = Genre_group.sort_values('mean_gross', ascending=False).head(5)
# Write your code for getting the 5 most popular combo of genres here
PopGenre


# **Checkpoint 5:** Well, as it turns out. `Family + Sci-Fi` is the most popular combo of genres out there!

# -  ### Subtask 3.7: Find the critic-favorite and audience-favorite actors
# 
#     1. Create three new dataframes namely, `Meryl_Streep`, `Leo_Caprio`, and `Brad_Pitt` which contain the movies in which the actors: 'Meryl Streep', 'Leonardo DiCaprio', and 'Brad Pitt' are the lead actors. Use only the `actor_1_name` column for extraction. Also, make sure that you use the names 'Meryl Streep', 'Leonardo DiCaprio', and 'Brad Pitt' for the said extraction.
#     2. Append the rows of all these dataframes and store them in a new dataframe named `Combined`.
#     3. Group the combined dataframe using the `actor_1_name` column.
#     4. Find the mean of the `num_critic_for_reviews` and `num_user_for_review` and identify the actors which have the highest mean.

# In[111]:


# Write your code for creating three new dataframes here

Meryl_Streep = movies.loc[movies['actor_1_name'] == 'Meryl Streep'] # Include all movies in which Meryl_Streep is the lead


# In[112]:


Leo_Caprio = movies.loc[movies['actor_1_name'] == 'Leonardo DiCaprio']# Include all movies in which Leo_Caprio is the lead


# In[113]:


Brad_Pitt = movies.loc[movies['actor_1_name'] == 'Brad pitt'] # Include all movies in which Brad_Pitt is the lead


# In[114]:


# Write your code for combining the three dataframes here

Combined = pd.concat([Meryl_Streep, Leo_Caprio, Brad_Pitt])


# In[118]:


# Write your code for grouping the combined dataframe here
groupby_actors = Combined.groupby('actor_1_name')


# In[119]:


# Write the code for finding the mean of critic reviews and audience reviews here
groupby_actors.agg({'num_critic_for_reviews': np.mean, 'num_user_for_reviews': np.mean})


# **Checkpoint 6:** `Leonardo` has aced both the lists!
