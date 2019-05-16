"""
    main.py is the entry point for you application if you are
    deploying the application instead of testing it using behave
"""

from application import app

if __name__ == '__main__':
    app.run()