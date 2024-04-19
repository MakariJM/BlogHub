import React, { useState } from 'react';
import './Login.css';

const LoginSignupPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLogin, setIsLogin] = useState(true);

  const handleSubmit = (event) => {
    event.preventDefault();
    if (isLogin) {
      console.log('Login:', { email, password });
    } else {
      console.log('Signup:', { email, password });
    }
  };

  return (
    <div className="login-signup-container">
      <h2>{isLogin ? 'Login' : 'Signup'}</h2>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="form-control"
            required
          />
        </div>
        <button type="submit" className="btn">
          {isLogin ? 'Login' : 'Signup'}
        </button>
      </form>
      <p>
        {isLogin
          ? "Don't have an account? "
          : 'Already have an account? '}
        <button onClick={() => setIsLogin(!isLogin)} className="toggle-btn">
          {isLogin ? 'Signup' : 'Login'}
        </button>
      </p>
    </div>
  );
};

export default LoginSignupPage;