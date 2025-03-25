import { Routes } from '@angular/router';
import { CreateSpeakerComponent } from './assistant-managment/create-speaker/create-speaker.component';

export const routes: Routes = [
    {path: 'sessions/speaker/create', component: CreateSpeakerComponent, pathMatch: 'full'},
];
