from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.skill_extractor import extract_skills


def calculate_job_match(resume_text: str, job_description: str):
    """
    Compare resume and job description using:
    1. TF-IDF + Cosine Similarity
    2. Skill Matching

    Returns:
    - Job match percentage
    - Matched skills
    - Missing skills
    """

    # ---------------------------------------------------
    # Step 1: TF-IDF Similarity
    # ---------------------------------------------------
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    tfidf_score = similarity * 100

    # ---------------------------------------------------
    # Step 2: Extract Technical Skills
    # ---------------------------------------------------
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    resume_set = {skill.lower() for skill in resume_skills}

    # ---------------------------------------------------
    # Step 3: Find Matched & Missing Skills
    # ---------------------------------------------------
    matched_keywords = [
        skill for skill in job_skills
        if skill.lower() in resume_set
    ]

    missing_keywords = [
        skill for skill in job_skills
        if skill.lower() not in resume_set
    ]

    # ---------------------------------------------------
    # Step 4: Skill Match Score
    # ---------------------------------------------------
    if len(job_skills) > 0:
        skill_score = (len(matched_keywords) / len(job_skills)) * 100
    else:
        skill_score = 0

    # ---------------------------------------------------
    # Step 5: Final Score
    # ---------------------------------------------------
    final_score = (0.7 * skill_score) + (0.3 * tfidf_score)

    match_percentage = round(final_score, 2)

    # ---------------------------------------------------
    # Step 6: Return Result
    # ---------------------------------------------------
    return {
        "job_match": match_percentage,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords
    }