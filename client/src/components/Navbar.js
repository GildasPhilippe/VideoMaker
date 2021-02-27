import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="navbar is-white topNav" role="navigation" aria-label="main navigation">
            <div className="navbar-brand">
                <a className="navbar-item" href="/">
                    <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28" alt="Bulma"/>
                </a>
                <a role="button" 
                    className="navbar-burger" 
                    aria-label="menu" 
                    aria-expanded="false" 
                    data-target="navbarBasicExample"
                    href="/"
                >
                </a>
            </div>
            <div id="navbarBasicExample" className="navbar-menu">
                <div className="navbar-start">
                    <Link to='/' className="navbar-item">Home</Link>
                    <Link to='/videos' className="navbar-item">New project</Link>
                </div>
                <div className="navbar-end">
                    <div className="navbar-item">
                        <div className="buttons">
                        <a className="button is-primary" href="/">
                            <strong>Sign up</strong>
                        </a>
                        <a className="button is-light" href="/">
                            Log in
                        </a>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    )
  }
  
export default Navbar;