from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/quesiton')


@bp.route('/list/')
def _list(): # _를 앞에 쓴 이유는 list가 파이썬의 예약어이기 떄문이다.
    question_list = Question.query.order_by(Question.create_date.desc()) # 역순 정렬
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question) 