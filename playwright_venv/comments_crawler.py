################ libararies
from playwright.sync_api import sync_playwright
import time
import os

################ twitter account information
user_name = "mz_mask77"
password = "MZ@654321"

################ start playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=200)
page = browser.new_page()

################  sign in to Twitter
base_address = "https://x.com/login"
page.goto(base_address)
#### username
page.locator("xpath=.//input[@autocapitalize='sentences']").fill(f"{user_name}")
time.sleep(1)
page.get_by_text("Next").click()
#### password
page.locator("xpath=.//input[@autocomplete='current-password']").fill(f"{password}")
time.sleep(1)
page.get_by_text("Log in").click()
#### accept cookies
page.get_by_text("Accept all cookies").click() # click accept cookies!!
time.sleep(1)

################ post crawling
#### twitter post address
user_names = ["drpezeshkian"]
post_ids = ["1850279442444333246"]

for user_name, post_id in zip(user_names, post_ids):
    twitter_URL = f"https://x.com/{user_name}/status/{post_id}"

    #### go to the page
    page.goto(twitter_URL)
    time.sleep(5)

    #### Prepare folder for saving comments
    post_folder = f"{user_name}/{post_id}"
    if not os.path.exists(post_folder):
        os.makedirs(post_folder)

    #### Crawling the Twitter post defined by twitter_URL variable
    max_comment_to_crawl = 1000
    comments_counter = 0
    collected_comments = set()

    while comments_counter < max_comment_to_crawl:
        comments = page.locator("xpath=.//div[@data-testid='tweetText']") # all comments of a post in twitter
        print(comments.count())
        
        for i in range(comments.count()):
            comment_text = comments.nth(i).inner_text()

            if comment_text not in collected_comments: # ignore duplicate comment
                collected_comments.add(comment_text)
                comments_counter += 1
                print(f"Comment {comments_counter}: {comment_text}")

                with open(f"{post_folder}/{comments_counter}.txt", "w", encoding="utf-8") as f: # save each comment in a seperate txt file
                    f.write(comment_text)

                if comments_counter >= max_comment_to_crawl: # break if we have crawled enough comments defined by max_comment_to_crawl variable
                    break

        if comments_counter < max_comment_to_crawl:  # scroll down if we have not reached max_comment_to_crawl variable
            previous_height = page.evaluate("document.body.scrollHeight")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)  # wait for new content to load
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == previous_height:
                print("No more comments found.")
                break  # break if there is no more comment






