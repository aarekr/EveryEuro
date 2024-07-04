class CreateMonths < ActiveRecord::Migration[7.0]
  def change
    create_table :months do |t|
      t.string :name
      t.integer :year
      t.integer :income
      t.integer :rent
      t.integer :food
      t.integer :saving

      t.timestamps
    end
  end
end
