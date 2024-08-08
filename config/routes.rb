Rails.application.routes.draw do
  get "up" => "rails/health#show", as: :rails_health_check

  root 'index#index'

  get '/mods/search' => 'mods#search'

  get '/login' => 'accounts#login'
  post '/login' =>'accounts#login_post'
  get '/signout' => 'accounts#signout'

  resources :accounts
  resources :mods
  resources :reviews
end