class Mod < ApplicationRecord
  self.primary_key = :course_code

  validates :course_code, presence: true, uniqueness: true
  validates :title, presence: true
end
