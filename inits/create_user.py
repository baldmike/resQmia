# This will create a user
# run from resQmia ROOT
# python manage.py shell
# execfile('./inits/create_user.py')

from apps.resQmia_app.models import User

import bcrypt
import getpass

first_name = raw_input('FIRST NAME OF USER:')
last_name = raw_input('LAST NAME OF USER:')
email = raw_input('EMAIL:')

user_check = User.objects.get(email=email)
if user_check:
    print "user exists, start over, nerd."

else:    
    password = getpass.getpass('PASSWORD:')

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = User.objects.create_user(first_name, last_name, email, hashed_password)
