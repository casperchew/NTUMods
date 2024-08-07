class CreateMods < ActiveRecord::Migration[7.1]
  def change
    create_table :mods, id: false, primary_key: :course_code do |t|
      t.text :course_code, null: false
      t.text :title
      t.text :prerequisite
      t.text :exclusive
      t.text :description

      t.timestamps
    end
  end
end
