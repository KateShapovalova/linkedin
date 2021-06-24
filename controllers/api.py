from flask import jsonify, make_response, request
from linkedin import Linkedin, SECRET_KEY
import jwt


def search():
    response = {}
    resp_code = 400
    try:
        request_params = request.args.to_dict()
        api_session = get_session(request_params)

        response['api_response'] = api_session.search_people(request_params)
        resp_code = 200

    except Exception as err:
        err_msg = err.args[0]
        response = jsonify(error=err_msg)
    finally:
        if not response:
            response = 'Unknown error'

        return make_response(response, resp_code)


def authentication():
    """
        Try to authenticate with passed credentials
        :return: api token
        """

    try:
        request_params = request.args.to_dict()

        username = request_params['username']
        password = request_params['password']

        token = jwt.encode(
            {'username': username,
             'password': password}, SECRET_KEY)

        return make_response(jsonify({'token': token.decode("utf-8")}), 200)

    except Exception as err:
        return make_response(jsonify(error=f'Error during authentication in linkedin,{err.args[0]}'), 400)


def get_session(request_data):
    """
    Creates private linkedin api session object,
    :param request_data: dict, data passed with request
    :return: Session of linkedin private api
    """
    try:
        token = request_data['LinkedIn-Token']
        decoded_token = jwt.decode(token, SECRET_KEY)
        username = decoded_token['username']
        password = decoded_token['password']

        try:
            api_session = Linkedin(username, password)
        except:
            raise Exception('This account required manual login')

        del request_data['LinkedIn-Token']

        return api_session

    except Exception as err:
        raise Exception(err.args[0])
