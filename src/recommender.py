import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py

    Reads each row into a dictionary keyed by the CSV header. Numeric
    fields (id and all audio features) are converted to floats; text
    fields are left as strings.
    """
    numeric_fields = {
        "id",
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in numeric_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)
    return songs

# Weights for each scoring component (sum to 100), from the Algorithm Recipe.
WEIGHTS = {
    "genre": 25,
    "mood": 25,
    "energy": 15,
    "valence": 10,
    "danceability": 8,
    "bpm": 7,
    "acousticness": 7,
    "artist": 3,
}

# BPM is not on a 0–1 scale, so differences are normalized by this range.
BPM_MIN = 60
BPM_MAX = 168
BPM_RANGE = BPM_MAX - BPM_MIN

# Component names differ from song dict keys only for BPM (stored as tempo_bpm).
SONG_KEYS = {"bpm": "tempo_bpm"}


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences using the Algorithm Recipe.

    Component weights (sum to 100):
        Genre 25, Mood 25, Energy 15, Valence 10,
        Danceability 8, BPM 7, Acousticness 7, Artist 3.

    Categorical components (genre, mood, artist) award full weight on a
    case-insensitive match and zero otherwise. Numeric components award
    weight * similarity, where similarity is 1 minus the normalized distance
    between the user's target and the song's value (clamped to [0, 1]).

    Returns a tuple of (score, reasons), where score is the total out of 100
    and reasons is a list of human-readable strings explaining the score.
    """
    score = 0.0
    reasons: List[str] = []

    def categorical(component: str, pref_key: str, label: str) -> None:
        nonlocal score
        pref = user_prefs.get(pref_key)
        if pref is None:
            return
        weight = WEIGHTS[component]
        song_key = SONG_KEYS.get(component, component)
        song_value = str(song.get(song_key, "")).strip().lower()
        if str(pref).strip().lower() == song_value:
            score += weight
            reasons.append(f"{label} matches '{pref}' (+{weight})")
        else:
            reasons.append(
                f"{label} '{song.get(component)}' differs from '{pref}' (+0)"
            )

    def numeric(component: str, target: float, label: str, scale: float) -> None:
        nonlocal score
        weight = WEIGHTS[component]
        song_key = SONG_KEYS.get(component, component)
        song_value = float(song[song_key])
        distance = abs(float(target) - song_value) / scale
        similarity = max(0.0, 1.0 - distance)
        earned = weight * similarity
        score += earned
        reasons.append(
            f"{label} {song_value} vs target {target} "
            f"(+{round(earned, 1)} of {weight})"
        )

    categorical("genre", "favorite_genre", "Genre")
    categorical("mood", "favorite_mood", "Mood")

    if user_prefs.get("target_energy") is not None:
        numeric("energy", user_prefs["target_energy"], "Energy", scale=1.0)
    if user_prefs.get("target_valence") is not None:
        numeric("valence", user_prefs["target_valence"], "Valence", scale=1.0)
    if user_prefs.get("target_danceability") is not None:
        numeric("danceability", user_prefs["target_danceability"], "Danceability", scale=1.0)
    if user_prefs.get("target_bpm") is not None:
        numeric("bpm", user_prefs["target_bpm"], "BPM", scale=BPM_RANGE)

    acoustic_target = _acoustic_target(user_prefs)
    if acoustic_target is not None:
        numeric("acousticness", acoustic_target, "Acousticness", scale=1.0)

    categorical("artist", "favorite_artist", "Artist")

    return round(score, 1), reasons


def _acoustic_target(user_prefs: Dict) -> Optional[float]:
    """
    Resolves the acousticness target, supporting either a numeric
    'target_acousticness' preference or the boolean 'likes_acoustic'
    (True -> 1.0, False -> 0.0). Returns None if neither is provided.
    """
    if user_prefs.get("target_acousticness") is not None:
        return float(user_prefs["target_acousticness"])
    if user_prefs.get("likes_acoustic") is not None:
        return 1.0 if user_prefs["likes_acoustic"] else 0.0
    return None

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py

    Scores every song against the user's preferences, then returns the top k
    as (song_dict, score, explanation) tuples sorted from highest score to
    lowest. The explanation joins the per-component reasons from score_song.
    """
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in scored[:k]
    ]
