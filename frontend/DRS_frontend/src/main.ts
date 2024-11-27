import { bootstrapApplication } from '@angular/platform-browser';
import { importProvidersFrom } from '@angular/core';
import { AppComponent } from './app/app.component';
import { RouterModule } from '@angular/router'; // Import RouterModule for routing
import { routes } from './app/app.routes'; // Import routes
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule for HTTP requests
import { appConfig } from './app/app.config'; // Import the appConfig

// Bootstrap the application with required providers
bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(
      RouterModule.forRoot(routes),
      HttpClientModule // Add HttpClientModule to provide HttpClient // Add RouterModule for routing
    ),
  ]
})
  .catch((err) => console.error(err));

  bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));