require "sinatra"
require "json"
require_relative "service"

get "/block/:email" do
  content_type :json
  result = GetBlockedUserService.get(params[:email])
  halt 404 if result[:error]
  result.to_json
end
