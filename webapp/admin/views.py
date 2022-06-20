from flask import Blueprint, render_template
from flask import Blueprint
from flask_login import  current_user, login_required


blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@login_required
def admin_index():
    title = 'Панель управления'
    return render_template('admin/index.html', page_title=title)


