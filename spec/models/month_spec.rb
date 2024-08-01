require 'rails_helper'

RSpec.describe Month, type: :model do
  it "has the month set correctly" do
    month = Month.new name: "October"
    expect(month.name).to eq("October")
  end
end
