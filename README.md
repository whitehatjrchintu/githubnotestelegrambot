# Github notes telegram bot

With this telegram bot you can **create notes on [GitHub](https://www.github.com). You can even read [GitHub](https://www.github.com) uploaded files.** This TG bot is **heroku** based. Now before you continue i recommend you to read [**Prerequisites**](https://github.com/whitehatjrchintu/githubnotestelegrambot#Prerequisites-) section and [**What this bot can do?**](https://github.com/whitehatjrchintu/githubnotestelegrambot#What-this-bot-can-do) section.

## Example:-

screenshot 1 | screenshot 2
--- | ---
![photo_2021-10-20_15-46-43](https://user-images.githubusercontent.com/74552895/146686403-5cc7a948-c90f-4ac2-a497-2a755f1b96c6.PNG) | ![photo_2021-10-20_15-46-51](https://user-images.githubusercontent.com/74552895/146686413-8fabad3f-2020-4086-8a56-35171a0ba9bb.PNG)

## Prerequisites:-
<details>
<summary>
  :information_source: Important information.
</summary>

  1. Create account on [GitHub](https://www.github.com) (if you haven't for only this script. i will recomment not to use personal account.).
  2. Create account on [Heroku](https://dashboard.heroku.com) (if you haven't).
  3. Create account on [Telegram](https://web.telegram.org) (if you haven't).
  4. Go to [my.telegram.org/auth](https://my.telegram.org/auth), login and create app. Check [how to create app on telegram](https://core.telegram.org/api/obtaining_api_id). Now save api_id and api_hash which you got from [my.telegram.org/auth](https://my.telegram.org/auth).
  5. Create a telegram bot by using [Bot Father](https://t.me/botfather). Check [how to create bot in telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot). [Bot Father](https://t.me/botfather) will give you bot token save that token.
  6. Create repository on GitHub and create 4 empty files in the same repository named as instagram.txt, youtube.txt, notes.txt and other.txt.
  7. Create GitHub access token. Check [how to create GitHub access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Now save GitHub access token.
  8. So now you have saved **nine** things:-
		- api_id
		- api_hash
		- bot_token
		- github_access_token
		- github_repository_link
		- instagram_file_from_same_repository
		- youtube_file_from_same_repository
		- notes_file_from_same_repository
		- other_file_from_same_repository
</details>

## How to use?
<details>
  <summary>
    Steps to use.
  </summary>
	
#### Step 1:
- Just git clone this repository.

   `git clone https://github.com/whitehatjrchintu/githubnotestelegrambot.git`
   
   `cd githubnotestelegrambot`

- Or download this [repository](https://github.com/whitehatjrchintu/githubnotestelegrambot/archive/main.zip) as zip.
#### Step 2:
- Now create repository (i will recommend to create private repository.) in your github account and upload all files.
#### Step 3:
- Copy your github repository's link and paste after **?template=** in this link `https://www.heroku.com/deploy/?template=`. Like this:-

   `https://www.heroku.com/deploy/?template=https://github.com/whitehatjrchintu/githubnotestelegrambot`
#### Step 5:
- Now enter App name in **app_name** and **api_id**, **api_hash**, **bot_token**, **github_access_token**, **github_repository_link**, **instagram_file_from_same_repository**, **youtube_file_from_same_repository**, **notes_file_from_same_repository** and **other_file_from_same_repository** which you saved/did in above steps, in **respective** asked field. Then click **Deploy app**.
#### Step 6:
- Finally go to your bot, click start button and save your notes.
</details>

## What this bot can do?
<details>
	<summary>
		List of commands
	</summary>
	

|commands|mean|
|---|---|
|#ls|list files that are in your github current repository.|
|#read|read a particular file which is available in your current repository. like:- #read notes.txt|
|#get|download files that are in your github current repository. like:- #get notes.txt|
|youtube urls|send youtube urls and it will save those urls in your github current repository's youtube.txt.|
|instagram urls|send instagram urls and it will save those urls in your github current repository's instagram.txt.|
|#other text|send a simple text/message and it will save that text/message content into other.txt. like:- #other sample_text|
|a txt file|send a txt file and it will copy that txt file's content into notes.txt|
	
</details>

### If you found any mistake or have any suggestion let me know i will correct/apply that.	
## Meant for educational purpose only. I am not responsible if github or telegram block your account.
