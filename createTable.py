import psycopg2

import urllib.parse

result = urllib.parse.urlparse(
    "postgres://durzuuei:MhkXGfqIVm_PseuFu7k_k9zaWNupACLF@queenie.db.elephantsql.com:5432/durzuuei")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
conn = psycopg2.connect(
    database=database,
    user=username,
    password=password,
    host=hostname
)
cur = conn.cursor()

# SZC
# SHC
cur.execute("CREATE TABLE szc (id serial PRIMARY KEY,date varchar, stock_code varchar, stock_name varchar,shareholding_CCASS varchar, shares_percentage varchar);")
cur.execute("CREATE TABLE shc (id serial PRIMARY KEY,date varchar, stock_code varchar, stock_name varchar,shareholding_CCASS varchar, shares_percentage varchar);")
cur.execute("CREATE TABLE hk (id serial PRIMARY KEY,date varchar, stock_code varchar, stock_name varchar,shareholding_CCASS varchar, shares_percentage varchar);")
