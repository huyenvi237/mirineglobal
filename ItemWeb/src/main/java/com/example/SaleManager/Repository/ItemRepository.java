package com.example.SaleManager.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.example.SaleManager.Model.Item;

@Repository
public interface ItemRepository extends JpaRepository<Item, Long> {

}
