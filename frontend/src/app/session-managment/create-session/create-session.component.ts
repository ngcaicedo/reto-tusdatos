import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Speaker } from '../speaker';
import { SessionService } from '../session.service';
import { NotificationService } from '../../shared/services/notification.service';

@Component({
  selector: 'app-create-session',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-session.component.html',
  styleUrl: './create-session.component.css',
})
export class CreateSessionComponent {
  sessionForm!: FormGroup;
  speakers: Array<Speaker> = [];

  constructor(
    private formBuilder: FormBuilder,
    private sessionService: SessionService,
    private notify: NotificationService
  ) {}

  ngOnInit() {
    this.sessionForm = this.formBuilder.group({
      sessionName: ['', Validators.required],
      sessionDescription: ['', Validators.required],
      sessionDuration: ['', Validators.required],
      speaker: ['', Validators.required],
    });
  }

  createSession() {
    this.sessionService.createSession(this.sessionForm.value).subscribe({
      next: (response) => {
        this.notify.success('Sesión creada');
      },
      error: (error) => {
        this.notify.error(`Error al crear sesión: ${error.message}`);
      },
    });
  }
}
