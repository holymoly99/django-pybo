from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField('제목', max_length=200, help_text="질문의 제목은 한줄로 작성해라")
    content = models.TextField('내용', help_text="침착하게 내용을 작성하세요")
    create_date = models.DateTimeField('작성일')
    modify_date = models.DateTimeField(null=True, blank=True)

    voter = models.ManyToManyField(User, related_name='voter_question') # author의 User 모델과 중복되기 때문에 오류가난다. 별명인 voter_question을 주어 이름 중복 문제를 해결

    def __str__(self):
        return f'{self.id} {self.subject}'

class Answer(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 정의
    content = models.TextField('답변 내용')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')
    create_date = models.DateTimeField('생성일')
    modify_date = models.DateTimeField('수정일', null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
