require 'rails_helper'

describe "Months page" do
    it "EveryEuro text is visible on the page" do
        visit months_path
        expect(page).to have_content 'EveryEuro'
    end

    it "Months are not initialized when program starts from 0" do
        visit months_path
        expect(page).not_to have_content 'January'
        expect(page).not_to have_content 'February'
        expect(page).not_to have_content 'August'
        expect(page).not_to have_content 'December'
    end

    it "Allows user to navigate to New Month page" do
        visit months_path
        click_link "Create a new month"
        expect(page).to have_content "New month"
        expect(page).to have_content "Enter the estimated budgeting items for this month."
        expect(page).to have_content "Income"
        expect(page).to have_content "Rent"
        expect(page).to have_content "Food"
    end
end

describe "When user account exists" do
    let(:user) { FactoryBot.create(:user) }

    it "the user account is saved" do
        expect(user).to be_valid
        expect(User.count).to eq(2)
        #FactoryBot.create(:user, username: 'Tuomo')
    end

    it "the new month is saved" do
        FactoryBot.create(:month, name: "November")
        expect(Month.count).to eq(1)
        FactoryBot.create(:month, name: "December", year: 2024)
        expect(Month.count).to eq(2)
        visit months_path
        expect(page).to have_content "November"
        expect(page).to have_content "December"
        expect(page).not_to have_content "March"
    end
end