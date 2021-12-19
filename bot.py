from pyrogram.types import Message
from pyrogram import Client, filters
from github import Github
from os import environ
import os

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
github_access_token = environ["GITHUB_ACCESS_TOKEN"]
github_repository_link = environ["GITHUB_REPOSITORY_LINK"]
instagram_file_from_same_repository = environ["INSTGRAM_FILE_FROM_SAME_REPOSITORY"]
other_file_from_same_repository = environ["OTHER_FILE_FROM_SAME_REPOSITORY"]
youtube_file_from_same_repository = environ["YOUTUBE_FILE_FROM_SAME_REPOSITORY"]
notes_file_from_same_repository = environ["NOTES_FILE_FROM_SAME_REPOSITORY"]
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.command(["start"]))
def start(client: Client, message: Message):
        msg = app.send_message(message.from_user.id,"Welcome",reply_to_message_id=message.message_id)

@app.on_message(filters.regex(r'#read'))
def read_files(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)

        #getting text
        msg_textedd = (message.text)
        msg_texted = msg_textedd.lstrip("#read ")
        print(msg_texted)
        
        #getting repo and files
        repo = g.get_repo(github_repository_link)
        contents = repo.get_contents(msg_texted, ref="main")
        reading_file = contents.decoded_content.decode()
        
        #sending message
        msg = app.send_message(chat_id=message.from_user.id, reply_to_message_id=message.message_id, text="The content of " + "<b>" + msg_texted + "</b>" + " file:" + "\n\n" + reading_file,parse_mode="html")

        #delete message
        working_msg.delete()

@app.on_message(filters.regex(r'#ls'))
def list_files(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)
        
        #getting repo and files
        repo = g.get_repo(github_repository_link)

        all_files = []
        contents = repo.get_contents("")
        while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                else:
                    file = file_content
                    all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

        all_filess = str(all_files).lstrip("['").rstrip("']").replace("'","")
        
        #sending message
        msg = app.send_message(chat_id=message.from_user.id, reply_to_message_id=message.message_id, text="These files are in your current repository:" + "\n\n"+ "<b>" + all_filess + "</b>",parse_mode="html")

        #delete message
        working_msg.delete()

@app.on_message(filters.regex(r'#get'))
def get(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)
        
        #getting text
        msg_textedd = (message.text)
        msg_texted = msg_textedd.lstrip("#get ")
        
        #getting repo and file
        repo = g.get_repo(github_repository_link)
        contents = repo.get_contents(msg_texted, ref="main")
        aaa = contents.decoded_content.decode()

        #copying old with new
        f = open("file.txt","w")
        f.write(aaa)
        f.close()
        orig = "file.txt"
        document = (open(orig,'rb'))

        #sending message
        app.send_document(chat_id=message.from_user.id,reply_to_message_id=message.message_id,document=document)
        msg = app.send_message(message.from_user.id,"Done.",reply_to_message_id=message.message_id)

        #removing files
        os.remove("file.txt")

        #delete message
        working_msg.delete()

@app.on_message(filters.regex(r'#other'))
def other(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)
        
        #getting text
        msg_textedd = (message.text)
        msg_texted = msg_textedd.lstrip("#other ")
        
        #getting repo and file
        repo = g.get_repo(github_repository_link)
        contents = repo.get_contents(other_file_from_same_repository, ref="main")
        aaa = contents.decoded_content.decode()

        #copying old with new
        aa = msg_texted + "\n" + aaa
        f = open("file.txt","w")
        f.write(aa)
        f.close()

        #removing duplicate
        lines_seen = set()
        outfile = open("filee.txt", "w")
        for line in open("file.txt", "r"):
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        ff = open("filee.txt","r")
        content = ff.read()

        #updating file
        repo.update_file(contents.path, "updated", content, contents.sha, branch="main")

        #removing files
        os.remove("file.txt")
        os.remove("filee.txt")

        #sending message
        msg = app.send_message(message.from_user.id,"Done.",reply_to_message_id=message.message_id)

        #delete message
        working_msg.delete()

@app.on_message(filters.regex(r'youtube.com|youtu.be'))
def youtube(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)
        
        #getting text
        msg_texted = (message.text)
        
        #getting repo and file
        repo = g.get_repo(github_repository_link)
        contents = repo.get_contents(youtube_file_from_same_repository, ref="main")
        aaa = contents.decoded_content.decode()

        #copying old with new
        aa = msg_texted + "\n" + aaa
        f = open("file.txt","w")
        f.write(aa)
        f.close()

        #removing duplicate
        lines_seen = set()
        outfile = open("filee.txt", "w")
        for line in open("file.txt", "r"):
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        ff = open("filee.txt","r")
        content = ff.read()

        #updating file
        repo.update_file(contents.path, "updated", content, contents.sha, branch="main")

        #removing files
        os.remove("file.txt")
        os.remove("filee.txt")

        #sending message
        msg = app.send_message(message.from_user.id,"Done.",reply_to_message_id=message.message_id)

        #delete message
        working_msg.delete()

@app.on_message(filters.regex(r'instagram.com'))
def instagram(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)
        
        #getting text
        msg_texted = (message.text)
        
        #getting repo and file
        repo = g.get_repo(github_repository_link)
        contents = repo.get_contents(instagram_file_from_same_repository, ref="main")
        aaa = contents.decoded_content.decode()

        #copying old with new
        aa = msg_texted + "\n" + aaa
        f = open("file.txt","w")
        f.write(aa)
        f.close()

        #removing duplicate
        lines_seen = set()
        outfile = open("filee.txt", "w")
        for line in open("file.txt", "r"):
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        ff = open("filee.txt","r")
        content = ff.read()

        #updating file
        repo.update_file(contents.path, "updated", content, contents.sha, branch="main")

        #removing files
        os.remove("file.txt")
        os.remove("filee.txt")

        #sending message
        msg = app.send_message(message.from_user.id,"Done.",reply_to_message_id=message.message_id)

        #delete message
        working_msg.delete()

@app.on_message(filters.document)
def notes_file(client: Client, message: Message):
        working_msg = app.send_message(message.from_user.id,"Working on it.",reply_to_message_id=message.message_id)
        
        #login
        g = Github(github_access_token)
        
        #getting file id
        file_id = None
        if message.media:
                if message.document:
                    file_id = message.document.file_id

        #downloading
        download_file = app.download_media(file_id)
        
        #read file
        with open(download_file, 'r') as file:
                contentss = file.read()
        
        #getting repo and file
        repo = g.get_repo(github_repository_link)
        contents = repo.get_contents(notes_file_from_same_repository, ref="main")
        aaa = contents.decoded_content.decode()

        #copying old with new
        aa = contentss + "\n" + aaa
        f = open("file.txt","w")
        f.write(aa)
        f.close()

        #removing duplicate
        lines_seen = set()
        outfile = open("filee.txt", "w")
        for line in open("file.txt", "r"):
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        ff = open("filee.txt","r")
        content = ff.read()

        #updating file
        repo.update_file(contents.path, "updated", content, contents.sha, branch="main")

        #removing files
        os.remove("file.txt")
        os.remove("filee.txt")

        #sending message
        msg = app.send_message(message.from_user.id,"Done.",reply_to_message_id=message.message_id)

        #delete message
        working_msg.delete()

app.run()
