FROM adoptopenjdk/openjdk11:alpine
LABEL maintainer="jinseong.dev@gmail.com"
VOLUME /tmp
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ARG SPRING_ENV
ENTRYPOINT ["java", "-Dspring.profiles.active=${SPRING_ENV}", "-Duser.timezone=Asia/Seoul", "-jar", "/app.jar"]
