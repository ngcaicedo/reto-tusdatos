import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { SpinnerComponent } from './shared/spinner.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, HeaderComponent, SpinnerComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
