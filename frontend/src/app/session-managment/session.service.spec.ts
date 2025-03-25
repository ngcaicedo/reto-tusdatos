import { TestBed } from '@angular/core/testing';

import { SessionService } from './session.service';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';
import { Speaker } from './speaker';
import { environment } from '../../environments/environment';

describe('SessionService', () => {
  let service: SessionService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        SessionService,
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    service = TestBed.inject(SessionService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should send a POST request to create session', () => {
    const speaker = new Speaker(1, 'test');
    const session = {
      sessionName: 'test',
      sessionDescription: 'test',
      sessionDuration: 100,
      speaker: speaker.id,
    };

    service.createSession(session).subscribe({
      next: (res) => {
        expect(res).toEqual(session);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(`${environment.apiUrl}/sessions/create`);
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(session);

    req.flush(session);
  });

  it('should send a POST request to create Speaker', () => {
    const speaker = {
      name: 'test',
    };

    service.createSpeaker(speaker).subscribe({
      next: (res) => {
        expect(res).toEqual(speaker);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(
      `${environment.apiUrl}/sessions/create/speaker`
    );

    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(speaker);

    req.flush(speaker);
  });

  it('should send a GET request to get speakers', () => {
    const speakers = [
      new Speaker(1, 'test1'),
      new Speaker(2, 'test2'),
      new Speaker(3, 'test3'),
    ];

    service.getSpeakers().subscribe({
      next: (res) => {
        expect(res).toEqual(speakers);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(`${environment.apiUrl}/sessions/speakers`);
    expect(req.request.method).toBe('GET');
    req.flush(speakers);
  });
});
