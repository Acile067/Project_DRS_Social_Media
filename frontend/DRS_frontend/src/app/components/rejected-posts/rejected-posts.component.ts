import { CommonModule } from '@angular/common';
import { Component, inject, OnInit } from '@angular/core';
import {
  IAPIResponsePostDataModel,
  IAPIResponsePostMessageModel,
  IPost,
} from '../../model/interfaces/post';
import { PostService } from '../../services/post.service';
import { Router } from '@angular/router';
import { PostId } from '../../model/class/post';

@Component({
  selector: 'app-rejected-posts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './rejected-posts.component.html',
  styleUrl: './rejected-posts.component.css',
})
export class RejectedPostsComponent implements OnInit {
  posts: IPost[] = [];
  postService: PostService = inject(PostService);
  router = inject(Router);
  postId: PostId = new PostId();

  ngOnInit(): void {
    this.postService.getRejectedPosts().subscribe(
      (res: IAPIResponsePostDataModel) => {
        this.posts = res.data;
      },
      (error) => {
        console.error('Error:', error);
      }
    );
  }

  onEditPost(postId: string) {
    if (postId) {
      this.router.navigate(['/editpost', postId]);
    }
  }

  onDeletePost(postId: string) {
    this.postId.post_id = postId;
    this.postService.deletePost(this.postId).subscribe(
      (response: IAPIResponsePostMessageModel) => {
        if (response.message === 'Post deleted successfully') {
          this.posts = this.posts.filter((post) => post.post_id !== postId);
          alert(response.message);
        } else {
          alert('Unknown Response');
        }
      },
      (error) => {
        console.error('Error:', error);
        alert('An error occurred while deleting the post.');
      }
    );
  }

  getImageUrl(postId: string): string {
    return `http://localhost:5000/post/post-image/${postId}`;
  }
}
