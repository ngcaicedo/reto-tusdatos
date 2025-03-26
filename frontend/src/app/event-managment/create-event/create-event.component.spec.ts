import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEventComponent } from './create-event.component';
import { NotificationService } from '../../shared/services/notification.service';
import { EventService } from '../event.service';
import { of, throwError } from 'rxjs';

describe('CreateEventComponent', () => {
  let component: CreateEventComponent;
  let fixture: ComponentFixture<CreateEventComponent>;
  let mockEventService: jasmine.SpyObj<EventService>;
  let mockNotifyService: jasmine.SpyObj<NotificationService>;

  beforeEach(async () => {
    mockEventService = jasmine.createSpyObj('EventService', ['createEvent']);
    mockNotifyService = jasmine.createSpyObj('NotificationService', [
      'success',
      'error',
      'info',
      'warning',
    ]);
    await TestBed.configureTestingModule({
      imports: [CreateEventComponent],
      providers: [
        { provide: EventService, useValue: mockEventService },
        { provide: NotificationService, useValue: mockNotifyService },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(CreateEventComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have show create session form', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('form')).toBeTruthy();
  });

  it('should have show name input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="name"]')
    ).toBeTruthy();
  });

  it('should have show description input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('textarea[formControlName="description"]')
    ).toBeTruthy();
  });

  it('should have show duration input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="capacity"]')
    ).toBeTruthy();
  });

  it('should have show date start input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="date_start"]')
    ).toBeTruthy();
  });

  it('should have show date end input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="date_end"]')
    ).toBeTruthy();
  });

  it('should have show location input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="location"]')
    ).toBeTruthy();
  });

  it('should register event', () => {
    mockEventService.createEvent.and.returnValue(of({ message: 'Evento creado' }));
    component.createEvent();
    expect(mockEventService.createEvent).toHaveBeenCalledWith(
      component.eventForm.value
    );
  });

  it('should register error', () => {
    const errorResponse = {
      status: 401,
      error: {
        detail: 'Creacion de evento no exitosa',
      },
    };
    mockEventService.createEvent.and.returnValue(throwError(() => errorResponse));
    component.createEvent();
    expect(mockEventService.createEvent).toHaveBeenCalledWith(
      component.eventForm.value
    );
    expect(mockNotifyService.error).toHaveBeenCalled();
  });

});
