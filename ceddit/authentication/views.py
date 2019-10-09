from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint

from .models import Programmer, Admin
from ..app import db
