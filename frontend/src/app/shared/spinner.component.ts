// spinner.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AsyncPipe } from '@angular/common';
import { LoadingService } from './interceptors/loading.service';

@Component({
  selector: 'app-spinner',
  standalone: true,
  imports: [CommonModule, AsyncPipe],
  template: `
    <div class="spinner-overlay" *ngIf="loadingService.loading$ | async">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Cargando...</span>
      </div>
    </div>
  `,
  styles: [
    `
      .spinner-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.7);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
      }
    `,
  ],
})
export class SpinnerComponent {
  constructor(public loadingService: LoadingService) {}
}
