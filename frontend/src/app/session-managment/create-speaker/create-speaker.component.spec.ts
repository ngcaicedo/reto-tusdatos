import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateSpeakerComponent } from './create-speaker.component';
import { SessionService } from '../session.service';
import { NotificationService } from '../../shared/services/notification.service';
import { of, throwError } from 'rxjs';

describe('CreateSpeakerComponent', () => {
  let component: CreateSpeakerComponent;
  let fixture: ComponentFixture<CreateSpeakerComponent>;
  let mockSessionService: jasmine.SpyObj<SessionService>;
  let mockNotifyService: jasmine.SpyObj<NotificationService>;

  beforeEach(async () => {
    mockSessionService = jasmine.createSpyObj('SessionService', ['createSpeaker']);
    mockNotifyService = jasmine.createSpyObj('NotificationService', ['success', 'error', 'info', 'warning']);
    await TestBed.configureTestingModule({
      imports: [CreateSpeakerComponent],
      providers: [
        { provide: SessionService, useValue: mockSessionService },
        { provide: NotificationService, useValue: mockNotifyService }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(CreateSpeakerComponent);
    component = fixture.componentInstance;
    component.ngOnInit();

    component.speakerForm.setValue({
      speakerName: 'test',
    });

    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have show create speaker form', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('form')).toBeTruthy();
  });

  it('should have show name input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="speakerName"]')
    ).toBeTruthy();
  });

  it('should create speaker', () => {
    mockSessionService.createSpeaker.and.returnValue(of({ name: 'test' }));
    component.createSpeaker();
    expect(mockSessionService.createSpeaker).toHaveBeenCalledWith(component.speakerForm.value);
    expect(mockNotifyService.success).toHaveBeenCalledWith('Ponente creado correctamente');
  });

  it('should create speaker error', () => {
    let error = new Error('error');
    mockSessionService.createSpeaker.and.returnValue(throwError(() => error));
    component.createSpeaker();
    expect(mockSessionService.createSpeaker).toHaveBeenCalledWith(component.speakerForm.value);
    expect(mockNotifyService.error).toHaveBeenCalledWith(`Error al crear ponente: error`);
  });
});
