from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.news.models import News

class CommentsForm(FlaskForm):
    news_id = HiddenField('ID комментария', validators=[DataRequired()])
    comment_text = StringField('Текст комментария', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Оправить', render_kw={"class": "btn btn-primary"})

    def validate_news_id(self, news_id):
        if not News.query.get(news_id.data):
            raise ValidationError('Новости с таким id оне существует')

 