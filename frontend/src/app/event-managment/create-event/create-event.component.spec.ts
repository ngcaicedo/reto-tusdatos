import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEventComponent } from './create-event.component';

describe('CreateEventComponent', () => {
  let component: CreateEventComponent;
  let fixture: ComponentFixture<CreateEventComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateEventComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CreateEventComponent);
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
      compiled.querySelector('input[formControlName="name"]')
    ).toBeTruthy();
  });

  it('should have show description input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('textarea[formControlName="description"]')
    ).toBeTruthy();
  });

  it('should have show duration input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="capacity"]')
    ).toBeTruthy();
  });

  it('should have show date start input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="date_start"]')
    ).toBeTruthy();
  });

  it('should have show date end input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="date_end"]')
    ).toBeTruthy();
  });

  it('should have show location input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="location"]')
    ).toBeTruthy();
  });
});
