import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SessionService {
  private apiUrl = environment.apiUrl;
  constructor(
    private http: HttpClient
  ) { }

  createSpeaker(speaker: { name: string; }) {
    return this.http.post(`${this.apiUrl}/sessions/create/speaker`, speaker);
  }

  getSpeakers() {
    return this.http.get(`${this.apiUrl}/sessions/speakers`);
  }

  createSession(session: { name: string; description: string; duration: number; speaker_id: number; }) {
    return this.http.post(`${this.apiUrl}/sessions/create`, session);
  }
}
