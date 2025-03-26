export class Session {
  id: number;
  name: string;
  description: string;
  duration: number;
  speaker_id: number;

  constructor(
    id: number,
    name: string,
    description: string,
    duration: number,
    speaker_id: number
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.duration = duration;
    this.speaker_id = speaker_id;
  }
}
