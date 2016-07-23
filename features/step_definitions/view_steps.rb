#encoding: utf-8
Given /^I am a user$/ do
  # I dont have to log in :P
end

When /^I view the website$/ do
  visit('localhost:3000')
end

And /^binding pry$/ do
  binding.pry
end