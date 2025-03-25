/* tslint:disable:no-unused-variable */
import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { HeaderComponent } from './header.component';

describe('HeaderComponent', () => {
  let component: HeaderComponent;
  let fixture: ComponentFixture<HeaderComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [HeaderComponent],
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
    const compiled = fixture.nativeElement as HTMLElement;
    const loginButton = compiled.querySelector('.btn-login');
    expect(loginButton).toBeTruthy();
    expect(loginButton?.textContent?.trim()).toBe('Iniciar sesión');
  });

  it(`should have show register buttom`, () => {
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

  it(`should have show events`, () =>{
    const compiled = fixture.nativeElement as HTMLElement;
    const eventosLink = Array.from(compiled.querySelectorAll('.nav-link'))
    .find(link => link.textContent?.trim() === 'Eventos');
    expect(eventosLink).toBeTruthy();
  })

  it(`should have show contact`, () =>{
    const compiled = fixture.nativeElement as HTMLElement;
    const homeLink = Array.from(compiled.querySelectorAll('.nav-link'))
    .find(link => link.textContent?.trim() === 'Contacto');
    expect(homeLink).toBeTruthy();
  })
});
