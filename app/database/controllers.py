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

from app import db, app
from app.database.models import PrescribingData, PracticeData
import pandas as pd
import numpy as np
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

    def count_treatment(self, treatment):
        return db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.BNF_code.startswith(treatment)).first()[0]

    def get_percentageof_all_infection_treatments(self):
        """Return Infection treatment drug % of all infection treatments"""

        treatment_amount_agg = []

        treatment_total_amount = db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.BNF_code.startswith("05")).first()[0]
        for item in ['0501', '0502', '0503', '0504', '0505']:
            treatment_amount_agg.append(round(self.count_treatment(item) / treatment_total_amount * 100, 2))

        return treatment_amount_agg

    def get_distinct_practice(self, pct):
        """Return the distinct Practice codes."""
        return db.session.query(PrescribingData.practice).filter(PrescribingData.PCT == pct).distinct().all()

    def get_n_antibiotics_per_practice_for_pct(self, pct):
        """Return the total number of antibiotics per practice for a given PCT."""
        return db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.BNF_code.startswith("0501"),
                                                                        PrescribingData.PCT == pct).group_by(PrescribingData.practice).all()

    def get_n_data_for_drug(self, name_or_code):
        """Return all the data for a given drug."""
        # Find all data related with the drug
        if str(name_or_code)[:5].isdigit() == True:
            drug_origin = db.session.query(PrescribingData.PCT,PrescribingData.items,PrescribingData.NIC,PrescribingData.ACT_cost,PrescribingData.quantity).filter(PrescribingData.BNF_code == name_or_code).all()
        else:
            drug_origin = db.session.query(PrescribingData.PCT,PrescribingData.items,PrescribingData.NIC,PrescribingData.ACT_cost,PrescribingData.quantity).filter(PrescribingData.BNF_name == name_or_code).all()

        drug_origin_pd = pd.DataFrame(drug_origin, columns=['PCT', 'ITEMS', 'NIC', 'ACTCOST', 'QUANTITY'])

        pct = list(set(list(drug_origin_pd['PCT'])))
        drug_pct_total =[]
        for item in pct:
            drug_select = drug_origin_pd[drug_origin_pd['PCT'] == item]
            drug_pct_items = sum(drug_select['ITEMS'])
            drug_pct_NIC = round(float(np.mean(drug_select['NIC'])),2)
            drug_pct_ACTcost = round(float(np.mean(drug_select['ACTCOST'])),2)
            drug_pct_quantity = round(float(np.mean(drug_select['QUANTITY'])),2)

            drug_pct_practice = drug_select.shape[0]
            print(drug_pct_practice)
            drug_pct_all = [item, drug_pct_items, drug_pct_NIC, drug_pct_ACTcost, drug_pct_quantity, drug_pct_practice]
            drug_pct_total.append(drug_pct_all)

        return drug_pct_total

    def get_practice_drug(self, PCT, BNFNAME):
        """Return all the data for a given drug."""
        # Find all data related with the drug
        drug_origin = db.session.query(PrescribingData.practice,PrescribingData.items,PrescribingData.NIC,PrescribingData.ACT_cost,PrescribingData.quantity).filter(PrescribingData.BNF_name == BNFNAME, PrescribingData.PCT == PCT).all()

        drug_origin_pd = pd.DataFrame(drug_origin, columns=['practice', 'ITEMS', 'NIC', 'ACTCOST', 'QUANTITY'])

        pct = list(set(list(drug_origin_pd['practice'])))
        drug_pct_total =[]
        for item in pct:
            drug_select = drug_origin_pd[drug_origin_pd['practice'] == item]
            drug_pct_items = sum(drug_select['ITEMS'])
            drug_pct_NIC = round(float(np.mean(drug_select['NIC'])),2)
            drug_pct_ACTcost = round(float(np.mean(drug_select['ACTCOST'])),2)
            drug_pct_quantity = round(float(np.mean(drug_select['QUANTITY'])),2)
            drug_pct_all = [item, drug_pct_items, drug_pct_NIC, drug_pct_ACTcost, drug_pct_quantity]
            drug_pct_total.append(drug_pct_all)

        return drug_pct_total
    def get_distinct_drugname(self):
        """Return the distinct drugname names."""
        return db.session.query(PrescribingData.BNF_name).distinct().all()

    def get_distinct_drugcode(self):
        """Return the distinct drugcode codes."""
        return db.session.query(PrescribingData.BNF_name).distinct().all()

    def get_bnf_code(self,drug):
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_name == drug).distinct().all()[0][0]

