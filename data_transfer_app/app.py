#!/usr/bin/env  python

import json
import pymysql.cursors
from config import db_connection_config, source_data_config
import logging

db_user = db_connection_config["user"]
db_password = db_connection_config["password"]
db_host = db_connection_config["host"]
db_database = db_connection_config["database"]
source_data_path = source_data_config["file_location"]

# Setting up logging for a file based logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def create_table():
   # Establishing the connection to the Database
   try:
      connection = pymysql.connect(host=db_host,
                                 user=db_user,
                                 password=db_password,
                                 db=db_database,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
   except Exception as err:
      logging.error("Exception occurred: {err}".format(err=err))

   # Creating a variable of string for creating table purpose 
   # if it does not exist as per the requirement
   sql ='''CREATE TABLE IF NOT EXISTS humans(
      name CHAR(100) NOT NULL,
      dob CHAR(100) NOT NULL,
      address CHAR(250),
      email CHAR(250),
      company_email CHAR(250),
      cigarates_smokes CHAR(10),
      number_of_childeren CHAR(10),
      phone_number CHAR(100),
      favourite_color CHAR(100),
      job CHAR(100),
   )'''

   cursor = connection.cursor()
   cursor.execute(sql)
   connection.commit()
   connection.close()
   

def getting_data_from_json(source_data_path):
   with open(source_data_path) as fo:
      data = json.load(fo)

def insert_data():
   pass


if __name__ == "__main__":
   logging.warning('Started app.py execution..')
   create_table()
   # insert_data()
