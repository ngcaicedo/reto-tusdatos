import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Event } from '../event';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthStateService } from '../../shared/states/auth-state.service';

@Component({
  selector: 'app-detail-event',
  imports: [CommonModule],
  templateUrl: './detail-event.component.html',
  styleUrl: './detail-event.component.css'
})
export class DetailEventComponent {
  event!: Event;
  user: any;

  constructor(
    private eventService: EventService,
    private notify: NotificationService,
    private router: ActivatedRoute,
    private authState: AuthStateService
  ) {}

  ngOnInit() {
    this.user = this.authState.user;
    const id = Number(this.router.snapshot.paramMap.get('event_id'));
    this.eventService.getEvent(id).subscribe({
      next: (response) => {
        this.event = response;
      },
      error: (error) => {
        this.notify.error(`Error al obtener evento: ${error.error.detail}`);
      },
    });
  }

  get groupedSessions(): Record<string, any[]> {
    const result: Record<string, any[]> = {};
  
    for (const session of this.event.sessions) {
      const date = new Date(session.date_start).toLocaleDateString('es-ES', {
        day: 'numeric',
        month: 'long'
      });
  
      if (!result[date]) result[date] = [];
      result[date].push(session);
    }
  
    return result;
  }

  registerUserToEvent() {
    this.eventService.registerUserToEvent(this.event.id).subscribe({
      next: (response) => {
        this.notify.success('Registrado correctamente');
      },
      error: (error) => {
        this.notify.error(`Error al registrarte: ${error.error.detail}`);
      },
    });
  }

  openAlert() {
    if (!this.user()) {
      this.notify.warning('Debes iniciar sesión para registrarte');
      return;
    }
    this.registerUserToEvent();
  }

  cancelRegister() {
    this.notify.warning('Funcionalidad no implementada'); 
    return;
  }
  
}
