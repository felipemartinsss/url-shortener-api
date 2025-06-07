import os
import psycopg2

database_name = os.getenv('DATABASE_NAME', '')
user_name = os.getenv('USER_NAME', '')
password = os.getenv('PASSWORD', '')

def insert_url_mapping(original_url, shortened_url):
    with psycopg2.connect(f"dbname={database_name} user={user_name} password={password}") as conn:
        with conn.cursor() as cursor:
            sql_stmt = "INSERT INTO url_mappings (original_url, shortened_url) VALUES (%s, %s)"
            cursor.execute(sql_stmt, (original_url, shortened_url))
            conn.commit()

def recover_url_mapping(shortened_url):
    with psycopg2.connect(f"dbname={database_name} user={user_name} password={password}") as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT original_url FROM url_mappings WHERE shortened_url = %s", (shortened_url,))
            original_url = cursor.fetchone()[0]
            return original_url
