<%@ page language="java" contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>

<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <title>${boardDTO.id}번 게시글</title>
</head>
<body>
<div class="container h-100">
        <div class="row justify-content-center my-auto p-3">
            <div class="col-3 text-end">제목</div>
            <div class="col-6">${boardDTO.title}</div>
        </div>
        <div class="row justify-content-center my-auto p-3">
            <div class="col-3 text-end">작성자</div>
            <div class="col-6">${boardDTO.nickname}</div>
        </div>
        <div class="row justify-content-center my-auto p-3">
            <div class="col-3 text-end">작성시간</div>
            <div class="col-6">${boardDTO.entryDate}</div>
        </div>
        <div class="row justify-content-center my-auto p-3 border-bottom border-red">
            <div class="col-3 text-end">수정시간</div>
            <div class="col-6">${boardDTO.modifyDate}</div>
        </div>
    <div class="row justify-content-center my-auto p-3">
        <div class="col-6">
            ${boardDTO.content}
        </div>
    </div>
    <c:if test="${userId eq boardDTO.writerId}">
        <div class="row justify-content-center my-auto p-1">
            <a href="/board/update/${boardDTO.id}" class="col-4 btn btn-info">수정하기</a>
            <a href="/board/delete/${boardDTO.id}" class="col-4 btn btn-danger">삭제하기</a>
        </div>

    </c:if>
    <div class="row justify-content-center my-auto p-1 border border-danger text-center">
        <div class="col-4">댓글 목록</div>
    </div>
    <c:forEach items="${replyList}" var="r">
        <div class="row justify-content-center">
            <div class="col-6 border border-primary">
                <c:choose>
                    <c:when test="${userId eq r.writerId}">
                        <form action ="/reply/update/${r.id}" method="post">
                                ${r.nickname}
                            <br>
                            <input type="text" class="from-control"
                                   value="${r.content}" name="content">
                            at ${r.modifyDate}
                            <input type="submit" class="btn btn-outline-primary" value="수정">
                            <a href="/reply/delete/${r.id}" class="btn btn-outline-danger">삭제</a>
                        </form>
                    </c:when>
                    <c:otherwise>
                        ${r.nickname}
                        <input type="text" class="from-control"
                               value=" ${r.content}" disabled>
                        ${r.modifyDate}
                    </c:otherwise>
                </c:choose>
            </div>

        </div>
    </c:forEach>
    <div class="row justify-content-center">
        <div class="col-6 border border-primary">
            <form action="/reply/write/${boardDTO.id}" method="post">
                <input type="text" class="form-control" name="content">
                <input type="submit" value="댓글 입력" class="btn btn-outline-success">
            </form>
        </div>
    </div>





</div>

</body>
</html>