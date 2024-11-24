import { Component, inject } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { OverlayModule } from '@angular/cdk/overlay';
import { SearchBarService } from '../../services/search-barS.service';
import { SearchOverlayComponent } from '../search-overlay/search-overlay.component';
import { NgClass } from '@angular/common';




@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [MatIconModule, MatButtonModule,OverlayModule,SearchOverlayComponent,NgClass],
  templateUrl: './search-bar.component.html',
  styleUrl: './search-bar.component.css'
})
export class SearchBarComponent { 

  searchBarService=inject(SearchBarService);
  overlayOpen=this.searchBarService.overlayOpen;
  searchTerm=this.searchBarService.searchTerm;

  search(searchTerm:string){
    if(!searchTerm)return;

    this.searchBarService.search(searchTerm);
    
  }

  clearSearch(){
    this.searchBarService.clearSearch();
  }

}
