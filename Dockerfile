FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["/docker-entrypoint.sh"]
