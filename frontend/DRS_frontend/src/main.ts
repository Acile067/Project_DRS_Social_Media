import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { appConfig } from './app/app.config'; // Import the appConfig

// Bootstrap the application with required providers

bootstrapApplication(AppComponent, appConfig).catch((err) =>
  console.error(err)
);
