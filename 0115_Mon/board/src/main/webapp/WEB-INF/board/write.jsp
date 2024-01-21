<%@  page language="java" contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>

<html>
<head>
    <title>회원가입</title>
</head>
<body>
<h1>${message}</h1>
<form action="/user/register" method="post">
    아이디:<input type="text" name="username" value="${temp.username}"><br/>
    비밀번호:<input type="text" name="password"><br/>
    닉네임:<input type="text" name="nickname" value="${temp.nickname}"><br/>
    <input type="submit" value="회원가입">
</form>
</body>
</html>