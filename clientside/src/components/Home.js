import React from 'react';
import backgroundImage from '../assets/blog.jpg';

const Home = () => {
  const homeStyle = {
    backgroundImage: `url(${backgroundImage})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '84vh',
  };

  return (
    <div>
      <div className="container-fluid" style={homeStyle}>
        <div className="row justify-content-center align-items-center" style={{ height: '100%' }}>
          {/* Your content goes here */}
        </div>
      </div>
      <footer className="bg-dark text-white text-center py-3">
        <p>&copy; {new Date().getFullYear()}. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default Home;
