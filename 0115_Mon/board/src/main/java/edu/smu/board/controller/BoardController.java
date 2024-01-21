package edu.smu.board.controller;

import edu.smu.board.model.BoardDTO;
import edu.smu.board.model.ReplyDTO;
import edu.smu.board.model.UserDTO;
import edu.smu.board.service.BoardService;
import edu.smu.board.service.ReplyService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/board/")

public class BoardController {
    @Autowired
    private BoardService boardService;
    @Autowired
    private ReplyService replyService;


    @GetMapping("showAll")

    public String showAll(HttpSession session, Model model) {
        UserDTO logIn = (UserDTO)session.getAttribute("logIn");
        if (logIn == null) {
            return "redirect:/";
        }
        model.addAttribute("logIn", logIn);
        model.addAttribute("list", boardService.selectAll());
        return "board/showAll";
    }

    @GetMapping("write")
    public String showWrite() {
        return "board/write";
    }

    @PostMapping("write")
    public String write(HttpSession session, BoardDTO boardDTO) {
        UserDTO logIn = (UserDTO) session.getAttribute("logIn");
        if (logIn == null) {
            return "redirect:/";
        }
        boardDTO.setWriterId(logIn.getId());
        boardService.write(boardDTO);

        return "redirect:/board/showAll";
    }

    @GetMapping("showOne/{id}")                         //글 번호
    public String showOne(HttpSession session, @PathVariable int id, Model model) {

        BoardDTO boardDTO = boardService.selectOne(id);
        if (boardDTO != null) {
            model.addAttribute("boardDTO", boardDTO);
            model.addAttribute("replyList",replyService.selectByBoardId(id));
            UserDTO logIn = (UserDTO)session.getAttribute("logIn");
            if(logIn!=null){//로그인 했을 때
                model.addAttribute("userId",logIn.getId());
            }
            return "board/showOne";
        }
        return "redirect:/";
    }

    @GetMapping("update/{id}")
    public String showUPdate(HttpSession session, @PathVariable int id, Model model) {
        BoardDTO boardDTO = boardService.selectOne(id);
        //1. 로그인 하지 않응ㄴ 사용자일 경우
        UserDTO logIn = (UserDTO) session.getAttribute("logIn");
        if (logIn == null) {
            return "redirect:/";
        }
        //2. 글 번호가 유효하지 않을 경우
        if (boardDTO == null) {
            return "redirect:/board/showAll";
        }
        //3. 로그인 돼있고, 유효한 경우
        model.addAttribute("boardDTO", boardDTO);
        return  "board/update";
    }

    @PostMapping("update/{id}")
    public String update(HttpSession session, @PathVariable int id, BoardDTO boardDTO){
        //1.로그인 상태 확인
        UserDTO logIn = (UserDTO) session.getAttribute("logIn");
        if(logIn == null){
            return "redirect:/";
        }

        //2. 유효한 글 번호인지 체크
        BoardDTO origin = boardService.selectOne(id);
        if(origin == null){
            return "redirect:/board/showAll";
        }

        //3. 글쓴이가 맞는 지 확인
        if(logIn.getId() != origin.getWriterId()){
            return "redirect:/board/showOne/"+id;
        }
        //위의 조건 다 통과시 업데이트
        boardService.update(boardDTO);
        return  "redirect:/board/showOne/"+id;
    }
    @GetMapping("delete/{id}")
    public String delete(HttpSession session, @PathVariable int id){

        //1. 사용자가 로그인 했는지 확인
        if(session.getAttribute("logIn")==null)
            return "redirect:/";

        //2. 게시글이 존재하는지 확인
        if(boardService.selectOne(id) == null){
            return "redirect:/board/showAll";
        }

        //3. 사용자가 해당 게시글의 작성자가 맞는지 확인
        UserDTO logIn = (UserDTO) session.getAttribute("logIn");
        BoardDTO boardDTO = boardService.selectOne(id);

        if(logIn.getId() != boardDTO.getWriterId()){
            return "redirect:/board/showOne/"+id;
        }

        //4. 문제가 없으므로 삭제 후 리스트 보기로 이동
        boardService.delete(id);
        return "redirect:/board/showAll";
    }

}
