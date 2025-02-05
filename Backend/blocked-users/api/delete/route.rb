require "sinatra"
require "json"
require_relative "service"

delete "/block/:email" do
  content_type :json
  result = DeleteBlockedUserService.delete(params[:email])
  result.to_json
end
