import { AuthStateService } from './auth-state.service';

describe('AuthStateService', () => {
  let service: AuthStateService;

  const mockUser = {
    token: 'abc123',
    user: 'test',
    role: 'ADMIN',
    user_id: 1,
  };

  beforeEach(() => {
    sessionStorage.clear();
    service = new AuthStateService();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should init with state null if not have sessionStorage', () => {
    expect(service.user()).toBeNull();
  });

  it('should set user state correctly', () => {
    service.setUser(mockUser);
    expect(service.user()).toEqual(mockUser);
  });

  it('should save data in sessionStorage when login', () => {
    service.setUser(mockUser);
    expect(sessionStorage.getItem('token')).toBe(mockUser.token);
    expect(sessionStorage.getItem('user')).toBe(mockUser.user);
    expect(sessionStorage.getItem('role')).toBe(mockUser.role);
    expect(sessionStorage.getItem('user_id')).toBe(mockUser.user_id.toString());
  });

  it('should clear data in sessionStorage when logout', () => {
    service.setUser(mockUser);
    service.clearUser();
    expect(service.user()).toBeNull();
    expect(sessionStorage.getItem('token')).toBeNull();
  });

  it('should load user from sessionStorage on init', () => {
    sessionStorage.setItem('token', mockUser.token);
    sessionStorage.setItem('user', mockUser.user);
    sessionStorage.setItem('role', mockUser.role);
    sessionStorage.setItem('user_id', mockUser.user_id.toString());

    service = new AuthStateService();
    expect(service.user()).toEqual(mockUser);
  });

  it('should be isLoggedIn', () => {
    expect(service.isLoggedIn()).toBeFalse();
    service.setUser(mockUser);
    expect(service.isLoggedIn()).toBeTrue();
  });
});
