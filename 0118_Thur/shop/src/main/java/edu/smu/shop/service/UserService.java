package service;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;

public class UserService {
    @Autowired
    SqlSession sqlSession;
    private final String NAMESPACE="edu.smu.shop.UserMapper";
    public void register(UserDTO temp){
        sqlSession.insert(NAMESPACE+".register",temp);
    }
}
