from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, FileField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Register(FlaskForm):
    user_name = StringField(
        label='用户名称',
        validators=[DataRequired(message='用户名不能为空'),
                    Length(min=3, max=15, message='用户名长度在3到15个字符之间')],
        render_kw={'id': 'user_name', 'class': 'form-control', 'placeholder': '请输入用户名', 'required': 'reqiured'})
    user_pwd = PasswordField(
        label='用户密码',
        validators=[DataRequired(message='密码不能为空'),
                    Length(min=3, max=15, message='用户密码长度在3到15个字符之间')],
        render_kw={'id': 'user_pwd', 'class': 'form-control', 'placeholder': '请输入密码', 'required': 'reqiured'})
    user_confirm = PasswordField(
        label='确认密码',
        validators=[EqualTo('password', message='两次密码不一致')],
        render_kw={'id': 'user_pwd', 'class': 'form-control', 'placeholder': '请输入密码', 'required': 'reqiured'})
    user_email = StringField(
        label='用户邮箱',
        validators=[DataRequired(message='邮箱不能为空'),
                    Email(message='邮箱格式不正确')],
        render_kw={'id': 'user_email', 'class': 'form-control', 'placeholder': '请输入邮箱', 'required': 'reqiured'})
    user_phone = StringField(
        label='用户电话',
        validators=[DataRequired(message='用户电话不能为空'),
                    Length(min=3, max=15, message='用户名长度在3到15个字符之间')],
        render_kw={'id': 'user_name', 'class': 'form-control', 'placeholder': '请输入电话', 'required': 'reqiured'})
    # user_birthday = IntegerField(
    #     label='用户生日',
    #     validators=[DataRequired(message='用户生日不能为空')],
    #     render_kw={'id': 'user_birthday', 'class': 'form-control', 'placeholder': '请输入生日'})
    # user_face = FileField(
    #     label='用户头像',
    #     validators=[],
    #     render_kw={'id': 'user_face', 'class': 'form-control'})
    submit = SubmitField(
        render_kw={'value': '注册', 'class': 'form-control'})

class Login(FlaskForm):
    account = StringField(
        label='用户名称',
        validators=[DataRequired(message='用户名不能为空'),
                    Length(min=3, max=15, message='用户名长度在3到15个字符之间')],
        render_kw={'id': 'user_name', 'class': 'form-control', 'placeholder': '请输入用户名', 'required': 'reqiured'})
    pwd = PasswordField(
        label='用户密码',
        validators=[DataRequired(message='密码不能为空'),
                    Length(min=3, max=15, message='用户密码长度在3到15个字符之间')],
        render_kw={'id': 'user_pwd', 'class': 'form-control', 'placeholder': '请输入密码', 'required': 'reqiured'})
    submit = SubmitField(
        render_kw={'value': '登陆', 'class': 'form-control'})

class Changepwd(FlaskForm):
    pwd = PasswordField(
        label='用户密码',
        validators=[DataRequired(message='密码不能为空'),
                    Length(min=3, max=15, message='用户密码长度在3到15个字符之间')],
        render_kw={'id': 'user_pwd', 'class': 'form-control', 'placeholder': '请输入密码', 'required': 'reqiured'})
    submit = SubmitField(
        render_kw={'value': '登陆', 'class': 'form-control'})

class AddBlog(FlaskForm):
    title = StringField(
        label='文章标题',
        validators=[DataRequired(message='文章标题不能为空'),
                    Length(min=1, max=72, message='用户名长度在1到72个字符之间')],
        render_kw={'id': 'blog_tilte', 'class': 'form-control collapsed', 'placeholder': '请输入文章标题', 'required': 'reqiured'})
    info = StringField(
        label='文章标题',
        validators=[DataRequired(message='简介'),
                    Length(max=100, message='简介在一百字以内')],
        render_kw={'id': 'blog_info', 'class': 'form-control collapsed', 'placeholder': '请输入简介', 'required': 'reqiured'})
    text = TextAreaField(label='文章正文',
        validators=[DataRequired(message='正文'),
                    Length(min=1, message='正文不能为空')],
        render_kw={'id': 'blog_text', 'class': 'form-control collapsed', 'placeholder': '请输入正文', 'required': 'reqiured'})
    submit = SubmitField(
        render_kw={'value': '添加文章', 'class': 'form-control'})

# class PostForm(Form):
#     """Post Form."""
#
#     title = StringField('Title', [DataRequired(), Length(max=255)])
#     text = TextAreaField('Blog Content', [DataRequired()])
