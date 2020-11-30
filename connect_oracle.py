import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_19_8")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect(
    "lehacsc423", "leahharper99", "lawtech.law.miami.edu/CSC_423") 
cursor = connection.cursor()
cursor.execute("""
    SELECT * FROM VEHICLE
    WHERE curr_mileage > 10000
    """)

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print("\n*************** FIRST QUERY *************\n\n") 
print(df) # examine
print("\n") 
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column



cursor.execute("""
    SELECT * 
    FROM STAFF
    WHERE SALARY >= 50000
    ORDER BY HIRE_DATE
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print("\n*************** SECOND QUERY *************\n\n") 
print(df) # examine
print("\n") 
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column



cursor.execute("""
    SELECT VEHICLE.MODEL, VEHICLE.MAKE
    FROM ((CLIENT
    INNER JOIN HIRE_AGREEMENT ON CLIENT.CLIENT_NUM = HIRE_AGREEMENT.CLIENT_NUM)
    INNER JOIN VEHICLE ON HIRE_AGREEMENT.REG_NUM = VEHICLE.REG_NUM)
    WHERE client.f_name='Justin'
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print("\n*************** THIRD QUERY *************\n\n") 
print(df) # examine
print("\n") 
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column



cursor.execute("""
    SELECT VEHICLE.model, VEHICLE.make, OUTLET.address
    FROM VEHICLE
    INNER JOIN OUTLET ON OUTLET.out_num = VEHICLE.out_num
    WHERE OUTLET.out_num = 5
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print("\n*************** FOURTH QUERY *************\n\n") 
print(df) # examine
print("\n") 
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column




cursor.execute("""
    SELECT STAFF.f_name, STAFF.l_name, STAFF.address, STAFF.job_title, OUTLET.out_num
    FROM STAFF
    INNER JOIN OUTLET ON OUTLET.out_num = STAFF.out_num
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print("\n*************** FIFTH QUERY *************\n\n") 
print(df) # examine
print("\n") 
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column
