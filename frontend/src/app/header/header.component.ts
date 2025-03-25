import { Component, OnInit } from '@angular/core';
import { LoginComponent } from '../auth-user/login/login.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../auth-user/register/register.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
})
export class HeaderComponent implements OnInit {

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
  }

  openLoginModal() {
    this.modalService.open(LoginComponent, { centered: true });
  }

  openRegisterModal() {
    this.modalService.open(RegisterComponent, { centered: true });
  }

}
