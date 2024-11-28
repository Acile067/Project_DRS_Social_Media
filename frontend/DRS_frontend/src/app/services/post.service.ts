import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IAPIResponsePostDataModel, IAPIResponsePostMessageModel } from '../model/interfaces/post';
import { environment } from '../../environments/environment.development';
import { Constant } from '../constant/constant';
import { ApproveOrRejectId, Post } from '../model/class/post';

@Injectable({
  providedIn: 'root'
})
export class PostService {

  constructor(private http:HttpClient) { }

  createPost(obj:FormData): Observable<IAPIResponsePostMessageModel>{
    return this.http.post<IAPIResponsePostMessageModel>(
      environment.API_URL + Constant.API_METHOD.CREATE_POST,
      obj
    );
  }

  getUnapprovedPosts(): Observable<any[]> {
    return this.http.get<any[]>(environment.API_URL + Constant.API_METHOD.UNAPPROVED_POSTS);
  }

  getApprovedPostsForUser(): Observable<IAPIResponsePostDataModel> {
    const token = localStorage.getItem('token');  // Retrieve the token from localStorage or another source
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });

    return this.http.get<IAPIResponsePostDataModel>(`${environment.API_URL}${Constant.API_METHOD.APPROVED_POSTS_FOR_USER}`, { headers });
  }

  approvePost(obj: ApproveOrRejectId): Observable<IAPIResponsePostMessageModel> {
    return this.http.post<IAPIResponsePostMessageModel>(environment.API_URL + Constant.API_METHOD.APPROVE_POST, obj );
  }

  rejectPost(obj: ApproveOrRejectId): Observable<IAPIResponsePostMessageModel> {
    return this.http.post<IAPIResponsePostMessageModel>(environment.API_URL + Constant.API_METHOD.REJECT_POST, obj );
  }
}
