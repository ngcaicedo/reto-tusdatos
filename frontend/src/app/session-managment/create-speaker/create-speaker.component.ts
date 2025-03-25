import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { SessionService } from '../session.service';
import { NotificationService } from '../../shared/services/notification.service';

@Component({
  selector: 'app-create-speaker',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-speaker.component.html',
  styleUrl: './create-speaker.component.css',
})
export class CreateSpeakerComponent {
  speakerForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private sessionService: SessionService,
    private notify: NotificationService
  ) {}

  ngOnInit() {
    this.speakerForm = this.formBuilder.group({
      speakerName: ['', Validators.required],
    });
  }

  createSpeaker() {
    this.sessionService.createSpeaker(this.speakerForm.value).subscribe({
      next: (response) => {
        this.notify.success('Ponente creado correctamente');
      },
      error: (error) => {
        this.notify.error(`Error al crear ponente: ${JSON.stringify(error.error.detail)}`);
      },
    });
  }
}
