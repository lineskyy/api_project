# setup.py 파일이 있으면 pip로 설치 가능하다.
from gettext import install
from setuptools import setup

setup(
    name ="myapi", # 이 이름으로 패키지가 설치
    version = "0.0.1",  # 0.0.1 순서대로 릴리즈,메이저,마이너
    description = "my api lib",
    url = "https://github.com/lineskyy/api_project.git",
    author = "seungcheun",
    author_email ="clehftm@gmail.com",
    package = ["my_api"],
    install_requires = [
        "requests"
    ]
)
