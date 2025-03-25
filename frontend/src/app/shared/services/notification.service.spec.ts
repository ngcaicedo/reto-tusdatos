import { TestBed } from '@angular/core/testing';
import { NotificationService } from './notification.service';
import { ToastrService } from 'ngx-toastr';

describe('NotificationService', () => {
  let service: NotificationService;
  let toastrSpy: jasmine.SpyObj<ToastrService>;

  beforeEach(() => {
    toastrSpy = jasmine.createSpyObj('ToastrService', ['success', 'error', 'info', 'warning']);

    TestBed.configureTestingModule({
      providers: [
        NotificationService,
        { provide: ToastrService, useValue: toastrSpy }
      ]
    });

    service = TestBed.inject(NotificationService);
  });

  it('should call success', () => {
    service.success('Creado');
    expect(toastrSpy.success).toHaveBeenCalledWith('Creado', 'Éxito');
  });

  it('should call error', () => {
    service.error('Falló');
    expect(toastrSpy.error).toHaveBeenCalledWith('Falló', 'Error');
  });

  it('should call info', () => {
    service.info('Algo sucedió');
    expect(toastrSpy.info).toHaveBeenCalledWith('Algo sucedió', 'Información');
  });

  it('should call warning', () => {
    service.warning('Cuidado');
    expect(toastrSpy.warning).toHaveBeenCalledWith('Cuidado', 'Advertencia');
  });
});
