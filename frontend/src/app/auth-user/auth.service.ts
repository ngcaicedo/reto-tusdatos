import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = environment.apiUrl;

  constructor(
    private http: HttpClient
  ) { }

  registerUser(user: {
    name: string;
    email: string;
    phone: string;
    password: string;
    role: string;
  }) {
    return this.http.post(`${this.apiUrl}/auth/register`, user);
  }
}
