#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob
from flask import Flask
from flask import render_template, request


# In[2]:


app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        r=TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html",result = 'waiting...'))


# In[ ]:


if __name__ == "__main__":
    app.run()
    # app.run(host='127.0.0.0',port=80)


# In[ ]:




