import pandas as pd
import tabula as tb

import requests

df = pd.read_csv("6sep-15nov.csv")

links = df.iloc[:, 0]
print(links.head())

# ************** download pdf files
def download_pdf_files(links):
    i=0
    for link in links:
        url = link
        response = requests.get(url)
        with open(str(i)+'sample.pdf', 'wb') as f:
            f.write(response.content)
        i+= 1

# ************** convert to csv
def save_as_csv(links):
    for link in links:
        file ='./pdf/'+str(i)+'sample.pdf'
        pdfData = tb.read_pdf(file, pages=1)
        newCSV = link.removeprefix('http://kenesh.kg//').replace('/','-')+'.csv'
        output = tb.convert_into(file,newCSV, output_format="csv", pages=[1])
        i=+1



