import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV
df = pd.read_csv('netflix_titles.csv')

# Drop NaN for available columns
cols_to_check = [c for c in ['type', 'rating', 'duration'] if c in df.columns]
df = df.dropna(subset=cols_to_check)

# --- Bar chart ---
type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color=['blue', 'orange'])
plt.title('Number of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('plot_movies_vs_tv.png')  # save chart

# --- Pie chart ---
ratings_counts = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(ratings_counts, labels=ratings_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('plot_ratings_pie.png')

# --- Histogram ---
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '', regex=False).astype(int)

plt.figure(figsize=(8, 6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('plot_movie_duration_hist.png')


