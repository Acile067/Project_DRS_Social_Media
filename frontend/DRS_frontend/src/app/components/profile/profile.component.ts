import { Component, inject } from '@angular/core';
import { IAPIResponsePostDataModel, IPost } from '../../model/interfaces/post';
import { PostService } from '../../services/post.service';
import { CommonModule } from '@angular/common';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {
  posts: IPost[] = [];
  postService: PostService = inject(PostService);
  subscriptionList: Subscription[] = [];

  ngOnInit(): void {
    this.subscriptionList.push(
      this.postService.getApprovedPostsForUser().subscribe(
        (res: IAPIResponsePostDataModel) => {
        this.posts = res.data;
      },
      (error) => {
        console.error('Error:', error);
      })
    );
  }

  ngOnDestroy(): void {
    this.subscriptionList.forEach((element) => {
      element.unsubscribe();
    });
  }

}
