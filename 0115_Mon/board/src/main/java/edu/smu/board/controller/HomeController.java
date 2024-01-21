package edu.smu.board.controller;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Controller
public class HomeController {
    @GetMapping("/")
    public String showIndex(){
        System.out.println("showIndex()");
        return "index";
    }

    @GetMapping("/hello")
    public String sendHello(){
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://localhost:8000/hello/bye";
        String result = restTemplate.getForObject(url, String.class);
        System.out.println(result);
        return "redirect:/index";
    }


    @GetMapping("/hello2")
    public String sendHello2(){
        String name = "윤재형";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

        MultiValueMap<String, String> values = new LinkedMultiValueMap<>();
        values.add("name", name);

        HttpEntity<MultiValueMap<String, String>> request =
                new HttpEntity<MultiValueMap<String, String>>(values, headers);
        RestTemplate restTemplate = new RestTemplate();
        String url="http://localhost:8000/hello/bye2";

        ResponseEntity<String> response = restTemplate.postForEntity(url, request, String.class);


        System.out.println(response);
        return "redirect:/";
    }
}
