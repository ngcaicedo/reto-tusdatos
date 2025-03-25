import { TestBed } from '@angular/core/testing';

import { RegisterAssistantService } from './register-assistant.service';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { environment } from '../../../environments/environment';
import { provideHttpClient } from '@angular/common/http';

describe('RegisterAssistantService', () => {
  let service: RegisterAssistantService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        RegisterAssistantService,
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    service = TestBed.inject(RegisterAssistantService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should send a POST request to register assistant', () => {
    const assistant = {
      name: 'test',
      email: 'prueba@gmail.com',
      password: '123456',
      phone: '1234567890',
      role: 'ASISTENTE',
    };

    service.registerAssistant(assistant).subscribe({
      next: (res) => {
        expect(res).toEqual(assistant);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(
      `${environment.apiUrl}/users/register/assistant`
    );
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(assistant);

    req.flush(assistant);
  });
});
