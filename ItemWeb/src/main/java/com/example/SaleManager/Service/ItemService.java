package com.example.SaleManager.Service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.namedparam.BeanPropertySqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Service;

import com.example.SaleManager.Model.Item;
import com.example.SaleManager.Repository.ItemRepository;


@Service
public class ItemService {

	@Autowired
	private ItemRepository itemRepository;
	
	private JdbcTemplate jdbcTemplate;
	
	public ItemService(JdbcTemplate jdbcTemplate) {
		this.jdbcTemplate = jdbcTemplate;
	}



	public List<Item> itemsList() {
		String sql = "SELECT * FROM SALES";
		
		List<Item> listSale=jdbcTemplate.query(sql, BeanPropertyRowMapper.newInstance(Item.class));
		return listSale;
	}
	
	public void update (Item item) {
		NamedParameterJdbcTemplate updateActor = new NamedParameterJdbcTemplate(jdbcTemplate);
		String sql = "UPDATE SALES SET item=:item, quantity=:quantity, amount=:amount WHERE id=:id";
		BeanPropertySqlParameterSource param = new BeanPropertySqlParameterSource(item);
		updateActor.update(sql,param);
	}
	
}
