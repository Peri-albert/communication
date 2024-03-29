
FROM registry.cn-hangzhou.aliyuncs.com/aix/python27:latest

ADD . /service
WORKDIR /service

RUN pip install -i http://pypi.douban.com/simple/ \
    --trusted-host pypi.douban.com \
    -r ./requirements.txt \
    && rm -rf ~/.pip

ENTRYPOINT ["/usr/local/bin/dumb-init", "/bin/bash", "start_service.sh"]

