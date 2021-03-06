import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import VideoDropzone from './components/VideoDropzone';
import Library from './components/Library';
import Process from './components/Process';

import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/fontawesome.js';
import 'react-dropzone-uploader/dist/styles.css'

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
        path='/videos/:session_id'
        render={(props) => (
          <>
            <VideoDropzone session_id={props.match.params.session_id} />
            <br/>
            <div className="container">
              <Library session_id={props.match.params.session_id} />
              <Process session_id={props.match.params.session_id} />
            </div>
          </>
        )}
      />
      <br />

      <Footer />
    </Router>
  );
}

export default App;
