package routes

import (
	"user-crud-update/src/Controller"

	"github.com/gin-gonic/gin"
)

// Setup routes for updating user information
func SetupRouter() *gin.Engine {
	r := gin.Default()
	r.PUT("/api/users", Controller.UpdateUser)
	return r
}
