class CreateAccounts < ActiveRecord::Migration[7.1]
  def change
    create_table :accounts, id: false, primary_key: :username do |t|
      t.text :username
      t.text :password

      t.timestamps
    end
  end
end
