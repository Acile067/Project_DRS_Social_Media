export class Post {
    post_id: string;
    txt: string;
    image_path: string;
   
  
    constructor() {    
        (this.post_id = ''),
        (this.txt = ''),
        (this.image_path = '');
       
    }
  }

  export class ApproveOrRejectId{
    post_id: string;

    constructor(){
        this.post_id = "";
    }
  }