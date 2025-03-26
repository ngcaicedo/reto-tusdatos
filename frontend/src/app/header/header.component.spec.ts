/* tslint:disable:no-unused-variable */
import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { HeaderComponent } from './header.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from '../auth-user/login/login.component';
import { RegisterComponent } from '../auth-user/register/register.component';
import { AuthStateService } from '../shared/states/auth-state.service';

describe('HeaderComponent', () => {
  let component: HeaderComponent;
  let fixture: ComponentFixture<HeaderComponent>;
  let modalServiceSpy: jasmine.SpyObj<NgbModal>;

  beforeEach(waitForAsync(() => {
    modalServiceSpy = jasmine.createSpyObj('NgbModal', ['open']);

    TestBed.configureTestingModule({
      imports: [HeaderComponent],
      providers: [{ provide: NgbModal, useValue: modalServiceSpy }],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it(`should have show login buttom`, () => {
    const authStateMock = TestBed.inject(AuthStateService);
    authStateMock.clearUser();
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    const loginButton = compiled.querySelector('.btn-login');
    expect(loginButton).toBeTruthy();
    expect(loginButton?.textContent?.trim()).toBe('Iniciar sesión');
  });

  it(`should have show register buttom`, () => {
    const authStateMock = TestBed.inject(AuthStateService);
    authStateMock.clearUser();
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    const registerButton = compiled.querySelector('.btn-register');
    expect(registerButton).toBeTruthy();
    expect(registerButton?.textContent?.trim()).toBe('Crear cuenta');
  });

  it(`should have show logo`, () => {
    const compiled = fixture.nativeElement as HTMLElement;
    const logo = compiled.querySelector('.navbar-brand');
    expect(logo).toBeTruthy();
  });

  it(`should have show events`, () => {
    const authStateMock = TestBed.inject(AuthStateService);
    authStateMock.setUser({
      token: 'token',
      user: 'Test User',
      role: 'ORGANIZADOR',
      user_id: '1',
    });
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    const eventosLink = Array.from(compiled.querySelectorAll('.nav-link')).find(
      (link) => link.textContent?.trim() === 'Eventos'
    );
    expect(eventosLink).toBeTruthy();
  });

  it(`should have show contact`, () => {
    const authStateMock = TestBed.inject(AuthStateService);
    authStateMock.setUser({
      token: 'token',
      user: 'Test User',
      role: 'ASISTENTE',
      user_id: '1',
    });
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    const homeLink = Array.from(compiled.querySelectorAll('.nav-link')).find(
      (link) => link.textContent?.trim() === 'Contacto'
    );
    expect(homeLink).toBeTruthy();
  });

  it('should open login modal', () => {
    component.openLoginModal();
    expect(modalServiceSpy.open).toHaveBeenCalledWith(LoginComponent, {
      centered: true,
    });
  });

  it('should open register modal', () => {
    component.openRegisterModal();
    expect(modalServiceSpy.open).toHaveBeenCalledWith(RegisterComponent, {
      centered: true,
    });
  });
});
