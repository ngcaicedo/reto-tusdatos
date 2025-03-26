import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { NotificationService } from '../../shared/services/notification.service';

@Component({
  selector: 'app-register-organization',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './register-organization.component.html',
  styleUrl: './register-organization.component.css',
})
export class RegisterOrganizationComponent {
  userForm!: FormGroup;
  constructor(
    private formBuilder: FormBuilder,
    private notify: NotificationService,
  ) {}

  ngOnInit(): void {
    this.userForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      phone: ['', Validators.required],
      role: ['', Validators.required],
    });
  }

  createUser() {
    this.notify.success('Usuario creado correctamente');
  }
}
