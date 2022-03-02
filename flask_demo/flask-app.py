from platform import python_branch
#!/usr/bin/env python
import os
from flask import Flask,json,render_template,request,send_file,Response
from craigslist_df_func import scraping
from IPython.display import HTML


#create instance of Flask app
app = Flask(__name__)

@app.route("/") # return text
def hello():
    text = '''if you call ('/scrape') it saves the dataFrame and will see url,
     if you call('/all') a dataFrame will appear.'''
    return text

@app.route('/scrape')# return link
def scrape():
     url = '''https://stlouis.craigslist.org/search/hhh?hasPic=1&availabilityMode=0&is_furnished=1&sale_date=all+dates'''
     return url


@app.route('/scrape/all') # return dataframe
def all():
    data_df = scraping()
    html_1 = HTML(data_df.to_html(justify='center',classes='table table striped',index=False))
    return render_template("index.html", data=html_1)

if __name__ == '__main__':
    app.run(debug=True)