# docker build -t pyspark:latest ./
ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8
ARG PYTHON_VERSION=3.9.8

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

COPY --from=py3 / /

ARG PYSPARK_VERSION=3.2.0
RUN pip --no-cache-dir install pyspark==${PYSPARK_VERSION}
RUN pip --no-cache-dir install pandas
RUN pip --no-cache-dir install pyarrow
RUN pip --no-cache-dir install findspark
RUN pip --no-cache-dir install grpcio
RUN pip --no-cache-dir install tqdm
RUN pip --no-cache-dir install pyngrok
RUN pip --no-cache-dir install grpcio-tools

RUN mkdir -p /stream

ENTRYPOINT ["python"]