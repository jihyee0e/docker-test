# 8.0에 비해 194MB로 줄었음.
FROM alpine:latest as builder  

RUN apk add --no-cache openjdk8 curl tar && \
    curl -O https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.89/bin/apache-tomcat-9.0.89.tar.gz && \
    mkdir -p /usr/local/tomcat && \
    tar -xzf apache-tomcat-9.0.89.tar.gz -C /usr/local/tomcat --strip-components=1 && \
    rm apache-tomcat-9.0.89.tar.gz && \
    rm -rf /usr/local/tomcat/webapps/examples \
           /usr/local/tomcat/webapps/docs \
           /usr/local/tomcat/webapps/manager \
           /usr/local/tomcat/webapps/host-manager && \
    chmod +x /usr/local/tomcat/bin/*.sh
    
# index.html 파일을 컨테이너 내의 특정 경로로 복사합니다.
COPY index.html /usr/local/tomcat/webapps/ROOT/index.html

# Stage2: 실행 빌드 - 불필요한건 걷어내고 필요한 것만 가져옴
# 경량화된 리눅스 이미지
FROM alpine:latest

# 경량화된 자바 이미지 - 개발자용 JDK가 아닌 자바 파일 실행용 JRE만 설치 
RUN apk add --no-cache openjdk8-jre-base && \
    rm -rf /var/cache/apk/*

# 환경변수 지정
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $JAVA_HOME/bin:$CATALINA_HOME/bin:$PATH

COPY --from=builder /usr/local/tomcat /usr/local/tomcat

# Tomcat 사용자와 그룹을 생성하고 권한을 설정
RUN addgroup -S tomcat && adduser -S -G tomcat -h /usr/local/tomcat -s /sbin/nologin tomcat && \
    chown -R tomcat:tomcat /usr/local/tomcat

USER tomcat
WORKDIR /usr/local/tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]
