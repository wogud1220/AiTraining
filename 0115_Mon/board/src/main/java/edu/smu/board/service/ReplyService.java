package edu.smu.board.service;

import edu.smu.board.model.ReplyDTO;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ReplyService {
    @Autowired
    private SqlSession session;

    private final String NAMESPACE = "edu.smu.board.ReplyMapper";

    //1. 게시글 번호에 따른 댓글 리스트를 데이터베이스에서 읽어오는 메소드

    public List<ReplyDTO> selectByBoardId(int boardId){
        return session.selectList(NAMESPACE+".selectByBoardId", boardId);
    }

    //2. 댓글을 데이터베이스에 등록하는 메소드
    public void insert(ReplyDTO replyDTO) {
        session.insert(NAMESPACE + ".insert", replyDTO);
    }

    //3. 댓글을 수정하는 메소드
    public void update(ReplyDTO replyDTO) {
        session.update(NAMESPACE + ".update", replyDTO);
    }

    //4. 댓글을 삭제하는 메소드
    public void delete(int id){
        session.delete(NAMESPACE+".delete", id);
    }
//5. 개별 댓글을 불러오는 메소드
    public ReplyDTO selectById(int id){
        return session.selectOne(NAMESPACE+".selectById",id);
    }

}
