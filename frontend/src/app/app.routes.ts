import { Routes } from '@angular/router';
import { authGuard } from './shared/guard/auth.guard';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'events',
    pathMatch: 'full',
  },
  {
    path: 'events',
    loadComponent: () =>
      import('./event-managment/list-event/list-event.component').then(m => m.ListEventComponent),
    pathMatch: 'full',
  },
  {
    path: 'events/assistant/register',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./event-managment/detail-event-assistant/detail-event-assistant.component').then(m => m.DetailEventAssistantComponent),
    pathMatch: 'full',
  },
  {
    path: 'events/:event_id',
    loadComponent: () =>
      import('./event-managment/detail-event/detail-event.component').then(m => m.DetailEventComponent),
    pathMatch: 'full',
  },
  {
    path: 'sessions/speaker/create',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./session-managment/create-speaker/create-speaker.component').then(m => m.CreateSpeakerComponent),
    pathMatch: 'full',
  },
  {
    path: 'sessions/create',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./session-managment/create-session/create-session.component').then(m => m.CreateSessionComponent),
    pathMatch: 'full',
  },
  {
    path: 'create/events',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./event-managment/create-event/create-event.component').then(m => m.CreateEventComponent),
    pathMatch: 'full',
  },

  {
    path: 'users/register',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./auth-user/register-organization/register-organization.component').then(m => m.RegisterOrganizationComponent),
    pathMatch: 'full',
  }
];
