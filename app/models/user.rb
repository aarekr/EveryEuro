class User < ApplicationRecord
  has_secure_password
  validates :username, uniqueness: true, length: { minimum: 3 }
  validates :password, length: { minimum: 3 }
end
