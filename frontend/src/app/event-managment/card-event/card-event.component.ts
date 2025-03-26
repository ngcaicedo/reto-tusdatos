import { Component, Input, SimpleChanges } from '@angular/core';
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

  readableDate = '';

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['date'] && this.date) {
      const parsed = new Date(this.date);
  
      this.readableDate = parsed.toLocaleDateString('es-ES', {
        day: 'numeric',
        month: 'short'
      });
    }
  }
}
