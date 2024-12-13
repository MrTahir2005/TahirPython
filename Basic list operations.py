# 1. Basic List Operations
# List of favorite movies
movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Forrest Gump"]

# Add a new movie
movies.append("The Shawshank Redemption")
print("After adding a new movie:", movies)

# Remove a movie by name
movie_to_remove = "Interstellar"
if movie_to_remove in movies:
    movies.remove(movie_to_remove)
print("After removing a movie:", movies)

# Find the index of a specific movie
movie_to_find = "The Matrix"
if movie_to_find in movies:
    index = movies.index(movie_to_find)
    print(f"The index of '{movie_to_find}' is:", index)
else:
    print(f"'{movie_to_find}' is not in the list.")
