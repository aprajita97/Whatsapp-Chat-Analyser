from flask import *
import re
import pandas as pd
import matplotlib.pyplot as plt
import emoji
import os
import fn

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/GetName',  methods=['POST'])
def name_accept():
   if request.method == 'POST':
        name = request.form['name']
        data = fn.chat_file("WhatsApp Chat with %s.txt" % name)
        df = fn.chat_df(data)
        user1 = df.columns[0]
        user2 = df.columns[1]
        
        count_msg = fn.count_msg(data)
        
        muw1 = fn.most_used_word(df,user1)
        muw2 = fn.most_used_word(df,user2)
        
        emoji1 = fn.emoji_count(data,df,user1)
        emoji2 = fn.emoji_count(data,df,user2)
        
        mc1 = fn.media_count(df,user1)
        mc2 = fn.media_count(df,user2)
        
        wl1 = fn.word_list(df,user1)
        wl2 =fn.word_list(df,user2)
        
        bd = fn.busy_date_calc(data)
        bdc = bd.columns
        bdv = bd.values
        
        nbd = fn.non_busy_date_calc(data)
        nbdc = nbd.columns
        nbdv = nbd.values
        
        bh = fn.busy_hours_calc(data)
        bhc = bh.columns
        bhv = bh.values
        
        nbh = fn.non_busy_hours_calc(data)
        nbhc = nbh.columns
        nbhv = nbh.values
              
        return render_template('analysis.html', user1=user1, user2=user2, muw1=muw1, muw2=muw2, count_msg=count_msg, emoji1=emoji1.to_html(),emoji2=emoji2.to_html(), mc1=mc1, mc2=mc2,df=df.to_html(),wl1=wl1.to_html(),wl2=wl2.to_html(),nbh=nbh.to_html(), bh=bh.to_html(), bd=bd.to_html(), nbd=nbd.to_html())
   
if __name__ == "__main__":
    app.run(debug=True)