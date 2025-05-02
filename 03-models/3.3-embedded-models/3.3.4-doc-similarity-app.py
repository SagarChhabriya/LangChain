from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load local embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# dataset
documents = [
    "Messi is a soccer player who is very good at scoring and passing the ball.",
    "Serena Williams is a tennis player who has won many big tournaments.",
    "Michael Jordan played basketball and is known as one of the best players ever.",
    "Usain Bolt is a runner who runs faster than almost anyone in the world.",
    "Tom Brady throws the football and has won many Super Bowls."
]

# Query
query = "who is the fastest runner?"

# Get Embeddings
doc_embeddings = model.encode(documents)
query_embedding = model.encode(query)


# Get cosine similarity
# The input/parameters to cosine_similarity must be 2D 
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the most similar doc
# Scores is a list. Assign the index to each value using enumerate. 
# Convert the enumerate returned tuples to a list.
# Sort the list on values second index i.e., index[1]
# return the max element (high similarity) which is on last index.

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("Query: ", query)
print("Best match", documents[index])
print("Similarity score: ", score)

# Output:
# Query:  who is the fastest runner?
# Best match Usain Bolt is a runner who runs faster than almost anyone in the world.
# Similarity score:  0.57063067