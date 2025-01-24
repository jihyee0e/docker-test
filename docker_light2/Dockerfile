# 1단계: 빌드
FROM python:3.11-alpine as builder

# 작업 디렉터리 설정
WORKDIR /app

# 빌드 컨텍스트에서 /app/requirement.txt 불필요한 파일 제외를 위해 .dockerignore 사용 권장
# 뒤에 슬래시(/) 없어도 됨
COPY requirements.txt ./

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 2단계: 실행
FROM python:3.11-alpine

# 비루트 사용자 생성  그룹:아이디
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 작업 디렉터리 설정
WORKDIR /app

# 빌드 결과물 복사 (필요한 파일만 복사)
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

# 비루트 사용자로 실행
USER appuser

# 기본 실행 명령
CMD ["python", "app.py"]
