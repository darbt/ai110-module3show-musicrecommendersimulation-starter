# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Most real-life reccomendations work are based a lot on a user's behavior. This goes beyond just music. When you deliberatly like, save, subscribe to, or thumbs-down something, you are telling systems a lot of information. Recommenders also notice the things that we don't even think twice about, for example. skipping, replays, and completion rate. These behaviors let reccomendation systems know what you like and what you dislike and do its best to infer from there.  

Explain your design in plain language.

My design will mainly focus on the features of songs that are liked and the songs that are disliked or constantly skipped. 

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo

Each song will use, genre, energy, BPM, mood, danceability, and acoustics, 

- What information does your `UserProfile` store

The UserProfile will store a user's top three music genres, their top 5 favorite songs, and their top 5 favorite music artists, as well as their most listened song for the month. 

- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...

============================================================
                    TOP RECOMMENDATIONS                     
============================================================

1. Sunrise City — Neon Echo
   Final score: 98.10
   Reasons:
     • Genre matches 'pop' (+25); Mood matches 'happy' (+25); Energy 0.82 vs target 0.8 (+14.7 of 15); Valence 0.84 vs target 0.85 (+9.9 of 10); Danceability 0.79 vs target 0.8 (+7.9 of 8); BPM 118.0 vs target 120 (+6.9 of 7); Acousticness 0.18 vs target 0.0 (+5.7 of 7); Artist matches 'Neon Echo' (+3)

2. Rooftop Lights — Indigo Parade
   Final score: 68.10
   Reasons:
     • Genre 'indie pop' differs from 'pop' (+0); Mood matches 'happy' (+25); Energy 0.76 vs target 0.8 (+14.4 of 15); Valence 0.81 vs target 0.85 (+9.6 of 10); Danceability 0.82 vs target 0.8 (+7.8 of 8); BPM 124.0 vs target 120 (+6.7 of 7); Acousticness 0.35 vs target 0.0 (+4.5 of 7); Artist 'Indigo Parade' differs from 'Neon Echo' (+0)

3. Gym Hero — Max Pulse
   Final score: 67.50
   Reasons:
     • Genre matches 'pop' (+25); Mood 'intense' differs from 'happy' (+0); Energy 0.93 vs target 0.8 (+13.1 of 15); Valence 0.77 vs target 0.85 (+9.2 of 10); Danceability 0.88 vs target 0.8 (+7.4 of 8); BPM 132.0 vs target 120 (+6.2 of 7); Acousticness 0.05 vs target 0.0 (+6.6 of 7); Artist 'Max Pulse' differs from 'Neon Echo' (+0)

4. Basement Groove — The Low Enders
   Final score: 43.80
   Reasons:
     • Genre 'funk' differs from 'pop' (+0); Mood 'playful' differs from 'happy' (+0); Energy 0.78 vs target 0.8 (+14.7 of 15); Valence 0.86 vs target 0.85 (+9.9 of 10); Danceability 0.89 vs target 0.8 (+7.3 of 8); BPM 108.0 vs target 120 (+6.2 of 7); Acousticness 0.19 vs target 0.0 (+5.7 of 7); Artist 'The Low Enders' differs from 'Neon Echo' (+0)

5. Neon Overdrive — Circuit Fox
   Final score: 43.00
   Reasons:
     • Genre 'edm' differs from 'pop' (+0); Mood 'euphoric' differs from 'happy' (+0); Energy 0.95 vs target 0.8 (+12.8 of 15); Valence 0.83 vs target 0.85 (+9.8 of 10); Danceability 0.9 vs target 0.8 (+7.2 of 8); BPM 128.0 vs target 120 (+6.5 of 7); Acousticness 0.04 vs target 0.0 (+6.7 of 7); Artist 'Circuit Fox' differs from 'Neon Echo' (+0)

============================================================

Edge Cases: 

### Profile: [EDGE] String-bool bug ###

============================================================
                    TOP RECOMMENDATIONS                     
============================================================

1. Library Rain — Paper Lanterns
   Final score: 71.00
   Reasons:
     • Genre matches 'lofi' (+25); Mood matches 'chill' (+25); Energy 0.35 vs target 0.35 (+15.0 of 15); Acousticness 0.86 vs target 1.0 (+6.0 of 7)

2. Midnight Coding — LoRoom
   Final score: 68.90
   Reasons:
     • Genre matches 'lofi' (+25); Mood matches 'chill' (+25); Energy 0.42 vs target 0.35 (+13.9 of 15); Acousticness 0.71 vs target 1.0 (+5.0 of 7)

3. Spacewalk Thoughts — Orbit Bloom
   Final score: 45.40
   Reasons:
     • Genre 'ambient' differs from 'lofi' (+0); Mood matches 'chill' (+25); Energy 0.28 vs target 0.35 (+14.0 of 15); Acousticness 0.92 vs target 1.0 (+6.4 of 7)

4. Focus Flow — LoRoom
   Final score: 44.70
   Reasons:
     • Genre matches 'lofi' (+25); Mood 'focused' differs from 'chill' (+0); Energy 0.4 vs target 0.35 (+14.2 of 15); Acousticness 0.78 vs target 1.0 (+5.5 of 7)

5. Coffee Shop Stories — Slow Stereo
   Final score: 20.90
   Reasons:
     • Genre 'jazz' differs from 'lofi' (+0); Mood 'relaxed' differs from 'chill' (+0); Energy 0.37 vs target 0.35 (+14.7 of 15); Acousticness 0.89 vs target 1.0 (+6.2 of 7)

