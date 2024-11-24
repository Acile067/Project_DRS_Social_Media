import { Component } from '@angular/core';
import { SearchBarComponent } from '../search-bar/search-bar.component';
import { MatToolbar } from '@angular/material/toolbar';
import { ShowSearchedFriendsComponent } from '../show-searched-friends/show-searched-friends.component';

@Component({
  selector: 'app-friends',
  standalone: true,
  imports: [SearchBarComponent, MatToolbar, ShowSearchedFriendsComponent],
  templateUrl: './friends.component.html',
  styleUrl: './friends.component.css',
})
export class FriendsComponent {}
