from django.db import models
from django.conf import settings

class MySubjectList(models.Model):
    year = models.CharField(max_length=4)
    # 학기 (예: 1)
    semester = models.CharField(max_length=1)
    # 이수 구분 (예: 교양, 전필, 전선 등)
    sub_area = models.CharField(max_length=50)
    # 이수 영역/주제 (예: 정치와 경제)
    sub_sub = models.CharField(max_length=200, blank=True, null=True)
    # 교과목명 (예: 대학생을 위한 실용금융)
    sub_name = models.CharField(max_length=200)
    # 학점 (예: 2)
    credit = models.DecimalField(max_digits=3, decimal_places=1)
    # 등급 (예: A+)
    grade = models.CharField(max_length=3)
    
    def __str__(self):
        return f"{self.subject_name} ({self.year}-{self.semester} {self.subject_type})"
