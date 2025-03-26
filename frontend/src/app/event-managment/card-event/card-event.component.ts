import { Component, Input } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-card-event',
  imports: [RouterModule],
  templateUrl: './card-event.component.html',
  styleUrl: './card-event.component.css'
})
export class CardEventComponent {
  @Input() title!: string;
  @Input() location!: string;
  @Input() date!: string;
  @Input() img!: string;
  @Input() state!: string;
  @Input() capacity!: number;
  @Input() event_id!: number;
}
