# Views of the Programmer Panel App

from flask import Flask, request, render_template, redirect, session


def programmer_panel_signup():
    '''
        programmer panel signup: is the view where a new programmer to the
        company can signup their accounts
    '''

    # process the signup form
    if request.method == "POST":
        print(request.form['username'])
        print(request.form['password'])
        print(request.form['key'])

    data = {

    }
    return render_template(
        'programmer_panel/programmer_panel_signup.html', data=data
    )


def programmer_panel_login():
    '''
        programmer panel login: is the view where the programmer of the sites
        can login to their accounts and view their programmer-admin page
    '''

    data = {

    }
    return 'programmer panel login'


def programmer_panel_dashboard():
    '''
        programmer panel dashboard is the landing page after a programmer
        logins to their accounts.
    '''

    data = {

    }
    return 'prgorammer panel dashboard'
