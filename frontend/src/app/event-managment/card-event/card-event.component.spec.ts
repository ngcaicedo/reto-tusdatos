import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardEventComponent } from './card-event.component';
import { provideRouter } from '@angular/router';

describe('CardEventComponent', () => {
  let component: CardEventComponent;
  let fixture: ComponentFixture<CardEventComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardEventComponent],
      providers: [
        provideRouter([])
      ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CardEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it(`should have show card event`, () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('.card')).toBeTruthy();
  });

  it(`should have show card event title`, () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#title')).toBeTruthy();
  });

  it(`should have show card event location`, () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#location')).toBeTruthy();
  });

  it(`should have show card event date`, () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#date')).toBeTruthy();
  });

  it(`should have show card event img`, () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('.card-img-top')).toBeTruthy();
  });
});
