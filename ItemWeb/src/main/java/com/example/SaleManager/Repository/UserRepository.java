package com.example.SaleManager.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.example.SaleManager.Model.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
	@Query("SELECT u FROM User u WHERE u.username = ?1")
	//User findByEmail(String email);
	User findByUsername(String username);
}
