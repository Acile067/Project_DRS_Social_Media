import { Component } from '@angular/core';
import { SearchBarComponent } from '../search-bar/search-bar.component';
import {MatToolbar} from '@angular/material/toolbar'

@Component({
  selector: 'app-friends',
  standalone: true,
  imports: [SearchBarComponent,MatToolbar],
  templateUrl: './friends.component.html',
  styleUrl: './friends.component.css'
})
export class FriendsComponent {

}
