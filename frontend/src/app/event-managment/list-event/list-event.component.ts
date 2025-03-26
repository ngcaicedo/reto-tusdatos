import { Component, OnInit } from '@angular/core';
import { Event } from '../event';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { CardEventComponent } from '../card-event/card-event.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-list-event',
  imports: [CommonModule, CardEventComponent],
  standalone: true,
  templateUrl: './list-event.component.html',
  styleUrl: './list-event.component.css',
})
export class ListEventComponent implements OnInit {
  events: Event[] = [];

  constructor(
    private eventService: EventService,
    private notify: NotificationService
  ) {}

  ngOnInit(): void {
    this.eventService.getEvents().subscribe({
      next: (response) => {
        this.events = response;
      },
      error: (error) => {
        this.notify.error(`Error al obtener eventos: ${error.error.detail}`);
      },
    });
  }
}
