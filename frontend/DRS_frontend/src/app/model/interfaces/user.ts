export interface IUser {
  email: string;
  lastname: string;
  name: string;
  username: string;
}

export interface IAPIResponseUserDataModel {
  data: any;
}

export interface IAPIResponseUserMessageModel {
  message: string;
}

export interface IAPIResponseUserTokenModel {
  message: string;
  token: string;
}
