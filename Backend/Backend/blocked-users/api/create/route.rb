require "sinatra"
require "json"
require_relative "service"

post "/block" do
  content_type :json
  data = JSON.parse(request.body.read)

  if data["email"].nil? || data["reason"].nil?
    halt 400, { error: "Missing required fields" }.to_json
  end

  result = BlockUserService.block(data["email"], data["reason"])
  result.to_json
end
