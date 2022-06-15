# Imports
from databricks import sql

# Connection parameters
hostname = "cse2.cloud.databricks.com"
http_path = "/sql/1.0/endpoints/489386e89600d733"
pat = "dapi0b42c9b7f9218082329c83e136cf1d5e"

# Query data

with sql.connect(server_hostname=hostname,
                 http_path=http_path,
                 access_token=pat) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM amitoz_sidhu_databricks.top_trips_per_vendor")
        result = cursor.fetchall()

        for row in result:
          print(row)

# Insert data
with sql.connect(server_hostname=hostname, http_path=http_path, access_token=pat) as connection:
  with connection.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS squares (x int, x_squared int)")
    squares = [(i, i * i) for i in range(100)]
    values = ",".join([f"({x}, {y})" for (x, y) in squares])

    cursor.execute(f"INSERT INTO squares VALUES {values}")

# Query metadata

with sql.connect(server_hostname=hostname, http_path=http_path, access_token=pat) as connection:
  with connection.cursor() as cursor:
    cursor.columns(schema_name="default", table_name="squares")
    print(cursor.fetchall())

# Cursor and connection management

# connection = sql.connect(server_hostname=hostname, http_path=http_path, access_token=pat)
# cursor = connection.cursor()
#
# cursor.execute("SELECT * from range(10)")
# print(cursor.fetchall())
#
# cursor.close()
# connection.close()