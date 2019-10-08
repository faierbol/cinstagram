# Development Config will go here
def development_config():
    app.config["static_folder"] = "./static"
    app.config["template_folder"] = "./templates"
    app.secret_key = "changeThisInProduction"
    app.debug = True
    app.host = "127.0.0.1"
    app.config["port"] = 8080

# The code below here is for the future use, it is psuedo code for now

# baseConfigClass:
#   debug = False
#   host = ...
#   port = ...


# ProductionConfigClass:
#   ...

# DevelopmentConfigClass:
#   ...

# TestingConfigClass
#   ...
