require 'rails_helper'

RSpec.describe User, type: :model do
  it "has the username set correctly" do
    user = User.new username: "Pekka"
    expect(user.username).to eq("Pekka")
  end

  it "is not saved if username too short" do
    user = User.new username: "M"
    expect(User.count).to be(0)
  end

  it "is not saved without a password" do
    user = User.create username: "Pekka"
    expect(user).not_to be_valid
    expect(User.count).to eq(0)
  end

  it "is saved with a proper password" do
    user = User.create username: "Pekka", password: "Secret1", password_confirmation: "Secret1"
    expect(user.valid?).to be(true)
    expect(User.count).to eq(1)
  end

  it "is not saved if password too short" do
    user = User.create username: "Pekka", password: "P", password_confirmation: "P"
    expect(user).not_to be_valid
    expect(User.count).to eq(0)
  end
end
