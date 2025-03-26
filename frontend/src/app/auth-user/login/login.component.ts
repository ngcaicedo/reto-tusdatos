import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  Validators,
  ReactiveFormsModule,
  FormGroup,
} from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthUserService } from './auth-user.service';
import { NotificationService } from '../../shared/services/notification.service';
import { AuthStateService } from '../../shared/states/auth-state.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [CommonModule, ReactiveFormsModule],
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;

  constructor(
    public activeModal: NgbActiveModal,
    private formBuilde: FormBuilder,
    private authService: AuthUserService,
    private notify: NotificationService,
    private authState: AuthStateService,
    private router: Router
  ) {}

  ngOnInit() {
    this.loginForm = this.formBuilde.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  login() {
    sessionStorage.setItem('token', '');
    sessionStorage.setItem('role', '');
    sessionStorage.setItem('user', '');
    sessionStorage.setItem('user_id', '');

    this.authService.login(this.loginForm.value).subscribe({
      next: (response) => {
        const userState = {
          token: response.token,
          user: response.user,
          role: response.role,
          user_id: response.user_id
        };
        this.authState.setUser(userState);
        this.notify.success('Inicio de sesión exitoso');
        this.activeModal.dismiss();
      },
      error: (error) => {
        this.notify.error(`Error en inicio de sesión: ${error.error.detail}`);
      },
    });
  }

  cancel() {
    this.activeModal.dismiss();
  }
}
