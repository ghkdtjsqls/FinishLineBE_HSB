from django.shortcuts import render
# user_auth/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # DB에 저장
            return Response({"message": "회원가입 성공!"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # 에러 출력
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            studentId = data.get('studentId')
            password = data.get('password')

            print(f"Received studentId: {studentId}, password: {password}")

            if not studentId or not password:
                return JsonResponse({"message": "Missing studentId or password"}, status=400)

            # authenticate()로 사용자 인증 처리
            user = authenticate(request, studentId=studentId, password=password)

            if user is None:
                print(f"Authentication failed for studentId: {studentId}")
                return JsonResponse({"message": "Invalid credentials"}, status=400)

            if user is not None:
                # 로그인 성공, 세션 생성
                login(request, user)

                return JsonResponse({
                    "message": "Login successful",
                    "user": {
                        "name": user.name,
                        "studentId": user.studentId,
                    }
                }, status=200)
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=400)

        except KeyError:
            return JsonResponse({"message": "Missing data"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)


def authenticate_by_student_id(studentId, password):
    try:
        user = User.objects.get(studentId=studentId)  # 커스텀 User 모델을 사용
        if user.password == password:
            return user
        else:
            return None
    except User.DoesNotExist:
        return None

