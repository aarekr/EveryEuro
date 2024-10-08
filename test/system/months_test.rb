require "application_system_test_case"

class MonthsTest < ApplicationSystemTestCase
  setup do
    @month = months(:one)
  end

  test "visiting the index" do
    visit months_url
    assert_selector "h1", text: "Months"
  end

  test "should create month" do
    visit months_url
    click_on "New month"

    fill_in "Food", with: @month.food
    fill_in "Income", with: @month.income
    fill_in "Name", with: @month.name
    fill_in "Rent", with: @month.rent
    fill_in "Saving", with: @month.saving
    fill_in "Year", with: @month.year
    click_on "Create Month"

    assert_text "Month was successfully created"
    click_on "Back"
  end

  test "should update Month" do
    visit month_url(@month)
    click_on "Edit this month", match: :first

    fill_in "Food", with: @month.food
    fill_in "Income", with: @month.income
    fill_in "Name", with: @month.name
    fill_in "Rent", with: @month.rent
    fill_in "Saving", with: @month.saving
    fill_in "Year", with: @month.year
    click_on "Update Month"

    assert_text "Month was successfully updated"
    click_on "Back"
  end

  test "should destroy Month" do
    visit month_url(@month)
    click_on "Destroy this month", match: :first

    assert_text "Month was successfully destroyed"
  end
end
