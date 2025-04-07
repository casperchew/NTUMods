class CreateReviews < ActiveRecord::Migration[7.1]
  def change
    create_table :reviews do |t|
      t.text :course_code
      t.text :author
      t.text :review

      t.timestamps
    end
  end
end
