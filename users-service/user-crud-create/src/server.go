package main

import (
	"log"
	"user-crud-create/src/routes"
)

func main() {
	r := routes.SetupRouter()
	log.Println("🚀 User Create Service running on port 8006")
	r.Run(":8006")
}
