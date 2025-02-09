package routes

import (
	"user-crud-create/src/Controller"

	"github.com/gin-gonic/gin"
)

// Setup routes for user creation
func SetupRouter() *gin.Engine {
	r := gin.Default()
	r.POST("/api/users", Controller.CreateUser)
	return r
}
