# Info-fetching-from-web
This is a web data fetching project which I did for my friend who asked me to... Well he needed to know prices of all products at a certain web store for what recently became legal in Canada - cannabis😅

Structure:
1. Intro.py file. Disclaimer. It invites a user to consult a government website with all the laws related to cannabis in Canada.
2. interface.py file. User interface. It collects data about a user (DOB) as well as data about a product he/she would like to get prices for.
3. Scrape_for_Kaz.py file. The application itself. It runs Google Chrome, fetches data, creates an Excel file and stores data in it.

To run the app, launch Scrape_for_Kaz.py file. Also, make sure chromedriver is in the same folder as all .py files.

Tools used: beautifulsoup and selenium
