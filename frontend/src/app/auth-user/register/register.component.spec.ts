/* tslint:disable:no-unused-variable */
import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { RegisterComponent } from './register.component';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { ReactiveFormsModule } from '@angular/forms';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';
import { RegisterAssistantService } from './register-assistant.service';
import { of, throwError } from 'rxjs';
import { provideToastr, Toast, ToastrService } from 'ngx-toastr';
import { NotificationService } from '../../shared/services/notification.service';

describe('RegisterComponent', () => {
  let component: RegisterComponent;
  let fixture: ComponentFixture<RegisterComponent>;
  let activeModalSpy: jasmine.SpyObj<NgbActiveModal>;
  let mockRegisterAssistantService: jasmine.SpyObj<RegisterAssistantService>;
  let mockNotificationService: jasmine.SpyObj<NotificationService>;

  beforeEach(waitForAsync(() => {
    activeModalSpy = jasmine.createSpyObj('NgbActiveModal', ['dismiss']);
    mockRegisterAssistantService = jasmine.createSpyObj('RegisterAssistantService', ['registerAssistant']);
    mockNotificationService = jasmine.createSpyObj('NotificationService', ['success', 'error', 'info', 'warning']);
    TestBed.configureTestingModule({
      imports: [RegisterComponent, ReactiveFormsModule],
      providers: [
        { provide: NgbActiveModal, useValue: activeModalSpy },
        { provide: RegisterAssistantService, useValue: mockRegisterAssistantService },
        { provide: NotificationService, useValue: mockNotificationService },
        provideHttpClient(),
        provideHttpClientTesting(),
        provideToastr(),
      ],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegisterComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    component.registerForm.setValue({
      name: 'test',
      phone: '1234567890',
      email: 'test@gmail.com',
      password: '123456'
    })
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show login form', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('form')).toBeTruthy();
  });

  it('should show name input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(
      compiled.querySelector('input[formControlName="name"]')
    ).toBeTruthy();
  });

  it('should show phone input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(
      compiled.querySelector('input[formControlName="phone"]')
    ).toBeTruthy();
  });

  it('should show email input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(
      compiled.querySelector('input[formControlName="email"]')
    ).toBeTruthy();
  });

  it('should show password input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(
      compiled.querySelector('input[formControlName="password"]')
    ).toBeTruthy();
  });

  it('should close modal', () => {
    component.cancel();
    expect(activeModalSpy.dismiss).toHaveBeenCalled();
  });

  it('should register assistant', () => {
    mockRegisterAssistantService.registerAssistant.and.returnValue(of({message: 'success'}));
    component.registerAssistant();
    expect(mockRegisterAssistantService.registerAssistant).toHaveBeenCalledWith(component.registerForm.value);
    expect(activeModalSpy.dismiss).toHaveBeenCalled();;
  });

  it('should show error message', () => {
    const errorResponse = {
      status: 401,
      error: {
        detail: 'Registro fallido'
      }
    };
    mockRegisterAssistantService.registerAssistant.and.returnValue(throwError(() => errorResponse));
    component.registerAssistant();
    expect(mockRegisterAssistantService.registerAssistant).toHaveBeenCalledWith(component.registerForm.value);
    expect(activeModalSpy.dismiss).not.toHaveBeenCalled();
    expect(mockNotificationService.error).toHaveBeenCalledWith(`Error al registrar: Registro fallido`);
  });

});
