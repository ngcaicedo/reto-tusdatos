/* tslint:disable:no-unused-variable */
import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { LoginComponent } from './login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { NotificationService } from '../../shared/services/notification.service';
import { AuthUserService } from './auth-user.service';
import { of, throwError } from 'rxjs';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let activeModalSpy: jasmine.SpyObj<NgbActiveModal>;
  let mockNotificationService: jasmine.SpyObj<NotificationService>;
  let mockAuthUserService: jasmine.SpyObj<AuthUserService>;

  beforeEach(waitForAsync(() => {
    activeModalSpy = jasmine.createSpyObj('NgbActiveModal', ['dismiss']);
    mockNotificationService = jasmine.createSpyObj('NotificationService', [
      'success',
      'error',
      'info',
      'warning',
    ]);
    mockAuthUserService = jasmine.createSpyObj('AuthUserService', ['login']);
    TestBed.configureTestingModule({
      imports: [LoginComponent, ReactiveFormsModule],
      providers: [
        { provide: NgbActiveModal, useValue: activeModalSpy },
        { provide: NotificationService, useValue: mockNotificationService },
        { provide: AuthUserService, useValue: mockAuthUserService },
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    component.loginForm.setValue({
      email: 'test@gmail.com',
      password: '123456',
    });
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show login form', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('form')).toBeTruthy();
  });

  it('should show email input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('input[type="email"]')).toBeTruthy();
  });

  it('should show password input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('input[type="password"]')).toBeTruthy();
  });

  it('should close modal', () => {
    component.cancel();
    expect(activeModalSpy.dismiss).toHaveBeenCalled();
  });

  it('should login user', () => {
    mockAuthUserService.login.and.returnValue(of({message: 'success'}));
    component.login();
    expect(mockAuthUserService.login).toHaveBeenCalledWith(component.loginForm.value);
    expect(mockNotificationService.success).toHaveBeenCalledWith('Inicio de sesión exitoso');
    expect(activeModalSpy.dismiss).toHaveBeenCalled();
  });

  it('should login show error message', () => {
    const errorResponse = {
      status: 401,
      error: {
        detail: 'Inicio de sesión no exitoso'
      }
    };
    mockAuthUserService.login.and.returnValue(throwError(() => errorResponse));
    component.login();
    expect(mockAuthUserService.login).toHaveBeenCalledWith(component.loginForm.value);
    expect(mockNotificationService.error).toHaveBeenCalledWith('Error en inicio de sesión: Inicio de sesión no exitoso');
  });

  it('should session storage empty', () => {
    expect(sessionStorage.getItem('token')).toBeNull();
    expect(sessionStorage.getItem('user')).toBeNull();
    expect(sessionStorage.getItem('role')).toBeNull();
    expect(sessionStorage.getItem('user_id')).toBeNull();
  });
});
