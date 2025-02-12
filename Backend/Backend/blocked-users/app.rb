require "sinatra"
require_relative "api/create/route"
require_relative "api/read/route"
require_relative "api/delete/route"

set :bind, "0.0.0.0"
set :port, 8000

get "/" do
  "Blocked Users Microservice Running 🚀"
end
