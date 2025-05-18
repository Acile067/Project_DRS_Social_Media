data azurerm_key_vault main {
  name                = "kv-socialmediadrs-mng"
  resource_group_name = "rg-socialmediadrs-mng-eun"
}

data azurerm_key_vault_secret admin_login {
  name         = "sql-admin"
  key_vault_id = data.azurerm_key_vault.main.id
}

data azurerm_key_vault_secret admin_password {
  name         = "sql-password"
  key_vault_id = data.azurerm_key_vault.main.id
}

data azurerm_key_vault_secret mail_password {
  name         = "mail-password"
  key_vault_id = data.azurerm_key_vault.main.id
}