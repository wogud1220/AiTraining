<%@  page language="java" contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>

<html>
<head>
    <title>글 쓰기</title>
</head>
<body>
<form action="/board/write" method="POST">
    제목: <input type="text" name="title">
    내용: <input type="text" name="content">
    <input type="submit" value="작성하기">
</form>

</body>
</html>