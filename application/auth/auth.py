class Authenticator:
    """
    #======================== IMPORTANT NOTE ===========================#
    #  This class is just for demo purpose as it has in-memory AUTH_DB  #
    #  Ideally you should use some persistent storage for auth data.    #
    #  Also writing passwords in plain text is not a good practice.     #
    #  You should store password hashes instead of actual passwords     #
    #===================================================================#
    """

    AUTH_DB = {
        'validusername': 'validpassword'
    }

    def is_valid(username, password):
        if username and password and Authenticator.AUTH_DB.get(username) == password:
            return True
        return False
