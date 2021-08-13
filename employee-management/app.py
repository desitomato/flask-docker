from flask import Flask, request, jsonify
from flask_restful import Api
from resources.company import Company, Companylist
from resources.employee import Employee, EmployeeList
from db import db
from resources.user import UserRegister, UserLogin, UserLogout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'prateek'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Company, '/company/<string:name>')
api.add_resource(Companylist, '/company')
api.add_resource(Employee, '/employee/<string:name>')
api.add_resource(EmployeeList, '/employee')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout/<string:username>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)













#API's without flask_restful
""" companies = [{
    'name': 'samsung',
    'employees': [{
        'name':'prateek',
        'salary':10000
        }]
}]

@app.route('/company', methods=['POST'])
def create_company():
    request_data = request.get_json()
    new_company = {'name': request_data['name'],
                    'employees': []
    }
    companies.append(new_company)
    return jsonify(new_company), 201

@app.route('/company/<string:name>')
def get_company(name):
    for company in companies:
        if company['name'] == name:
            return jsonify(company), 200

@app.route('/company')
def get_company_list():
    return jsonify(companies), 200

@app.route('/company/<string:name>/employee', methods=['POST'])
def create_employee_in_company(name):
    request_data = request.get_json()
    print(request_data)
    for company in companies:
        if company['name'] == name:
            new_employee = {
                'name' : request_data['name'], 
                'salary': request_data['salary']
                }
            company['employees'].append(new_employee)
            return jsonify(new_employee), 201

@app.route('/company/<string:name>/employee')
def get_employee_in_company(name):
    for company in companies:
        if company['name'] == name:
            return jsonify(company['employees']), 200 """


