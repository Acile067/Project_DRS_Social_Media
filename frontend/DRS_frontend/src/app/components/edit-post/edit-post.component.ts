import { Component, inject } from '@angular/core';
import { Post } from '../../model/class/post';
import { PostService } from '../../services/post.service';
import { IAPIResponsePostDataModel, IAPIResponsePostMessageModel } from '../../model/interfaces/post';
import { Subscription } from 'rxjs';
import { Constant } from '../../constant/constant';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-edit-post',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './edit-post.component.html',
  styleUrl: './edit-post.component.css'
})
export class EditPostComponent {
  imagePreview: string | ArrayBuffer | null = null;
  imageFile: File | null = null;
  post: Post = new Post();
  postService = inject(PostService);
  subscriptionList: Subscription[] = [];
  router = inject(Router);
  route = inject(ActivatedRoute);

  ngOnInit(): void {
    const postId = this.route.snapshot.paramMap.get('id');
    if (postId) {
      this.subscriptionList.push(
        this.postService.getPostInfoForEdit(postId).subscribe(
          (res: IAPIResponsePostDataModel) => {
            this.post = res.data;
          },
          (error) => {
            alert(error.error.message);
          }
        )
      );
    }
  }

  triggerFileInput() {
    document.getElementById('image-input')!.click();
  }

  // Handle image selection and preview
  onImageSelected(event: Event) {
    const fileInput = event.target as HTMLInputElement;
    if (fileInput.files && fileInput.files[0]) {
      this.imageFile = fileInput.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        this.imagePreview = reader.result;
      };
      reader.readAsDataURL(this.imageFile);
    }
  }

  onSaveEdit() {
    this.postService.editPost(this.post).subscribe(
      (res: IAPIResponsePostMessageModel) => {
        if (res.message === 'Ok') {
          alert('Post Edited Successfully');
          this.router.navigate(['/profile']);
        } else {
          alert(Constant.ALERT_MESSAGES.UNKNOWN_RESPONSE);
        }
      },
      (error) => {
        if (error.status === 400 && error.error.message) {
          alert(error.error.message);
        } else {
          alert(Constant.ALERT_MESSAGES.UNKONOW_ERROR);
        }
        console.error('Error:', error);
      }
    );
  }


  ngOnDestroy(): void {
    this.subscriptionList.forEach((element) => {
      element.unsubscribe();
    });
  }

}