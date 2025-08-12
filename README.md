# Web-Scrapping-Python

I used pythons' BeautifulSoup to Webscrape Wikipendia for a List of largest companies in the United States by revenue

I used a virtual Environment to run the code on VS Code via CMD Prompt. 


# Steps
1. Creating a file directory and a virtual Environment.
   Touch scrape.py --- to create a file via CMD 
   code scrape.py ---  to access the file in VS code.
   python -m venv env

2. Accessing the ENV and isntalling packages, BeautifulSoup and Pandas.
    env\Scripts\activate.bat --- activate the VE. 
    pip install packages BeautifulSoup pandas --- install the python files in the VE. 
   
3. Accessing the website to scrap ie. Wikipendia: list of largest companies in the US by revenue.
4. Analyze/Inspect the html link elements to find where the data is located.
5. using a Find_all BS synatax to locate the table of content available on html site(wiki site has a table with the data neeed, hence
   the need to access this table).as shown in [Web Scrape](scape.py)
7. Using Pandas DataFrame synax we create a table for the data extracted from the website.
8. Finally, we have can download the data as a CSV by create one and input the dataFrame Columns into the CSV file.  
   [Largest Us Companies](Largest%20US%20companies.csv)

