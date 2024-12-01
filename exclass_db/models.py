from django.db import models


class MajorSubject(models.Model):
    sub_area = models.CharField(max_length=255)  # 이수구분/전필
    sub_code = models.CharField(max_length=100)  # 과목코드
    sub_name = models.CharField(max_length=255)  # 과목명
    sub_credit = models.FloatField()  # 학점


# class HumanSubject(models.Model):
#     sub_sub = models.CharField(max_length=255) #주제
#     sub_area = models.CharField(max_length=255)  # 이수구분/전필
#     sub_code = models.CharField(max_length=100)  # 과목코드
#     sub_name = models.CharField(max_length=255)  # 과목명
#     sub_credit = models.FloatField()  # 학점

    def __str__(self):
        return self.sub_code
