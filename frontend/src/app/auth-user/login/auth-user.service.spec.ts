import { TestBed } from '@angular/core/testing';

import { AuthUserService } from './auth-user.service';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

describe('AuthUserService', () => {
  let service: AuthUserService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        AuthUserService,
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    service = TestBed.inject(AuthUserService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should send a POST request to login', () => {
    const user = {
      email: 'test@gmail.com',
      password: '123456',
    };

    const responseMock = {
      user_id: 1,
      token: 'token',
      token_type: 'Bearer',
      user: 'test',
      role: 'ASISTENTE',
    };

    const expectedBody = `grant_type=password&username=${user.email}&password=${user.password}&client_id=string&client_secret=string`;

    service.login(user).subscribe({
      next: (res) => {
        expect(res).toEqual(responseMock);
      },
      error: (err) => {
        console.error('error en la petición', err);
      },
    });

    const req = httpMock.expectOne(`${environment.apiUrl}/auth/login`);

    expect(req.request.method).toBe('POST');
    expect(req.request.body.toString()).toEqual(expectedBody);

    req.flush(responseMock);
  });
});
