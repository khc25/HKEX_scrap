import psycopg2
import urllib.parse

result = urllib.parse.urlparse("postgres://durzuuei:MhkXGfqIVm_PseuFu7k_k9zaWNupACLF@queenie.db.elephantsql.com:5432/durzuuei")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
conn = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname
)
cur = conn.cursor()
