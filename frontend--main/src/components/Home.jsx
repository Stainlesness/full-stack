import React from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useNavigate } from 'react-router-dom';
import './Home.css'; // Custom CSS for additional flair
import logo from '../assets/IMG-20240819-WA0003.jpg'; 
import carousel1 from '../assets/IMG-20240819-WA0003.jpg';
import carousel2 from '../assets/IMG-20240818-WA0006.jpg';
import carousel3 from '../assets/IMG-20240818-WA0005.jpg';
import carousel4 from '../assets/IMG-20240819-WA0005.jpg';
import carousel5 from '../assets/IMG-20240819-WA0005.jpg';
import newCarousel1 from './path_to_your_new_image_1'; // Replace with your image paths
import newCarousel2 from './path_to_your_new_image_2';
import newCarousel3 from './path_to_your_new_image_3';
import newCarousel4 from './path_to_your_new_image_4';
import newCarousel5 from './path_to_your_new_im

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
      <header className="bg-primary p-3 shadow-lg sticky-top">
        <div className="container d-flex justify-content-between align-items-center">
          <img src={logo} alt="School Logo" className="logo img-fluid" style={{ width: '150px', height: 'auto' }} />
          <nav>
            <ul className="nav">
              <li className="nav-item">
                <button className="btn btn-light me-2 fw-bold" onClick={goToDashboard}>Dashboard</button>
              </li>
              <li className="nav-item">
                <button className="btn btn-light me-2 fw-bold" onClick={() => navigate('/events')}>Events</button>
              </li>
              <li className="nav-item">
                <button className="btn btn-light me-2 fw-bold" onClick={() => navigate('/gallery')}>Gallery</button>
              </li>
              <li className="nav-item">
                <button className="btn btn-light me-2 fw-bold" onClick={() => navigate('/notifications')}>Notifications</button>
              </li>
              <li className="nav-item dropdown">
                <button className="btn btn-light dropdown-toggle fw-bold" id="aboutDropdown" data-bs-toggle="dropdown">
                  About Us
                </button>
                <ul className="dropdown-menu" aria-labelledby="aboutDropdown">
                  <li><a className="dropdown-item" href="/about">About Us</a></li>
                  {isLoggedIn ? (
                    <li><a className="dropdown-item" href="/logout">Logout</a></li>
                  ) : (
                    <li><a className="dropdown-item" href="/login">Login</a></li>
                  )}
                  <li><a className="dropdown-item" href="/contact">Contact Us</a></li>
                </ul>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <div className="hero-section text-white text-center d-flex align-items-center justify-content-center" style={{ backgroundImage: `url(${carousel1})`, height: '60vh', backgroundSize: 'cover', backgroundPosition: 'center', filter: 'brightness(0.8)' }}>
        <div className="hero-text">
          <h1 className="display-4 fw-bold">Bora Sigor School</h1>
          <p className="lead">Empowering the leaders of tomorrow with quality education.</p>
          <button className="btn btn-lg btn-light shadow-sm mt-3" onClick={goToDashboard}>Visit Dashboard</button>
        </div>
      </div>

      {/* Carousel */}
      <div id="homeCarousel" className="carousel slide mt-5" data-bs-ride="carousel">
        <div className="carousel-inner shadow-lg rounded">
          <div className="carousel-item active">
            <img src={carousel1} className="d-block w-100" alt="Slide 1" style={{ height: '400px', objectFit: 'cover' }} />
            <div className="carousel-caption d-none d-md-block">
              <h5>Excellence in Learning</h5>
            </div>
          </div>
          <div className="carousel-item">
            <img src={carousel2} className="d-block w-100" alt="Slide 2" style={{ height: '400px', objectFit: 'cover' }} />
            <div className="carousel-caption d-none d-md-block">
              <h5>Empowering Students</h5>
            </div>
          </div>
          <div className="carousel-item">
            <img src={carousel3} className="d-block w-100" alt="Slide 3" style={{ height: '400px', objectFit: 'cover' }} />
            <div className="carousel-caption d-none d-md-block">
              <h5>Innovation and Growth</h5>
            </div>
          </div>
          <div className="carousel-item">
            <img src={carousel4} className="d-block w-100" alt="Slide 4" style={{ height: '400px', objectFit: 'cover' }} />
            <div className="carousel-caption d-none d-md-block">
              <h5>Nurturing Talents</h5>
            </div>
          </div>
          <div className="carousel-item">
            <img src={carousel5} className="d-block w-100" alt="Slide 5" style={{ height: '400px', objectFit: 'cover' }} />
            <div className="carousel-caption d-none d-md-block">
              <h5>Building Leaders</h5>
            </div>
          </div>
        </div>
        <button className="carousel-control-prev" type="button" data-bs-target="#homeCarousel" data-bs-slide="prev">
          <span className="carousel-control-prev-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button className="carousel-control-next" type="button" data-bs-target="#homeCarousel" data-bs-slide="next">
          <span className="carousel-control-next-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>

      {/* Vision, Mission, Core Values */}
      <section className="container mt-5">
        <div className="row">
          <div className="col-md-4 text-center mb-4">
            <h2 className="text-primary fw-bold">Our Vision</h2>
            <p className="lead">To nurture roots to grow and wings to fly for our pupils.</p>
          </div>
          <div className="col-md-4 text-center mb-4">
            <h2 className="text-primary fw-bold">Our Mission</h2>
            <p className="lead">To be a center of affordable quality learning responsive to modern challenges.</p>
          </div>
          <div className="col-md-4 text-center mb-4">
            <h2 className="text-primary fw-bold">Core Values</h2>
            <ul className="list-unstyled">
              <li className="mb-2">Humility</li>
              <li className="mb-2">Excellence</li>
              <li className="mb-2">Accountability</li>
              <li className="mb-2">Respect</li>
              <li className="mb-2">Teamwork</li>
            </ul>
          </div>
        </div>
      </section>
      <section className="container mt-5">
        <h2 className="text-center text-primary fw-bold mb-4">Study Corner</h2>
        <div id="studyCarousel" className="carousel slide" data-bs-ride="carousel">
          <div className="carousel-inner shadow-lg rounded">
            <div className="carousel-item active">
              <img src={assignments} className="d-block w-100" alt="Assignments" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Assignments</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={pastpapers} className="d-block w-100" alt="Past Papers" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Past Papers</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={fairytales} className="d-block w-100" alt="Fairy Tales" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Fairy Tales</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={notifications} className="d-block w-100" alt="Notifications" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Notifications</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={reportcard} className="d-block w-100" alt="Report Cards" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Report Card</h5>
              </div>
            </div>
          </div>
          <button className="carousel-control-prev" type="button" data-bs-target="#studyCarousel" data-bs-slide="prev">
            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Previous</span>
          </button>
          <button className="carousel-control-next" type="button" data-bs-target="#studyCarousel" data-bs-slide="next">
            <span className="carousel-control-next-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Next</span>
          </button>
        </div>
      </section>

      {/* Administrator's Message */}
      <div>
      {/* Sliding Content for Assignments, Past Papers, Fairy Tales, etc. */}
      <section className="container mt-5">
        <h2 className="text-center text-primary fw-bold mb-4">Study Corner</h2>
        <div id="studyCarousel" className="carousel slide" data-bs-ride="carousel">
          <div className="carousel-inner shadow-lg rounded">
            <div className="carousel-item active">
              <img src={assignmentsImage} className="d-block w-100" alt="Assignments" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Assignments</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={pastPapersImage} className="d-block w-100" alt="Past Papers" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Past Papers</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={fairyTalesImage} className="d-block w-100" alt="Fairy Tales" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Fairy Tales</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={notificationsImage} className="d-block w-100" alt="Notifications" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Notifications</h5>
              </div>
            </div>
            <div className="carousel-item">
              <img src={reportCardsImage} className="d-block w-100" alt="Report Cards" style={{ height: '400px', objectFit: 'cover' }} />
              <div className="carousel-caption d-none d-md-block">
                <h5>Report Cards</h5>
              </div>
            </div>
          </div>
          <button className="carousel-control-prev" type="button" data-bs-target="#studyCarousel" data-bs-slide="prev">
            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Previous</span>
          </button>
          <button className="carousel-control-next" type="button" data-bs-target="#studyCarousel" data-bs-slide="next">
            <span className="carousel-control-next-icon" aria-hidden="true"></span>
            <span className="visually-hidden">Next</span>
          </button>
        </div>
      </section>

      {/* Administrator's Message */}
      <section className="container mt-5">
        <h2 className="text-center text-primary fw-bold mb-4">Administrator's Message</h2>
        <div className="row align-items-center shadow-lg p-3 mb-5 bg-body rounded">
          <div className="col-md-4 text-center">
            <img src={schoolImage} alt="Admin" className="img-fluid rounded-circle" style={{ width: '150px', height: '150px' }} />
          </div>
          <div className="col-md-8">
            <p className="lead">Welcome to Bora Sigor School, where excellence in education meets a nurturing environment. Our dedicated team of educators is committed to fostering the intellectual and personal growth of our students.</p>
          </div>
        </div>
      </section>

      {/* Why Choose Msingi Bora */}
      <section className="container mt-5">
        <img src={schoolImage} alt="School" className="img-fluid mb-4" />
        <h2 className="text-center text-primary fw-bold mb-4">Why Choose Msingi Bora?</h2>
        <div className="row align-items-center shadow-lg p-3 mb-5 bg-body rounded">
        </div>
      </section>
    </div>

      {/* Footer */}
      <footer className="bg-dark text-white text-center py-4">
        <p className="mb-1">&copy; 2024 Bora Sigor School | Knowledge is Power</p>
        <p>Contact us: 123-456-7890 | Email: info@borasigor.com</p>
        <div className="d-flex justify-content-center mt-2">
          <a href="#" className="text-white me-3"><i className="fab fa-facebook fa-lg"></i></a>
          <a href="#" className="text-white me-3"><i className="fab fa-twitter fa-lg"></i></a>
          <a href="#" className="text-white"><i className="fab fa-instagram fa-lg"></i></a>
        </div>
      </footer>
    </div>
  );
};

export default Home;
