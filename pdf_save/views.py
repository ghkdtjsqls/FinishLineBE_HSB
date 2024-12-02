import pdfplumber
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
import os
import re
from .models import MySubjectList  # 모델 임포트

def save_subjects_to_db(subjects_data):
    for subject in subjects_data:
        # MySubjectList 모델을 사용하여 교과목 데이터를 DB에 저장
        subject_instance = MySubjectList(
            year=subject['이수년도'],
            semester=subject['학기'],
            sub_area=subject['이수구분'],
            sub_sub=subject['이수영역'],  # 이수 영역/주제
            sub_name=subject['교과목명'],  # 교과목명
            credit=subject['학점'],  # 학점
            grade=subject['등급'],  # 등급
        )
        subject_instance.save()

# PDF 제목에서 이수년도와 학기를 추출하는 함수
def extract_year_and_semester_from_title(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # 첫 페이지를 읽어 제목을 추출
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        # 정규 표현식으로 '이수년도 - 학기' 패턴을 찾아서 추출
        # 예: '2024 - 1 학기', '2023 - 2 학기'
        match = re.search(r'(\d{4})\s*-\s*(\d)\s*학기', text)

        if match:
            year = match.group(1)  # 이수년도 (예: 2024)
            semester = match.group(2)  # 학기 (예: 1)
            return year, semester
        else:
            return None, None

# 교과목 데이터를 추출하는 함수
def extract_subjects_from_table(pdf_path):
    year, semester = extract_year_and_semester_from_title(pdf_path)
    with pdfplumber.open(pdf_path) as pdf:
        table_data = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    # '교양', '전필', '전선', '소전' 항목을 가진 행만 선택
                    if any(subject_type in row for subject_type in ["교양", "전필", "전선", "소전", "교필", "교선", "전공선택", "전공필수"]):
                        # 표에서 이수 구분, 이수 영역/주제, 교과목명 등을 분리하여 저장
                        subject_data = {
                            '이수년도': year,  # 제목에서 추출한 이수년도
                            '학기': semester,  # 제목에서 추출한 학기
                            '이수구분': row[0],  # 예: 교양
                            '이수영역': row[1] if row[1] != '' else ' ',  # 공란이면 스페이스바로 대체
                            '교과목명': row[4],  # 예: 대학생을 위한 실용금융
                            '학점': row[7],      # 예: 2
                            '등급': row[9],      # 예: A+
                        }
                        table_data.append(subject_data)
    return table_data


@api_view(['POST'])
def upload_pdf(request):
    if 'files' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    files = request.FILES.getlist('files')  # 여러 파일 처리
    uploaded_files = []

    for file in files:
        # 파일 시스템에 저장
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(file.name, file)  # 파일 저장
        file_url = fs.url(filename)  # 파일의 URL 반환

        # 파일 텍스트 추출 (PDF에서 표 추출)
        if file.name.endswith('.pdf'):
            pdf_path = os.path.join(settings.MEDIA_ROOT, filename)
            
            # PDF에서 교과목 데이터를 추출하는 함수 호출
            subject_table = extract_subjects_from_table(pdf_path)

            save_subjects_to_db(subject_table)  # DB에 저장하는 부분

            # 추출된 교과목 데이터를 출력
            print(f"Extracted subjects: {subject_table}")

            # JSON 응답에 교과목 데이터를 추가
            uploaded_files.append({
                'file_url': file_url,
                'extracted_subjects': subject_table
            })

    return JsonResponse({'message': 'File(s) uploaded successfully', 'files': uploaded_files})
