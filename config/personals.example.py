'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.11.28.16.00
'''


###################################################### EXAMPLE PERSONAL DETAILS ######################################################

# Copy this file to config/personals.py and replace every placeholder with
# your own details. config/personals.py is git-ignored, so the real file never
# enters the repository. The bot will not start until a valid personals.py and
# questions.py exist next to this file.

# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Your legal name
first_name = "First"
middle_name = ""
last_name = "Last"

# Phone number (required), make sure it is valid.
phone_number = "YOUR_PHONE_NUMBER"

# What is your current city?
current_city = ""
'''
Note: If left empty as "", the bot will fill in the location of the job.
'''

# Address, used by the occasional application that asks for it.
street = "123 Example Street"
state = "State"
zipcode = "00000"
country = "Country"

## Equal opportunity questions
# What is your ethnicity or race? If left empty as "", the tool will not answer.
ethnicity = "Decline"              # "Decline", "Hispanic/Latino", "American Indian or Alaska Native", "Asian", "Black or African American", "Native Hawaiian or Other Pacific Islander", "White", "Other"

# How do you identify yourself? If left empty as "", the tool will not answer.
gender = "Decline"                 # "Male", "Female", "Other", "Decline" or ""

# Are you physically disabled or have a history/record of a disability?
disability_status = "Decline"      # "Yes", "No", "Decline"

veteran_status = "Decline"         # "Yes", "No", "Decline"
##


'''
For string variables followed by comments with options, only use the answers
from the given options. Answers are case sensitive.
'''


############################################################################################################
'''
Upstream project: https://github.com/GodsScion/Auto_job_applier_linkedIn
License: GNU Affero General Public License v3.0
'''
############################################################################################################
