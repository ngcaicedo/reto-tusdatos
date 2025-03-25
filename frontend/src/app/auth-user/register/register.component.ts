import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  Validators,
  ReactiveFormsModule,
  FormGroup,
} from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterAssistantService } from './register-assistant.service';
import { ToastrService } from 'ngx-toastr';
import { NotificationService } from '../../shared/services/notification.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  imports: [CommonModule, ReactiveFormsModule],
})
export class RegisterComponent implements OnInit {
  registerForm!: FormGroup;
  constructor(
    public activeModal: NgbActiveModal,
    private formBuilde: FormBuilder,
    private regiserService: RegisterAssistantService,
    private notify: NotificationService
  ) {}

  ngOnInit() {
    this.registerForm = this.formBuilde.group({
      name: ['', [Validators.required]],
      phone: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  registerAssistant() {
    this.regiserService.registerAssistant(this.registerForm.value).subscribe({
      next: (response) => {
        this.notify.success('Registro exitoso');
        this.activeModal.dismiss();
      },
      error: (error) => {
        this.notify.error(`Error al registrar: ${error.error.detail}`);
      },
    });
  }

  cancel() {
    this.activeModal.dismiss();
  }
}