============================================================


### Profile: [EDGE] Contradiction ###

============================================================
                    TOP RECOMMENDATIONS                     
============================================================

1. Midnight Coding — LoRoom
   Final score: 69.10
   Reasons:
     • Genre matches 'lofi' (+25); Mood matches 'chill' (+25); Energy 0.42 vs target 0.95 (+7.0 of 15); Danceability 0.62 vs target 0.95 (+5.4 of 8); BPM 78.0 vs target 160 (+1.7 of 7); Acousticness 0.71 vs target 1.0 (+5.0 of 7)

2. Library Rain — Paper Lanterns
   Final score: 68.40
   Reasons:
     • Genre matches 'lofi' (+25); Mood matches 'chill' (+25); Energy 0.35 vs target 0.95 (+6.0 of 15); Danceability 0.58 vs target 0.95 (+5.0 of 8); BPM 72.0 vs target 160 (+1.3 of 7); Acousticness 0.86 vs target 1.0 (+6.0 of 7)

3. Focus Flow — LoRoom
   Final score: 44.20
   Reasons:
     • Genre matches 'lofi' (+25); Mood 'focused' differs from 'chill' (+0); Energy 0.4 vs target 0.95 (+6.8 of 15); Danceability 0.6 vs target 0.95 (+5.2 of 8); BPM 80.0 vs target 160 (+1.8 of 7); Acousticness 0.78 vs target 1.0 (+5.5 of 7)

4. Spacewalk Thoughts — Orbit Bloom
   Final score: 40.60
   Reasons:
     • Genre 'ambient' differs from 'lofi' (+0); Mood matches 'chill' (+25); Energy 0.28 vs target 0.95 (+5.0 of 15); Danceability 0.41 vs target 0.95 (+3.7 of 8); BPM 60.0 vs target 160 (+0.5 of 7); Acousticness 0.92 vs target 1.0 (+6.4 of 7)

5. Neon Overdrive — Circuit Fox
   Final score: 27.80
   Reasons:
     • Genre 'edm' differs from 'lofi' (+0); Mood 'euphoric' differs from 'chill' (+0); Energy 0.95 vs target 0.95 (+15.0 of 15); Danceability 0.9 vs target 0.95 (+7.6 of 8); BPM 128.0 vs target 160 (+4.9 of 7); Acousticness 0.04 vs target 1.0 (+0.3 of 7)

============================================================


### Profile: [EDGE] Numeric-only exploit ###

============================================================
                    TOP RECOMMENDATIONS                     
============================================================

1. Neon Overdrive — Circuit Fox
   Final score: 46.70
   Reasons:
     • Genre 'edm' differs from 'zzz' (+0); Mood 'euphoric' differs from 'zzz' (+0); Energy 0.95 vs target 0.95 (+15.0 of 15); Valence 0.83 vs target 0.83 (+10.0 of 10); Danceability 0.9 vs target 0.9 (+8.0 of 8); BPM 128.0 vs target 128 (+7.0 of 7); Acousticness 0.04 vs target 0.0 (+6.7 of 7); Artist 'Circuit Fox' differs from 'zzz' (+0)

2. Gym Hero — Max Pulse
   Final score: 45.30
   Reasons:
     • Genre 'pop' differs from 'zzz' (+0); Mood 'intense' differs from 'zzz' (+0); Energy 0.93 vs target 0.95 (+14.7 of 15); Valence 0.77 vs target 0.83 (+9.4 of 10); Danceability 0.88 vs target 0.9 (+7.8 of 8); BPM 132.0 vs target 128 (+6.7 of 7); Acousticness 0.05 vs target 0.0 (+6.6 of 7); Artist 'Max Pulse' differs from 'zzz' (+0)

3. Sunrise City — Neon Echo
   Final score: 42.20
   Reasons:
     • Genre 'pop' differs from 'zzz' (+0); Mood 'happy' differs from 'zzz' (+0); Energy 0.82 vs target 0.95 (+13.1 of 15); Valence 0.84 vs target 0.83 (+9.9 of 10); Danceability 0.79 vs target 0.9 (+7.1 of 8); BPM 118.0 vs target 128 (+6.4 of 7); Acousticness 0.18 vs target 0.0 (+5.7 of 7); Artist 'Neon Echo' differs from 'zzz' (+0)

4. Basement Groove — The Low Enders
   Final score: 41.40
   Reasons:
     • Genre 'funk' differs from 'zzz' (+0); Mood 'playful' differs from 'zzz' (+0); Energy 0.78 vs target 0.95 (+12.5 of 15); Valence 0.86 vs target 0.83 (+9.7 of 10); Danceability 0.89 vs target 0.9 (+7.9 of 8); BPM 108.0 vs target 128 (+5.7 of 7); Acousticness 0.19 vs target 0.0 (+5.7 of 7); Artist 'The Low Enders' differs from 'zzz' (+0)

5. Rooftop Lights — Indigo Parade
   Final score: 40.60
   Reasons:
     • Genre 'indie pop' differs from 'zzz' (+0); Mood 'happy' differs from 'zzz' (+0); Energy 0.76 vs target 0.95 (+12.2 of 15); Valence 0.81 vs target 0.83 (+9.8 of 10); Danceability 0.82 vs target 0.9 (+7.4 of 8); BPM 124.0 vs target 128 (+6.7 of 7); Acousticness 0.35 vs target 0.0 (+4.5 of 7); Artist 'Indigo Parade' differs from 'zzz' (+0)

============================================================

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



