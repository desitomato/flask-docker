from db import db

class EmployeeModel(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    salary = db.Column(db.Integer)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship('CompanyModel')

    def __init__(self, name, salary, company_id):
        self.name = name
        self.salary = salary
        self.company_id = company_id

    def json(self):
        return {'name': self.name, 'id':self.id, 'salary': self.salary, 'company': self.company_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()