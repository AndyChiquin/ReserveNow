package Controller

import (
	"net/http"
	"user-crud-delete/src/Model"
	"user-crud-delete/src/config"

	"github.com/gin-gonic/gin"
)

// DeleteUser permanently deletes a user by ID
func DeleteUser(c *gin.Context) {
	db := config.InitDB()
	var user Model.User
	id := c.Param("user_id")

	// Check if user exists
	if err := db.First(&user, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "User not found"})
		return
	}

	// Perform hard delete (permanent deletion)
	if err := db.Unscoped().Delete(&user).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to delete user"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "User permanently deleted"})
}
