import mysql.connector
from mysql.connector import errorcode
from datetime import datetime 

col_1=0

col_1 = col_1+1 
col_2 = datetime.now()

print('ID:',col_1)
print('Timestamp:',col_2)

#Create table details after creating a database.
create table `details`(
Id int(20)  not null,
Time datetime null 
);

#Connect Python with MySQL database
try:
        #Connection to the MySQL server
        cnct = mysql.connector.connect(host = 'localhost',user='root',port='3306',password = '*****',database='test')
   
        cursor = cnct.cursor()
         #Insert values into table details in database test
        sql_query = ("insert into details "
                    "(Id,Time)" 
                    "values(%(id)s,%(time)s)")
        #The data to be inserted is stored in the variable info
        info =  {
                    'id': col_1,
                    'time': col_2
                  }
        cursor.execute(sql_query,info)
        cnct.commit()
                   
#Error Handling

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnct.close()