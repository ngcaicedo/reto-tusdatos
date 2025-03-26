import { Session } from '../session-managment/session';

export class Event {
  id: number;
  name: string;
  description: string;
  capacity: number;
  state: string;
  date_start: string;
  date_end: string;
  location: string;
  user_created_id: number;
  sessions: Session[];
  is_registered: boolean;

  constructor(
    id: number,
    name: string,
    description: string,
    capacity: number,
    state: string,
    date_start: string,
    date_end: string,
    location: string,
    user_created_id: number,
    sessions: Session[],
    is_registered: boolean
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.capacity = capacity;
    this.state = state;
    this.date_start = date_start;
    this.date_end = date_end;
    this.location = location;
    this.user_created_id = user_created_id;
    this.sessions = sessions;
    this.is_registered = is_registered
  }
}
