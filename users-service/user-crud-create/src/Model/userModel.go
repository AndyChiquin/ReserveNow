package Model

type User struct {
	ID    uint   `gorm:"primaryKey"`
	Name  string `json:"name"`
	Email string `json:"email" gorm:"unique"`
	Phone string `json:"phone"`
	Role  string `json:"role"`
}
