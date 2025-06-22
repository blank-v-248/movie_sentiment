# 🎬 Emotion-Based Movie Recommender

This is a Python tool that recommends movies based on the emotional content of a natural language prompt.

It works by:
1. Extracting **emotions** from the input prompt using a pretrained Hugging Face model.
2. Mapping those emotions to movie **genres**.
3. Scoring movies based on how many genre tags match and recommending the best matches.

---

## 🚀 Example Usage

main.py --prompt "I'm feeling nostalgic and want something heartwarming"

## 🚀 Example Output
Loaded 87585 movies.
Classified emotions: ['love', 'joy']
Target genres: ['Romance', 'Animation', 'Adventure', 'Drama', 'Comedy']

Top Recommendations:
                                                                                                                                            title                                                            genres  match_score
                                                                                      Pretty Guardian Sailor Moon Eternal The Movie Part 1 (2021)           Action|Adventure|Animation|Comedy|Drama|Fantasy|Romance            5
Revolutionary Girl Utena: Adolescence of Utena (a.k.a. Revolutionary Girl Utena the Movie) (Shoujo kakumei Utena: Adolescence mokushiroku) (1999)           Action|Adventure|Animation|Comedy|Drama|Fantasy|Romance            5
                                                                                                Wonderful World of the Brothers Grimm, The (1962) Adventure|Animation|Children|Comedy|Drama|Fantasy|Musical|Romance            5

---                                                                                                ---.
## 📄 Dataset

This project uses the [MovieLens 32M dataset](https://grouplens.org/datasets/movielens/) as a source.

> **Citation:**  
> F. Maxwell Harper and Joseph A. Konstan. 2015.  
> *The MovieLens Datasets: History and Context.*  
> ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19.  
> [https://doi.org/10.1145/2827872](https://doi.org/10.1145/2827872)
