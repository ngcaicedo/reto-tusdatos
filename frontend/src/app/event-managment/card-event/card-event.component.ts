import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-card-event',
  imports: [],
  templateUrl: './card-event.component.html',
  styleUrl: './card-event.component.css'
})
export class CardEventComponent {
  @Input() title!: string;
  @Input() location!: string;
  @Input() date!: string;
  @Input() img!: string;
  @Input() state!: string;
}
