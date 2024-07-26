FROM python:3.10

RUN mkdir -p /src/app/

WORKDIR /src/app/

COPY ./ /src/app/

RUN pip install tensorflow[and-cuda]

RUN python -m pip install "tensorflow[and-cuda]==2.15" --extra-index-url https://pypi.nvidia.com

RUN pip install -r requirements.txt

