

# Iteratively made to extact tweets throughout the day for single person
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

subject = "Stocki_zen"

sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("NiharR007997")
nextbutton = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
nextbutton.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("Nihar@007")
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)
sleep(3)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

sleep(3)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()
sleep(4)

# UserTag = UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
# Timestamp = driver.find_element(By.XPATH,"//time").get_attribute("datetime")
# Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
# Reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
# Like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text


UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]
articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
while True:
    for article in articles:
        # UserTag = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[4]/div/div/article/div/div/div[2]/div[2]/div[1]").text
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        UserTags.append(UserTag)

        Timestamp = driver.find_element(By.XPATH,"//time").get_attribute("datetime")
        TimeStamps.append(Timestamp)

        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)

        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)

        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)

        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break

print("Success")
df = pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes)
                  ,columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes'])

df.head()

df.to_excel(r"/Users/Business/Desktop/TweetData/tweets_live.xlsx",index=False)

# import os
# os.system('start "Numbers" "/Users/Business/Desktop/TweetData/tweets_live.xlsx"')
