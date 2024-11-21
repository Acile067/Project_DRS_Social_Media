export class Post {
    id: string;
    username: string;
    txt: string;
    imagepath: string;
    approved: string;
   
  
    constructor() {
        (this.id = ''),
        (this.username = ''),       
        (this.txt = ''),
        (this.imagepath = ''),
        (this.approved = '');
       
    }
  }