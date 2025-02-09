package Controller

import (
	"net/http"
	"user-crud-read/src/Model"
	"user-crud-read/src/config"

	"github.com/gin-gonic/gin"
)

// Get user by ID
func GetUser(c *gin.Context) {
	db := config.InitDB()
	var user Model.User
	id := c.Param("user_id")

	if err := db.First(&user, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "User not found"})
		return
	}

	c.JSON(http.StatusOK, user)
}
