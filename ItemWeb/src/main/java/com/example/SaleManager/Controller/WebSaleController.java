package com.example.SaleManager.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.example.SaleManager.Model.Item;
import com.example.SaleManager.Model.User;
import com.example.SaleManager.Repository.ItemRepository;
import com.example.SaleManager.Repository.UserRepository;
import com.example.SaleManager.Service.ItemService;

@Controller
public class WebSaleController {
	
	@Autowired
	private UserRepository userRepository;
	
	@Autowired
	private ItemRepository itemRepository;
	
	@Autowired
	private ItemService itemService;
	
	@RequestMapping("/login")
	public String login(Model model) {
		User user = new User();
		model.addAttribute("user",user);
		
		return "login";
	}
	
	@GetMapping("/register")
	public String showSignUpForm(Model model) {
		model.addAttribute("user", new User());
		return "SignPage";
	}
	
	@PostMapping("/process_register")
	public String process(User user) {
		BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
		String encodedPassword = encoder.encode(user.getPassword());
		user.setPassword(encodedPassword);
		
		userRepository.save(user);
		
		return "register";
	}
	
	@GetMapping("/homepage")
	public String home(Model model) {
		List<Item> itemList = itemService.itemsList();
		model.addAttribute("itemList", itemList);
		return "HomePage";
	}
	
	@GetMapping("/new_item")
	public String newItem(Model model) {
		Item item = new Item();
		model.addAttribute("item", item);
		return "new_form";
	}
	
	@RequestMapping(value = "/save", method = RequestMethod.POST)
	public String save(@ModelAttribute("sale") Item item) {
		itemRepository.save(item);
		
		return "redirect:/homepage";
	}
	
	@RequestMapping("/edit/{id}")
	public ModelAndView showEdit(@PathVariable(name="id") Long id) {
		ModelAndView modelAndView = new ModelAndView("edit_form");
		Item item = itemRepository.getById(id);
		modelAndView.addObject("item", item);
		return modelAndView;
	}
	
	@RequestMapping(value = "/update", method = RequestMethod.POST)
	public String update(@ModelAttribute("sale") Item item) {
		itemService.update(item);
		
		return "redirect:/homepage";
	}
	
	@RequestMapping("/delete/{id}")
	public String delete(@ModelAttribute("sale") Item item) {
		itemRepository.deleteById(item.getId());
		
		return "redirect:/homepage";
	}

}
