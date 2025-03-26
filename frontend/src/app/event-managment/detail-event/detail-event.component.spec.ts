import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailEventComponent } from './detail-event.component';
import { EventService } from '../event.service';
import { NotificationService } from '../../shared/services/notification.service';
import { Event } from '../event';
import { Session } from '../../session-managment/session';
import { of } from 'rxjs';

describe('DetailEventComponent', () => {
  let component: DetailEventComponent;
  let fixture: ComponentFixture<DetailEventComponent>;
  let mockEventService: jasmine.SpyObj<EventService>;
  let mockNotifyService: jasmine.SpyObj<NotificationService>;

  const mockEvent = new Event(
    1,
    'test',
    'test',
    100,
    'CREADO',
    '2021-09-02',
    '2021-09-03',
    'test',
    1,
    [new Session(1, 'Session 1', 'Session 1', new Date().toString(), 60, 1)]
  );

  beforeEach(async () => {
    mockEventService = jasmine.createSpyObj('EventService', ['getEvent']);
    mockEventService.getEvent.and.returnValue(of(mockEvent));
    mockNotifyService = jasmine.createSpyObj('NotificationService', [ 'success', 'error', 'info', 'warning' ]);
    await TestBed.configureTestingModule({
      imports: [DetailEventComponent],
      providers: [
        { provide: EventService, useValue: mockEventService },
        { provide: NotificationService, useValue: mockNotifyService },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(DetailEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have show title', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#title')).toBeTruthy();
  });

  it('should have show location', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#location')).toBeTruthy();
  });

  it('should have show capacity', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#capacity')).toBeTruthy();
  });

  it('should get event', () => {
    expect(component.event).toEqual(mockEvent);
    expect(mockEventService.getEvent).toHaveBeenCalled();
  });

});
