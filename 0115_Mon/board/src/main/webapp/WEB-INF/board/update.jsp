<%@ page language="java" contentType="text/html;charset=UTF-8"%>

<html>
<head>
    <title>${boardDTO.id}번 게시글</title>
</head>
<body>
<h1>제목: ${boardDTO.title}</h1><br/>
<h1>작성자:${boardDTO.nickname}</h1><br/>
<h1>작성시간: ${boardDTO.entryDate}</h1><br/>
<h1>수정시간 ${boardDTO.modifyDate}</h1><br/>
<h2>==========================</h2><br/>
<h1>${boardDTO.content}</h1>
</body>
</html>