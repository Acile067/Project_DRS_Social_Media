export interface IPost {
  post_id: string,
  username: string,
  txt: string;
  image_path: string;

}

export interface IAPIResponsePostDataModel {
    data: any;
  }
  
  export interface IAPIResponsePostMessageModel {
    message: string;
  }