# Emoji Extractor

This repo includes the following:
* `Proxi Code Challenge.ipynb` is the notebook containing code and explanations that connect to solving the problem.
    * Running the notebook requires a few things: first you must download Google's pre-trained model (1.5 GB) [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit).
    * You must also install gensim `conda install -c conda-forge gensim` to load the file.
    * Furthermore, you must have the following libraries of the latest versions installed: emoji, numpy, pandas, sklearn
* `emoji_appy.py` is my scratch pad, rough draft of `app.py`.
* `activity.txt`,`person.txt`, `thing.txt`, `time.txt`, `mood.txt`, and `place.txt` are files I used as test input to evaluate the quality of my model.  
* `emoji_dict.csv` contains all emojis from the emoji API with their corresponding label calculated by my model.
* `app.py` is where final tasks are completed. Routing might need editing.


