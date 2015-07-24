from codebase import app

#run the following command from terminal to create the database and schema 
#go into the codebase directory and then run the command 
# mysql -u root -p < Restaurant.sql
#password will be prompted to enter for root user of database server

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='student'
app.config['MYSQL_DATABASE_DB'] ='Restaurant'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.secret_key = 'Your private key'

