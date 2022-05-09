package com.example.demoWeb.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.example.demoWeb.model.UserModel;
import com.example.demoWeb.service.UserService;

@Controller
public class UserController {
    private final UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;

    }

    @RequestMapping("/new")
    public String addUser(Model model) {
        model.addAttribute("User", new UserModel());
        return "NewUser.html";
    }

    @PostMapping("/new")
    public String create(@Validated @ModelAttribute UserModel user, Model model) {
        userService.insert(user);
        return "redirect:userlist";
    }

    @GetMapping("/userlist")
    public String displayUsers(Model model) {
        List<UserModel> users = userService.selectAll();
        model.addAttribute("users", users);
        return "UserList.html";
    }
}
