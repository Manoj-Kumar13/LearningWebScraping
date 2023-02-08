import psycopg2 as pg

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'manoj123'
port_id = '5432'
conn = None
cur = None

try :
    conn = pg.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur  =  conn.cursor()
    cur.execute('drop table if exists demo_table')

    create_table_script  = """create table if not exists demo_table (
                        id  int PRIMARY Key,
                        name varchar(30) not null,
                        salary int  
    )"""
    cur.execute(create_table_script)

    insert_value_script  = 'insert into demo_table (id, name, salary) values(%s, %s, %s)'
    insert_value = [(1,'Peter', 25000),(2,'Kelvin', 30000)]
    for record in insert_value:
        cur.execute(insert_value_script, record)

    cur.execute("select * from demo_table")
    results = cur.fetchall()
    for result in results:
        print(result)

    conn.commit()

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()

