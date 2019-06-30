from flaskext.mysql import MySQL
from app import app
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'ashraf'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'flask_crud_api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)