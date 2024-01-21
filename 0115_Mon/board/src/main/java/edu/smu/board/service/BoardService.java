package edu.smu.board.service;

import edu.smu.board.model.BoardDTO;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BoardService {
    @Autowired
    private SqlSession session;
    private final String NAMESPACE="edu.smu.board.BoardMapper";
    public List<BoardDTO> selectAll(){

        return session.selectList(NAMESPACE+".selectAll");
    }
    public void write(BoardDTO b){
        session.insert(NAMESPACE+".write", b);
    }
    public BoardDTO selectOne(int id){
        return session.selectOne(NAMESPACE+".selectOne", id);
    }
    public void update(BoardDTO boardDTO){
        session.update(NAMESPACE+".update", boardDTO);
    }

    public void delete(int id){
        session.delete(NAMESPACE+".delete", id);
    }
}

