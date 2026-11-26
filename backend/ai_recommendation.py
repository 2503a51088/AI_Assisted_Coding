from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_events(interests, events, top_n=5):
    """
    Recommend events based on a student's interests.

    interests: Student interests as text.
    events: List of event dictionaries.
    top_n: Maximum number of recommendations.
    """

    if not interests or not interests.strip():
        return []

    if not events:
        return []

    # Prepare event descriptions
    event_texts = []

    for event in events:
        title = event.get("title", "")
        description = event.get("description", "")

        text = f"{title} {description}"
        event_texts.append(text)

    # Convert interests and event descriptions into numerical vectors
    documents = [interests] + event_texts

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Calculate similarity between interests and events
    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    # Sort events by similarity score
    ranked_indices = similarity_scores.argsort()[::-1]

    recommendations = []

    for index in ranked_indices[:top_n]:
        score = float(similarity_scores[index])

        if score > 0:
            recommended_event = events[index].copy()
            recommended_event["match_score"] = round(score * 100, 2)

            recommendations.append(recommended_event)

    return recommendations