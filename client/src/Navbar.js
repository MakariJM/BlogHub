
import React, { useState } from 'react';
import './Navbar.css';

const Navbar = () => {
  const [showForm, setShowForm] = useState(false);
  const [activeTab, setActiveTab] = useState('signup');

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  const handleFormToggle = () => {
    setShowForm(!showForm);
  };

  const handleTabChange = (tab) => {
    setActiveTab(tab);
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo" onClick={scrollToTop}>
BlogHub      </div>
      <ul className="navbar-links">
        <li className="navbar-link" onClick={scrollToTop}>Home</li>
        <li className="navbar-link" onClick={handleFormToggle}>{showForm ? 'Close' : 'Sign Up / Login'}</li>
      </ul>
      {showForm && (
        <div className="auth-form">
          <div className="tab-buttons">
            <button className={activeTab === 'signup' ? 'active' : ''} onClick={() => handleTabChange('signup')}>Sign Up</button>
            <button className={activeTab === 'login' ? 'active' : ''} onClick={() => handleTabChange('login')}>Login</button>
          </div>
          {activeTab === 'signup' && (
            <form className="signup-form">
              <h2>Sign Up</h2>
              <input type="text" placeholder="Name" />
              <input type="email" placeholder="Email" />
              <button type="submit">Sign Up</button>
            </form>
          )}
          {activeTab === 'login' && (
            <form className="login-form">
              <h2>Login</h2>
              <input type="email" placeholder="Email" />
              <input type="password" placeholder="Password" />
              <button type="submit">Login</button>
            </form>
          )}
        </div>
      )}
    </nav>
  );
};

export default Navbar;
