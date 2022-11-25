"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = [r[0] for r in db_mod.get_distinct_pcts()]
    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct = str(form['pct-option'])
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
    else:
        # pick a default PCT to show
        selected_pct = str(pcts[0])
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    title_data_items = generate_data_for_tiles()
    top_item_name = generate_description_for_top_item()
    max_quantity = db_mod.get_max_quantity()
    total_quantity = db_mod.get_total_quantity()
    percentage = round(max_quantity/total_quantity*100, 2)
    num_unique_items = generate_data_for_unique_items()
    all_infection_treatments = db_mod.get_percentageof_all_infection_treatments()


    bar = generate_antibiotics_barchart_data(selected_pct)
    bar_y = bar[0]
    bar_x = bar[1]


    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', tile_data=title_data_items,
                           top_data=percentage, top_name=top_item_name, quantity=max_quantity, num_data=num_unique_items,
                           pct={'data': bar_values, 'labels': bar_labels},
                           pct_list=pcts, pct_data=selected_pct_data,
                           all_infection_treatments_data=all_infection_treatments,
                           antibiotics={'data': bar_y, 'labels': bar_x})


def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items(), db_mod.get_average_act_cost()]


def generate_description_for_top_item():
    """Generate the name for the item with max quantity."""
    return [db_mod.get_max_quantity_item_name()]


def generate_data_for_unique_items():
    """Generate the number of unique items."""
    return [db_mod.get_numberof_unique_items()]


def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]


def generate_percentageof_all_infection_treatments():
    """Generate percentage of all infection treatments needed to populate the barchart."""
    data_values = db_mod.get_percentageof_all_infection_treatments()
    data_values = [r[0] for r in data_values]

    return data_values


def generate_antibiotics_barchart_data(pct):
    """Generate the antibiotics data needed to populate the barchart."""
    data_values = db_mod.get_n_antibiotics_per_practice_for_pct(pct)
    practice_codes = db_mod.get_distinct_practice(pct)

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    practice_codes = [r[0] for r in practice_codes]
    return [data_values, practice_codes]

    return data_values
