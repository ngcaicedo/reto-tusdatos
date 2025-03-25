/* tslint:disable:no-unused-variable */
import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { RegisterComponent } from './register.component';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { ReactiveFormsModule } from '@angular/forms';

describe('RegisterComponent', () => {
  let component: RegisterComponent;
  let fixture: ComponentFixture<RegisterComponent>;
  let activeModalSpy: jasmine.SpyObj<NgbActiveModal>;

  beforeEach(waitForAsync(() => {
    activeModalSpy = jasmine.createSpyObj('NgbActiveModal', ['dismiss']);
    TestBed.configureTestingModule({
      imports: [ RegisterComponent, ReactiveFormsModule ],
      providers: [{ provide: NgbActiveModal, useValue: activeModalSpy }],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegisterComponent);
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

  it('should show name input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('input[formControlName="name"]')).toBeTruthy();
  });

  it('should show phone input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('input[formControlName="phone"]')).toBeTruthy();
  });

  it('should show email input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('input[formControlName="email"]')).toBeTruthy();
  });

  it('should show password input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('input[formControlName="password"]')).toBeTruthy();
  });

  it('should close modal', () => {
    component.cancel();
    expect(activeModalSpy.dismiss).toHaveBeenCalled();
  });
});
