FROM nginx:1.14-alpine
LABEL maintainer="고지혜<aseiwej@naver.com>"

# 우리가 실행할 명령구들을 작성, .(현재 경로)
COPY . /usr/share/nginx/html/

RUN echo "작업완료"

# 컨테이너 안에서 노출
EXPOSE 80

# RUN과 CMD는 같은 명령어. CMD에 띄어쓰기 단위로 값을 전달해서 실행하는 걸 권장
# 다음과정으로 가버리니까 실행이 안됨
RUN nginx -g "daemon off;"  
# RUN은 빌드 과정에서 실행, CMD는 빌드한 컨테이너가 동작할 때 실행
# RUN echo "실행함"
# CMD ["echo", "실행함"]
# 내부적으로 띄어쓰기 창으로 nginx -g daemon off 실행하는 명령어가 됨
# CMD ["nginx", "-g", "daemon off;"]
