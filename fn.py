import re
import pandas as pd
import matplotlib.pyplot as plt
import emoji
import os

def chat_file(filename):
    os.system('cls')
    file = open(filename,mode='r',encoding="utf8")
    data = file.read()
    file.close()
    return data

def count_msg(data):
    pattern = re.compile('\d+\/\d+\/\d+,\s+\d+:\d+\s+[AP]M\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
    messengers = re.findall(pattern,data)
    count_messages={}
    for each in messengers:
            if each in count_messages.keys():
                count_messages[each]+=1
            else:
                count_messages[each]=1
    return count_messages

def chat_df(data):
    pattern = re.compile('\d+\/\d+\/\d+,\s+\d+:\d+\s+[AP]M\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
    messages_split = pattern.split(data)
    count_messages = count_msg(data)
    sep_msgs=[]
    for each in count_messages.keys():
        for msg in range(len(messages_split)):
            if each == messages_split[msg]:
                sep_msgs.append(messages_split[msg+1])   #obtaining the message mentioned after sender along with dates
    cleaned_sep_msg = []
    for each in sep_msgs:
        if '\n' in each:
            cleaned_sep_msg.append(each.split('\n'))
    my_msg = []
    for each in cleaned_sep_msg:
        my_msg.append(each[0])
    who_sent_what = []
    prev = 0
    for each in count_messages.keys():
        num = count_messages[each]
        nex = num+prev
        messages = my_msg[prev:nex]
        who_sent_what.append(messages)
        prev = nex
    who_sent_what
    my_df = pd.DataFrame(who_sent_what)
    my_df = my_df.transpose()
    my_df.columns = [list(count_messages.keys())[0],list(count_messages.keys())[1]]
    user1 = my_df.columns[0]
    user2 = my_df.columns[1]
    my_df.columns=[user1,user2]
    return my_df

def most_used_word(my_df,user):
    mo="<Media omitted>"
    used_word=my_df[user].value_counts().index.tolist()[0]
    index = 0
    if mo in used_word:
        used_word = my_df[user].value_counts().index.tolist()[1] 
        index = index + 1
    while any(x in used_word for x in emoji.UNICODE_EMOJI):
        used_word = my_df[user].value_counts().index.tolist()[index+1] 
        index = index + 1
        
    return used_word
    
'''def word_list(my_df,user):    
    x=my_df[user].value_counts().head(10)
    x=pd.DataFrame(x)
    return x'''

def word_list(my_df,user):    
    df = my_df
    df = df[df.columns[user]!=emoji.UNICODE_EMOJI]
    x=df[user].value_counts().head(10)
    x=pd.DataFrame(x)
    return x   
    
  
  

    
def emoji_count(data,my_df,user):
    def extract_emojis(user):
        emojis=[]
        for string in my_df[user]:
            my_str = str(string)
            for each in my_str:
                if each in emoji.UNICODE_EMOJI:
                    emojis.append(each)
        return emojis
    emoji_dict={}         
    emoji_dict[user] = extract_emojis(user)
    emoji_df = pd.DataFrame(emoji_dict[user])
    x=pd.DataFrame(emoji_df[0].value_counts()[:10])
    x.columns=[user]
    return x
        

def media_count(my_df,user):
    media = my_df[user].value_counts()["<Media omitted>"]
    return media
    
def busy_hours_calc(data):
    hour_pattern = '(\d+):\d+ ([AP]M) - \w+\s?\w+?\s?\w+\s?\w+:\s'
    hours = re.findall(hour_pattern,data)
    time = pd.DataFrame({'hours':hours})
    busy_hours = time['hours'].value_counts().head(10)
    x = pd.DataFrame(busy_hours)
    x.columns = ['No of messages']
    return x

def non_busy_hours_calc(data):
    hour_pattern = '(\d+):\d+ ([AP]M) - \w+\s?\w+?\s?\w+\s?\w+:\s'
    hours = re.findall(hour_pattern,data)
    time = pd.DataFrame({'hours':hours})
    non_busy_hours = time['hours'].value_counts().tail(10)
    x = pd.DataFrame(non_busy_hours)
    x.columns = ['No of messages']
    return x  

def busy_date_calc(data):
    date_pattern = '(\d+\/\d+\/\d+), \d+:\d+ [AP]M - \w+\s?\w+?\s?\w+\s?\w+:\s'
    date = re.findall(date_pattern,data)
    date_pd = pd.DataFrame({'dates':date})
    busy_dates = date_pd['dates'].value_counts().head(10)
    x = pd.DataFrame(busy_dates)
    x.columns = ['No of messages']
    return x
    
    
def non_busy_date_calc(data):
    date_pattern = '(\d+\/\d+\/\d+), \d+:\d+ [AP]M - \w+\s?\w+?\s?\w+\s?\w+:\s'
    date = re.findall(date_pattern,data)
    date_pd = pd.DataFrame({'dates':date})
    non_busy_dates = date_pd['dates'].value_counts().tail(10)
    x =  pd.DataFrame(non_busy_dates)
    x.columns = ['No of messages']
    return x
    

    
    