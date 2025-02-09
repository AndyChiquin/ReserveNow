package routes

import (
	"user-crud-delete/src/Controller"

	"github.com/gin-gonic/gin"
)

// Setup routes for deleting users
func SetupRouter() *gin.Engine {
	r := gin.Default()
	r.DELETE("/api/users/:user_id", Controller.DeleteUser)
	return r
}
