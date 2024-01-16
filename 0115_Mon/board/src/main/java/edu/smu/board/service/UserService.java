package edu.smu.board.service;

import edu.smu.board.model.UserDTO;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    SqlSession sqlSession;
    private final String NAMESPACE = "edu.smu.board.UserMapper";

    public UserDTO auth(UserDTO temp){
        return sqlSession.selectOne(NAMESPACE + ".auth", temp);
    }
    public void register(UserDTO temp){
        sqlSession.insert(NAMESPACE+".register",temp);
    }
    public boolean validate(UserDTO temp){
        return sqlSession.selectOne(NAMESPACE+".validate",temp)==null;
    }

}
