import json
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import tool
import mysql.connector
from mysql.connector import errorcode

def get_connection(host, user, password, database, ssl_ca_path):
  config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database,
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': ssl_ca_path
  }
  try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  return conn

def get_database_schema(conn):
  cursor = conn.cursor()
  cursor.execute("SHOW TABLES;")
  tables = cursor.fetchall()
  tables_schemas = []
  for table in tables:
    cursor.execute(f"DESCRIBE {table[0]};")
    tables_schemas.append((("table_name", table[0]), ("table_schema", cursor.fetchall())))
  return tables_schemas

def get_agent(conn, api_key):

  # OpenAI LLM
  llm=OpenAI(model="text-davinci-003", temperature=0.8, openai_api_key=api_key)
  
  # Build tools
  @tool
  def run_the_sql_query(query:str):
      """ The input should be a valid SQL query. 
      This function executes the query to get the desired records from the database.
      """
      cursor = conn.cursor()
      cursor.execute(query)
      output = cursor.fetchall()
      return output

  # get db schema
  db_schema = get_database_schema(conn)
  
  # prompt prefix
  prefix = f"You are working as a SQL script generator. You are given a database schema with information of each table below: \n\n ```{db_schema}```."
  
  # list of tools
  tools = [run_the_sql_query]

  # create agent
  agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, agent_kwargs={"prefix": prefix}, verbose=True)
  return agent

def main(config_path):
  config = json.load(open(config_path, "r"))
  conn = get_connection(config.get("host"), config.get("user"), config.get("password"), config.get("database"), config.get("ssl_ca_path"))
  agent = get_agent(conn, config.get("openai_api_key"))
  return agent


if __name__=="__main__":
  agent = main("./config.json")
  response = agent.run("how many employees are there?")
  print(f"Number of employees: {response}")