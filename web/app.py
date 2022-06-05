import connexion


app = connexion.FlaskApp(__name__, specification_dir='../docs/', debug=True)
app.add_api('swagger.yaml', arguments={'title': 'Hello World Example'})


if __name__ == '__main__':
    app.run()
