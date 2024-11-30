from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse

def csrf_token_view(request):
    """
    CSRF 토큰을 반환하는 뷰
    """
    csrf_token = get_token(request)  # CSRF 토큰을 가져옵니다.
    return JsonResponse({'csrfToken': csrf_token})  # JSON 형식으로 반환
