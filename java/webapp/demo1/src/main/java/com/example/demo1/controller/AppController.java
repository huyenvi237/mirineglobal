package com.example.demo1.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AppController {
    @RequestMapping("") 
    public String callWeb() {
        int x = (int) (Math.random()*3);

        if (x % 2 == 0 ) {
            System.out.println (x);
            return "index.html";
        } else {
            return "index1.html";
        }
    }

    @RequestMapping("/file")
    public void callW(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException{
        res.setContentType("text/html;charset=utf-8");
        PrintWriter out = res.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Check Page</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>Hello</h1>");
        out.println("<h2>Submit after check information</h2>");
        out.println("Account:<strong>" + req.getParameter("account") + "</strong><br>");
        out.println("Password:<strong>" + req.getParameter("pass") + "</strong><br>");
        String sex = req.getParameter("sex");
        if (sex.equals("Male")){
            sex = "Male";
        } else {
            sex = "Female";
        }
        out.println("Sex:<strong>" + sex + "</strong><br>");
        out.println("</body>");
        out.println("</html>");
    }

    @RequestMapping("/account")
    public String callAccount(){
        return "form.html";
    }

    @RequestMapping("/book")
    public String getBook() {
        return "session.html";
    }

    @RequestMapping("/checkbook")
    public void checkB(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException{
        HttpSession session = req.getSession(true);
        ArrayList<String> bookList = 
            (ArrayList<String>)session.getAttribute("cart");
        
        if (bookList == null) {
            bookList = new ArrayList<String>();
        } else {
            req.setCharacterEncoding("utf-8");
            String book = req.getParameter("book");
            bookList.add(book);
        }
        session.setAttribute("cart", bookList);
        res.setContentType("text/html;charset=utf-8");
        PrintWriter out = res.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Order Menu</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h2>Choose following title<h2>");
        out.println("<form action=\"checkbook\" method=\"post\">");
        out.println("<select name=\"book\" size=\"1\">");
        out.println("<option value=\"Java\"> Java</option>");
        out.println("<option value=\"Oracle\"> Oracle</option>");
        out.println("<option value=\"Java Basic\"> Java Basic</option>");
        out.println("</select>");
        out.println("<input type=\"submit\" value=\"submit\">");
        out.println("<h2>Cart</h2>");

        for (int i = 0; i <bookList.size();i++) {
            out.println(bookList.get(i) + "<br>");
        }

        out.print("</body></html>");
    }
    
}
