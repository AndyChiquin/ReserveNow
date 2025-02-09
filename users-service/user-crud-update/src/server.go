package main

import (
	"log"
	"user-crud-update/src/routes"
)

func main() {
	r := routes.SetupRouter()
	log.Println("🚀 User Update Service running on port 8008")
	r.Run(":8008")
}
