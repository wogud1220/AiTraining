package edu.smu.board.controller;

import edu.smu.board.model.UserDTO;
import edu.smu.board.service.UserService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/user/")
public class UserController {


    @Autowired
    UserService userService;


    @PostMapping("auth")
    public String auth(HttpSession session, UserDTO temp){
        UserDTO result = userService.auth(temp);
        if(result !=null){
            session.setAttribute("logIn",result);
            return "redirect:/board/showAll";
        }
        else{

        return "redirect:/";
    }
    }
    @GetMapping("register")

    public String showRegister(){
        return "user/register";
    }

    @PostMapping("register")

    public String register(Model model, UserDTO temp){
        System.out.println("temp: "+temp);
    if(userService.validate(temp)){
        userService.register(temp);
    return "redirect:/";
    }
    else{model.addAttribute("message", "중복된 아이디입니다.");
        model.addAttribute("temp", temp);
        return "user/register";
    }
    }
}
