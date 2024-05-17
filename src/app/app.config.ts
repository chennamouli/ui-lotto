import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter, withHashLocation } from '@angular/router';

import { routes } from './app.routes';
import { provideAnimations } from '@angular/platform-browser/animations';
import { HttpClientJsonpModule, HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { MatIcon, MatIconModule } from '@angular/material/icon';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes, withHashLocation()),
    provideAnimations(),
    importProvidersFrom(DatePipe),
    importProvidersFrom(HttpClientModule),
    importProvidersFrom(HttpClientJsonpModule),
    importProvidersFrom(
      HttpClientXsrfModule.withOptions({
      cookieName: 'My-Xsrf-Cookie',
      headerName: 'My-Xsrf-Header',
    })
  ),
  ]
};
