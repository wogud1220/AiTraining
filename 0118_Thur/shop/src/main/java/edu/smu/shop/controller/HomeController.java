package edu.smu.shop;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
@Controller
public class HomeController {
    @GetMapping("/")
    public String showIndex(){
        System.out.println("showIndex()");
        return "index";
    }
}