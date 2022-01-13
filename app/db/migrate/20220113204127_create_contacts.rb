class CreateContacts < ActiveRecord::Migration[5.2]
  def change
    create_table :contacts do |t|
      t.string :nome
      t.string :phone

      t.timestamps
    end
  end
end
