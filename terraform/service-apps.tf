resource azurerm_service_plan main {
  name                = "asp-${var.application_name}-${var.environment_name}-${var.location_short}-${var.resource_version}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = var.sku_name
}

resource azurerm_linux_web_app backend {
  name                = "lwa-${var.application_name}-be-${var.environment_name}-${var.location_short}-${var.resource_version}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    ip_restriction_default_action = "Allow"
    minimum_tls_version           = 1.2
    always_on                     = false
    app_command_line              = "gunicorn --worker-class eventlet -w 1 run:flask_app"

  application_stack {
    python_version = "3.9"
    }
}

  identity {
    type = "SystemAssigned"  
  }
  app_settings = {
    "FLASK_APP"           = "run:flask_app"
    "DB_PASSWORD"         = "${data.azurerm_key_vault_secret.admin_password.value}"
    "MAIL_USERNAME"       = "aleksandarsasastefanjovana@gmail.com"
    "MAIL_PASSWORD"       = "${data.azurerm_key_vault_secret.mail_password.value}"
    "MAIL_DEFAULT_SENDER" = "aleksandarsasastefanjovana@gmail.com"
    "CORS_ORIGINS"        = "*"
    "FLASK_ENV"           = "production"
    
    "AZURE_STORAGE_ACCOUNT_CONNECTION_STRING" = azurerm_storage_account.main.primary_connection_string
    "AZURE_STORAGE_CONTAINER"                 = azurerm_storage_container.main.name
  }
}

resource azurerm_linux_web_app frontend {
  name                = "lwa-${var.application_name}-fe-${var.environment_name}-${var.location_short}-${var.resource_version}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    ip_restriction_default_action = "Allow"
    minimum_tls_version           = 1.2
    always_on                     = false
    app_command_line              = "npx serve -s ."
    application_stack {
      node_version = "20-lts"
    }
  }
}
