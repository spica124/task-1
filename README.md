# tesk-1
_들어가기전_
유저 모델을 import 시킨뒤 
  ```AUTH_USER_MODEL = 'users.User'```

settings.py 에 모델을 사용한다고 쓴다.


__________________________________________


1.models.py 에 사용자정보를 입력받을 틀을 class로 짠다
```
class User(AbstractUser):
    student_id = models.CharField(max_length=10)
```
일단은 학번만 입력하고 나중에 추가를 이어나간다


2.나중에 추가할때는 아래와 같은 방식으로 이어나가면 된다.
```
        user = User.objects.create_user(username, email, password)
        user.favorite = favorite
        user.student_id = student_id
        user.gender = gender
        
        user.Department = Department
        user.save()
```


____________________________________________________________



+html에서 input으로 입력받은 정보들을 request와post를 이용하여 db에 저장한다
```
 username  = request.POST["username"]
        password  = request.POST["password"]
        email  = request.POST["email"]
        
```


+django 내장함수를 사용해서 db에 있는 아이디,비번인지 체크한뒤 true , false 로 return한다
```
from django.contrib.auth import authenticate,login,logout
user = authenticate(username=username,password=password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else :
            print("인증실패")
```
login(request,user)은 로그인이 성공했을때 
메인페이지로 넘기기위한 코드이다.


>이 코드는 백엔드의 코드를 작성한것이므로 프론트엔드의 부분은 간단하게 작성하여
>오류가있는지 없는지 판별한다.
```

<br>
{% if user.is_authenticated %}
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <p>login succeed</p>
    </body>
    
    <a href="{%url 'user:logout'%}">로그아웃</a>
</html>
{%else%}
<form action="" method="POST">
    {% csrf_token %}
    <input name="username" type="text">
    <input name="password" type="password">
    <input type="submit" value="로그인">
</form>
<a href="{% url 'user:signup' %}">회원가입</a>
{%endif%}
```


******************************************

서버를 실행할때는 cmd에서 프로그램 위치로 이동한뒤(cd로 이동) 
``` python mange.py runserver ```
으로 실행시킨다.
