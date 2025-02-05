require_relative "../../db/database"
require "securerandom"

class BlockUserService
  def self.block(email, reason)
    db = Database.connection
    db.execute("INSERT INTO blocked_users (id, email, reason, blocked_at) VALUES (?, ?, ?, ?)", 
               [SecureRandom.uuid, email, reason, Time.now.to_s])
    { message: "User blocked successfully" }
  rescue SQLite3::Exception => e
    { error: "Error blocking user: #{e.message}" }
  end
end
