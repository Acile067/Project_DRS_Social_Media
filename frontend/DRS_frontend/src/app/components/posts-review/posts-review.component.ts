import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WebSocketService } from '../../services/web-socket.service'; // Import your WebSocketService

@Component({
  selector: 'app-posts-review',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './posts-review.component.html',
  styleUrls: ['./posts-review.component.css'] // Fixed typo here
})
export class PostsReviewComponent implements OnInit {
  posts: any[] = [];

  constructor(private webSocketService: WebSocketService) { }

  ngOnInit(): void {
    // Listen for the 'new_post' event from the server
    this.webSocketService.on('new_post').subscribe((post: any) => {
      this.posts.push(post); // Add new post to the list
    });
  }
}
