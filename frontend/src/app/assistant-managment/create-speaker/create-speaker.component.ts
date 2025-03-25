import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-create-speaker',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-speaker.component.html',
  styleUrl: './create-speaker.component.css',
})
export class CreateSpeakerComponent {
  speakerForm!: FormGroup;

  constructor(private formBuilder: FormBuilder) {}

  ngOnInit() {
    this.speakerForm = this.formBuilder.group({
      speakerName: ['', Validators.required],
    });
  }
}
