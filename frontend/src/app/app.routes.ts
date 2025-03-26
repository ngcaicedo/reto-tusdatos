import { Routes } from '@angular/router';
import { CreateSpeakerComponent } from './session-managment/create-speaker/create-speaker.component';
import { CreateSessionComponent } from './session-managment/create-session/create-session.component';
import { CreateEventComponent } from './event-managment/create-event/create-event.component';
import { ListEventComponent } from './event-managment/list-event/list-event.component';
import { DetailEventComponent } from './event-managment/detail-event/detail-event.component';
import { DetailEventAssistantComponent } from './event-managment/detail-event-assistant/detail-event-assistant.component';
import { authGuard } from './shared/guard/auth.guard';

export const routes: Routes = [
    {path: '', redirectTo: 'events', pathMatch: 'full'},
    {path: 'events', component: ListEventComponent, pathMatch: 'full'},
    {path: 'events/assistant/register', component: DetailEventAssistantComponent, pathMatch: 'full', canActivate: [authGuard]},
    {path: 'events/:event_id', component: DetailEventComponent, pathMatch: 'full'},
    {path: 'sessions/speaker/create', component: CreateSpeakerComponent, pathMatch: 'full', canActivate: [authGuard]},
    {path: 'sessions/create', component: CreateSessionComponent, pathMatch: 'full', canActivate: [authGuard]},
    {path: 'create/events', component: CreateEventComponent, pathMatch: 'full', canActivate: [authGuard]},
];
