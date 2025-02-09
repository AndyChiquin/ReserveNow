package Controller

import (
	"net/http"
	"user-crud-create/src/Model"
	"user-crud-create/src/config"

	"github.com/gin-gonic/gin"
)

// Create a new user
func CreateUser(c *gin.Context) {
	db := config.InitDB()
	var user Model.User
	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid request"})
		return
	}

	// Check if user already exists
	var existingUser Model.User
	if err := db.Where("email = ?", user.Email).First(&existingUser).Error; err == nil {
		c.JSON(http.StatusConflict, gin.H{"error": "Email already exists"})
		return
	}

	db.Create(&user)
	c.JSON(http.StatusCreated, gin.H{"message": "User created successfully", "data": user})
}
