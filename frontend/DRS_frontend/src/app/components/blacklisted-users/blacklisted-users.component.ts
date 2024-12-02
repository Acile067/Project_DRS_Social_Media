import { CommonModule } from '@angular/common';
import { Component, inject, OnInit } from '@angular/core';
import { IAPIResponseUserDataModel, IUser } from '../../model/interfaces/user';
import { UserService } from '../../services/user.service';
import { Constant } from '../../constant/constant';

@Component({
  selector: 'app-blacklisted-users',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './blacklisted-users.component.html',
  styleUrl: './blacklisted-users.component.css',
})
export class BlacklistedUsersComponent implements OnInit {
  myFriendsList: IUser[] = [];
  userService = inject(UserService);

  ngOnInit(): void {
    this.userService.getAllBlacklistedUsers().subscribe(
      (res: IAPIResponseUserDataModel) => {
        this.myFriendsList = res.data;
      },
      (error) => {
        if (
          (error.status === 400 || error.status === 500) &&
          error.error.message
        ) {
          alert(error.error.message);
        } else {
          alert(Constant.ALERT_MESSAGES.UNKONOW_ERROR);
        }
        console.error('Error:', error);
      }
    );
  }
}
