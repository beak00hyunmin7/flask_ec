from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField #유효성 검증 : DataRequired, Inputrequired, email, length....
from wtforms.validators import DataRequired, length

#사용자 신규 작성, 편집 폼 클래스
class BoardForm(FlaskForm):
    title = StringField(
        "제목",
        validators=[
            DataRequired(message="사용자명은 필수입니다."),
            length(max=30, message="30자 이내로 입력해주세요."), #유효성 검사
        ]
    )

    content = StringField(   #StringField = 문자열을 넣을 수 있는..
        "내용",
        validators=[
            DataRequired(message="내용은 필수입니다"),
            length(max = 500, message = "500자 이내로 입력해주세요.") #이메일 형식 유효성 검사
        ]
    )
    
    submit = SubmitField("등록")
