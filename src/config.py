# Development Config will go here
def development_config(app):
    app.config["static_folder"] = "./static"
    app.config["template_folder"] = "./templates"
    app.secret_key = "changeThisInProduction"
    app.debug = True

    # Database configs
    postgresql_URI = "postgresql://demir@localhost:5432/ceddit"
    app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_URI

# The code below here is for the future use, it is psuedo code for now

# baseConfigClass:
#   debug = False
#   host = ...
#   port = ...


# ProductionConfigClass:
#   ...

# DevelopmentConfigClass:
#    ...

# TestingConfigClass
