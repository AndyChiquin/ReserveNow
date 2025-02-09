package config

import (
	"fmt"
	"log"
	"os"
	"user-crud-update/src/Model"

	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// Initialize PostgreSQL connection and migrate schema
func InitDB() *gorm.DB {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("❌ Error loading .env file")
	}

	dsn := fmt.Sprintf(
		"host=%s user=%s password=%s dbname=%s port=%s sslmode=require",
		os.Getenv("DB_HOST"), os.Getenv("DB_USER"), os.Getenv("DB_PASSWORD"), os.Getenv("DB_NAME"), os.Getenv("DB_PORT"),
	)

	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("❌ Failed to connect to PostgreSQL: ", err)
	}

	// Auto-migrate the User model
	err = db.AutoMigrate(&Model.User{})
	if err != nil {
		log.Fatal("❌ Migration failed: ", err)
	}

	log.Println("✅ Connected to PostgreSQL and migrations completed")
	return db
}
