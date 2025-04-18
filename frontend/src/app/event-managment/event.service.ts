import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Event } from './event';

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
    return this.http.get<Event[]>(`${this.apiUrl}/events/events`);
  }

  getEvent(event_id: number): Observable<Event> {
    return this.http.get<Event>(`${this.apiUrl}/events/${event_id}`);
  }

  registerUserToEvent(event_id: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/events/register/${event_id}`, {});
  }

  getEventsRegistedAssistant(): Observable<Event[]> {
    return this.http.get<Event[]>(`${this.apiUrl}/events/assistant/register`);
  }
}
