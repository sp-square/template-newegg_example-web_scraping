from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = "http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# opening up connection, grabbing the page
client = urlopen(my_url)
html = client.read()
client.close()

# html parsing
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.body.p)

# grab each product
containers = soup.findAll('div', {"class": "item-container"})
# print(len(containers))
# print(containers[0].prettify())

# create file to save to
filename = "products.csv"
f = open(filename, 'w')

# write first line to be the headers
headers = "brand, product_name, shipping\n"
f.write(headers)

# extract data wanted
for container in containers:
    brand = container.div.div.a.img["title"]
    product_name = container.find('a', {"class", "item-title"}).text
    shipping = container.find('li', {"class", "price-ship"}).text.strip()
    # print(brand)
    # print(product_name)
    # print(shipping + '\n')
    # concatenate as a comma separated string for csv file. Replace the commas inside the 'product_name' with pipes
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

# close the file
f.close()
