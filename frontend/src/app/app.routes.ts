import { Routes } from '@angular/router';
import { CreateSpeakerComponent } from './session-managment/create-speaker/create-speaker.component';

export const routes: Routes = [
    {path: 'sessions/speaker/create', component: CreateSpeakerComponent, pathMatch: 'full'},
];
