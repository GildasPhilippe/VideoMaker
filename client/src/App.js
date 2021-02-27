import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import VideoDropzone from './components/VideoDropzone';
import Process from './components/Process';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/fontawesome.js';

function App() {
  return (

    <Router>
      <Navbar />
      <br />
      <Route path='/' exact render = {() => (
        <div className="container">
          <h1 className="title">Hello world</h1>
        </div>
      )} />
      <Route path='/videos' exact render = {() => (
        <div className="container">
          <h1 className="title">No id founded</h1>
          <p>
          <Link 
            to='/videos/my5678super56testide543secret098my5678super56testide543secret999' 
            className="navbar-item">
              Go to example
          </Link>
          </p>
        </div>
      )} />
      <Route
        path='/videos/:id'
        render={(props) => (
          <>
            <VideoDropzone id={props.match.params.id}/>
            <br/>
            <Process />
          </>
        )}
      />
      <br />
      <Footer />
    </Router>
  );
}

export default App;
