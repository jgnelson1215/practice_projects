'''
flask_template.py
provides a baseline of a lightweight web backend application
'''

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
    '''
    index
    '''
    return {"message":"Hello World!"}

@app.errorhandler(404)
def api_not_found(error):
    '''
    api_not_found
    '''
    return {"message": "API not found"}, 404

@app.route("/no_content", methods = ['GET'])
def no_content():
    '''
    no_content
    '''
    response = make_response({"message":"No content found"})
    response.status_code = 204
    return response

@app.route("/exp", methods = ['GET'])
def index_explicit():
    '''
    index_explicit
    '''
    response = make_response({"message":"exp"})
    response.status_code = 200
    return response

@app.route("/data", methods = ['GET'])
def get_data():
    '''
    get_data
    '''
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            response = make_response({"message": f"Data of length {len(data)} found"})
            return response
        else:
            # If 'data' is empty, return a JSON response with a 500 status code
            response = make_response({"message": "Data is empty"})
            response.status_code = 500
            return response
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        response = make_response({"message": "Data not found"})
        response.status_code = 404
        return response

@app.route("/name_search", methods = ['GET'])
def name_search():
    '''
    name_search
    '''
    first_name = request.args.get("q")
    if first_name:
        for person in data:
            if first_name.lower() in person["first_name"].lower():
                response = make_response(person)
                response.status_code = 200
                return response
        response = make_response({"message": "Person not found"})
        response.status_code = 404
        return response
    elif not first_name:
        response = make_response({"message": "Query parameter 'q' is missing"})
        response.status_code = 422
        return response

@app.route("/count", methods = ['GET'])
def count():
    '''
    count
    '''
    return{"data_count": f"{len(data)}"}

# Have to have <> for variable to work
@app.route("/person/<unique_identifier>", methods = ['GET', 'DELETE'])
def identifier_ops(unique_identifier):
    '''
    idOps
    '''
    if request.method == 'GET':
        for person in data:
            if str(unique_identifier) == person["id"]:
                response = make_response(person)
                response.status_code = 200
                return response
        response = make_response({"message": "Person not found"})
        response.status_code = 404
        return response

    elif request.method == 'DELETE':
        for person in data:
            if str(unique_identifier) == person["id"]:
                response = make_response({"message": f"User {unique_identifier} removed"})
                response.status_code = 200
                data.remove(person)
                return response
        response = make_response({"message": "Person not found"})
        response.status_code = 404
        return response

@app.route("/person", methods = ['POST'])
def add_user():
    '''
    add_user
    '''
    req = request.get_json()
    if req and req['id']:
        global data
        data += [req]
        response = make_response({"message": f"User {req['id']} added"})
        response.status_code = 200
        return response
    else:
        response = make_response({"message": "JSON body is missing"})
        response.status_code = 422
        return response

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
