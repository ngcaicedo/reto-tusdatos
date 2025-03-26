import { ComponentFixture, fakeAsync, TestBed, tick } from '@angular/core/testing';

import { ListEventComponent } from './list-event.component';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { Event } from '../../event-managment/event';
import { Session } from '../../session-managment/session';
import { of, throwError } from 'rxjs';
import { By } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { CardEventComponent } from '../card-event/card-event.component';
import { provideRouter } from '@angular/router';

describe('ListEventComponent', () => {
  let component: ListEventComponent;
  let fixture: ComponentFixture<ListEventComponent>;
  let mockEventService: jasmine.SpyObj<EventService>;
  let mockNotifyService: jasmine.SpyObj<NotificationService>;
  const mockEvents = [
    new Event(
      1,
      'Event 1',
      'Description 1',
      100,
      'active',
      '2021-10-10',
      '2021-10-11',
      'Location 1',
      1,
      [new Session(1, 'Session 1', 'Description 1', new Date().toString(), 1, 1, {id: 1, name: 'test'})],
      false
    ),
    new Event(
      2,
      'Event 2',
      'Description 2',
      200,
      'inactive',
      '2021-10-12',
      '2021-10-13',
      'Location 2',
      2,
      [new Session(2, 'Session 2', 'Description 2', new Date().toString(), 2, 2, {id: 1, name: 'test'})],
      true
    ),
  ];

  beforeEach(async () => {
    mockEventService = jasmine.createSpyObj('EventService', ['getEvents']);
    mockEventService.getEvents.and.returnValue(of(mockEvents));
    mockNotifyService = jasmine.createSpyObj('NotificationService', [
      'success',
      'error',
      'info',
      'warning',
    ]);
    await TestBed.configureTestingModule({
      imports: [ListEventComponent, CardEventComponent],
      providers: [
        { provide: NotificationService, useValue: mockNotifyService },
        { provide: EventService, useValue: mockEventService },
        provideRouter([]),
        provideHttpClient(),
        provideHttpClientTesting()
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(ListEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show message when there are no events', () => {
    mockEventService.getEvents.and.returnValue(of([]));
    fixture = TestBed.createComponent(ListEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    const msg =
      fixture.debugElement.nativeElement.querySelector('.empty-message');
    expect(msg.textContent).toContain('No hay eventos disponibles');
  });

  it('should load events on init', fakeAsync(() => {
    mockEventService.getEvents.and.returnValue(of(mockEvents));
  
    fixture = TestBed.createComponent(ListEventComponent);
    const component = fixture.componentInstance;
    component.ngOnInit();
    tick();
  
    expect(component.events).toEqual(mockEvents);
  }));

  it('should call notify.error on event load failure', fakeAsync(() => {
    const mockError = {
      error: { detail: 'Algo salió mal' }
    };
  
    mockEventService.getEvents.and.returnValue(throwError(() => mockError));
  
    fixture = TestBed.createComponent(ListEventComponent);
    const component = fixture.componentInstance;
    fixture.detectChanges();
    tick();
  
    expect(mockNotifyService.error).toHaveBeenCalledWith('Error al obtener eventos: Algo salió mal');
  }));
});
