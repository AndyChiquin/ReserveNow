require_relative "../../db/database"

class GetBlockedUserService
  def self.get(email)
    db = Database.connection
    user = db.execute("SELECT * FROM blocked_users WHERE email = ?", [email])
    return { user: user.first } unless user.empty?
    { error: "User not found" }
  end
end
