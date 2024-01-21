<%@ page language="java" contentType="text/html;charset=UTF-8"%>

<html>
<head>
    <title>게시글 수정</title>
</head>
<body>
<form action="/board/update/${boardDTO.id}" method="post">
    제목:<input type="text" name="title" value="${boardDTO.title}">
    내용:<input type="text" name="content" value="${boardDTO.content}">
    <input type="submit" value="수정하기">


</form>

</body>
</html>