import { TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { NotificationService } from './shared/services/notification.service';

describe('AppComponent', () => {
  let mockNotifyService: jasmine.SpyObj<NotificationService>;
  beforeEach(async () => {
    mockNotifyService = jasmine.createSpyObj('NotificationService', ['success', 'error', 'info', 'warning']);
    await TestBed.configureTestingModule({
      imports: [AppComponent],
      providers: [
        { provide: NotificationService, useValue: mockNotifyService },
        provideHttpClient(),
        provideHttpClientTesting()
      ]
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have the 'frontend' title`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('frontend');
  });

});
