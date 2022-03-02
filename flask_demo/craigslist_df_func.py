from bs4 import BeautifulSoup
import requests
import pandas as pd 

def scraping(url = 'https://stlouis.craigslist.org/search/hhh?hasPic=1&availabilityMode=0&is_furnished=1&sale_date=all+dates'):
    headers= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'}
    
    response = requests.get(url,headers=headers)
    html_soup = BeautifulSoup(response.text,'html.parser')
    posts_li = html_soup.find_all('li',class_='result-row')
    crg_all_results = []
    for li in posts_li:
        try:
            post_one_title = li.find('a',class_='result-title hdrlnk').text
            post_one_hood = li.find('span',class_="result-hood").text
            post_one_time = li.find('time',class_='result-date')['datetime']
            post_one_sqft = li.find('span',class_='housing').text.split()[2][:-3]
            post_one_num_bedrooms= li.find('span',class_='housing').text.split()[0]
            post_one_price = li.a.text

            house_dict = {'Title':post_one_title,
                         'Location':post_one_hood,
                         'Date and Time':post_one_time,
                         'Sqft':post_one_sqft,
                         'Bedrooms':post_one_num_bedrooms,
                         'Price':post_one_price}
            crg_all_results.append(house_dict)
        except Exception as e:
            print(e)
    return pd.DataFrame(crg_all_results)