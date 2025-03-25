import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthUserService {
  private apiUrl = environment.apiUrl;
  constructor(
    private http: HttpClient
  ) { }

  login(user: { email: string; password: string; }): Observable<any> {
    const body = new HttpParams()
    .set('grant_type', 'password')
    .set('username', user.email)
    .set('password', user.password)
    .set('client_id', 'string')
    .set('client_secret', 'string');

    const headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
    };
    return this.http.post(`${this.apiUrl}/auth/login`, body, { headers });
  }
}
