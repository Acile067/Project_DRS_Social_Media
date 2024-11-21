export interface IPost {
  id: string;
  username: string;
  txt: string;
  imagepath: string;
  approved: string;
}

export interface IAPIResponsePostDataModel {
    data: any;
  }
  
  export interface IAPIResponsePostMessageModel {
    message: string;
  }