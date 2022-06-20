from flask_login import login_user, logout_user, current_user
from flask import Blueprint, render_template, flash, redirect, url_for

from webapp.user.forms import LoginUser
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Авторизация'
    login_form = LoginUser()
    return render_template('user/login.html', title = title, form = login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginUser()

    if form.validate_on_submit():
        user = User.query.filter(User.username==form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно прошли авторизацию!')
            return redirect(url_for('news.index'))
    flash('Неверные данные')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились!')
    return redirect(url_for('news.index'))
