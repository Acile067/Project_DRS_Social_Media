import { Component, OnInit } from '@angular/core';
import { Socket } from 'ngx-socket-io';


@Component({
  selector: 'app-posts-review',
  standalone: true,
  imports: [],
  templateUrl: './posts-review.component.html',
  styleUrl: './posts-review.component.css'
})


export class PostsReviewComponent implements OnInit {
  posts: any[] = [];

  constructor(private socket: Socket) { }

  ngOnInit(): void {
    this.socket.on('new_post', (post: any) => {
      this.posts.push(post);
    });
  }
}