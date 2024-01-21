package edu.smu.board.controller;

import edu.smu.board.model.ReplyDTO;
import edu.smu.board.model.UserDTO;
import edu.smu.board.service.BoardService;
import edu.smu.board.service.ReplyService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/reply/")

public class ReplyController {
    @Autowired
    private BoardService boardService;
    @Autowired
    private ReplyService replyService;
    @PostMapping("write/{boardId}")
    public String write(HttpSession session, ReplyDTO replyDTO, @PathVariable int boardId){
        //1. 로그인 상태 확인
        UserDTO logIn = (UserDTO) session.getAttribute("logIn");
        if(logIn==null){
            return "redirect:/";
        }
        //2. 유효한 게시글인지 확인
        if(boardService.selectOne(boardId)==null){
            return "redirect:/board/showAll";
        }

        //3. 지금 로그인한 회원의 번호를 replyDTO에 입력
        replyDTO.setWriterId(logIn.getId());

        //4. replyDTO의 내용을 DB에 저장
        replyService.insert((replyDTO));

        return "redirect:/board/showOne/"+boardId;

    }
    @PostMapping("update/{id}")
    public  String update(HttpSession session, ReplyDTO replyDTO, @PathVariable int id){
        UserDTO logIn=(UserDTO) session.getAttribute("logIn");
        if(logIn==null){
            return "redirect:/";
        }
        ReplyDTO origin = replyService.selectById(id);
        if(logIn.getId() == origin.getWriterId()){
            replyService.update(replyDTO);
        }
        return "redirect:/board/showOne/" + origin.getBoardId();
    }
    @GetMapping("delete/{id}")
    public String delete(HttpSession session,@PathVariable int id){
        UserDTO logIn=(UserDTO) session.getAttribute("logIn");
        if(logIn==null){
            return "redirect:/";
        }
        ReplyDTO origin = replyService.selectById(id);
        if(logIn.getId()==origin.getWriterId()){
            replyService.delete(id);
    }
        return"redirect:/board/showOne/" + origin.getBoardId();
    }
}
