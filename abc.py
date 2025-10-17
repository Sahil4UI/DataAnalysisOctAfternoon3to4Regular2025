import pandas as pd

# Read HTML table from a URL
url = "https://www.flipkart.com/apple-iphone-17-black-256-gb/p/itm6eb39da622cdd?pid=MOBHFN6YN2HXB5HE&lid=LSTMOBHFN6YN2HXB5HER9QXGU&marketplace=FLIPKART&q=iphone+17&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=d3eb2a42-d8c3-4e63-9160-1f7a88318bd9.MOBHFN6YN2HXB5HE.SEARCH&ppt=None&ppn=None&ssid=1a2b0l36ps0000001760698009041&qH=c9eeb2d6cc488f0b"
tables = pd.read_html(url)
# Access the first table from the URL
df = tables[3]

# Display the resultant DataFrame
print('Output First DataFrame:', df.head())