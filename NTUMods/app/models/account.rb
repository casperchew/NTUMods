class Account < ApplicationRecord
  self.primary_key = :username
  validates :username, presence: true, uniqueness: true
  validates :password, presence: true
end
