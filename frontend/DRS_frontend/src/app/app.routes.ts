import { Routes } from '@angular/router';
import { MasterComponent } from './components/master/master.component';
import { RegisterComponent } from './components/register/register.component';
import { LoginComponent } from './components/login/login.component';
import { EditUserProfileComponent } from './components/edit-user-profile/edit-user-profile.component';
import { authGuard } from './services/guard/auth.guard';
import { adminGuard } from './services/guard/admin.guard';
import { logInGuard } from './services/guard/log-in.guard';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full',
  },
  {
    path: 'login',
    component: LoginComponent,
    canActivate: [logInGuard],
  },
  {
    path: 'index',
    component: MasterComponent,
    canActivate: [authGuard],
  },
  {
    path: 'register',
    component: RegisterComponent,
    canActivate: [authGuard, adminGuard],
  },
  {
    path: 'edituserprofile',
    component: EditUserProfileComponent,
    canActivate: [authGuard],
  },
];
