import connexion
from os import environ

# TODO: add middleware to catch db exceptions


show_ui = environ.get("BUSES_SHOW_SWAGGER") in ["True", "1"]

app = connexion.FlaskApp(__name__, specification_dir='../docs/', options = {"swagger_ui": show_ui})
app.add_api('swagger.yaml', arguments={'title': 'Hello World Example'})


if __name__ == '__main__':
    app.run(debug=True)
