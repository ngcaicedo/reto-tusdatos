import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {
  FormArray,
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { Session } from '../../session-managment/session';
import { SessionService } from '../../session-managment/session.service';

@Component({
  selector: 'app-create-event',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-event.component.html',
  styleUrl: './create-event.component.css',
})
export class CreateEventComponent {
  eventForm!: FormGroup;
  sessions: Array<Session> = [];

  constructor(
    private formBuilder: FormBuilder,
    private eventService: EventService,
    private sessionService: SessionService,
    private notifyService: NotificationService
  ) {}

  ngOnInit(): void {
    this.sessionService.getSessions().subscribe({
      next: (response) => {
        this.sessions = response as Session[];
      },
      error: (error) => {
        this.notifyService.error(
          `Error al obtener sesiones: ${error.error.detail}`
        );
      },
    });

    this.eventForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      state: ['CREADO'],
      capacity: ['', Validators.required],
      date_start: ['', Validators.required],
      date_end: ['', Validators.required],
      location: ['', Validators.required],
      user_created_id: [sessionStorage.getItem('user_id')],
      session_ids: this.formBuilder.array([]),
    });

    this.addSession();
  }

  createEvent() {
    this.eventService.createEvent(this.eventForm.value).subscribe({
      next: (res) => {
        this.notifyService.success('Evento creado');
      },
      error: (error) => {
        this.notifyService.error(
          `Error al crear evento: ${error.error.detail}`
        );
      },
    });
  }

  get session_ids(): FormArray {
    return this.eventForm.get('session_ids') as FormArray;
  }

  addSession() {
    this.session_ids.push(this.formBuilder.control(null));
  }

  removeSession(index: number) {
    this.session_ids.removeAt(index);
  }

  validarSession() {
    return (
      this.session_ids.length > 0 &&
      this.session_ids.controls.every((control) => control.value !== null)
    );
  }
}
