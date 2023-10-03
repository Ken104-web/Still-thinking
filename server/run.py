from myapp import app, routes
from myapp.routes import Home

if __name__ == '__main__':
    app.run(port=5001, debug=True)