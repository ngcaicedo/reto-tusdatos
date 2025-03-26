import { Component, OnInit } from '@angular/core';
import { Event } from '../event';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { CommonModule } from '@angular/common';
import { CardEventComponent } from '../card-event/card-event.component';

@Component({
  selector: 'app-detail-event-assistant',
  imports: [CommonModule, CardEventComponent],
  templateUrl: './detail-event-assistant.component.html',
  styleUrl: './detail-event-assistant.component.css'
})
export class DetailEventAssistantComponent implements OnInit {
  events: Event[] = [];
  constructor(
    private eventService: EventService,
    private notify: NotificationService
  ) {}

  ngOnInit(): void {
    this.eventService.getEventsRegistedAssistant().subscribe({
      next: (response) => {
        this.events = response;
      },
      error: (error) => {
        this.notify.error(`Error al obtener eventos: ${error.error.detail}`);
      },
    });
  }
}
