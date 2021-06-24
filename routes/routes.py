from flask import current_app as app
from src.core import token_required, platform_token_required
from src.linkedin.controllers.api import *


@app.route('/api/linkedin/search_people', methods=['GET'])
@platform_token_required('Linkedin')
def search_people():
    return search()


@app.route('/api/linkedin/login', methods=['POST'])
@token_required
def login_linkedin():
    return authentication()
