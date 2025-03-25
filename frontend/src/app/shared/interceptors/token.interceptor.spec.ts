import { TestBed } from '@angular/core/testing';
import { HTTP_INTERCEPTORS, HttpClient, HttpHeaders, provideHttpClient } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TokenInterceptor } from './token.interceptor';
import { environment } from '../../../environments/environment';



describe('TokenInterceptor', () => {
  let http: HttpClient;
  let httpMock: HttpTestingController;
  let url: string;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true },
        provideHttpClient(),
        provideHttpClientTesting(),
      ]
    });

    http = TestBed.inject(HttpClient);
    httpMock = TestBed.inject(HttpTestingController);
    url = environment.apiUrl + '/sessions/speakers';
  });

  afterEach(() => {
    httpMock.verify();
    sessionStorage.clear();
  });

  it('should add Authorization header if token exists', () => {
    sessionStorage.setItem('token', 'abc123');
    http.get(url).subscribe();

    const req = httpMock.expectOne(url);
    expect(req.request.headers.has('Authorization')).toBeTrue();
    expect(req.request.headers.get('Authorization')).toBe('Bearer abc123');

    req.flush({});
  });

  it('should NOT add Authorization header if token does NOT exist', () => {
    http.get(url).subscribe();

    const req = httpMock.expectOne(url);
    expect(req.request.headers.has('Authorization')).toBeFalse();

    req.flush({});
  });
});
