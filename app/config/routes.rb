Rails.application.routes.draw do
  resources :contacts
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  
  root to: "static_pages#index"

  get 'contato', to: 'static_pages#contato'
  get 'sobre', to: 'static_pages#sobre'

end
