<%@  page language="java" contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <title>
        인덱스
    </title>
</head>
<body>
<form action="/user/auth" method="post">
    <div class="row justify-content-center">
        <div class="col-6">
    아이디:<input type="text" name="username" class="form-control"><br/>
        </div>
    </div>

    <div class="row justify-content-center">
        <div class="col-6">
    비밀번호:<input type="text" name="password" class="form-control"><br/>
        </div>
    </div>

    <div class="row justify-content-center">
        <div class="col-4">
    <input type="submit" value="로그인" class="btn btn-outline-success">
        </div>
        <div class="col-3">
            <a href="/user/register" class="btn btn-outline-info">회원 가입</a>
        </div>
    </div>
</form>
</body>
</html>