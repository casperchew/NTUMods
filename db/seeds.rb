require 'csv'

Account.create(username: :admin, password: :password)

mods = CSV.read(Rails.root.join('db', 'mods.csv'), headers: true).each do |mod|
  Mod.create(mod)
end

Review.create(course_code: :CC0001, author: :admin, review: :test)