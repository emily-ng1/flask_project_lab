from api.main import create_app
from api.settings import db_name, user_name, password_name

app=create_app(db_name, user_name, password_name)
app.run(debug=True)


