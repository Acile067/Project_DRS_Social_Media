import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from './services/auth.service';
import { AdminService } from './services/admin.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, RouterLink, RouterLinkActive],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'DRS_frontend';
  isUserLoggedIn: boolean = false;
  isUserAdmin: boolean = false;
  username: string | null = null;
  isSidebarVisible: boolean = false;

  constructor(
    private authService: AuthService,
    private adminService: AdminService
  ) {}

  ngOnInit(): void {
    this.authService.isLoggedIn.subscribe((loggedIn: boolean) => {
      this.isUserLoggedIn = loggedIn;
    });
    this.adminService.isAdmin.subscribe((admin: boolean) => {
      this.isUserAdmin = admin;
    });
    this.authService.username.subscribe((username: string | null) => {
      this.username = username;
    });
  }

  toggleSidebar() {
    this.isSidebarVisible = !this.isSidebarVisible;
  }

  logout() {
    this.authService.logout();
    this.isUserAdmin = false;
    this.username = null;
    this.isSidebarVisible = false;
  }
}
