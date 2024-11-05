# sentiment-analysis-on-twitter-comments
**playwright-venv:**  
A Python virtual environment set up to use the Playwright framework for crawling specific Twitter comments. Twitter comments are identified by the `"user_names"` and `"post_ids"` variables in `comments_crawler.py`, which together specify a unique Twitter post. The post and comments are then saved in a dedicated directory, organized by `"user_names"` and `"post_ids"`.

**sentiment_analysis.py:**  
This script uses the `"persiannlp/mt5-small-parsinlu-sentiment-analysis"` open-source hugging face models to perform sentiment analysis on all comments collected in the previous step. There are larger models like this:
`"persiannlp/mt5-base-parsinlu-sentiment-analysis"`
`"persiannlp/mt5-large-parsinlu-sentiment-analysis"`

Note that the size of the model is about 1.2GB and I haven't uploaded it in this repo. you should download it yourself to run the code on your pc locally.
