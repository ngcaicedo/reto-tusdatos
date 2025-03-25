import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateSpeakerComponent } from './create-speaker.component';

describe('CreateSpeakerComponent', () => {
  let component: CreateSpeakerComponent;
  let fixture: ComponentFixture<CreateSpeakerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateSpeakerComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CreateSpeakerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have show create speaker form', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('form')).toBeTruthy();
  });

  it('should have show name input', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(
      compiled.querySelector('input[formControlName="speakerName"]')
    ).toBeTruthy();
  });
});
