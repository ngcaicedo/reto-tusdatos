import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateSessionComponent } from './create-session.component';

describe('CreateSessionComponent', () => {
  let component: CreateSessionComponent;
  let fixture: ComponentFixture<CreateSessionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateSessionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateSessionComponent);
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
      compiled.querySelector('input[formControlName="speakerName"]')
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
      compiled.querySelector('input[formControlName="description"]')
    ).toBeTruthy();
  });

  it('should have show speaker input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('select[formControlName="speaker"]')
    ).toBeTruthy();
  });
  
});
