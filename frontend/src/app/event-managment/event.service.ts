import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class EventService {
  private apiUrl = environment.apiUrl;
  constructor(private http: HttpClient) {}

  createEvent(event: {
    name: string;
    description: string;
    capacity: number;
    state: string;
    date_start: string;
    date_end: string;
    location: string;
    user_created_id: number;
    session_ids: number[];
  }): Observable<any> {
    return this.http.post(`${this.apiUrl}/events/create`, event);
  }

  getEvents(): Observable<Event[]> {
    return this.http.get<Event[]>(`${this.apiUrl}/events`);
  }
}
