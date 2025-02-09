package main

import (
	"log"
	"user-crud-delete/src/routes"
)

func main() {
	r := routes.SetupRouter()
	log.Println("🚀 User Delete Service running on port 8009")
	r.Run(":8009")
}
