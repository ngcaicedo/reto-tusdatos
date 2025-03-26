import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListEventComponent } from './list-event.component';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { Event } from '../../event-managment/event';
import { Session } from '../../session-managment/session';
import { of } from 'rxjs';
import { By } from '@angular/platform-browser';

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
      [new Session(1, 'Session 1', 'Description 1', 1, 1)]
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
      [new Session(2, 'Session 2', 'Description 2', 2, 2)]
    ),
  ];

  beforeEach(async () => {
    mockEventService = jasmine.createSpyObj('EventService', ['getEvents']);
    mockEventService.getEvents.and.returnValue(of(mockEvents));
    await TestBed.configureTestingModule({
      imports: [ListEventComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(ListEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should render a card for each event', () => {
    const cards = fixture.debugElement.queryAll(By.css('app-evento-card'));
    expect(cards.length).toBe(2);
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
});
