import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RegisterAssistantService {
  private apiUrl = environment.apiUrl;
  constructor(
    private http: HttpClient
  ) { }

  registerAssistant(assistant: { name: string; email: string; password: string; phone: string; role: string; }) {
    return this.http.post(`${this.apiUrl}/users/register/assistant`, assistant);
  }
}
