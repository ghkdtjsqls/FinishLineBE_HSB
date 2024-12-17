from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# 사용자 관리 클래스 정의
class UserManager(BaseUserManager):
    def create_user(self, studentId, password=None, **extra_fields):
        if not studentId:
            raise ValueError('The Student ID must be set')
        user = self.model(studentId=studentId, **extra_fields)
        user.set_password(password)  # 비밀번호를 해시화
        user.save(using=self._db)
        return user

    def create_superuser(self, studentId, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(studentId, password, **extra_fields)

# 커스텀 사용자 모델 정의
class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    studentId = models.CharField(max_length=20, unique=True)

    # majortype, secondmajor, microdegree 필드가 선택적 필드로 설정
    majortype = models.CharField(max_length=100, null=True, blank=True)  # null=True, blank=True로 설정
    secondmajor = models.CharField(max_length=100, null=True, blank=True)
    microdegree = models.CharField(max_length=100, null=True, blank=True)

    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'studentId'
    REQUIRED_FIELDS = ['name', 'department']  # 필수 필드 목록 추가
    
    # 커스텀 모델에 UserManager 추가
    objects = UserManager()

    def __str__(self):
        return self.name

    # # is_anonymous 메소드 추가
    # @property
    # def is_anonymous(self):
    #     return not self.is_authenticated

    # # is_authenticated 메소드 추가
    # @property
    # def is_authenticated(self):
    #     return True  # 기본적으로 인증된 상태로 간주 (로그인 상태일 경우)