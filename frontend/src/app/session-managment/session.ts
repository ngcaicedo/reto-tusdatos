import { Speaker } from "./speaker";

export class Session {
  id: number;
  name: string;
  description: string;
  date_start: string;
  duration: number;
  speaker_id: number;
  speaker: Speaker;

  constructor(
    id: number,
    name: string,
    description: string,
    date_start: string,
    duration: number,
    speaker_id: number,
    speaker: Speaker
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.date_start = date_start;
    this.duration = duration;
    this.speaker_id = speaker_id;
    this.speaker = speaker;
  }
}
