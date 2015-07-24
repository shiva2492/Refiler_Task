from codebase import app


app.config['MYSQL_DATABASE_USER']='USER'
app.config['MYSQL_DATABASE_PASSWORD']='PASSWORD'
app.config['MYSQL_DATABASE_DB'] ='Restaurant'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.secret_key = 'Enter your key'

