from flask_restful import Resource
from models.company import CompanyModel

class Company(Resource):
    def get(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            return company.json(), 200
        return {'message': 'company not found'}, 404

    def post(self, name):
        #if CompanyModel.find_by_name(name):
            #return {'message': 'company already exists'}, 400
        company = CompanyModel(name)
        try:
            company.save_to_db()
        except:
            return {'message': 'error occured while creating company'}, 500
        return company.json(), 201

    def delete(self, name):
        company = CompanyModel.find_by_name(name)
        try:
            company.delete_from_db()
        except:
            return {'message': 'error occured while deleted company'}, 500
        return{'message': 'company deleted'}, 200

class Companylist(Resource):
    def get(self):
        company_list = []
        company = CompanyModel.query.all()
        for x in company:
            company_list.append(x.json())
        return company_list
