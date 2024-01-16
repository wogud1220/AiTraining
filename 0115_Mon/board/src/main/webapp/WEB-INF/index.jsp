<%@  page language="java" contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>
        인덱스
    </title>
</head>
<body>
<form action="/user/auth" method="post">
    아이디:<input type="text" name="username"><br/>
    비밀번호:<input type="text" name="password"><br/>
    <input type="submit" value="로그인">
</form>
<a href="user/register">회원가입</a>
</body>
</html>