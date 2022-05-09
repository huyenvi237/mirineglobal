package com.example.demoWeb.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demoWeb.mapper.UserMapper;
import com.example.demoWeb.model.UserModel;

@Service
public class UserService {

    private final UserMapper dao;

    @Autowired
    public UserService(UserMapper dao) {
        this.dao = dao;
    }

    public boolean insert(UserModel user) {
        return dao.insert(user) > 0;
    }

    public List<UserModel> selectAll() {
        return dao.selectAll();
    }
}
