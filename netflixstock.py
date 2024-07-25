import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data=requests.get(url).text
#print(data)
soup = BeautifulSoup(data, 'html.parser')
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
s= soup.find("tbody")
for row in s.find_all('tr'):
    col=row.find_all('td')
    date=col[0].text
    open=col[1].text
    high=col[2].text
    low=col[3].text
    close=col[4].text
    adj_close = col[5].text
    volume=col[6].text
    #netflix_data=pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)
    netflix_data=netflix_data._append({"Date":date, "Open":open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    
#print(netflix_data)
read_html_pandas_data = pd.read_html(url)
netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe.head())

    