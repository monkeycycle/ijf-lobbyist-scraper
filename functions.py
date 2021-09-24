import os
import time
import csv
import re
import lxml
import pandas as pd
from bs4 import BeautifulSoup


def transpose_label_value(table_rows):

  table_row = []

  for table_row in table_rows:

    try:
      label = table_row.findAll('td')[0].text
      label = label.strip()
      table_row.append(label)
    except:
      continue

    try:
      value = table_row.find("td", {"class": "populated"}).text
      value = value.strip()
      table_row.append(value)
    except:
      continue

    if len(table_row) > 0:
      table_rows.append(table_row)

  return(table_rows)


################################################################################
# get_registration_details(tables)
# Convert stacked tables into usable data
################################################################################

def get_registration_details(reg_id, soup):

  lobbyist_tables = soup.find_all('div', {"id": "mainColumn"})[0].find_all("table")

  if(len(soup.find_all('div', {"id": "mainColumn"})[0].find_all("table")) == 12):

    table_details = pd.DataFrame()
    for table in lobbyist_tables:
    
      try:
        df = pd.read_html(str(table))
        table_details = table_details.append(df)

      except:
        continue


    table_details = table_details.transpose

    table_details.to_csv('data/table_details.csv',
                         encoding='utf-8', index=False)







  # table_org_address_rows  = pd.read_html(str(lobbyist_tables[3]))
  # table_org_lobby_act_rows  = pd.read_html(str(lobbyist_tables[4]))


  # table_name_rows = pd.DataFrame(table_name_rows)
  # table_name_rows = table_name_rows.transpose()
  # print(table_name_rows)

  # df.to_csv('data/some.csv', encoding='utf-8', index=False)

  # table_name_rows_t = transpose_label_value(table_name_rows)
  # table_lobbyist_address_rows = transpose_label_value(able_lobbyist_address_rows)
  # table_org_info_rows = transpose_label_value(able_org_info_rows)
  # table_org_address_rows = transpose_label_value(able_org_address_rows)
  # table_org_lobby_act_rows = transpose_label_value(able_org_lobby_act_rows)

  # print(table_org_address_rows)



  # table_org_interfaces_rows = lobbyist_tables[5]
  # table_org_desc_rows = lobbyist_tables[6]
  # table_org_corp_rows = lobbyist_tables[7]

  # Require different approach
  # table_org_csubsidiary_rows = lobbyist_tables[8]
  # table_org_corp_contact_rows = lobbyist_tables[9]
  # table_org_corp_contact_rows = lobbyist_tables[10]





# df=pd.DataFrame(table_rows[1:], columns=table_header)
# df.to_csv('data/mb_lobbyists_scraped.csv', encoding='utf-8', index=False)













  #   print(label, value)


    # header.append(label)
    # row.append(value)

    # if len(row) > 0:
    #   rows.append(row)

    # .replace("\xa0", " ")
      # .replace("  ", " ")
      # 
    # print(reg_id, label)



  #   # for header, value in zip(td.select('td')[0], td.select('td')[1]):

  #     # print(header)
  #     # print(value)
  #   first_column = row.findAll('th')[0].contents
  #   third_column = row.findAll('td')[1].contents
  #   print(first_column, third_column)

    # label = td.select('td')[0].text
    # value = td.select('td')[1].text
    # print(label)
    # print(value.replace('\n', '').replace('\t', '').replace(
    #     "\xa0", " ").replace("  ", " ").strip())

    # print(td.select('td')[1])




  #     if num == 0:
  #       headers.append(header)
  #     values.append(value)
  #   rows.append(values)
  #   values = []
  #   num += 1
  #   if num > 50:
  #     break
    
  # df = pd.DataFrame(rows, columns=headers)
  # print(df.head())

  # df.to_csv('mycsv.csv')

