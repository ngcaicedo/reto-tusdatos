import { TestBed } from '@angular/core/testing';

import { AuthService } from './auth.service';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

describe('AuthService', () => {
  let service: AuthService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AuthService, provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(AuthService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify;
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should send a POST request to register user', () => {
    const user = {
      id: 1,
      name: 'test',
      email: 'test@gmail.com',
      phone: '1234567890',
      password: 'test',
      role: 'ADMIN',
    };

    service.registerUser(user).subscribe({
      next: (res) => {
        expect(res).toEqual(user);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });
    const req = httpMock.expectOne(`${environment.apiUrl}/auth/register`);
    expect(req.request.method).toBe('POST');
    req.flush(user);
  });
});
