import os
import time
import csv
import re
import lxml
import pandas as pd
from functions import get_registration_details
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_options = Options()
driver_options.headless = True
driver_options.add_argument('--window-size= 1920,1200')

driver = webdriver.Chrome(
  options= driver_options, executable_path= '/Users/michael/browser-drivers/chromedriver')



################################################################################
# Top-level advanced search returns a list of lobbyists linked to registrations
################################################################################
url_lobbyist_reg_mb = 'https://registry.lobbyistregistrar.mb.ca'
url_advanced_search = 'https://registry.lobbyistregistrar.mb.ca/lra/reporting/public/advanceSearch.do'
driver.get(url_advanced_search)

# Select all lobbyist registration roles and status
select_registration_role = Select(driver.find_element_by_xpath('//*[@id = "publicReportForm_form_registrationRole"]'))
select_registration_role.select_by_value('all')
select_registration_status = Select(driver.find_element_by_xpath('//*[@id = "publicReportForm_form_registrationStatus"]'))
select_registration_status.select_by_value('all')
driver.find_element_by_xpath('//*[@id = "activeTypeACTIVE_TERMINATED"]').click()
driver.find_element_by_xpath('//*[@id = "publicReportForm"]/div/table/tbody/tr[11]/td/a/img').click()

# Wait for results and hand over to beautiful soup
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.results')))
bs4_lobbyists = BeautifulSoup(driver.page_source, 'html.parser')

# Grab top-level lobbyist list for CSV output 
table_header = ["reg_id", "url", "name", "reg_role", "reg_type", "reg_status", "reg_status_date", "client", "organization", "lobbying_firm"]
table_rows = []
for child in bs4_lobbyists.find_all('table', {"class": "results"})[0].find("tbody").children:

  table_row = []
  for td in child:
    try:

      # First column has url to the registration and contains the registration key (possible ID?)
      for a in td.find_all('a'):
        link = a['href']
        table_row.append(link.replace('/lra/reporting/public/registrar/view.do?method=get&registrationId=', ''))
        table_row.append(link)

      table_row.append(
        td.text.replace('\n', '')
          .replace('\t', '')
          .replace("\xa0", " ")
          .replace("  ", " ")
          .strip()
      )
    except:
      continue

  if len(table_row) > 0:
    table_rows.append(table_row)

df = pd.DataFrame(table_rows[1:], columns=table_header)
df.to_csv('data/mb_lobbyists_scraped.csv', encoding='utf-8', index=False)


################################################################################
# Individual registrations to pull data from
################################################################################
for i in df.index:
  
  reg_id = df['reg_id'][i]
  url_lobby_reg = url_lobbyist_reg_mb + df['url'][i]
  driver.get(url_lobby_reg)
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  get_registration_details(reg_id, soup)



driver.quit()


