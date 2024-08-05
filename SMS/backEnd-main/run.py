from app import create_app
#from flask_cors import CORS

# Import your blueprint from routes.py

app = create_app()

# Set up CORS to allow requests from any origin
#CORS(app)

# Register the 'routes' blueprint


if __name__ == "__main__":
    app.run(debug=True)
