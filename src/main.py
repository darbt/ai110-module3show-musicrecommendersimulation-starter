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

    # Starter example profile. Keys must match those read by score_song.
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_valence": 0.85,
        "target_danceability": 0.80,
        "target_bpm": 120,
        "likes_acoustic": False,
        "favorite_artist": "Neon Echo",
    }

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
