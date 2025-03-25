import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateSessionComponent } from './create-session.component';
import { of, throwError } from 'rxjs';
import { SessionService } from '../session.service';
import { NotificationService } from '../../shared/services/notification.service';

describe('CreateSessionComponent', () => {
  let component: CreateSessionComponent;
  let fixture: ComponentFixture<CreateSessionComponent>;
  let mockSessionService: jasmine.SpyObj<SessionService>;
  let mockNotifyService: jasmine.SpyObj<NotificationService>;

  beforeEach(async () => {
    mockSessionService = jasmine.createSpyObj('SessionService', ['createSession', 'getSpeakers']);
    mockSessionService.getSpeakers.and.returnValue(of([]));
    mockNotifyService = jasmine.createSpyObj('NotificationService', ['success', 'error', 'info', 'warning']);
    await TestBed.configureTestingModule({
      imports: [CreateSessionComponent],
      providers: [
        { provide: SessionService, useValue: mockSessionService },
        { provide: NotificationService, useValue: mockNotifyService }
      ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateSessionComponent);
    component = fixture.componentInstance;
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
      compiled.querySelector('input[formControlName="sessionName"]')
    ).toBeTruthy();
  });

  it('should have show description input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('textarea[formControlName="sessionDescription"]')
    ).toBeTruthy();
  });

  it('should have show duration input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="sessionDuration"]')
    ).toBeTruthy();
  });

  it('should have show speaker input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('select[formControlName="speaker"]')
    ).toBeTruthy();
  });

  it('should register session', () => {
    mockSessionService.createSession.and.returnValue(of({message: 'Sesión creada'}));
    component.createSession();
    expect(mockSessionService.createSession).toHaveBeenCalledWith(component.sessionForm.value);
  });

  it('should register error', () => {
    const errorResponse = {
      status: 401,
      error: {
        detail: 'Creacion de sesion no exitosa'
      }
    };
    mockSessionService.createSession.and.returnValue(throwError(() => errorResponse));
    component.createSession();
    expect(mockSessionService.createSession).toHaveBeenCalledWith(component.sessionForm.value);
    expect(mockNotifyService.error).toHaveBeenCalled();
  });
  
});
