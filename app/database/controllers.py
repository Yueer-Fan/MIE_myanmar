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

    def get_max_quantity(self):
        """Return the quantity of items with max quantity."""
        max_quantity = int(db.session.query(func.max(PrescribingData.quantity)).first()[0])
        return max_quantity

    def get_total_quantity(self):
        """Return the sum of quantity for total items."""
        total_quantity = int(db.session.query(func.sum(PrescribingData.quantity).label('total_quantity')).first()[0])
        return total_quantity

    def get_max_quantity_item_name(self):
        """Return the item with max quantity."""
        max_quantity = self.get_max_quantity()
        return db.session.query(PrescribingData.BNF_name).filter(PrescribingData.quantity == max_quantity).first()[0]

    def get_average_act_cost(self):
        """Return the average act cost of prescribed items."""
        return round(db.session.query(func.avg(PrescribingData.ACT_cost).label('average_act_cost')).first()[0], 2)
    
    def get_numberof_unique_items(self):
        """Return the number of unique items"""
        return db.session.query(func.count(PrescribingData.BNF_code.distinct())).first()[0]

    def get_percentageof_all_infection_treatments(self):
        """Return Infection treatment drug % of all infection treatments"""
        def count_treatment(treatment):
            return db.session.query(func.count(PrescribingData.BNF_code)).filter(PrescribingData.BNF_code.startswith(treatment)).first()[0]

        treatment_amount_agg = []
        treatment_total_amount = db.session.query(func.count(PrescribingData.BNF_code.startswith("05"))).first()[0]
        for item in ['0501', '0502', '0503', '0504', '0505']:
            treatment_amount_agg.append(count_treatment(item)/treatment_total_amount)
        return treatment_amount_agg


