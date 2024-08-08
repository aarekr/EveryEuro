class CreateBudgets < ActiveRecord::Migration[7.0]
  def change
    create_table :budgets do |t|
      t.integer :year
      t.integer :user_id

      t.timestamps
    end
  end
end
