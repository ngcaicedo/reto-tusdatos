import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Speaker } from '../speaker';

@Component({
  selector: 'app-create-session',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-session.component.html',
  styleUrl: './create-session.component.css',
})
export class CreateSessionComponent {
  sessionForm!: FormGroup;
  speakers: Array<Speaker> = [];

  constructor(private formBuilder: FormBuilder) {}

  ngOnInit() {
    this.sessionForm = this.formBuilder.group({
      sessionName: ['', Validators.required],
      sessionDescription: ['', Validators.required],
      sessionDuration: ['', Validators.required],
      speaker: ['', Validators.required],
    });
  }
}
