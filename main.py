import pandas as pd
from transformers import pipeline

# Load emotion classifier once
emotion_classifier = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion", top_k=None)

# Genre-emotion mapping
emotion_to_genres = {
    "joy": ["Comedy", "Animation", "Adventure"],
    "love": ["Romance", "Drama"],
    "sadness": ["Drama"],
    "anger": ["Action", "Thriller"],
    "surprise": ["Mystery", "Fantasy", "Adventure"],
    "fear": ["Horror", "Thriller"],
    "nostalgia": ["Drama", "Family", "Romance"],
    "loneliness": ["Drama", "Romance"],
    "hope": ["Drama", "Adventure"],
    "excitement": ["Action", "Adventure", "Sci-Fi"]
}


def get_prompt_emotions(prompt, top_n=2):
    results = emotion_classifier(prompt[:512])[0]
    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
    return [e['label'] for e in sorted_results[:top_n]]


def emotions_to_genres(emotions):
    matched_genres = set()
    for emotion in emotions:
        matched_genres.update(emotion_to_genres.get(emotion, []))
    return list(matched_genres)


def genre_match_score(movie_genres_str, target_genres):
    movie_genres = set(movie_genres_str.split("|"))
    return len(movie_genres.intersection(target_genres))


def recommend_movies(prompt, csv_path='movies.csv', top_n=3):
    print("Prompt:", prompt)

    # Step 1: Load data
    data = pd.read_csv(csv_path)
    print(f"Loaded {data.shape[0]} movies.")

    # Step 2: Get emotions from prompt
    emotions = get_prompt_emotions(prompt)
    print("Classified emotions:", emotions)

    # Step 3: Map emotions to genres
    target_genres = emotions_to_genres(emotions)
    print("Target genres:", target_genres)

    # Step 4: Score movies by genre match
    data['match_score'] = data['genres'].apply(lambda g: genre_match_score(g, target_genres))

    # Step 5: Recommend top movies
    recommended = data[data['match_score'] > 0].sort_values(by='match_score', ascending=False)
    top_recommendations = recommended[['title', 'genres', 'match_score']].head(top_n)

    print("\nTop Recommendations:")
    print(top_recommendations.to_string(index=False))


if __name__ == "__main__":
    prompt = "I'm feeling nostalgic and want something heartwarming"
    recommend_movies(prompt)
