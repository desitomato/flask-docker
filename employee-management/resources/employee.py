from flask_restful import Resource, reqparse
from models.employee import EmployeeModel

class Employee(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('salary',
    type=int,
    required=True,
    help="This field cannot be left blank!"
    )
    parser.add_argument('company_id',
    type=int,
    required=True,
    help="This field cannot be left blank!"
    )
    def get(self,name):
        employee = EmployeeModel.find_by_name(name)
        if employee:
            return employee.json(), 200

    def post(self, name):
        if EmployeeModel.find_by_name(name):
            return {'message': 'employee already exists'}, 400

        data = Employee.parser.parse_args()

        employee = EmployeeModel(name, **data)
        try:
            employee.save_to_db()
        except:
            return {'message': 'error occur while creating employee'}, 500
        return employee.json(), 201

    def delete(self, name):
        employee = EmployeeModel.find_by_name(name)
        if employee:
            employee.delete_from_db()
            return {'message': 'employee deleted'}, 200
        return {'message': 'error occur while deleting employee'}, 500

    def put(self, name):
        data = Employee.parser.parse_args()
        
        employee = EmployeeModel.find_by_name(name)
        if employee:
            employee.salary = data['salary']
        else:
            employee = EmployeeModel(name, **data)
        employee.save_to_db()
        return employee.json()


class EmployeeList(Resource):
    def get(self):
        employee_list = []
        employee = EmployeeModel.query.all()
        for x in employee:
            employee_list.append(x.json())
        return employee_list