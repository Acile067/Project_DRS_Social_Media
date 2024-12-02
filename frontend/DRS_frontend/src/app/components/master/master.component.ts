import { CommonModule } from '@angular/common';
import { Component, inject, OnDestroy, OnInit } from '@angular/core';
import { IAPIResponseUserDataModel, IUser } from '../../model/interfaces/user';
import { UserService } from '../../services/user.service';
import { Subscription } from 'rxjs';
import { NewPostComponent } from '../new-post/new-post.component';
import { MyFriendsPostsComponent } from '../my-friends-posts/my-friends-posts.component';
@Component({
  selector: 'app-master',
  standalone: true,
  imports: [CommonModule, NewPostComponent, MyFriendsPostsComponent],
  templateUrl: './master.component.html',
  styleUrl: './master.component.css',
})
export class MasterComponent {}
