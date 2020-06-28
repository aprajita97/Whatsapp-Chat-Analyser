import re
import pandas as pd
import matplotlib.pyplot as plt
import emoji
import os

os.system('cls')
file = open("WhatsApp Chat with Shreya.txt",mode='r',encoding="utf8")
data = file.read()
file.close()



pattern = re.compile('\d+\/\d+\/\d+,\s+\d+:\d+\s+[AP]M\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
messengers = re.findall(pattern,data)

count_messages={}
for each in messengers:
    if each in count_messages.keys():
        count_messages[each]+=1
    else:
        count_messages[each]=1
print("__________________________________________________")
print("No of message exchanges")
print(count_messages)

messages_split = pattern.split(data)
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
my_df=pd.DataFrame(who_sent_what)
my_df = my_df.transpose()
my_df.columns = [list(count_messages.keys())[0],list(count_messages.keys())[1]]
user1 =my_df.columns[0]
user2 =my_df.columns[1]
my_df.columns=[user1,user2]

'''
print("__________________________________________________")
print("Most used words\n\n")
mo="<Media omitted>"
used_word1=my_df[user1].value_counts().index.tolist()[0]
if mo in used_word1:
    used_word1 = my_df[user1].value_counts().index.tolist()[1]  
print("Most used word by " + user1 + ": " + used_word1)
used_word2=my_df[user2].value_counts().index.tolist()[0]
if mo in used_word2:
    used_word2 = my_df[user2].value_counts().index.tolist()[1]
    
print("Most used word by " + user2 + ":" + used_word2)

print(my_df[user1].value_counts().head(10))
print(my_df[user2].value_counts().head(10))

print("__________________________________________________")
print("Most used emojis\n\n")
def extract_emojis(columnname):
    emojis=[]
    for string in my_df[columnname]:
        my_str = str(string)
        for each in my_str:
            if each in emoji.UNICODE_EMOJI:
                emojis.append(each)
    return emojis
emoji_dict1={}
emoji_dict1[user1] = extract_emojis(user1)
emoji_df1 = pd.DataFrame(emoji_dict1[user1])
print(emoji_df1[0])
print(emoji_df1[0].value_counts()[:5])
emoji_dict2={}
emoji_dict2[user2] = extract_emojis(user2)
emoji_df2 = pd.DataFrame(emoji_dict2[user2])
print(emoji_df2[0])
x=pd.DataFrame(emoji_df2[0].value_counts()[:5])
print(type(x))
    
    

print("__________________________________________________")
print("Media sent\n\n")
media1 = my_df[user1].value_counts()["<Media omitted>"]
media2 = my_df[user2].value_counts()["<Media omitted>"]
print("%s sent %d media files" % (user1,media1))
print("%s sent %d media files" % (user2,media2))
'''

print("__________________________________________________")
print("busy and non busy hours\n\n")
hour_pattern = '(\d+):\d+ ([AP]M) - \w+\s?\w+?\s?\w+\s?\w+:\s'
hours = re.findall(hour_pattern,data)
time = pd.DataFrame({'hours':hours})
busy_hours = time['hours'].value_counts().head(10)
print(busy_hours)
non_busy_hours = time['hours'].value_counts().tail(10)
print(non_busy_hours)


print("__________________________________________________")
print("busy and non busy days\n\n")
date_pattern = '(\d+\/\d+\/\d+), \d+:\d+ [AP]M - \w+\s?\w+?\s?\w+\s?\w+:\s'
date = re.findall(date_pattern,data)
date_pd = pd.DataFrame({'dates':date})
busy_dates = pd.DataFrame(date_pd['dates'].value_counts().head(10))
print(busy_dates)
non_busy_dates = date_pd['dates'].value_counts().tail(10)
print(non_busy_dates)
#busy_hours.plot.bar()
#plt.show()

print(busy_dates.values)
