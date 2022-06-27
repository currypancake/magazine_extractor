# magazine_extractor
잡지 추출기

## 다운 받기
[링크](https://github.com/currypancake/wiki-info-macro)
이거 따라하면 됩니다.

## 필수 파트
### 라이브러리 설치
(이미 설치되있으면 설치 안해도 됩니다.)
~~~bash
pip install bs4
pip install requests
~~~

### 쿠키 설정
[자신의 쿠키값 가져오기](https://github.com/currypancake/SaveImage)
여기 링크 들어가서 밑으로 내리다보면 자신의 쿠키값을 찾는 법 나오는데 따라서 쿠키 찾고
값 복사하고 **login_cookie.txt** 파일에 붙여넣습니다.


### 추출할 잡지 링크 설정
![ex](https://github.com/currypancake/magazine_extractor/blob/master/img/ex.png)


캐릭터 각각의 잡지 링크 말고 이렇게 한군데 다 모여있는 잡지 리스트의 링크를 복사하고 **magazine_list_url.txt** 파일에 붙여넣습니다.
> 이미지 추출할 잡지는 전부 메모 사용해서 까져있어야함!!! 안까져있으면 다운안됨!!
> 초회무료티켓도 안됨 무적권 메모로 까야함

## 사용법
1. src폴더에 들어간다.
2. 파워쉘을 켠다.
3. 아래 명령어를 입력한다. [파워쉘을 여는 법](https://www.manualfactory.net/11724)
~~~bash
python main.py
~~~
좀만 기다리면 숫자 폴더와 함께 캐릭터별로 증간호 이미지들이(대사, 효과음도 잇음) 다운되어 있습니다~

오류가 나거나 이해가 안되는 부분이 있으면 호출 ㄱㄱ 해주세요.
