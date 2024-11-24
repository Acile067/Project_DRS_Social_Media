import { Component, inject } from '@angular/core';
import { IUser } from '../../model/interfaces/user';
import { UserService } from '../../services/user.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-show-searched-friends',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './show-searched-friends.component.html',
  styleUrl: './show-searched-friends.component.css',
})
export class ShowSearchedFriendsComponent {
  userList: IUser[] = [];

  constructor(private userService: UserService) {
    // Subscribe to the user list observable
    this.userService.userList$.subscribe((userList) => {
      this.userList = userList; // Update the user list when it changes
    });
  }
}
