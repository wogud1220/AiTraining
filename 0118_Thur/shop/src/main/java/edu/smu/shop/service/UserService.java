package edu.smu.shop.service;

import edu.smu.shop.model.UserDTO;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    SqlSession sqlSession;
    private final String NAMESPACE="edu.smu.shop.UserMapper";
    public UserDTO auth(UserDTO temp){
        return sqlSession.selectOne(NAMESPACE + ".auth", temp);
    }
    public boolean validate(UserDTO temp){
        return sqlSession.selectOne(NAMESPACE+".validate",temp)==null;
    }
    public void register(UserDTO temp){
        sqlSession.insert(NAMESPACE+".register",temp);
    }
}
