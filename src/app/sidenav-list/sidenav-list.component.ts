import { Component, OnInit, Output, EventEmitter, NO_ERRORS_SCHEMA } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import { MatList, MatListItem, MatNavList } from '@angular/material/list';
import { MatMenu, MatMenuModule } from '@angular/material/menu';
import { MatSidenavModule } from '@angular/material/sidenav';
import { RouterModule, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-sidenav-list',
  standalone: true,
  imports: [RouterModule, MatIcon, MatList, MatListItem, MatMenu, MatNavList],
  schemas: [NO_ERRORS_SCHEMA],
  templateUrl: './sidenav-list.component.html',
  styleUrl: './sidenav-list.component.scss'
})
export class SidenavListComponent implements OnInit {
  @Output() sidenavClose = new EventEmitter();

  constructor() { }

  ngOnInit() {
  }

  public onSidenavClose = () => {
    this.sidenavClose.emit();
  }

}