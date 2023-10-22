# 기본 이미지로 파이썬 3.11를 사용합니다.
FROM python:3.11

# 환경변수를 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리를 생성하고 설정합니다.
WORKDIR /app

# 의존성을 설치합니다.
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 프로젝트 파일을 복사합니다.
COPY . /app/