json.extract! contact, :id, :nome, :phone, :created_at, :updated_at
json.url contact_url(contact, format: :json)
