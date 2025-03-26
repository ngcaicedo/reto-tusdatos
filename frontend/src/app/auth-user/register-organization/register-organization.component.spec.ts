import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterOrganizationComponent } from './register-organization.component';

describe('RegisterOrganizationComponent', () => {
  let component: RegisterOrganizationComponent;
  let fixture: ComponentFixture<RegisterOrganizationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RegisterOrganizationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegisterOrganizationComponent);
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

  it('should show role select', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(
      compiled.querySelector('select[formControlName="role"]')
    ).toBeTruthy();
  });

  it('should show password input', () => {
    const compiled = fixture.debugElement.nativeElement;
    expect(
      compiled.querySelector('input[formControlName="password"]')
    ).toBeTruthy();
  });
});
