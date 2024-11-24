import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PostService } from '../../services/post.service';
import { Router } from '@angular/router';
import { Post } from '../../model/class/post';
import { IAPIResponsePostMessageModel } from '../../model/interfaces/post';
import { Constant } from '../../constant/constant';

@Component({
  selector: 'app-new-post',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './new-post.component.html',
  styleUrl: './new-post.component.css'
})
export class NewPostComponent {

  imagePreview: string | ArrayBuffer | null = null;
  imageFile: File | null = null;  // Store selected image file
  postService = inject(PostService);
  router = inject(Router);
  postObject = new Post();

  // Open file input
  triggerFileInput() {
    document.getElementById('image-input')!.click();
  }

  // Handle image selection
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

  // Handle post submission
  onPost() {
    const formData = new FormData();
    formData.append('txt', this.postObject.txt);
  
    // Append image file if selected
    if (this.imageFile) {
      formData.append('image', this.imageFile, this.imageFile.name);
    }
  
    this.postService.createPost(formData).subscribe(
      (res: IAPIResponsePostMessageModel) => {
        if (res.message === 'Created') {
          alert('Post Created Successfully');
          this.router.navigate(['/index']);
        } else {
          alert('Unknown Response');
        }
      },
      (error) => {
        console.error('Error:', error);
        if (error.status === 400 && error.error.message) {
          alert(error.error.message);
        } else {
          alert('Unknown Error');
        }
      }
    );
  }
}  
