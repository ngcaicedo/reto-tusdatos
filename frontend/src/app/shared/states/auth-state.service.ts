import { Injectable, signal, computed } from '@angular/core';

interface UserAuthState {
  token: string;
  user: string;
  role: string;
  user_id: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthStateService {
  private userSignal = signal<UserAuthState | null>(this.getStoredUser());
  user = computed(() => this.userSignal());

  private getStoredUser(): UserAuthState | null {
    const token = sessionStorage.getItem('token');
    const user = sessionStorage.getItem('user');
    const role = sessionStorage.getItem('role');
    const user_id = sessionStorage.getItem('user_id');
    if (token && user) {
      return {
        token,
        user,
        role: role ?? '',
        user_id: user_id ?? '',
      };
    }
    return null;
  }

  setUser(user: UserAuthState) {
    this.userSignal.set(user);
    sessionStorage.setItem('token', user.token);
    sessionStorage.setItem('user', user.user);
    sessionStorage.setItem('role', user.role);
    sessionStorage.setItem('user_id', user.user_id);
  }

  clearUser() {
    this.userSignal.set(null);
    sessionStorage.clear();
  }

  isLoggedIn() {
    return this.user() !== null;
  }
}
