class Restaurant:
    def __init__(self, id, name, address, phone, email, status):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "status": self.status
        }
