package Controller

import (
	"net/http"
	"user-crud-update/src/Model"
	"user-crud-update/src/config"

	"github.com/gin-gonic/gin"
)

// Update user information
func UpdateUser(c *gin.Context) {
	db := config.InitDB()
	var user Model.User

	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid request"})
		return
	}

	if db.Model(&user).Updates(user).RowsAffected == 0 {
		c.JSON(http.StatusNotFound, gin.H{"error": "User not found or no changes made"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "User updated successfully"})
}
