#Question 1
tesla = yf.Ticker("TSLA")
tesla_data= tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()

#Question 2
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data= requests.get(url).text
print(html_data)

soup = BeautifulSoup(html_data, 'html.parser')
tag_object=soup.title
print("tag object:",tag_object)

import pandas as pd
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
read_html_pandas_data = pd.read_html(url)
tesla_revenue_data = read_html_pandas_data[1]
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    tesla_revenue = pd.concat([
            tesla_revenue,
            pd.DataFrame({"Date": [date], "Revenue": [revenue]})
        ], ignore_index=True)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.tail()

#Question 3
gamestop = yf.Ticker("GME")
tesla_revenue.tail()
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()

#Question 4:
url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2= requests.get(url_2).text
print(html_data_2)

soup = BeautifulSoup(html_data_2, 'html.parser')
tag_object=soup.title
print("tag object:",tag_object)

import pandas as pd
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
read_html_pandas_data = pd.read_html(url_2)
gme_revenue_data = read_html_pandas_data[1]
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    gme_revenue = pd.concat([
            gme_revenue,
            pd.DataFrame({"Date": [date], "Revenue": [revenue]})
        ], ignore_index=True)

gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"",regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue.tail()

#Question 5
make_graph(tesla_data, tesla_revenue, 'Tesla')
#Question 6
make_graph(gme_data, gme_revenue, 'Gamestop')
