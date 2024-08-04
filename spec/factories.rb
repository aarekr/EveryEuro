FactoryBot.define do
    factory :user do
      username { "Pekka" }
      password { "Salasana1" }
      password_confirmation { "Salasana1" }
    end

    factory :month do
      name { "null" }
      year { "0000" }
    end
end