def user_name_validation(user_name):
    if user_name == None:
        raise ValueError('name is not set')