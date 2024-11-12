import { CommonModule } from '@angular/common';
import { Component, inject, OnDestroy, OnInit } from '@angular/core';
import { IAPIResponseUserDataModel, IUser } from '../../model/interfaces/user';
import { UserService } from '../../services/user.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-master',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './master.component.html',
  styleUrl: './master.component.css',
})
export class MasterComponent implements OnInit, OnDestroy {
  userList: IUser[] = [];

  subscriptionList: Subscription[] = [];

  userService = inject(UserService);

  isLoader: boolean = true;

  ngOnInit(): void {
    this.subscriptionList.push(
      this.userService.getAllUsers().subscribe(
        (res: IAPIResponseUserDataModel) => {
          this.userList = res.data;
          this.isLoader = false;
        },
        (error) => {
          alert('ERROR Geting Users');
          this.isLoader = false;
        }
      )
    );
  }

  ngOnDestroy(): void {
    this.subscriptionList.forEach((element) => {
      element.unsubscribe();
    });
  }
}
