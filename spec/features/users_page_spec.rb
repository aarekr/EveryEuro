require 'rails_helper'

describe "User" do
  before :each do
    FactoryBot.create :user
  end

  describe "who has signed up" do
    it "can sign in with right credentials" do
      visit signin_path
      expect(page).to have_content "username"
      expect(page).to have_content "password"
      fill_in('username', with: 'Pekka')
      fill_in('password', with: 'Salasana1')
      click_button('Log in')

      expect(page).to have_content "EveryEuro"
      expect(page).to have_content 'Pekka'

      visit months_path
      expect(page).to have_content "Pekka signed in"
    end
  end
end