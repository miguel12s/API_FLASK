from flask import Blueprint


register=Blueprint("register",__name__)

@register.route('/register')

def register():
    return "hola desde register"