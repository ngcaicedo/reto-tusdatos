/* tslint:disable:no-unused-variable */
import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { LoginComponent } from './login.component';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [LoginComponent],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
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
});
