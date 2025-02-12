require 'sequel'
require 'dotenv/load'

DB = Sequel.connect(
  adapter: :firebird,
  database: ENV['DB_PATH'],
  host: ENV['DB_HOST'],
  user: ENV['DB_USER'],
  password: ENV['DB_PASSWORD'],
  charset: 'UTF8'
)
