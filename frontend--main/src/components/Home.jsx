import React from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useNavigate } from 'react-router-dom';
import './Home.css'; // Assuming you will create a CSS file for styles
import logo from '../assets/logo.png'; // Assuming logo is in the assets folder
import carousel1 from '../assets/carousel1.jpg'; // Add carousel images similarly
import carousel2 from '../assets/carousel2.jpg';
import carousel3 from '../assets/carousel3.jpg';
import carousel4 from '../assets/carousel4.jpg';
import carousel5 from '../assets/carousel5.jpg';

const Home = () => {
  const { isLoggedIn, role } = useAuth();
  const navigate = useNavigate();

  const goToDashboard = () => {
    switch (role) {
      case 'admin':
        navigate('/admin');
        break;
      case 'bursar':
        navigate('/bursar');
        break;
      case 'director':
        navigate('/director');
        break;
      case 'teacher':
        navigate('/teacher');
        break;
      case 'student':
        navigate('/student');
        break;
      default:
        navigate('/login');
    }
  };

  return (
    <div className="home-container">
      {/* Header */}
      <header className="header">
        <img src={logo} alt="School Logo" className="logo" />
        <nav className="nav-menu">
          <ul>
            <li><button onClick={goToDashboard}>Dashboard</button></li>
            <li><button onClick={() => navigate('/events')}>Events</button></li>
            <li><button onClick={() => navigate('/gallery')}>Gallery</button></li>
            <li><button onClick={() => navigate('/notifications')}>Notifications</button></li>
            <li>
              <div className="dropdown">
                <button className="dropbtn">About Us</button>
                <div className="dropdown-content">
                  <a href="/about">About Us</a>
                  {isLoggedIn ? (
                    <a href="/logout">Logout</a>
                  ) : (
                    <a href="/login">Login</a>
                  )}
                  <a href="/contact">Contact Us</a>
                </div>
              </div>
            </li>
          </ul>
        </nav>
      </header>

      {/* Carousel */}
      <div className="carousel">
        <div className="carousel-item">
          <img src={carousel1} alt="Slide 1" />
          <div className="carousel-caption">Excellence in Learning</div>
        </div>
        <div className="carousel-item">
          <img src={carousel2} alt="Slide 2" />
          <div className="carousel-caption">Empowering Students</div>
        </div>
        <div className="carousel-item">
          <img src={carousel3} alt="Slide 3" />
          <div className="carousel-caption">Innovation and Growth</div>
        </div>
        <div className="carousel-item">
          <img src={carousel4} alt="Slide 4" />
          <div className="carousel-caption">Nurturing Talents</div>
        </div>
        <div className="carousel-item">
          <img src={carousel5} alt="Slide 5" />
          <div className="carousel-caption">Building Leaders</div>
        </div>
      </div>

      {/* Vision, Mission, Core Values */}
      <section className="school-info">
        <h2>Our Vision</h2>
        <p>To nurture roots to grow and wings to fly for our pupils.</p>
        <h2>Our Mission</h2>
        <p>To be a center of affordable quality learning responsive to modern challenges.</p>
        <h2>Core Values</h2>
        <ul>
          <li>Humility</li>
          <li>Excellence</li>
          <li>Accountability</li>
          <li>Respect</li>
          <li>Teamwork</li>
        </ul>
      </section>

      {/* Footer */}
      <footer className="footer">
        <p>&copy; 2024 Bora Sigor School | Knowledge is Power | Contact us: 123-456-7890 | Email: info@borasigor.com</p>
        <div className="social-links">
          <a href="#">Facebook</a>
          <a href="#">Twitter</a>
          <a href="#">Instagram</a>
        </div>
      </footer>
    </div>
  );
};

export default Home;
      
