# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

EchoMatch 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This reccomender is supposed to help find songs a user would most likely enjoy, based on a profile that defines their music taste. 
---

## 3. How the Model Works  

Explain your scoring approach in simple language. 
 
Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  

- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Each song uses the features: artist, energy, BPM, Valence, genre, acousteness, danceability, and mood.

Genre, I believe, is the most important when helping determine if a user will like a song. So that feature will have the highest max point. Energy and mood have the same amount of maxs points because I feel like energy and mood work hand in hand. Low energy is good for a chill or melanchily mood, High energy is good for a happy and excited mood, etc. I also include Artists which is just between Genre and Mood since people tend to like songs from the same Artist. Once we go down the line of features thats when the points start to decrease based on it's "obscurity".

The first starter logic that came from the chatbot only wanted to compare genre and mood on a numerical 0-1 scale. This logic needed to grow to include a lot more factors to make it more accurate. 

Because Genre has the highest max score points, the Ai might prioritize those points. The system may also focus more on a specific artist instead of branching out to newer ones. 
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The model uses a sing list of about 20 songs. Each song has its own genre and numerical features. There is only 20 songs so we are working with a very limited dataset. 

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

The system works well when working with very clear tastes. So someone who mainly pop will get reccommended pop and exciting songs. Same thing with someone who mainly like Heacy rock songs. 

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

One weakness that I discovered is that acousticness has no middle ground. Meaning that a song that is considered "mid-acoustic", won't be registered because there is no proper measurement for it. The song is either acoustic or not. 

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested profiles for exciting pop, a calm study vibe, and heavy rock. These profiles were very distinct so the songs that were reccomended made sense. What I did notice, however, is that because the reccomender chose 5 of the top matched songs no matter what, if there wasn't enough songs that matched the music perfectly, it will still choose songs from other genres, even if the score is extremely low, instead of just ending the list. 
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
I would defiently work with a much bigger dataset. I would also want to utiize a user's history and behavior so that the program can learn. Example, imolement a like system so the user can tell the program when it likes or dislikes a song so that it can learn for next time. 

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that there is a lot more that goes into reccomendation systems than I initially thought. There are many aspects to a song that a system has to consider. It's not only just based on genre and artist. The AI tools helped me understand how I should develop my scoring system since I had no idea where to start with that and it helped when needing to point out biases. If I were to extend this project, I belive that I would try to incorporate human interaction so that the program can learn. I would also update the scoring system. 