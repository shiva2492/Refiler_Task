from flask import Flask
from flaskext.mysql import MySQL


#run following command on your terminal to create the database and schema
#mysql -u root -p <Restaurant.sql


app=Flask(__name__)
mysql=MySQL()
app.config.from_object('config')
mysql.init_app(app)


from codebase import views,models

