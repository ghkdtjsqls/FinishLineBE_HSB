#새 mySQL로 변경
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test1_django', #DB이름
        'USER': 'test1_django_id', #db 사용자 계정이름
        'PASSWORD': 'sql#4746test1',
        'HOST': 'localhost', #나중에 aws로 연결
        'PORT': '3306', #mySQL 포트번호
    }
}