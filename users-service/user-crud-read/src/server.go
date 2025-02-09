package main

import (
	"log"
	"user-crud-read/src/routes"
)

func main() {
	r := routes.SetupRouter()
	log.Println("🚀 User Read Service running on port 8007")
	r.Run(":8007")
}
