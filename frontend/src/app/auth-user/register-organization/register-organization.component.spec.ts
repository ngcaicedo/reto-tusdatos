import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterOrganizationComponent } from './register-organization.component';
import { NotificationService } from '../../shared/services/notification.service';
import { ReactiveFormsModule } from '@angular/forms';

describe('RegisterOrganizationComponent', () => {
  let component: RegisterOrganizationComponent;
  let fixture: ComponentFixture<RegisterOrganizationComponent>;
  let mockNotifyService: jasmine.SpyObj<NotificationService>;

  beforeEach(async () => {
    mockNotifyService = jasmine.createSpyObj('NotificationService', [
      'success',
      'error',
      'info',
      'warning',
    ]);
    await TestBed.configureTestingModule({
      imports: [RegisterOrganizationComponent],
      providers: [
        { provide: NotificationService, useValue: mockNotifyService },
      ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegisterOrganizationComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
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
