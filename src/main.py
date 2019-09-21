'''

    Title: Ceddit

    Desc: This project is just a reddit clone. The reason I am not putting a
          MIT license on this project because this is just an educational pro
          -ject for me and I want it to stay it that way.

    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com

'''

# core python modules

from flask import Flask, request, render_template, redirect, session

# my own modules


# Configuration
app = Flask(
    __name__,
    static_folder="./static",
    template_folder="./templates"
)

app.secret_key = "change this in production"



# URLS
