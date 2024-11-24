import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IAPIResponsePostDataModel, IAPIResponsePostMessageModel } from '../model/interfaces/post';
import { environment } from '../../environments/environment.development';
import { Constant } from '../constant/constant';
import { Post } from '../model/class/post';

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
}
