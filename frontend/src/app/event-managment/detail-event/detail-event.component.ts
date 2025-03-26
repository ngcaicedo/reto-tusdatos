import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Event } from '../event';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-detail-event',
  imports: [CommonModule],
  templateUrl: './detail-event.component.html',
  styleUrl: './detail-event.component.css'
})
export class DetailEventComponent {
  event!: Event;

  constructor(
    private eventService: EventService,
    private notify: NotificationService,
    private router: ActivatedRoute
  ) {}

  ngOnInit() {
    const id = Number(this.router.snapshot.paramMap.get('id'));
    this.eventService.getEvent(id).subscribe({
      next: (response) => {
        this.event = response;
      },
      error: (error) => {
        this.notify.error(`Error al obtener evento: ${error.error.detail}`);
      },
    });
  }
}
