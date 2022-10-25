"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def get_average_act_cost(self):
        """Return the average act cost of prescribed items with two decimal places."""
        return round(db.session.query(func.avg(PrescribingData.ACT_cost).label('average_act_cost')).first()[0], 2)

    def get_top_prescribed_item(self):
        """Return the proportion of top prescribed items with two decimal places."""
        max_quantity = int(db.session.query(func.max(PrescribingData.quantity)).first()[0])
        total_quantity = int(db.session.query(func.sum(PrescribingData.quantity).label('total_quantity')).first()[0])
        #item = db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.quantity == max_quantity)
        #result = int(item.first()[0])/int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])
        return round((max_quantity/total_quantity)*100, 2)

    def get_numberof_unique_items(self):
        """Return number of unique items."""
        return db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.items == 1).first()[0]
