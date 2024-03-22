import psycopg2

def create_database(db_name):
    conn = psycopg2.connect(dbname="jberkowitz",
                        user="jberkowitz",
                        host="127.0.0.1",
                        password="password",
                        port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE " + db_name)
    print(f"Database {db_name} has been created successfully")
    conn.close()

def create_schema(db_name, schema_name):
    conn = psycopg2.connect(dbname=db_name,
                        user="jberkowitz",
                        host="127.0.0.1",
                        password="password",
                        port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE SCHEMA " + schema_name)
    print(f"Schema {schema_name} has been created successfully")
    conn.close()

if __name__ == "__main__":
    create_database('ff_analytics')
    create_schema('ff_analytics', 'raw')