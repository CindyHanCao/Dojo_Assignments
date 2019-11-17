from config import app
from controller_functions import home_page, add_dojo, add_ninja

app.add_url_rule('/', view_func=home_page)
app.add_url_rule('/process', view_func=add_dojo, methods=['POST'])
app.add_url_rule('/process/ninja', view_func=add_ninja, methods=['POST'])