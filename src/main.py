"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    # Works when run as a package: `python -m src.main` (from the project root)
    from .recommender import load_songs, recommend_songs
except ImportError:
    # Works when run as a script from inside src/: `python main.py`
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Three distinct listener profiles. Keys must match those read by score_song.

    # 1. High-energy pop/dance fan who wants upbeat, danceable tracks.
    exciting_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
        "target_valence": 0.85,
        "target_danceability": 0.85,
        "target_bpm": 125,
        "likes_acoustic": False,
        "favorite_artist": "Neon Echo",
    }

    # 2. Chill study listener who prefers calm, acoustic, low-tempo tracks.
    chill_study = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "target_valence": 0.55,
        "target_danceability": 0.55,
        "target_bpm": 75,
        "likes_acoustic": True,
        "favorite_artist": "LoRoom",
    }

    # 3. Intense rock/metal fan who wants loud, fast, driving tracks.
    heavy_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "target_valence": 0.45,
        "target_danceability": 0.60,
        "target_bpm": 160,
        "likes_acoustic": False,
        "favorite_artist": "Voltline",
    }

    # --- Adversarial / edge-case profiles (meant to trip up the scorer) ---

    # A. Type-confusion: likes_acoustic is the STRING "False", not the bool.
    #    A non-empty string is truthy, so this flips to "prefers acoustic".
    string_bool_bug = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "likes_acoustic": "False",
    }

    # B. Contradictory: wants chill + acoustic but ALSO high energy + fast BPM.
    #    No real song fits, yet the scorer sums each part in isolation.
    contradiction = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.95,
        "target_danceability": 0.95,
        "target_bpm": 160,
        "likes_acoustic": True,
    }

    # C. Numeric-only exploit: nonsense genre/mood/artist, but audio targets
    #    tuned to a specific song — it still scores high on "soft" points.
    numeric_exploit = {
        "favorite_genre": "zzz",
        "favorite_mood": "zzz",
        "favorite_artist": "zzz",
        "target_energy": 0.95,
        "target_valence": 0.83,
        "target_danceability": 0.90,
        "target_bpm": 128,
        "likes_acoustic": False,
    }

    profiles = {
        "Exciting Pop": exciting_pop,
        "Chill Study": chill_study,
        "Heavy Rock": heavy_rock,
        "[EDGE] String-bool bug": string_bool_bug,
        "[EDGE] Contradiction": contradiction,
        "[EDGE] Numeric-only exploit": numeric_exploit,
    }

    for name, user_prefs in profiles.items():
        print(f"\n### Profile: {name} ###")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(recommendations)


def print_recommendations(recommendations: list) -> None:
    """Render the recommender's output in a clean, readable terminal layout."""
    width = 60

    print()
    print("=" * width)
    print("TOP RECOMMENDATIONS".center(width))
    print("=" * width)

    if not recommendations:
        print("\nNo recommendations to show yet.\n")
        return

    for rank, rec in enumerate(recommendations, start=1):
        # Each item is (song, score, reasons). `reasons` may be a list of
        # strings from the scoring function, or a single explanation string.
        song, score, reasons = rec

        title = song["title"]
        artist = song.get("artist", "")
        heading = f"{rank}. {title}"
        if artist:
            heading += f" — {artist}"

        print()
        print(heading)
        print(f"   Final score: {score:.2f}")

        # Normalize reasons into a list so we can print one per line.
        if isinstance(reasons, str):
            reason_list = [reasons] if reasons else []
        else:
            reason_list = list(reasons)

        if reason_list:
            print("   Reasons:")
            for reason in reason_list:
                print(f"     • {reason}")
        else:
            print("   Reasons: (none provided)")

    print()
    print("=" * width)
    print()


if __name__ == "__main__":
    main()
