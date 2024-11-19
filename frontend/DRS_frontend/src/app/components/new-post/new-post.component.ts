import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-new-post',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './new-post.component.html',
  styleUrl: './new-post.component.css'
})
export class NewPostComponent {

  postText: string = '';
  imagePreview: string | ArrayBuffer | null = null;

  triggerFileInput() {
    document.getElementById('image-input')!.click();
  }

  onImageSelected(event: Event) {
    const fileInput = event.target as HTMLInputElement;
    if (fileInput.files && fileInput.files[0]) {
      const file = fileInput.files[0];
      const reader = new FileReader();
      reader.onload = (e) => {
        this.imagePreview = e.target!.result;
      };
      reader.readAsDataURL(file);
    }
  }

  onPost() {
    if (!this.postText.trim()) {
      alert("Please enter some text to post.");
      return;
    }
    // Here you can add the code to submit the post data to your server
    alert("Post submitted!");
  }
}
