package routes

import (
	"user-crud-read/src/Controller"

	"github.com/gin-gonic/gin"
)

// Setup routes for user retrieval
func SetupRouter() *gin.Engine {
	r := gin.Default()
	r.GET("/api/users/:user_id", Controller.GetUser)
	return r
}
