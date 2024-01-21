<%@ page language="java" contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>
<%@ taglib prefix="fmt" uri="jakarta.tags.fmt" %>

<html>
<head>
    <title>게시판</title>
</head>
<body>
<table>
    <thead>
    <tr>
        <th>글 번호</th>
        <th>제목</th>
        <th>작성자</th>
        <th>작성일</th>
    </tr>
    </thead>
    <tbody>
    <c:forEach items="#{list}" var="b">
        <tr>
            <td>${b.id}</td>
            <td><a href="/board/showOne/${b.id}">
                    ${b.title}
                </a>
            </td>
            <td>${b.nickname}</td>
            <td><fmt:formatDate value="${b.entryDate}" pattern="yy/MM/dd HH:mm:ss"/></td>
        </tr>
    </c:forEach>

    </tbody>
</table>
<a href="/board/write">글 쓰기</a>
</body>
</html>