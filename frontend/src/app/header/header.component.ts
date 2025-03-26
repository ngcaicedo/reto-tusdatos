import { Component, OnInit } from '@angular/core';
import { LoginComponent } from '../auth-user/login/login.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../auth-user/register/register.component';
import { AuthStateService } from '../shared/states/auth-state.service';
import { CommonModule } from '@angular/common';
import { ListEventComponent } from '../event-managment/list-event/list-event.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
  imports: [CommonModule],
})
export class HeaderComponent implements OnInit {
  user: any;

  constructor(
    private modalService: NgbModal,
    private authState: AuthStateService
  ) {}

  ngOnInit() {
    this.user = this.authState.user;
  }

  openLoginModal() {
    this.modalService.open(LoginComponent, { centered: true });
  }

  openRegisterModal() {
    this.modalService.open(RegisterComponent, { centered: true });
  }

  logout() {
    this.authState.clearUser();
  }
}
