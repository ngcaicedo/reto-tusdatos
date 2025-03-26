import { TestBed } from '@angular/core/testing';

import { EventService } from './event.service';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Event } from './event';
import { Session } from '../session-managment/session';

describe('EventService', () => {
  let service: EventService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        EventService,
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    service = TestBed.inject(EventService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should send a POST request to create event', () => {
    const event = {
      name: 'test',
      description: 'test',
      capacity: 100,
      state: 'CREADO',
      date_start: '2021-09-02',
      date_end: '2021-09-03',
      location: 'test',
      user_created_id: 1,
      session_ids: [1],
    };

    service.createEvent(event).subscribe({
      next: (res) => {
        expect(res).toEqual(event);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(`${environment.apiUrl}/events/create`);
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(event);

    req.flush(event);
  });

  it('should send a GET request to get all events', () => {
    const events = [
      new Event(
        1,
        'test',
        'test',
        100,
        'CREADO',
        '2021-09-02',
        '2021-09-03',
        'test',
        1,
        [new Session(1, 'Session 1', 'Session 1', 60, 1)]
      ),
    ];

    service.getEvents().subscribe({
      next: (res) => {
        expect(res).toEqual(events);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(`${environment.apiUrl}/events`);
    expect(req.request.method).toBe('GET');

    req.flush(events);
  });
});
