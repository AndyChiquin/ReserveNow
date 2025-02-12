require_relative "../../db/database"

class DeleteBlockedUserService
  def self.delete(email)
    db = Database.connection
    db.execute("DELETE FROM blocked_users WHERE email = ?", [email])
    { message: "User unblocked successfully" }
  rescue SQLite3::Exception => e
    { error: "Error deleting user: #{e.message}" }
  end
end
