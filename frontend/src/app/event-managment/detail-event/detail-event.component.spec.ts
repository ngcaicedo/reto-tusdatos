import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailEventComponent } from './detail-event.component';

describe('DetailEventComponent', () => {
  let component: DetailEventComponent;
  let fixture: ComponentFixture<DetailEventComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DetailEventComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetailEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have show title', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#title')).toBeTruthy();
  });

  it('should have show location', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#location')).toBeTruthy();
  });

  it('should have show capacity', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('#capacity')).toBeTruthy();
  });
});
